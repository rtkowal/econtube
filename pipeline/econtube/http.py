"""Polite HTTP: honest UA, robots.txt, ~1 req/s per host, ETag/Last-Modified cache."""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlparse

import requests

UA = "EconTubeBot/1.0 (+https://www.econtube.org/about)"
CACHE = Path(os.environ.get("ECONTUBE_CACHE", ".cache/http"))
MIN_INTERVAL = 1.0


class Blocked(Exception):
    pass


class Client:
    def __init__(self) -> None:
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self._last: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        CACHE.mkdir(parents=True, exist_ok=True)

    def _wait(self, host: str) -> None:
        dt = time.monotonic() - self._last.get(host, 0)
        if dt < MIN_INTERVAL:
            time.sleep(MIN_INTERVAL - dt)
        self._last[host] = time.monotonic()

    def allowed(self, url: str) -> bool:
        p = urlparse(url)
        base = f"{p.scheme}://{p.netloc}"
        if base not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                self._wait(p.netloc)
                r = self.s.get(base + "/robots.txt", timeout=20)
                if r.status_code >= 400:
                    rp = None  # no robots.txt => allowed
                else:
                    rp.parse(r.text.splitlines())
            except requests.RequestException:
                rp = None
            self._robots[base] = rp
        rp = self._robots[base]
        return True if rp is None else rp.can_fetch(UA, url)

    def get(self, url: str, *, conditional: bool = True, timeout: int = 30) -> requests.Response | None:
        """Returns Response (status 200 or 304-served-from-cache) or raises Blocked."""
        if not self.allowed(url):
            raise Blocked(f"robots.txt disallows {url}")
        key = hashlib.sha256(url.encode()).hexdigest()
        meta_p, body_p = CACHE / f"{key}.json", CACHE / f"{key}.body"
        headers = {}
        if conditional and meta_p.exists():
            meta = json.loads(meta_p.read_text())
            if meta.get("etag"):
                headers["If-None-Match"] = meta["etag"]
            if meta.get("last_modified"):
                headers["If-Modified-Since"] = meta["last_modified"]
        self._wait(urlparse(url).netloc)
        r = self.s.get(url, headers=headers, timeout=timeout)
        if r.status_code == 304 and body_p.exists():
            r._content = body_p.read_bytes()
            r.status_code = 200
            r.from_cache = True  # type: ignore[attr-defined]
            return r
        if r.status_code in (401, 403, 429, 451):
            raise Blocked(f"HTTP {r.status_code} for {url}")
        if r.ok:
            body_p.write_bytes(r.content)
            meta_p.write_text(json.dumps({"url": url, "etag": r.headers.get("ETag"),
                                          "last_modified": r.headers.get("Last-Modified")}))
        return r
