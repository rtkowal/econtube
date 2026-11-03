"""Extract YouTube, podcast and Vimeo references from HTML/text.

Pure functions, no I/O, so they are cheap to test exhaustively.
"""
from __future__ import annotations

import html
import re
from dataclasses import dataclass
from urllib.parse import parse_qs, unquote, urlparse

YT_ID = r"[A-Za-z0-9_-]{11}"
_VIDEO_ID_RE = re.compile(rf"^{YT_ID}$")
_PLAYLIST_ID_RE = re.compile(r"^(PL|UU|LL|FL|OL|RD|UL|PU)[A-Za-z0-9_-]{10,}$")

YT_HOSTS = {
    "youtube.com", "www.youtube.com", "m.youtube.com",
    "youtube-nocookie.com", "www.youtube-nocookie.com",
}
YT_SHORT_HOSTS = {"youtu.be", "www.youtu.be"}

# Any URL-ish token (also catches iframe src / data-src / bare text links).
_URL_RE = re.compile(r"""(?:https?:)?//[^\s"'<>()\[\]{}]+""", re.I)

PODCAST_HOSTS = {
    "podcasts.apple.com": "apple",
    "itunes.apple.com": "apple",
    "open.spotify.com": "spotify",
    "overcast.fm": "overcast",
    "pca.st": "pocketcasts",
    "pocketcasts.com": "pocketcasts",
    "play.pocketcasts.com": "pocketcasts",
}


@dataclass(frozen=True)
class Ref:
    kind: str          # youtube_video | youtube_playlist | podcast | audio_file | vimeo
    id: str            # video id, playlist id, or canonical URL
    url: str           # the URL as found (normalised to https)
    platform: str = "" # for podcasts: apple/spotify/overcast/pocketcasts
    start: int | None = None  # t= seconds, if present


def _norm(url: str) -> str:
    url = html.unescape(url).strip().rstrip(".,;:!?")
    if url.startswith("//"):
        url = "https:" + url
    return url


def _parse_t(v: str | None) -> int | None:
    if not v:
        return None
    if v.isdigit():
        return int(v)
    m = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s?)?", v)
    if not m or not any(m.groups()):
        return None
    h, mi, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mi * 60 + s


def parse_youtube(url: str) -> list[Ref]:
    """Return refs for one URL (a watch URL with &list= yields both video and playlist)."""
    url = _norm(url)
    p = urlparse(url)
    host = (p.hostname or "").lower()
    q = parse_qs(p.query)
    out: list[Ref] = []
    vid: str | None = None
    start = _parse_t((q.get("t") or q.get("start") or [None])[0])

    if host in YT_SHORT_HOSTS:
        seg = p.path.lstrip("/").split("/")[0]
        vid = seg if _VIDEO_ID_RE.match(seg) else None
    elif host in YT_HOSTS:
        parts = [s for s in p.path.split("/") if s]
        if parts and parts[0] == "watch":
            vid = (q.get("v") or [None])[0]
        elif parts and parts[0] in {"embed", "shorts", "live", "v", "e"} and len(parts) > 1:
            vid = parts[1]
        elif parts and parts[0] == "attribution_link":
            inner = unquote((q.get("u") or [""])[0])
            return parse_youtube("https://www.youtube.com" + inner) if inner.startswith("/") else []
        elif parts and parts[0] == "oembed":
            inner = (q.get("url") or [""])[0]
            return parse_youtube(inner) if inner else []
        if vid and not _VIDEO_ID_RE.match(vid):
            vid = None
        # embed/videoseries?list=... and /playlist?list=...
        if parts and parts[:2] == ["embed", "videoseries"]:
            vid = None
    else:
        return []

    if vid:
        out.append(Ref("youtube_video", vid, url, start=start))
    lst = (q.get("list") or [None])[0]
    if lst and _PLAYLIST_ID_RE.match(lst) and not lst.startswith("RD"):  # RD = auto mixes
        out.append(Ref("youtube_playlist", lst, url))
    return out


def parse_podcast(url: str) -> Ref | None:
    url = _norm(url)
    p = urlparse(url)
    host = (p.hostname or "").lower()
    plat = PODCAST_HOSTS.get(host)
    path = p.path.lower()
    if plat == "spotify":
        if path.startswith(("/episode/", "/show/")):
            return Ref("podcast", url.split("?")[0], url, platform="spotify")
        return None
    if plat == "apple":
        if "/podcast/" in path:
            return Ref("podcast", url.split("#")[0], url, platform="apple")
        return None
    if plat:
        return Ref("podcast", url.split("?")[0], url, platform=plat)
    if re.search(r"\.(mp3|m4a)$", path):
        return Ref("audio_file", url.split("#")[0], url)
    return None


def parse_vimeo(url: str) -> Ref | None:
    url = _norm(url)
    p = urlparse(url)
    host = (p.hostname or "").lower()
    if host in {"vimeo.com", "www.vimeo.com", "player.vimeo.com"}:
        m = re.search(r"/(?:video/)?(\d{5,})", p.path)
        if m:
            return Ref("vimeo", m.group(1), url)
    return None


# Embed proxies wrap the real URL, percent-encoded, in a query param:
# cdn.iframe.ly/api/iframe?url=..., Drupal /media/oembed?url=..., embedly ?src=...
_WRAP_PARAMS = ("url", "src", "u")


def unwrap(url: str) -> str:
    p = urlparse(_norm(url))
    host = (p.hostname or "").lower()
    if host in YT_HOSTS or host in YT_SHORT_HOSTS:
        return url
    q = parse_qs(p.query)
    for k in _WRAP_PARAMS:
        v = (q.get(k) or [""])[0]
        if v.startswith(("http://", "https://", "//")):
            return unwrap(v)
    return url


# Never extract from page chrome: a blogroll in a sidebar is not an editorial pick.
CHROME_TAGS = ("header", "footer", "aside", "nav")
BODY_SELECTORS = ("article .entry-content", ".entry-content", ".post-body", ".post-content",
                  ".body.markup", "article", "main")


def post_body(page_html: str) -> str:
    """Return the HTML of the post body only (chrome removed). Falls back to whole page minus chrome."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_html, "html.parser")
    for t in soup.find_all(CHROME_TAGS):
        t.decompose()
    for el in soup.select('[class*="sidebar"], [id*="sidebar"], [class*="widget"], [class*="blogroll"]'):
        el.decompose()
    for sel in BODY_SELECTORS:
        hits = soup.select(sel)
        if hits:
            return "".join(str(h) for h in hits)
    return str(soup)


def extract_refs(text: str) -> list[Ref]:
    """All distinct refs in an HTML/text blob, in order of first appearance."""
    seen: set[tuple[str, str]] = set()
    out: list[Ref] = []
    for m in _URL_RE.finditer(html.unescape(text or "")):
        raw = unwrap(m.group(0))
        refs = parse_youtube(raw)
        if not refs:
            r = parse_podcast(raw) or parse_vimeo(raw)
            refs = [r] if r else []
        for r in refs:
            key = (r.kind, r.id)
            if key not in seen:
                seen.add(key)
                out.append(r)
    return out
