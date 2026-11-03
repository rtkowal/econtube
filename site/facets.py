"""Landing pages (topic / field / school / person / tag), /browse/, per-topic RSS. Stdlib only."""
from __future__ import annotations

import collections
import html
import json
import re
import unicodedata
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

e = lambda s: html.escape(str(s or ""), quote=True)  # noqa: E731
TAG_MIN = 5          # a tag gets its own page once it appears on this many items (brief: curated tags)
PERSON_MIN = 2       # people pages need at least 2 items


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fmt_dur(s) -> str:
    try:
        s = int(s)
    except (TypeError, ValueError):
        return s or ""
    h, m = divmod(s // 60, 60)
    return f"{h}:{m:02d} h" if h else f"{m} min"


def card(it: dict) -> str:
    thumb = it.get("art") if it["kind"] == "audio" else f"https://i.ytimg.com/vi/{it['id']}/hq2.jpg"
    names = sorted({s["name"] for s in it["sources"]})
    via = "via " + ", ".join(names[:2]) + (f" +{len(names) - 2}" if len(names) > 2 else "")
    badge = f'<span class="badge">{"🎧 " if it["kind"] == "audio" else ""}{e(fmt_dur(it.get("duration")))}</span>' if it.get("duration") else ""
    return (f'<a class="card" href="/v/{e(it["id"])}/"><div class="th"><img loading="lazy" src="{e(thumb)}" alt="">{badge}</div>'
            f'<h3>{e(it["title"])}</h3><div class="meta">{e(it["channel"])}{" · " + e((it.get("published") or "")[:4]) if it.get("published") else ""}</div>'
            f'<div class="via">{e(via)}</div></a>')


class Index:
    """All facet memberships, computed once."""

    def __init__(self, items: list[dict], tax: dict):
        self.items = items
        self.label = {k: {x["slug"]: x for x in tax[k]} for k in ("fields", "topics", "schools", "formats", "levels", "eras", "regions")}
        self.groups: dict[str, dict[str, list[dict]]] = collections.defaultdict(lambda: collections.defaultdict(list))
        self.person_name: dict[str, str] = {}
        for it in items:
            f = it.get("facets") or {}
            for k, key in (("topics", "topic"), ("fields", "field"), ("schools", "school")):
                for v in f.get(k) or []:
                    self.groups[key][v].append(it)
            ppl = it.get("people") or {}
            for n in {*(ppl.get("speakers") or []), *(ppl.get("discussed") or [])}:
                s = slug(n)
                if s:
                    self.person_name.setdefault(s, n)
                    self.groups["person"][s].append(it)
            for t in it.get("tags") or []:
                self.groups["tag"][slug(t)].append(it)
                self.person_name.setdefault("tag:" + slug(t), t)
        self.groups["person"] = {k: v for k, v in self.groups["person"].items() if len(v) >= PERSON_MIN}
        self.groups["tag"] = {k: v for k, v in self.groups["tag"].items() if len(v) >= TAG_MIN}

    def name(self, kind: str, key: str) -> str:
        if kind == "person":
            return self.person_name.get(key, key)
        if kind == "tag":
            return self.person_name.get("tag:" + key, key)
        tk = {"topic": "topics", "field": "fields", "school": "schools"}[kind]
        return (self.label[tk].get(key) or {}).get("label", key)

    def has_page(self, kind: str, key: str) -> bool:
        return key in self.groups.get(kind, {})

    def link(self, kind: str, key: str, text: str | None = None) -> str:
        t = e(text or self.name(kind, key))
        return f'<a href="/{kind}/{e(key)}/">{t}</a>' if self.has_page(kind, key) else f"<span>{t}</span>"


def chips(ix: Index, it: dict) -> str:
    f = it.get("facets") or {}
    parts = [ix.link("topic", v) for v in f.get("topics") or []]
    parts += [ix.link("school", v) for v in f.get("schools") or []]
    if f.get("format"):
        parts.append(f'<span>{e(ix.label["formats"].get(f["format"], {}).get("label", f["format"]))}</span>')
    if f.get("level"):
        parts.append(f'<span>{e(f["level"])}</span>')
    parts += [ix.link("tag", slug(t), t) for t in (it.get("tags") or [])[:6]]
    ppl = it.get("people") or {}
    parts += [ix.link("person", slug(n), n) for n in (ppl.get("speakers") or [])[:4] if ix.has_page("person", slug(n))]
    return '<p class="chips">' + "".join(parts) + "</p>" if parts else ""


def related(ix: Index, members: list[dict], kind: str, key: str) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    tc, gc = collections.Counter(), collections.Counter()
    for it in members:
        for t in (it.get("facets") or {}).get("topics") or []:
            if not (kind == "topic" and t == key):
                tc[t] += 1
        for g in it.get("tags") or []:
            s = slug(g)
            if ix.has_page("tag", s) and not (kind == "tag" and s == key):
                gc[s] += 1
    return tc.most_common(8), gc.most_common(10)


def landing(ix: Index, kind: str, key: str, page) -> str:
    members = sorted(ix.groups[kind][key], key=lambda x: -x["score"])
    name = ix.name(kind, key)
    srcs = collections.Counter(s["name"] for it in members for s in it["sources"]).most_common(3)
    noun = {"topic": "on", "field": "in", "school": "from the", "person": "featuring or about", "tag": "about"}[kind]
    tk = {"topic": "topics", "field": "fields", "school": "schools"}.get(kind)
    desc_tax = (ix.label[tk].get(key) or {}).get("description") if tk else None
    desc = (desc_tax + " " if desc_tax else "") + (
        f"{len(members)} lectures, interviews and podcast episodes {noun} {name}"
        f"{' school' if kind == 'school' else ''}, recommended by {', '.join(s for s, _ in srcs)}. "
        f"The most-recommended is “{members[0]['title']}”.")
    rt, rg = related(ix, members, kind, key)
    rel = ""
    if rt:
        rel += "<h2>Related topics</h2><p class=\"chips\">" + "".join(ix.link("topic", t) for t, _ in rt) + "</p>"
    if rg:
        rel += "<h2>Related tags</h2><p class=\"chips\">" + "".join(ix.link("tag", t) for t, _ in rg) + "</p>"
    rss = f'<a href="/topic/{e(key)}/feed.xml">RSS</a>' if kind == "topic" else ""
    browse = {"topic": "topic", "school": "school", "field": "field"}.get(kind)
    blink = f'<a href="/browse/?{browse}={e(key)}">Filter &amp; combine →</a>' if browse else ""
    body = (f'<div class="landing"><p class="kicker">{e(kind)}</p><h1>{e(name)}</h1><p class="lede">{e(desc)}</p>'
            f'<p class="meta">{blink} {rss}</p>{rel}</div><main class="grid">{"".join(card(i) for i in members[:60])}</main>')
    extra = f'<link rel="alternate" type="application/rss+xml" href="/topic/{e(key)}/feed.xml">' if kind == "topic" else ""
    return page(f"{name} — EconTube", body, desc=desc, path=f"/{kind}/{key}/", extra_head=extra)


def rss(ix: Index, key: str, base: str) -> str:
    members = sorted(ix.groups["topic"][key], key=lambda x: x.get("published") or "", reverse=True)[:50]
    def pub(it):
        try:
            return format_datetime(datetime.fromisoformat(it["published"]).replace(tzinfo=timezone.utc))
        except Exception:  # noqa: BLE001
            return ""
    items = "".join(f"<item><title>{e(it['title'])}</title><link>{base}/v/{e(it['id'])}/</link><guid>{base}/v/{e(it['id'])}/</guid>"
                    f"<description>{e(it.get('why') or '')}</description>{'<pubDate>' + pub(it) + '</pubDate>' if pub(it) else ''}</item>"
                    for it in members)
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>EconTube — {e(ix.name("topic", key))}</title>'
            f"<link>{base}/topic/{e(key)}/</link><description>Recommended economics videos and podcasts: {e(ix.name('topic', key))}</description>{items}</channel></rss>")


