"""Static site generator: data/videos.json -> dist/. No framework, no client-side templating for item pages."""
from __future__ import annotations

import html
import json
import shutil
from datetime import date
from pathlib import Path


import sys
sys.path.insert(0, str(Path(__file__).parent))
import facets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SITE, DIST = ROOT / "site", ROOT / "dist"
BASE = "https://econtube.org"
# stdlib only (Vercel's build image has no pip packages): config is pre-exported to JSON by pipeline/export_config.py
cfg_p = ROOT / "data/site.json"
CFG = json.loads(cfg_p.read_text()) if cfg_p.exists() else {}
e = lambda s: html.escape(str(s or ""), quote=True)  # noqa: E731


def page(title: str, body: str, *, desc: str = "", path: str = "/", extra_head: str = "", attrs: str = "", og_image: str = "") -> str:
    sponsor = CFG.get("sponsor")
    support = CFG.get("support_url")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><meta name="theme-color" content="#141413">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{BASE}{path}"><link rel="stylesheet" href="/style.css">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:site_name" content="EconTube">{f'<meta property="og:image" content="{e(og_image)}">' if og_image else ''}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ctext x='4' y='26' font-size='26' font-family='Georgia' fill='%23d98c6f'%3Ee%3C/text%3E%3C/svg%3E">
{extra_head}</head><body{attrs}><div class="wrap">
<header class="top"><a class="logo" href="/">Econ<i>Tube</i></a>
<nav class="tabs"><a href="/#foryou">For You</a><a href="/#top">Top</a><a href="/#new">New</a><a href="/topics/">Topics</a><a href="/browse/">Browse</a><a href="/sources/">Sources</a><a href="/about/">About</a></nav>
{'<label class="search"><input id="q" type="search" placeholder="Search  /" aria-label="Search"></label>' if path == "/" else ""}
</header>
{body}
<footer><span>Videos and episodes recommended by economists, blogs and institutions.</span>
<a href="/about/">How it works</a><a href="https://github.com/{e(CFG.get('repo', ''))}">Code &amp; data</a>
{f'<a href="{e(support)}">Support EconTube</a>' if support else ''}
{f'<span>EconTube is supported by {e(sponsor)}</span>' if sponsor else ''}</footer></div>
<div id="help"><kbd>j</kbd>/<kbd>k</kbd> move · <kbd>Enter</kbd> open · <kbd>/</kbd> search · <kbd>t</kbd> sources · <kbd>?</kbd> help</div>
<script src="/app.js" defer></script></body></html>"""


IX = None   # facets.Index, set in main()
_bp = ROOT / "data/books.json"
BOOKS = json.loads(_bp.read_text()) if _bp.exists() else {}


def book_link(it: dict) -> str:
    tag = CFG.get("amazon_tag")
    if not tag:
        return ""
    from urllib.parse import quote_plus
    ppl = it.get("people") or {}
    b = next((BOOKS.get("people", {})[n] for n in [*(ppl.get("speakers") or []), *(ppl.get("discussed") or [])] if n in BOOKS.get("people", {})), None)
    b = b or next((BOOKS.get("topics", {})[t] for t in (it.get("facets") or {}).get("topics") or [] if t in BOOKS.get("topics", {})), None)
    if not b:
        return ""
    url = f"https://www.amazon.com/s?k={quote_plus(b['title'] + ' ' + b['author'])}&tag={quote_plus(tag)}"
    return f'<p class="meta">Read: <a href="{e(url)}" rel="sponsored noopener">{e(b["title"])}</a> — {e(b["author"])}</p>'


def chips(it: dict) -> str:
    return facets.chips(IX, it) if IX else ""


def item_page(it: dict, related: list[dict]) -> str:
    vid = it["id"]
    if it["kind"] == "video":
        media = (f'<iframe class="player" src="https://www.youtube-nocookie.com/embed/{e(vid)}?rel=0" title="{e(it["title"])}" '
                 'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" loading="lazy"></iframe>')
        thumb = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    else:
        media = (f'<img class="art" src="{e(it.get("art"))}" alt="">'
                 f'<audio controls preload="none" src="{e(it["audio"])}"></audio>')
        thumb = it.get("art", "")
    if it.get("audio") and it["kind"] == "video":
        media += f'<p class="meta">Also as audio: <audio controls preload="none" src="{e(it["audio"])}"></audio></p>'
    srcs = "".join(f'<li><a href="{e(s["url"])}" rel="noopener">{e(s["name"])}</a>'
                   f'{" · " + e(s["date"]) if s.get("date") else ""}</li>' for s in it["sources"])
    rel = "".join(f'<li><a href="/v/{e(r["id"])}/">{e(r["title"])}</a> <span class="meta">— {e(r["channel"])}</span></li>' for r in related)
    why = it.get("why")
    ld = {"@context": "https://schema.org", "@type": "VideoObject" if it["kind"] == "video" else "PodcastEpisode",
          "name": it["title"], "description": it.get("desc") or it["title"], "thumbnailUrl": thumb,
          "uploadDate": it.get("published") or str(date.today())}
    if it["kind"] == "video":
        ld["embedUrl"] = f"https://www.youtube-nocookie.com/embed/{vid}"
    body = f"""<article class="item">{media}
