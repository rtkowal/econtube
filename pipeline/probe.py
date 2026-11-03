"""Step 1: probe every source and write reports/probe.md (+ reports/probe.json).

For each source: verify candidate feeds/sitemaps, count reachable posts, estimate YouTube
and podcast links from a sample, discover YouTube channels / podcast feeds linked from the
homepage, and (if YOUTUBE_API_KEY is set) resolve channels to titles and upload counts.

Never fails the whole run because one source fails.

    python pipeline/probe.py                # all sources
    python pipeline/probe.py --only marginal-revolution,hoover
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import traceback
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse

import feedparser
import yaml
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from econtube.extract import extract_refs  # noqa: E402
from econtube.http import Blocked, Client  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
YT_KEY = os.environ.get("YOUTUBE_API_KEY")
SAMPLE_PAGES = 15  # sitemap/html pages fetched per source to estimate link density

CHANNEL_RE = re.compile(
    r"youtube\.com/(?:(channel/UC[\w-]{22})|(@[\w.-]+)|(?:c|user)/([\w.-]+))", re.I)


def yt_api(c: Client, endpoint: str, **params) -> dict:
    params["key"] = YT_KEY
    q = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    r = c.s.get(f"https://www.googleapis.com/youtube/v3/{endpoint}?{q}", timeout=30)
    r.raise_for_status()
    return r.json()


def resolve_channel(c: Client, token: str) -> dict | None:
    """token: 'channel/UC..', '@handle' or legacy username."""
    if not YT_KEY:
        return None
    part = "snippet,statistics,contentDetails"
    if token.startswith("channel/"):
        j = yt_api(c, "channels", part=part, id=token.split("/", 1)[1])
    elif token.startswith("@"):
        j = yt_api(c, "channels", part=part, forHandle=token)
    else:
        j = yt_api(c, "channels", part=part, forUsername=token)
    items = j.get("items") or []
    if not items:
        return None
    it = items[0]
    return {"id": it["id"], "title": it["snippet"]["title"],
            "videos": int(it["statistics"].get("videoCount", 0)),
            "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"]}


def resolve_playlist(c: Client, pid: str) -> dict | None:
    if not YT_KEY:
        return None
    j = yt_api(c, "playlists", part="snippet,contentDetails", id=pid)
    items = j.get("items") or []
    if not items:
        return None
    return {"id": pid, "title": items[0]["snippet"]["title"],
            "channel": items[0]["snippet"]["channelTitle"],
            "videos": items[0]["contentDetails"]["itemCount"]}


def itunes_search(c: Client, term: str) -> list[dict]:
    r = c.s.get("https://itunes.apple.com/search",
                params={"term": term, "media": "podcast", "limit": 5}, timeout=30)
    r.raise_for_status()
    return [{"name": x.get("collectionName"), "feed": x.get("feedUrl"),
             "episodes": x.get("trackCount"), "artist": x.get("artistName")}
            for x in r.json().get("results", []) if x.get("feedUrl")]


def count_sitemap(c: Client, url: str, depth: int = 0, cap: int = 60) -> tuple[int, list[str]]:
    """Return (#page URLs, sample page URLs). Follows sitemap indexes up to `cap` children."""
    r = c.get(url)
    if r is None or not r.ok or b"<" not in r.content[:200]:
        return 0, []
    soup = BeautifulSoup(r.content, "xml")
    if soup.find("sitemapindex"):
        total, sample = 0, []
        children = [l.text.strip() for l in soup.find_all("loc")]
        # prefer post sitemaps
        children.sort(key=lambda u: 0 if re.search(r"post|article|blog|video", u) else 1)
        for ch in children[:cap]:
            if depth < 2:
                n, s = count_sitemap(c, ch, depth + 1, cap)
                total += n
                sample += s[:3]
        return total, sample
    locs = [l.text.strip() for l in soup.find_all("loc")]
    return len(locs), locs[-5:]


def probe_source(c: Client, s: dict) -> dict:
    row: dict = {"id": s["id"], "name": s["name"], "route": None, "feed_ok": [],
                 "feed_failed": [], "posts_reachable": 0, "sample_pages": 0,
                 "yt_links": 0, "pod_links": 0, "vimeo": 0, "est_yt_total": None,
                 "channels": [], "podcasts": [], "errors": []}
    # 1. candidate feeds / sitemaps
    sample_urls: list[str] = []
    feed_entries = []
    for f in s.get("feeds", []) or []:
        try:
            if "sitemap" in f:
                n, smp = count_sitemap(c, f)
                if n:
                    row["feed_ok"].append(f"{f} ({n} urls)")
                    row["posts_reachable"] = max(row["posts_reachable"], n)
                    row["route"] = row["route"] or "sitemap"
                    sample_urls += smp
                else:
                    row["feed_failed"].append(f)
            else:
                r = c.get(f)
                d = feedparser.parse(r.content if r is not None else b"")
                if d.entries:
                    row["feed_ok"].append(f"{f} ({len(d.entries)} items)")
                    row["route"] = row["route"] or "rss"
                    feed_entries += d.entries
                    row["posts_reachable"] = max(row["posts_reachable"], len(d.entries))
                else:
                    row["feed_failed"].append(f)
        except Blocked as e:
            row["errors"].append(str(e))
            row["feed_failed"].append(f)
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"{f}: {type(e).__name__}: {e}"[:200])
            row["feed_failed"].append(f)

    # 2. link density from feed bodies (+ a few HTML pages)
    blobs = []
    for e in feed_entries:
        blobs.append(" ".join([e.get("link", ""), e.get("summary", "")] +
                              [x.get("value", "") for x in e.get("content", [])] +
                              [x.get("href", "") for x in e.get("enclosures", [])]))
    pages = 0
    for u in sample_urls[:SAMPLE_PAGES] if not feed_entries else []:
        try:
            r = c.get(u)
            if r is not None and r.ok:
                blobs.append(r.text)
                pages += 1
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"{u}: {e}"[:200])
    n_blobs = len(blobs)
    yt = pod = vim = 0
    for b in blobs:
        refs = extract_refs(b)
        yt += sum(r.kind in ("youtube_video", "youtube_playlist") for r in refs)
        pod += sum(r.kind in ("podcast", "audio_file") for r in refs)
        vim += sum(r.kind == "vimeo" for r in refs)
    row.update(sample_pages=n_blobs, yt_links=yt, pod_links=pod, vimeo=vim)
    if n_blobs and row["posts_reachable"]:
        row["est_yt_total"] = round(yt / n_blobs * row["posts_reachable"])

    # 3. channel discovery from the homepage + explicit config
    tokens: set[str] = set()
    for ch in s.get("youtube_channels", []) or []:
        tokens.add(f"channel/{ch['id']}")
    tokens.update(s.get("youtube_handles", []) or [])
    try:
        home = c.get(s["url"]) if s["url"].startswith("http") and "youtube.com" not in s["url"] else None
        if home is not None and home.ok:
            for m in CHANNEL_RE.finditer(home.text):
                tokens.add(m.group(1) or m.group(2) or m.group(3))
            if row["route"] is None:
                row["route"] = "html"
                hrefs = {urljoin(s["url"], a.get("href")) for a in
                         BeautifulSoup(home.text, "html.parser").find_all("a", href=True)}
                row["posts_reachable"] = len([h for h in hrefs if urlparse(h).netloc == urlparse(s["url"]).netloc])
                refs = extract_refs(home.text)
                row["yt_links"] += sum(r.kind.startswith("youtube") for r in refs)
                row["sample_pages"] += 1
    except Exception as e:  # noqa: BLE001
        row["errors"].append(f"home: {type(e).__name__}: {e}"[:200])
    for t in sorted(tokens):
        info = None
        try:
            info = resolve_channel(c, t)
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"yt {t}: {e}"[:200])
        explicit = t in (s.get("youtube_handles") or []) or any(
            t == f"channel/{x['id']}" for x in s.get("youtube_channels", []) or [])
        row["channels"].append({"token": t, **(info or {}),
                                "verified": explicit,  # homepage-linked => review
                                "found_on": "config" if explicit else "homepage"})
    for pl in s.get("youtube_playlists", []) or []:
        try:
            row["channels"].append({"token": f"playlist/{pl}", **(resolve_playlist(c, pl) or {}),
                                    "verified": True, "found_on": "config"})
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"playlist {pl}: {e}"[:200])
    if row["channels"] and row["route"] is None:
        row["route"] = "youtube_channel"

    # 4. podcast discovery (iTunes) for sources that plausibly have one
    if s.get("type") in ("rss", "youtube_channel", "curated_list") and not s["name"].startswith("TBD"):
        try:
            hits = itunes_search(c, s["name"].split(" - ")[0])
            row["podcasts"] = [dict(h, verified=False) for h in hits[:2]]
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"itunes: {e}"[:200])
    return row