def index_page(ix: Index, page) -> str:
    def block(kind, title, keys):
        return (f"<h2>{title}</h2><p class=\"chips\">" +
                "".join(f'{ix.link(kind, k)}<small>{len(ix.groups[kind][k])}</small> ' for k in keys) + "</p>")
    g = ix.groups
    by = lambda kind: sorted(g.get(kind, {}), key=lambda k: -len(g[kind][k]))  # noqa: E731
    body = ('<div class="prose wide"><h1>Topics</h1>' + block("topic", "Topics", by("topic")) + block("field", "Fields", by("field"))
            + block("school", "Schools of thought", by("school")) + block("person", "People", by("person")[:80])
            + block("tag", "Tags", by("tag")[:120]) + "</div>")
    return page("Topics — EconTube", body, desc="Browse economics videos by topic, field, school of thought, person and tag.", path="/topics/")


def browse_page(page) -> str:
    body = ('<div class="browse"><aside id="facets" aria-label="Filters"></aside>'
            '<section><p id="active" class="meta"></p><main id="bgrid" class="grid"></main></section></div>'
            '<script src="/browse.js" defer></script>')
    return page("Browse — EconTube", body, desc="Combine topic, school, format, level, era, region and length filters.", path="/browse/")


def slim(it: dict) -> dict:
    """Client-side record for search / For You / browse."""
    f = it.get("facets") or {}
    ppl = it.get("people") or {}
    return {"id": it["id"], "kind": it["kind"], "title": it["title"], "channel": it["channel"], "published": it.get("published"),
            "score": it["score"], "duration": it.get("duration"), "art": it.get("art"), "lang": it.get("lang"),
            "sources": [{"name": s["name"]} for s in it["sources"]],
            "t": f.get("topics") or [], "s": f.get("schools") or [], "f": f.get("fields") or [], "fm": f.get("format"),
            "l": f.get("level"), "e": f.get("eras") or [], "r": f.get("regions") or [],
            "p": [*(ppl.get("speakers") or []), *(ppl.get("discussed") or [])][:6], "g": (it.get("tags") or [])[:8]}