<h1>{e(it["title"])}</h1><div class="meta">{e(it["channel"])}{" · " + e(it["published"]) if it.get("published") else ""}</div>
{f'<p class="why">{e(why)}</p>' if why else ''}
{chips(it)}
{book_link(it)}
<div class="thumbs"><button data-v="1">👍 More like this</button><button data-v="-1">👎 Less</button></div>
<h2>Recommended by</h2><ul class="src">{srcs}</ul>
{f'<h2>Related</h2><ul class="src">{rel}</ul>' if rel else ''}
</article>"""
    return page(f'{it["title"]} — EconTube', body, desc=it.get("desc") or f'Recommended by {", ".join(s["name"] for s in it["sources"])}',
                path=f"/v/{vid}/", og_image=thumb,
                extra_head=f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")}</script>',
                attrs=f' data-item="{e(vid)}" data-channel="{e(it["channel"])}"')


def main() -> None:
    data = json.loads((ROOT / "data/videos.json").read_text())
    items = data["items"]
    sources = [s for s in json.loads((ROOT / "data/sources.json").read_text()) if s.get("status") != "disabled"]
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "data").mkdir(parents=True)
    for f in ("style.css", "app.js", "browse.js"):
        shutil.copy(SITE / f, DIST / f)
    # slim client JSON (no descriptions)
    slim = [facets.slim(it) for it in items]
    (DIST / "data/videos.json").write_text(json.dumps({"items": slim}, ensure_ascii=False, separators=(",", ":")))
    shutil.copy(ROOT / "data/videos.json", DIST / "data/econtube-export.json")

    global IX
    tax = json.loads((ROOT / "data/taxonomy.json").read_text())
    facet_urls, IX = facets.write_all(DIST, items, tax, page, BASE)

    preview = ('<p class="note">Preview. Items are ranked by curator endorsements; topic tags, summaries and the full '
               'archive arrive once classification runs.</p>') if data.get("preview") else ""
    home = f"""{preview}<div class="bar"><button data-k="all">All</button><button data-k="video">Video</button><button data-k="audio">Audio</button>
<a id="reset" href="#" style="margin-left:auto">reset For You</a></div>
<main id="grid" class="grid" aria-live="polite"><p class="empty">Loading…</p></main>
<noscript>{"".join(f'<p><a href="/v/{e(i["id"])}/">{e(i["title"])}</a></p>' for i in items[:100])}</noscript>"""
    (DIST / "index.html").write_text(page("EconTube — economics videos, picked by economists", home,
        desc="Lectures, interviews, debates and podcasts on economics and finance, recommended by serious economics sources."))

    by_ch: dict[str, list] = {}
    for it in items:
        by_ch.setdefault(it["channel"], []).append(it)
    for it in items:
        rel = [r for r in by_ch[it["channel"]] if r["id"] != it["id"]][:6]
        d = DIST / "v" / it["id"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(item_page(it, rel))

    counts: dict[str, int] = {}
    for it in items:
        for s in {s["name"] for s in it["sources"]}:
            counts[s] = counts.get(s, 0) + 1
    rows = "".join(f'<tr><td><a href="{e(s["url"])}">{e(s["name"])}</a></td><td>{e(s.get("language","en")).upper()}</td>'
                   f'<td>{s.get("weight",1.0)}</td><td>{counts.get(s["name"],0)}</td></tr>' for s in sorted(sources, key=lambda x: -counts.get(x["name"], 0)))
    (DIST / "sources").mkdir()
    (DIST / "sources/index.html").write_text(page("Sources — EconTube", f"""<div class="prose"><h1>Sources</h1>
<p>Every item on EconTube is here because at least one of these sources linked to it, embedded it, or published it.</p>
<table><tr><th>Source</th><th>Lang</th><th>Weight</th><th>Items</th></tr>{rows}</table></div>""", path="/sources/",
        desc="The blogs, think tanks and institutions whose recommendations power EconTube."))

    (DIST / "about").mkdir()
    contact = CFG.get("contact_email", "")
    (DIST / "about/index.html").write_text(page("About — EconTube", f"""<div class="prose"><h1>About</h1>
<p>EconTube shows only economics and finance videos and podcast episodes that a hand-picked set of serious sources
(blogs, think tanks, universities, prize committees) has recommended, embedded or published. It is inspired by
Andrej Karpathy's HackerTube.</p>
<h2>Ranking</h2>
<p><code>score = Σ over distinct sources (source weight × kind × recency) + 0.05·log₁₀(views)</code></p>
<p>A video linked inside a curator's post counts 1.5× (an editorial pick). A source's own channel or podcast counts 1×.
Recommendations lose half their weight every two years but never fall below a quarter, so the classics stay visible.
Several independent curators beat one loud one.</p>
<h2>Privacy</h2><p>No accounts, no cookies, no ad networks. "For You" lives entirely in your browser's local storage;
the reset link clears it.</p>
<h2>Credit</h2><p>We never rehost video, audio or articles. Every item links back to the posts that recommended it.</p>
<p><a href="/data/econtube-export.json">Download the dataset</a> · <a href="/sources/">Sources</a>
{f' · <a href="mailto:{e(contact)}">{e(contact)}</a>' if contact else ''}</p>
<p class="note">Costs vs. revenue: {e(CFG.get("costs_line", "updated monthly by hand."))}</p></div>""", path="/about/",
        desc="How EconTube picks and ranks economics videos."))

    urls = ["/", "/about/", "/sources/"] + facet_urls + [f"/v/{it['id']}/" for it in items]
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + "".join(f"<url><loc>{BASE}{u}</loc></url>" for u in urls) + "</urlset>")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    (DIST / "404.html").write_text(page("Not found — EconTube", '<div class="prose"><h1>Not found</h1><p><a href="/">Back to EconTube</a></p></div>'))
    print(f"built {len(items)} item pages into {DIST}")


if __name__ == "__main__":
    main()