def render(rows: list[dict]) -> str:
    out = ["# Source probe\n",
           "| source | route | posts reachable | sample | YT links | pod links | est. YT total | YT channels | podcasts | notes |",
           "|---|---|---:|---:|---:|---:|---:|---|---|---|"]
    for r in rows:
        ch = "<br>".join(f"{c.get('title') or c['token']} ({c.get('videos', '?')} vids){'' if c['verified'] else ' ⚠unverified'}"
                         for c in r["channels"]) or "—"
        pod = "<br>".join(f"{p['name']} ({p.get('episodes')} eps) ⚠" for p in r["podcasts"]) or "—"
        notes = "; ".join(r["errors"])[:160] or ""
        out.append(f"| {r['name']} | {r['route'] or 'BLOCKED/none'} | {r['posts_reachable']} | {r['sample_pages']} | "
                   f"{r['yt_links']} | {r['pod_links']} | {r['est_yt_total'] or '—'} | {ch} | {pod} | {notes} |")
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    a = ap.parse_args()
    cfg = yaml.safe_load((ROOT / "sources.yaml").read_text())
    sources = [s for s in cfg["sources"] if s["id"] != "seeds"]
    if a.only:
        keep = set(a.only.split(","))
        sources = [s for s in sources if s["id"] in keep]
    c = Client()
    rows = []
    for s in sources:
        print(f"probing {s['id']} ...", flush=True)
        try:
            rows.append(probe_source(c, s))
        except Exception:  # noqa: BLE001
            rows.append({"id": s["id"], "name": s["name"], "route": None, "posts_reachable": 0,
                         "sample_pages": 0, "yt_links": 0, "pod_links": 0, "est_yt_total": None,
                         "channels": [], "podcasts": [], "errors": [traceback.format_exc()[-200:]]})
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports/probe.json").write_text(json.dumps(rows, indent=1, default=str))
    (ROOT / "reports/probe.md").write_text(render(rows))
    print(render(rows))


if __name__ == "__main__":
    main()