FAMILIES = [  # (slug, label, top-level fields or sub-fields that map here; first match walking up the tree wins)
    ("money-macro", "Money & Macro", {"macro"}),
    ("markets", "Markets & Investing", {"markets-investing", "finance"}),
    ("global", "Trade & Global", {"international", "development"}),
    ("work-welfare", "Work & Welfare", {"labor", "health-education-welfare"}),
    ("policy", "Policy & Regulation", {"public", "industrial-org", "law-econ", "urban-housing", "environment-energy"}),
    ("ideas", "History & Ideas", {"economic-history", "history-of-thought", "systems", "general", "quantitative", "micro", "behavioral"}),
    ("tech-business", "Tech & Business", {"business", "innovation"}),
    ("bitcoin", "Bitcoin & Sound Money", {"money-bitcoin"}),
]


def topic_families(tax: dict) -> dict[str, str]:
    parent = {f["slug"]: f.get("parent") for f in tax["fields"]}
    out = {}
    for t in tax["topics"]:
        node = t.get("parent")
        while node:
            fam = next((slug for slug, _, keys in FAMILIES if node in keys), None)
            if fam:
                out[t["slug"]] = fam
                break
            node = parent.get(node)
    return out


def write_all(dist: Path, items: list[dict], tax: dict, page, base: str) -> list[str]:
    ix = Index(items, tax)
    urls = ["/topics/", "/browse/"]
    for kind, members in ix.groups.items():
        for key in members:
            d = dist / kind / key
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(landing(ix, kind, key, page))
            if kind == "topic":
                (d / "feed.xml").write_text(rss(ix, key, base))
            urls.append(f"/{kind}/{key}/")
    (dist / "topics").mkdir(exist_ok=True)
    (dist / "topics/index.html").write_text(index_page(ix, page))
    (dist / "browse").mkdir(exist_ok=True)
    (dist / "browse/index.html").write_text(browse_page(page))
    labels = {k: {s: v.get("label", s) for s, v in ix.label[k].items()} for k in ix.label}
    aliases = {s: v.get("aliases", []) for s, v in ix.label["topics"].items() if v.get("aliases")}
    (dist / "data/facets.json").write_text(json.dumps({"labels": labels, "aliases": aliases,
                                                       "families": [[a, b] for a, b, _ in FAMILIES], "fam": topic_families(tax),
                                                       "people": {k: ix.person_name[k] for k in ix.groups["person"]},
                                                       "tags": {k: ix.name("tag", k) for k in ix.groups["tag"]}},
                                                      ensure_ascii=False, separators=(",", ":")))
    print(f"landing pages: " + ", ".join(f"{k} {len(v)}" for k, v in ix.groups.items()))
    return urls, ix
