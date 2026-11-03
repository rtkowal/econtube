import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
import facets as F  # noqa: E402
import yaml  # noqa: E402

TAX = yaml.safe_load((ROOT / "taxonomy.yaml").read_text())


def test_every_topic_has_a_family():
    fam = F.topic_families(TAX)
    missing = [t["slug"] for t in TAX["topics"] if t["slug"] not in fam]
    assert missing == [], missing
    assert fam["inflation"] == "money-macro" and fam["bitcoin"] == "bitcoin" and fam["ai-economy"] == "tech-business"


def test_slug():
    assert F.slug("Friedrich von Hayek") == "friedrich-von-hayek"
    assert F.slug("Leszek Balcerowicz") == "leszek-balcerowicz"
    assert F.slug("Ł. Łódź Économie") == "l-lodz-economie" or F.slug("Ł. Łódź Économie").endswith("economie")


def item(i, topics, people=(), tags=()):
    return {"id": f"v{i}", "kind": "video", "title": f"T{i}", "channel": "C", "score": i, "sources": [{"name": "S"}],
            "facets": {"topics": list(topics)}, "people": {"speakers": list(people)}, "tags": list(tags)}


def test_index_thresholds_and_slim():
    items = [item(i, ["inflation"], ["Milton Friedman"] if i < 2 else [], ["qe"] if i < 5 else []) for i in range(6)]
    ix = F.Index(items, TAX)
    assert ix.has_page("topic", "inflation")
    assert ix.has_page("person", "milton-friedman")          # 2 items >= PERSON_MIN
    assert ix.has_page("tag", "qe")                           # 5 items >= TAG_MIN
    s = F.slim(items[0])
    assert s["t"] == ["inflation"] and s["p"] == ["Milton Friedman"] and "desc" not in s
    json.dumps(s)
