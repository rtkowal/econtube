"""Relevance gate + facet classification (OpenAI, JSON mode), validated against taxonomy.yaml.

- gate(item): cheap model -> {relevant, confidence}; keep if relevant and confidence >= GATE_MIN.
- classify(item): returns facets + tags + is_recommendation + one_line_why. Values outside the
  vocabulary are rejected and retried once (with the errors fed back); anything still invalid is
  dropped and logged to taxonomy_suggestions.jsonl. Facet values below SHOW_MIN confidence are kept
  in the cache but not shown on the site.
- overrides.yaml (item id -> facet values) always wins over the model.
- Both caches are keyed by item id (decisions are per item, so re-runs cost nothing).
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import yaml

from . import llm

ROOT = Path(__file__).resolve().parents[2]
CACHE = Path(os.environ.get("ECONTUBE_CACHE", ROOT / ".cache"))
GATE_MIN = 0.7
CLASSIFY_CACHE = "classify_v3"   # _reroute is applied at read time too, so no bump needed   # bump to force re-classification after prompt/schema changes
SHOW_MIN = 0.6
MULTI = ("fields", "topics", "schools", "eras", "regions")   # 1-3 values each
SINGLE = ("format", "level")


def load_taxonomy(path: Path = ROOT / "taxonomy.yaml") -> dict[str, set[str]]:
    t = yaml.safe_load(path.read_text())
    return {"fields": {x["slug"] for x in t["fields"]}, "topics": {x["slug"] for x in t["topics"]},
            "schools": {x["slug"] for x in t["schools"]}, "eras": {x["slug"] for x in t["eras"]},
            "regions": {x["slug"] for x in t["regions"]}, "format": {x["slug"] for x in t["formats"]},
            "level": {x["slug"] for x in t["levels"]}}


import threading

_LOCK = threading.Lock()
_MEM: dict[str, tuple[Path, dict]] = {}
MAX_LLM = int(os.environ.get("MAX_LLM_CALLS", "4000"))   # per-run cap; the backfill spreads over several runs
_calls = 0


class Budget(Exception):
    pass


def _cache(name: str) -> tuple[Path, dict]:
    with _LOCK:
        if name not in _MEM:
            p = CACHE / f"{name}.json"
            _MEM[name] = (p, json.loads(p.read_text()) if p.exists() else {})
        return _MEM[name]


def flush() -> None:
    with _LOCK:
        for p, c in _MEM.values():
            p.parent.mkdir(parents=True, exist_ok=True)
            tmp = p.with_suffix(".tmp")
            tmp.write_text(json.dumps(c, ensure_ascii=False))
            tmp.replace(p)


def _spend() -> None:
    global _calls
    with _LOCK:
        if _calls >= MAX_LLM:
            raise Budget(f"MAX_LLM_CALLS={MAX_LLM} reached; remaining items wait for the next run")
        _calls += 1


def cached(name: str, item_id: str) -> bool:
    return item_id in _cache(name)[1]


def _text(item: dict, n: int = 1500) -> str:
    parts = [f"Title: {item.get('title','')}", f"Channel/show: {item.get('channel','')}",
             f"Description: {(item.get('desc') or '')[:n]}"]
    for s in item.get("posts", [])[:3]:
        parts.append(f"Curator post ({s.get('name')}): {s.get('context','')[:600]}")
    if item.get("captions"):
        parts.append(f"Transcript start: {item['captions'][:2000]}")
    return "\n".join(parts)


GATE_SYS = ("You decide whether a video or podcast episode belongs on EconTube, a catalogue of economics and finance content. "
            "Count it as relevant ONLY if its MAIN subject is economics, money, markets, business economics, economic history "
            "or political economy. Reject culture-war, partisan politics, geopolitics/military, entertainment, music, film "
            "trailers, science and general-interest items that only mention money in passing. "
            'Reply with JSON: {"relevant": true|false, "confidence": 0..1, "reason": "<10 words"}')


def gate(item: dict) -> bool:
    p, c = _cache("gate")
    if item["id"] not in c:
        _spend()
        d = llm.chat_json(GATE_SYS, _text(item, 600), max_tokens=200, tag="gate")
        with _LOCK:
            c[item["id"]] = d
    d = c[item["id"]]
    return bool(d.get("relevant")) and float(d.get("confidence", 0)) >= GATE_MIN


def _sys(tax: dict[str, set[str]]) -> str:
    voc = "\n".join(f"- {k}: {', '.join(sorted(v))}" for k, v in tax.items())
    return f"""You classify economics videos and podcast episodes for EconTube. Use ONLY these slugs:
{voc}

