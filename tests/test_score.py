from datetime import date, timedelta

from econtube import score as S
from econtube.score import Rec, recency_decay, score

T = date(2026, 11, 3)


def test_distinct_sources_not_posts():
    one = [Rec("mr", 3.0, T, True)]
    dup = one * 5
    assert score(dup, None, T) == score(one, None, T)


def test_more_curators_beats_one():
    a = [Rec("mr", 1, T, True)]
    b = a + [Rec("hayek", 1, T, True)]
    assert score(b, None, T) > score(a, None, T)


def test_editorial_beats_self():
    assert score([Rec("x", 1, T, True)], None, T) == S.EDITORIAL_MULT
    assert score([Rec("x", 1, T, False)], None, T) == S.SELF_MULT


def test_decay_half_life_and_floor():
    assert recency_decay(T, T) == 1.0
    assert abs(recency_decay(T - timedelta(days=S.HALF_LIFE_DAYS), T) - 0.5) < 1e-9
    assert recency_decay(date(1990, 1, 1), T) == S.DECAY_FLOOR
    assert recency_decay(None, T) == S.DECAY_FLOOR
    assert recency_decay(T + timedelta(days=3), T) == 1.0  # future dates clamp


def test_same_source_keeps_best_post():
    recs = [Rec("mr", 1, date(2000, 1, 1), True), Rec("mr", 1, T, True)]
    assert score(recs, None, T) == S.EDITORIAL_MULT


def test_views_small_term():
    base = score([Rec("x", 1, T, True)], None, T)
    with_views = score([Rec("x", 1, T, True)], 1_000_000, T)
    assert 0 < with_views - base < 0.5
    # views can't overturn a second curator
    assert score([Rec("a", 1, T, True)], 10**9, T) < score(
        [Rec("a", 1, T, True), Rec("b", 1, T, True)], 0, T)
