"""Build data/videos.json: collect -> gate -> enrich -> classify -> score.

Collect
  * YouTube channels/playlists in sources.yaml (verified only). With YOUTUBE_API_KEY: full upload
    archives via playlistItems (incremental: stops at known pages). Without: channel RSS (newest 15).
  * Curator posts ingested by ingest.py (.cache/raw/<source>/posts.jsonl) -> linked videos (editorial picks).
  * Podcast RSS feeds (verified): newest N episodes per show (all on backfill).
Gate     sources with filter: economics_only (and every curator-linked video) -> LLM relevance gate,
         keyword fallback without OPENAI_API_KEY. Nobel uses its title_filter.
Enrich   videos.list: duration, views, embeddable. Drop gone / non-embeddable / < 60 s.
Classify facets, tags, why (OPENAI_API_KEY). Parallel, cached per item id, capped by MAX_LLM_CALLS.
Score    econtube/score.py.
Every stage tolerates failures per source/item; caches make re-runs cheap and resumable.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

import feedparser
import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from econtube import classify, llm, youtube  # noqa: E402
from econtube.http import UA  # noqa: E402
from econtube.score import Rec, score  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(os.environ.get("ECONTUBE_CACHE", ROOT / ".cache"))
OUT = ROOT / "data"
S = requests.Session()
S.headers["User-Agent"] = UA
USE_LLM, USE_YT = llm.available(), youtube.available()
WORKERS = int(os.environ.get("LLM_WORKERS", "8"))
PODCAST_EPISODES = int(os.environ.get("PODCAST_EPISODES", "40"))
MIN_SECONDS = 60

ECON = re.compile(r"\b(econom\w*|inflation|deflation|money|monetary|fed\b|federal reserve|central bank|interest rate|"
                  r"rates?\b|debt|deficit|tax\w*|tariff\w*|trade|market\w*|capitalis\w*|socialis\w*|communis\w*|"
                  r"price\w*|wage\w*|labor|labour|jobs?|unemployment|growth|gdp|recession|depression|crisis|bank\w*|"
                  r"financ\w*|invest\w*|stock\w*|bond\w*|credit|currenc\w*|dollar|gold|bitcoin|crypto|budget|"
                  r"spending|welfare|regulat\w*|privati\w*|productiv\w*|industr\w*|housing|poverty|inequality|"
                  r"wealth|income|hayek|friedman|keynes\w*|sowell|mises|marx\w*|nobel|prize in economic|"
                  r"entrepreneur\w*|innovation|business|subsid\w*|healthcare|insurance|pension\w*)\b", re.I)


def econ_guess(text: str) -> bool:
    return bool(ECON.search(text or ""))


def parse_dt(s: str | None) -> str | None:
    if not s:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
        try:
            return datetime.strptime(s.replace("+00:00", "+0000"), fmt).date().isoformat()
        except ValueError:
            pass
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else None


def oembed(vid: str, cache: dict) -> dict | None:
    if vid not in cache:
        try:
            r = S.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=15)
            cache[vid] = r.json() if r.ok else None
        except Exception:  # noqa: BLE001
            cache[vid] = None
        time.sleep(0.2)
    return cache[vid]


class Catalogue:
    def __init__(self) -> None:
        self.items: dict[str, dict] = {}
        self.recs: dict[str, list[Rec]] = {}
        self.gated: set[str] = set()       # ids that must pass the relevance gate
        self.title_filters: dict[str, str] = {}

    def add(self, key, base, src, post_url, post_date, editorial, gate=False):
        it = self.items.setdefault(key, {**base, "sources": [], "classified": False})
        for k, v in base.items():
            if v and not it.get(k):
                it[k] = v
        if not any(s["id"] == src["id"] and s["url"] == post_url for s in it["sources"]):
            it["sources"].append({"id": src["id"], "name": src["name"], "url": post_url, "date": post_date})
        d = date.fromisoformat(post_date) if post_date else None
        self.recs.setdefault(key, []).append(Rec(src["id"], float(src.get("weight", 1.0)), d, editorial))
        if gate:
            self.gated.add(key)

    def drop(self, key):
        self.items.pop(key, None)
        self.recs.pop(key, None)


# ---------------------------------------------------------------- collect
def collect_youtube(cat: Catalogue, cfg: list[dict]) -> None:
    lst_p = CACHE / "yt_lists.json"
    lists = json.loads(lst_p.read_text()) if lst_p.exists() else {}
    for s in cfg:
        if s.get("status") == "disabled":
            continue
        feeds = []
        for ch in s.get("youtube_channels") or []:
            if isinstance(ch, dict) and ch.get("id") and ch.get("verified"):
                feeds.append(("channel", ch["id"], ch.get("filter") or s.get("filter"), ch.get("title_filter")))
        for pl in s.get("youtube_playlists") or []:
            if isinstance(pl, dict) and pl.get("verified"):
                feeds.append(("playlist", pl["id"], pl.get("filter"), None))
            elif isinstance(pl, str):
                feeds.append(("playlist", pl, s.get("filter"), None))
        for kind, fid, flt, tflt in feeds:
            entries = []
            try:
                if USE_YT:
                    pid = fid
                    if kind == "channel":
                        pid = lists.get(f"uploads:{fid}") or (youtube.channel(cid=fid) or {}).get("uploads")
                        lists[f"uploads:{fid}"] = pid
                    known = {e["id"] for e in lists.get(pid, [])}
                    fresh = youtube.playlist_ids(pid, known=known)
                    merged = {e["id"]: e for e in lists.get(pid, [])}
                    merged.update({e["id"]: e for e in fresh})
                    lists[pid] = list(merged.values())
                    entries = lists[pid]
                else:
                    q = "channel_id" if kind == "channel" else "playlist_id"
                    d = feedparser.parse(S.get(f"https://www.youtube.com/feeds/videos.xml?{q}={fid}", timeout=20).content)
                    entries = [{"id": e.get("yt_videoid"), "title": e.get("title", ""), "desc": e.get("summary", "")[:600],
                                "channel": e.get("author", ""), "published": parse_dt(e.get("published"))} for e in d.entries]
            except youtube.QuotaExceeded as e:
                print("youtube quota:", e)
            except Exception as e:  # noqa: BLE001
                print("feed fail", s["id"], fid, e)
            n = 0
            for e in entries:
                if not e.get("id") or (tflt and not re.search(tflt, e["title"], re.I)):
                    continue
                n += 1
                cat.add(e["id"], {"id": e["id"], "kind": "video", "title": e["title"], "channel": e["channel"],
                                  "published": e["published"], "desc": e["desc"]},
                        s, f"https://www.youtube.com/watch?v={e['id']}", e["published"], editorial=False,
                        gate=(flt == "economics_only"))
            print(f"yt  {s['id']:28s} {kind:8s} {fid[:26]:26s} {n:5d} kept of {len(entries)}")
    lst_p.parent.mkdir(parents=True, exist_ok=True)
    lst_p.write_text(json.dumps(lists))


def collect_posts(cat: Catalogue, cfg: list[dict]) -> None:
    by_id = {s["id"]: s for s in cfg}
    cache_p = CACHE / "oembed.json"
    oe = json.loads(cache_p.read_text()) if cache_p.exists() else {}
    for f in sorted((CACHE / "raw").glob("*/posts.jsonl")):
        src = by_id.get(f.parent.name)
        if not src or src.get("status") == "disabled":
            continue
        n = 0
        for line in f.open():
            p = json.loads(line)
            for r in p["refs"]:
                if r["kind"] != "youtube_video":
                    continue
                meta = None if USE_YT else oembed(r["id"], oe)
                if not USE_YT and not meta:
                    continue
                n += 1
                cat.add(r["id"], {"id": r["id"], "kind": "video", "title": (meta or {}).get("title", ""),
                                  "channel": (meta or {}).get("author_name", ""), "published": None, "desc": ""},
                        src, p["url"], parse_dt(p.get("date")), editorial=True, gate=True)
                cat.items[r["id"]].setdefault("posts", []).append({"name": src["name"], "context": r.get("context", "")[:600]})
        print(f"post {src['id']:28s} {n:5d} video links")
    cache_p.write_text(json.dumps(oe))


def collect_podcasts(cat: Catalogue, cfg: list[dict]) -> None:
    for s in cfg:
        for pf in s.get("podcast_feeds") or []:
            if not (isinstance(pf, dict) and pf.get("rss") and pf.get("verified")):
                continue
            try:
                d = feedparser.parse(S.get(pf["rss"], timeout=30).content)
            except Exception as e:  # noqa: BLE001
                print("pod fail", pf["name"], e)
                continue
            art = (d.feed.get("image") or {}).get("href") or d.feed.get("itunes_image", {}).get("href", "")
            for e in d.entries[:PODCAST_EPISODES]:
                enc = next((x.get("href") for x in e.get("enclosures", []) if "audio" in (x.get("type") or "audio")), None)
                if not enc:
                    continue
                key = "a-" + re.sub(r"[^a-z0-9]", "", (e.get("id") or enc).lower())[-20:]
                pub = parse_dt(e.get("published"))
                cat.add(key, {"id": key, "kind": "audio", "title": e.get("title", ""), "channel": pf["name"], "published": pub,
                              "desc": re.sub("<[^>]+>", " ", e.get("summary", ""))[:600], "audio": enc, "art": art,
                              "duration": e.get("itunes_duration")}, s, e.get("link") or pf["rss"], pub, editorial=False,
                        gate=bool(pf.get("filter") == "economics_only"))
            print(f"pod {pf['name']:30s} {min(len(d.entries), PODCAST_EPISODES)}")


# ---------------------------------------------------------------- stages
def run_parallel(fn, keys, label):
    done = 0
    with ThreadPoolExecutor(WORKERS) as ex:
        for _ in ex.map(fn, keys):
            done += 1
            if done % 200 == 0:
                classify.flush()
                print(f"  {label}: {done}/{len(keys)}", flush=True)
    classify.flush()


def gate_stage(cat: Catalogue) -> None:
    keys = [k for k in cat.gated if k in cat.items]
    verdict: dict[str, bool | None] = {}

    def one(k):
        it = cat.items[k]
        if not USE_LLM:
            verdict[k] = econ_guess(it["title"] + " " + (it.get("desc") or "")[:400])
            return
        try:
            verdict[k] = classify.gate({"id": k, "title": it["title"], "desc": it.get("desc", ""), "channel": it.get("channel", ""),
                                        "posts": it.get("posts", [])})
        except classify.Budget:
            verdict[k] = None          # undecided: hold back until a later run decides
        except Exception as e:  # noqa: BLE001
            print("gate error", k, e)
            verdict[k] = None
    run_parallel(one, keys, "gate")
    dropped = [k for k, v in verdict.items() if v is not True]
    for k in dropped:
        cat.drop(k)
    print(f"gate: {len(keys)} checked, {len(dropped)} dropped/undecided")


def enrich_stage(cat: Catalogue) -> None:
    if not USE_YT:
        return
    vids = [k for k, it in cat.items.items() if it["kind"] == "video"]
    try:
        meta = youtube.videos(vids)
    except youtube.QuotaExceeded as e:
        print("youtube quota during enrich:", e)
        meta = json.loads((CACHE / "yt_videos.json").read_text()) if (CACHE / "yt_videos.json").exists() else {}
    bad = 0
    for k in vids:
        m = meta.get(k)
        if m is None:
            continue                      # not enriched yet (quota) - keep, enrich next run
        short = m.get("duration", 0) and (m["duration"] < MIN_SECONDS or (m["duration"] < 180 and "#" in m.get("title", "")))
        if m.get("gone") or not m.get("embeddable") or short:
            cat.drop(k)
            bad += 1
            continue
        it = cat.items[k]
        it.update(title=it.get("title") or m["title"], channel=it.get("channel") or m["channel"],
                  published=it.get("published") or m["published"], desc=it.get("desc") or m["desc"],
                  duration=m["duration"], views=m["views"], lang=m.get("lang"))
    print(f"enrich: {len(vids)} videos, {bad} dropped (gone/non-embeddable/short); quota used {youtube.used}")


def classify_stage(cat: Catalogue) -> None:
    if not USE_LLM:
        return
    tax = classify.load_taxonomy()

    def one(k):
        it = cat.items[k]
        try:
            v = classify.visible(classify.classify(it, tax))
            it.update(facets={f: v[f] for f in ("fields", "topics", "schools", "eras", "regions", "format", "level")},
                      tags=v["tags"], why=v["why"], people=v["people"], classified=True)
        except classify.Budget:
            pass
        except Exception as e:  # noqa: BLE001
            print("classify error", k, e)
    run_parallel(one, list(cat.items), "classify")
    print(f"classify: {sum(i.get('classified', False) for i in cat.items.values())}/{len(cat.items)} classified")


def dedupe_audio(cat: Catalogue) -> None:
    norm = lambda t: re.sub(r"[^a-z0-9]", "", t.lower())[:60]  # noqa: E731
    vids = {norm(i["title"]): k for k, i in cat.items.items() if i["kind"] == "video" and i.get("title")}
    for k in [k for k, i in cat.items.items() if i["kind"] == "audio"]:
        vk = vids.get(norm(cat.items[k]["title"]))
        if vk:
            cat.items[vk]["audio"] = cat.items[k]["audio"]
            for src in cat.items[k]["sources"]:
                if src not in cat.items[vk]["sources"]:
                    cat.items[vk]["sources"].append(src)
            cat.recs[vk] += cat.recs[k]
            cat.drop(k)


def main() -> None:
    cfg = yaml.safe_load((ROOT / "sources.yaml").read_text())["sources"]
    cat = Catalogue()
    print(f"mode: llm={USE_LLM} youtube_api={USE_YT}")
    collect_youtube(cat, cfg)
    collect_posts(cat, cfg)
    collect_podcasts(cat, cfg)
    print(f"collected {len(cat.items)} items")
    gate_stage(cat)
    enrich_stage(cat)
    cat.items = {k: v for k, v in cat.items.items() if v.get("title")}
    dedupe_audio(cat)
    classify_stage(cat)

    today = date.today()
    out = []
    for k, it in cat.items.items():
        it.pop("posts", None)
        it["score"] = score(cat.recs[k], it.get("views"), today)
        out.append(it)
    out.sort(key=lambda x: -x["score"])
    OUT.mkdir(exist_ok=True)
    (OUT / "videos.json").write_text(json.dumps({"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                                  "preview": not USE_LLM, "items": out}, ensure_ascii=False, separators=(",", ":")))
    print(f"wrote {len(out)} items ({sum(i['kind'] == 'audio' for i in out)} audio, "
          f"{sum(i.get('classified', False) for i in out)} classified)")


if __name__ == "__main__":
    main()
