"""Build data/videos.json WITHOUT API keys (preview mode).

Inputs:  channel/playlist RSS (newest 15 each), ingested curator posts (data/raw), podcast RSS.
Titles for post-linked videos come from YouTube oEmbed (no key).
Relevance: until the Haiku gate runs (needs ANTHROPIC_API_KEY), gated sources use a keyword
heuristic (econ_guess). Each item carries "classified": false so the site can be rebuilt later.
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import feedparser
import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from econtube.http import UA  # noqa: E402
from econtube.score import Rec, score  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data"
S = requests.Session()
S.headers["User-Agent"] = UA

ECON = re.compile(r"\b(econom\w*|inflation|deflation|money|monetary|fed\b|federal reserve|central bank|interest rate|"
                  r"rates?\b|debt|deficit|tax\w*|tariff\w*|trade|market\w*|capitalis\w*|socialis\w*|communis\w*|"
                  r"price\w*|wage\w*|labor|labour|jobs?|unemployment|growth|gdp|recession|depression|crisis|bank\w*|"
                  r"financ\w*|invest\w*|stock\w*|bond\w*|credit|currenc\w*|dollar|gold|bitcoin|crypto|budget|"
                  r"spending|welfare|regulat\w*|privati\w*|productiv\w*|industr\w*|housing|poverty|inequality|"
                  r"wealth|income|hayek|friedman|keynes\w*|sowell|mises|smith|marx\w*|nobel|prize in economic|"
                  r"china'?s economy|entrepreneur\w*|innovation|business|subsid\w*|healthcare|insurance|pension\w*)\b",
                  re.I)


def econ_guess(text: str) -> bool:
    return len(set(m.group(0).lower() for m in ECON.finditer(text or ""))) >= 1


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
    if vid in cache:
        return cache[vid]
    try:
        r = S.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=15)
        cache[vid] = r.json() if r.ok else None  # 401/404 => private, deleted or non-embeddable
    except Exception:  # noqa: BLE001
        cache[vid] = None
    time.sleep(0.3)
    return cache[vid]


def main() -> None:
    cfg = yaml.safe_load((ROOT / "sources.yaml").read_text())["sources"]
    items: dict[str, dict] = {}
    recs: dict[str, list[Rec]] = {}

    def add(key, base, src, post_url, post_date, editorial):
        it = items.setdefault(key, {**base, "sources": [], "classified": False})
        if not any(s["id"] == src["id"] and s["url"] == post_url for s in it["sources"]):
            it["sources"].append({"id": src["id"], "name": src["name"], "url": post_url, "date": post_date})
        d = date.fromisoformat(post_date) if post_date else None
        recs.setdefault(key, []).append(Rec(src["id"], float(src.get("weight", 1.0)), d, editorial))

    # 1. YouTube channel + playlist RSS (verified only)
    for s in cfg:
        if s.get("status") == "disabled":
            continue
        feeds = []
        for ch in s.get("youtube_channels") or []:
            if isinstance(ch, dict) and ch.get("id") and ch.get("verified"):
                feeds.append((f"channel_id={ch['id']}", ch.get("filter") or s.get("filter"), ch.get("title_filter")))
        for pl in s.get("youtube_playlists") or []:
            if isinstance(pl, dict) and pl.get("verified"):
                feeds.append((f"playlist_id={pl['id']}", pl.get("filter"), None))
            elif isinstance(pl, str):
                feeds.append((f"playlist_id={pl}", s.get("filter"), None))
        for q, flt, tflt in feeds:
            try:
                d = feedparser.parse(S.get(f"https://www.youtube.com/feeds/videos.xml?{q}", timeout=20).content)
            except Exception as e:  # noqa: BLE001
                print("feed fail", s["id"], q, e)
                continue
            for e in d.entries:
                vid = e.get("yt_videoid")
                title, desc = e.get("title", ""), e.get("summary", "")
                if not vid or "/shorts/" in e.get("link", ""):
                    continue
                if tflt and not re.search(tflt, title, re.I):
                    continue
                if flt == "economics_only" and not econ_guess(title + " " + desc[:400]):
                    continue
                pub = parse_dt(e.get("published"))
                add(vid, {"id": vid, "kind": "video", "title": title, "channel": e.get("author", ""),
                          "published": pub, "desc": desc[:300]}, s, e.get("link"), pub, editorial=False)
            print(f"rss {s['id']:28s} {q[:40]:40s} {len(d.entries)}")

    # 2. Curator posts -> videos (editorial picks)
    cache_p = ROOT / ".cache/oembed.json"
    cache = json.loads(cache_p.read_text()) if cache_p.exists() else {}
    by_id = {s["id"]: s for s in cfg}
    for f in sorted((ROOT / "data/raw").glob("*/posts.jsonl")):
        src = by_id.get(f.parent.name)
        if not src:
            continue
        for line in f.open():
            p = json.loads(line)
            for r in p["refs"]:
                if r["kind"] != "youtube_video":
                    continue
                meta = oembed(r["id"], cache)
                if not meta:
                    continue
                text = f"{meta.get('title','')} {p.get('title','')} {r.get('context','')}"
                # title only: "Assorted links" contexts mix unrelated links, so context is too noisy for a keyword gate
                if not econ_guess(meta.get("title", "")):
                    continue
                add(r["id"], {"id": r["id"], "kind": "video", "title": meta.get("title", ""), "channel": meta.get("author_name", ""),
                              "published": None, "desc": ""}, src, p["url"], parse_dt(p.get("date")), editorial=True)
                _ = text
    cache_p.parent.mkdir(exist_ok=True)
    cache_p.write_text(json.dumps(cache))

    # 3. Podcasts (verified feeds; newest 8 episodes each)
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
            for e in d.entries[:8]:
                enc = next((x.get("href") for x in e.get("enclosures", []) if "audio" in (x.get("type") or "audio")), None)
                if not enc:
                    continue
                key = "a-" + re.sub(r"[^a-z0-9]", "", (e.get("id") or enc).lower())[-20:]
                pub = parse_dt(e.get("published"))
                add(key, {"id": key, "kind": "audio", "title": e.get("title", ""), "channel": pf["name"], "published": pub,
                          "desc": re.sub("<[^>]+>", "", e.get("summary", ""))[:300], "audio": enc, "art": art,
                          "duration": e.get("itunes_duration")}, s, e.get("link") or pf["rss"], pub, editorial=False)
            print(f"pod {pf['name']:30s} {len(d.entries)}")

    # Skip audio episodes that already have a video version (match normalised titles); link them.
    norm = lambda t: re.sub(r"[^a-z0-9]", "", t.lower())[:60]  # noqa: E731
    vids = {norm(i["title"]): k for k, i in items.items() if i["kind"] == "video"}
    for k in [k for k, i in items.items() if i["kind"] == "audio"]:
        vk = vids.get(norm(items[k]["title"]))
        if vk:
            items[vk]["audio"] = items[k]["audio"]
            for src in items[k]["sources"]:
                if src not in items[vk]["sources"]:
                    items[vk]["sources"].append(src)
            recs[vk] += recs.pop(k)
            del items[k]

    today = date.today()
    out = []
    for k, it in items.items():
        it["score"] = score(recs[k], None, today)
        out.append(it)
    out.sort(key=lambda x: -x["score"])
    OUT.mkdir(exist_ok=True)
    (OUT / "videos.json").write_text(json.dumps({"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                                  "preview": True, "items": out}, ensure_ascii=False, indent=0))
    print(len(out), "items;", sum(i["kind"] == "audio" for i in out), "audio")


if __name__ == "__main__":
    main()
