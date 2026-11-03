"""YouTube Data API v3 (key auth). Quota-aware; every call counted against a per-run budget.

Costs (units): channels.list 1, playlistItems.list 1 (50 items), videos.list 1 (50 ids), search.list 100.
Default daily quota 10,000. QUOTA_BUDGET caps one run so the daily cron never exhausts it.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import requests

API = "https://www.googleapis.com/youtube/v3"
CACHE = Path(os.environ.get("ECONTUBE_CACHE", ".cache"))
BUDGET = int(os.environ.get("QUOTA_BUDGET", "8000"))
used = 0


class QuotaExceeded(Exception):
    pass


def available() -> bool:
    return bool(os.environ.get("YOUTUBE_API_KEY"))


def _get(endpoint: str, cost: int = 1, **params) -> dict:
    global used
    if used + cost > BUDGET:
        raise QuotaExceeded(f"run budget {BUDGET} reached")
    params["key"] = os.environ["YOUTUBE_API_KEY"]
    r = requests.get(f"{API}/{endpoint}", params=params, timeout=30)
    used += cost
    if r.status_code == 403 and "quota" in r.text.lower():
        raise QuotaExceeded("daily quota exhausted")
    r.raise_for_status()
    return r.json()


def channel(cid: str | None = None, handle: str | None = None) -> dict | None:
    p = {"id": cid} if cid else {"forHandle": handle}
    items = _get("channels", part="snippet,contentDetails,statistics", **p).get("items") or []
    if not items:
        return None
    it = items[0]
    return {"id": it["id"], "title": it["snippet"]["title"], "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"],
            "videos": int(it["statistics"].get("videoCount", 0))}


def playlist_ids(pid: str, known: set[str] | None = None, max_pages: int = 400) -> list[dict]:
    """All items of a playlist, newest first. Stops early when a page is entirely `known` (incremental)."""
    out, token = [], None
    for _ in range(max_pages):
        j = _get("playlistItems", part="snippet,contentDetails", playlistId=pid, maxResults=50, **({"pageToken": token} if token else {}))
        page = [{"id": x["contentDetails"]["videoId"], "title": x["snippet"].get("title", ""),
                 "desc": x["snippet"].get("description", "")[:600], "channel": x["snippet"].get("videoOwnerChannelTitle") or x["snippet"].get("channelTitle", ""),
                 "published": (x["contentDetails"].get("videoPublishedAt") or x["snippet"].get("publishedAt", ""))[:10]}
                for x in j.get("items", []) if x["snippet"].get("title") not in ("Private video", "Deleted video")]
        out += page
        if known is not None and page and all(p["id"] in known for p in page):
            break
        token = j.get("nextPageToken")
        if not token:
            break
    return out


def _secs(iso: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def videos(ids: list[str]) -> dict[str, dict]:
    """Enrich ids (cached forever except view counts, refreshed when re-requested)."""
    p = CACHE / "yt_videos.json"
    cache = json.loads(p.read_text()) if p.exists() else {}
    todo = [i for i in dict.fromkeys(ids) if i not in cache]
    try:
        for k in range(0, len(todo), 50):
            batch = todo[k:k + 50]
            j = _get("videos", part="snippet,contentDetails,statistics,status", id=",".join(batch))
            seen = set()
            for v in j.get("items", []):
                seen.add(v["id"])
                cache[v["id"]] = {"title": v["snippet"]["title"], "channel": v["snippet"]["channelTitle"],
                                  "published": v["snippet"]["publishedAt"][:10], "desc": v["snippet"].get("description", "")[:600],
                                  "duration": _secs(v["contentDetails"].get("duration", "")),
                                  "views": int(v.get("statistics", {}).get("viewCount", 0) or 0),
                                  "embeddable": bool(v["status"].get("embeddable")) and v["status"].get("privacyStatus") == "public",
                                  "lang": v["snippet"].get("defaultAudioLanguage") or v["snippet"].get("defaultLanguage")}
            for i in batch:
                if i not in seen:
                    cache[i] = {"gone": True}   # private/deleted
    finally:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(cache))
    return {i: cache[i] for i in ids if i in cache}
