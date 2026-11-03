"""Ranking. All tunable constants live here; see OPERATIONS.md.

score = sum over DISTINCT recommending sources of
            source_weight * kind_multiplier * recency_decay(post_date)
        + VIEWS_COEF * log10(1 + views)

* Distinct sources, not posts: Marginal Revolution linking the same video
  five times counts once (its most recent post, i.e. the max contribution).
* kind_multiplier: a source's OWN channel/podcast = SELF_MULT (self-promotion);
  a third-party video linked/embedded in a post = EDITORIAL_MULT (editorial pick).
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime

SELF_MULT = 1.0          # source's own YouTube channel / podcast feed
EDITORIAL_MULT = 1.5     # third-party item linked/embedded in a curator post
HALF_LIFE_DAYS = 730     # recency half-life of a recommendation (2 years)
DECAY_FLOOR = 0.25       # old recommendations never fall below 25% (classics stay visible)
VIEWS_COEF = 0.05        # 1M views adds +0.3; deliberately small


@dataclass(frozen=True)
class Rec:
    source_id: str
    weight: float
    post_date: date | None
    editorial: bool  # True = linked in a post; False = source's own channel/feed


def recency_decay(post_date: date | None, today: date) -> float:
    if post_date is None:
        return DECAY_FLOOR
    if isinstance(post_date, datetime):
        post_date = post_date.date()
    age = max(0, (today - post_date).days)
    return max(DECAY_FLOOR, 0.5 ** (age / HALF_LIFE_DAYS))


def contribution(r: Rec, today: date) -> float:
    mult = EDITORIAL_MULT if r.editorial else SELF_MULT
    return r.weight * mult * recency_decay(r.post_date, today)


def score(recs: list[Rec], views: int | None, today: date) -> float:
    best: dict[str, float] = {}
    for r in recs:
        c = contribution(r, today)
        if c > best.get(r.source_id, -1.0):
            best[r.source_id] = c
    s = sum(best.values())
    if views and views > 0:
        s += VIEWS_COEF * math.log10(1 + views)
    return round(s, 4)
