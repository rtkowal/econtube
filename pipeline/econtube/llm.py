"""Minimal OpenAI client (Chat Completions, JSON mode) via requests - no SDK dependency.

Model choice: OPENAI_MODEL / OPENAI_MODEL_STRONG env vars win. Otherwise we list the models this key
can use (GET /v1/models) and take the first match from the preference lists below, so we never
hard-code a model that has been retired. Every call is logged to .cache/llm_cost.jsonl (tokens).
"""
from __future__ import annotations

import json
import os
import re
import time
from functools import lru_cache
from pathlib import Path

import requests

API = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
# Cheapest-first patterns. Edit freely; first model the key can see wins.
CHEAP_PREF = [r"^gpt-[\d.]+-nano$", r"^gpt-[\d.]+-mini$", r"^gpt-4o-mini$"]
STRONG_PREF = [r"^gpt-[\d.]+-mini$", r"^gpt-[\d.]+$", r"^gpt-4o$"]
LOG = Path(os.environ.get("ECONTUBE_CACHE", ".cache")) / "llm_cost.jsonl"


class LLMError(Exception):
    pass


def _key() -> str:
    k = os.environ.get("OPENAI_API_KEY")
    if not k:
        raise LLMError("OPENAI_API_KEY not set")
    return k


def available() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


@lru_cache(maxsize=1)
def _models() -> list[str]:
    r = requests.get(f"{API}/models", headers={"Authorization": f"Bearer {_key()}"}, timeout=30)
    r.raise_for_status()
    ids = [m["id"] for m in r.json().get("data", [])]

    def ver(m: str) -> tuple:  # newest version first within a pattern
        return tuple(int(x) for x in re.findall(r"\d+", m)) or (0,)
    return sorted(ids, key=ver, reverse=True)


def pick(strong: bool = False) -> str:
    env = os.environ.get("OPENAI_MODEL_STRONG" if strong else "OPENAI_MODEL")
    if env:
        return env
    ids = _models()
    for pat in STRONG_PREF if strong else CHEAP_PREF:
        for m in ids:
            if re.match(pat, m):
                return m
    raise LLMError(f"no preferred model available; set OPENAI_MODEL. Seen: {ids[:20]}")


def chat_json(system: str, user: str, *, strong: bool = False, max_tokens: int = 1200, tag: str = "") -> dict:
    """One JSON-mode call. Retries on 429/5xx with backoff. Returns the parsed object."""
    model = pick(strong)
    body = {"model": model, "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "max_completion_tokens": max_tokens}
    for attempt in range(5):
        r = requests.post(f"{API}/chat/completions", json=body, timeout=120,
                          headers={"Authorization": f"Bearer {_key()}"})
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(2 ** attempt * 2)
            continue
        if not r.ok:
            raise LLMError(f"{r.status_code}: {r.text[:300]}")
        j = r.json()
        u = j.get("usage", {})
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a") as f:
            f.write(json.dumps({"t": int(time.time()), "model": model, "tag": tag,
                                "in": u.get("prompt_tokens"), "out": u.get("completion_tokens")}) + "\n")
        txt = j["choices"][0]["message"]["content"] or "{}"
        try:
            return json.loads(txt)
        except json.JSONDecodeError as e:
            raise LLMError(f"bad JSON from model: {txt[:200]}") from e
    raise LLMError("rate-limited after retries")