Return JSON with exactly these keys:
  "is_recommendation": true if the curator post links the item approvingly or as a resource; false for ads, sidebars, footers, "subscribe" boilerplate (true when there is no curator post),
  "fields", "topics", "schools", "eras", "regions": lists of 0-3 objects {{"v": slug, "c": confidence 0..1}} (an EMPTY list is correct when nothing fits; never put a slug from one facet into another, e.g. a field slug into topics; schools ONLY when the content clearly argues from that school; eras = periods DISCUSSED, not publication date),
  "format", "level": ONE object (not a list) {{"v": slug, "c": confidence}},
  "people": {{"speakers": [names], "discussed": [names]}} (HUMANS ONLY: never institutions like "Federal Reserve"; full canonical names, e.g. "Milton Friedman"; "discussed" = people talked ABOUT who are not speaking; never repeat a speaker there),
  "tags": 3-10 lowercase specific concepts (never the channel, show or source name), institutions, events, books or policies (e.g. "phillips curve", "bretton woods", "balcerowicz plan"),
  "one_line_why": at most 20 words, your own words, no quotes from the source, saying why it is worth watching."""


def _normalise(out: dict) -> dict:
    """Models often wrap single-value facets in a one-item list; unwrap. Accept bare slugs too."""
    for k in SINGLE:
        x = out.get(k)
        if isinstance(x, list):
            x = max(x, key=lambda y: y.get("c", 0) if isinstance(y, dict) else 0) if x else None
        if isinstance(x, str):
            x = {"v": x, "c": 0.7}
        out[k] = x
    for k in MULTI:
        out[k] = [({"v": x, "c": 0.7} if isinstance(x, str) else x) for x in (out.get(k) or [])]
    return out


def _reroute(out: dict, tax: dict[str, set[str]]) -> dict:
    """Small models put slugs in the wrong facet (a field in topics, a topic in fields). Move them
    instead of paying for a retry; drop placeholders like 'general' from topics."""
    moves = {"topics": "fields", "fields": "topics"}
    for src, dst in moves.items():
        keep = []
        for x in out.get(src) or []:
            v = x.get("v") if isinstance(x, dict) else None
            if v in tax[src]:
                keep.append(x)
            elif v in tax[dst]:
                if v not in {y.get("v") for y in out.get(dst) or [] if isinstance(y, dict)} and v != "general":
                    out.setdefault(dst, []).append(x)
            elif v == "general":
                continue
            else:
                keep.append(x)   # genuinely unknown: let validation see it
        out[src] = keep
    return out


def _validate(out: dict, tax: dict[str, set[str]]) -> list[str]:
    out = _reroute(_normalise(out), tax)
    errs = []
    for k in MULTI:
        for x in out.get(k) or []:
            if not isinstance(x, dict) or x.get("v") not in tax[k]:
                errs.append(f"{k}: '{x.get('v') if isinstance(x, dict) else x}' is not an allowed slug")
    for k in SINGLE:
        x = out.get(k)
        if not isinstance(x, dict) or x.get("v") not in tax[k]:
            errs.append(f"{k}: '{x.get('v') if isinstance(x, dict) else x}' is not an allowed slug")
    if len((out.get("one_line_why") or "").split()) > 20:
        errs.append("one_line_why longer than 20 words")
    return errs


def _clean(out: dict, tax: dict[str, set[str]], item_id: str, drop_tags: set[str] = frozenset()) -> dict:
    out = _reroute(_normalise(out), tax)
    sugg = []
    for k in MULTI:
        keep = []
        for x in (out.get(k) or [])[:3]:
            if isinstance(x, dict) and x.get("v") in tax[k]:
                keep.append({"v": x["v"], "c": round(float(x.get("c", 0)), 2)})
            else:
                sugg.append({"id": item_id, "facet": k, "value": x})
        out[k] = keep
    for k in SINGLE:
        x = out.get(k)
        if not (isinstance(x, dict) and x.get("v") in tax[k]):
            sugg.append({"id": item_id, "facet": k, "value": x})
            out[k] = None
    norm = lambda t: re.sub(r"[\s_-]+", " ", str(t).strip().lower())  # noqa: E731
    out["tags"] = sorted({norm(t) for t in out.get("tags") or [] if str(t).strip()} - {norm(d) for d in drop_tags})[:10]
    out["one_line_why"] = " ".join((out.get("one_line_why") or "").split()[:20])
    if sugg:
        with (ROOT / "taxonomy_suggestions.jsonl").open("a") as f:
            for s in sugg:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
    return out


def classify(item: dict, tax: dict[str, set[str]] | None = None, *, strong: bool = False) -> dict:
    tax = tax or load_taxonomy()
    p, c = _cache(CLASSIFY_CACHE)
    if item["id"] not in c:
        _spend()
        sys_p, user = _sys(tax), _text(item)
        out = llm.chat_json(sys_p, user, strong=strong, tag="classify")
        errs = _validate(out, tax)
        if errs:  # one retry with the errors fed back
            out = llm.chat_json(sys_p, user + "\n\nYour previous answer had invalid values:\n- " + "\n- ".join(errs)
                                + "\nAnswer again using only allowed slugs.", strong=strong, tag="classify-retry")
        drop = {item.get("channel", "")} | {s.get("name", "") for s in item.get("posts", [])}
        res = _clean(out, tax, item["id"], drop)
        with _LOCK:
            c[item["id"]] = res
    return apply_overrides(item["id"], c[item["id"]])


def apply_overrides(item_id: str, cls: dict) -> dict:
    p = ROOT / "overrides.yaml"
    ov = (yaml.safe_load(p.read_text()) or {}) if p.exists() else {}
    if item_id in ov:
        cls = {**cls, **{k: ([{"v": v, "c": 1.0} for v in val] if isinstance(val, list) else {"v": val, "c": 1.0})
                         for k, val in ov[item_id].items()}}
    return cls


def visible(cls: dict) -> dict:
    """Facet values the site may show (confidence >= SHOW_MIN)."""
    out = {k: [x["v"] for x in cls.get(k) or [] if x["c"] >= SHOW_MIN] for k in MULTI}
    for k in SINGLE:
        x = cls.get(k)
        out[k] = x["v"] if x and x["c"] >= SHOW_MIN else None
    out["tags"], out["why"] = cls.get("tags", []), cls.get("one_line_why", "")
    out["people"] = cls.get("people", {})
    return out
