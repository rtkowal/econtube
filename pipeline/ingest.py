"""Stage 1+2: fetch posts from a source and extract video/podcast references.

Idempotent and resumable: every post is stored once in data/raw/<source>/posts.jsonl keyed by URL;
already-fetched URLs are skipped. Failure on one URL or source never stops the run.
Raw HTML lives in the uncommitted .cache/ (see http.py); only extracted refs + ~600 chars of
surrounding context per link (for the classifier, never published) are written.

    python pipeline/ingest.py marginal-revolution --limit 300      # newest N from sitemap
    python pipeline/ingest.py hoover nobel-economics --limit 200
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import feedparser
import yaml
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from econtube.extract import extract_refs, post_body  # noqa: E402
from econtube.http import Blocked, Client  # noqa: E402
from probe import count_sitemap  # noqa: E402,F401

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
CTX = 300  # chars of text either side of a link, given to the classifier


def sitemap_urls(c: Client, url: str, depth: int = 0) -> list[str]:
    r = c.get(url)
    if r is None or not r.ok:
        return []
    soup = BeautifulSoup(r.content, "xml")
    locs = [l.text.strip() for l in soup.find_all("loc")]
    if soup.find("sitemapindex"):
        out: list[str] = []
        for ch in locs:
            if depth < 2 and not re.search(r"(category|tag|author|page|attachment)", ch):
                out += sitemap_urls(c, ch, depth + 1)
        return out
    return locs


def contexts(body_html: str) -> dict[str, str]:
    """Map each ref id -> plain text surrounding its first link (for the classifier)."""
    soup = BeautifulSoup(body_html, "html.parser")
    text_all = soup.get_text(" ", strip=True)
    title = ""
    out: dict[str, str] = {}
    for el in soup.find_all(["a", "iframe"]):
        href = el.get("href") or el.get("src") or el.get("data-src") or ""
        for r in extract_refs(href):
            if r.id in out:
                continue
            anchor = el.get_text(" ", strip=True) or el.get("title", "")
            i = text_all.find(anchor) if anchor else -1
            out[r.id] = text_all[max(0, i - CTX): i + len(anchor) + CTX] if i >= 0 else text_all[:2 * CTX]
    _ = title
    return out


def nobel_urls(c: Client) -> list[str]:
    """Nobel economics: one prize-lecture page per laureate year. Discovered from the yearly prize pages."""
    urls: list[str] = []
    for year in range(1969, 2026):
        urls.append(f"https://www.nobelprize.org/prizes/economic-sciences/{year}/summary/")
    return urls


def candidate_urls(c: Client, s: dict, limit: int) -> list[str]:
    if s["id"] == "nobel-economics":
        return nobel_urls(c)[-limit:]
    urls: list[str] = []
    for f in s.get("feeds", []) or []:
        try:
            if "sitemap" in f:
                urls += sitemap_urls(c, f)
            else:
                urls += [e.link for e in feedparser.parse(c.get(f).content).entries if e.get("link")]
        except Exception as e:  # noqa: BLE001
            print(f"  feed {f}: {e}", file=sys.stderr)
    seen, out = set(), []
    for u in urls:
        u = re.sub(r"^http://", "https://", u)
        if u not in seen and urlish_post(u, s):
            seen.add(u)
            out.append(u)
    # newest first: by /YYYY/MM/ in the path when present, otherwise keep sitemap order reversed
    def key(u: str) -> str:
        m = re.search(r"/(\d{4})/(\d{2})/", u)
        return m.group(1) + m.group(2) if m else ""
    out.reverse()
    out.sort(key=key, reverse=True)
    return out[:limit]


def urlish_post(u: str, s: dict) -> bool:
    if s["id"] == "marginal-revolution":
        return bool(re.search(r"/marginalrevolution/\d{4}/\d{2}/", u))
    if s["id"] == "hoover":
        return bool(re.search(r"/research/|/news/|/publications/|uncommon|goodfellows", u))
    return True


def ingest(c: Client, s: dict, limit: int) -> dict:
    d = RAW / s["id"]
    d.mkdir(parents=True, exist_ok=True)
    store = d / "posts.jsonl"
    done = {json.loads(l)["url"] for l in store.open()} if store.exists() else set()
    stats = {"new": 0, "skipped": len(done), "errors": 0, "refs": 0}
    with store.open("a") as fh:
        for u in candidate_urls(c, s, limit):
            if u in done:
                continue
            try:
                r = c.get(u)
                if r is None or not r.ok:
                    stats["errors"] += 1
                    continue
                soup = BeautifulSoup(r.text, "html.parser")
                title = (soup.find("meta", property="og:title") or {}).get("content") or (soup.title.string if soup.title else "")
                date = (soup.find("meta", property="article:published_time") or {}).get("content")
                body = post_body(r.text)
                refs = extract_refs(body)
                ctx = contexts(body)
                rec = {"url": u, "source": s["id"], "title": (title or "").strip(), "date": date,
                       "refs": [{"kind": x.kind, "id": x.id, "url": x.url, "platform": x.platform,
                                 "context": ctx.get(x.id, "")} for x in refs]}
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
                stats["new"] += 1
                stats["refs"] += len(refs)
            except Blocked as e:
                print(f"  blocked: {e}", file=sys.stderr)
                stats["errors"] += 1
            except Exception as e:  # noqa: BLE001
                print(f"  {u}: {type(e).__name__}: {e}", file=sys.stderr)
                stats["errors"] += 1
    return stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="+")
    ap.add_argument("--limit", type=int, default=200)
    a = ap.parse_args()
    cfg = {s["id"]: s for s in yaml.safe_load((ROOT / "sources.yaml").read_text())["sources"]}
    c = Client()
    for sid in a.sources:
        s = cfg[sid]
        if s.get("status") == "disabled":
            print(f"{sid}: disabled, skipping")
            continue
        try:
            print(sid, ingest(c, s, a.limit), flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"{sid}: FAILED {e}", flush=True)


if __name__ == "__main__":
    main()
