from econtube import classify as C

TAX = C.load_taxonomy()


def good():
    return {"is_recommendation": True,
            "fields": [{"v": "monetary-policy", "c": 0.9}], "topics": [{"v": "inflation", "c": 0.8}],
            "schools": [{"v": "chicago-monetarist", "c": 0.7}], "eras": [{"v": "1970s", "c": 0.9}],
            "regions": [{"v": "us", "c": 0.95}], "format": {"v": "lecture", "c": 0.9},
            "level": {"v": "introductory", "c": 0.55}, "people": {"speakers": ["Milton Friedman"], "discussed": []},
            "tags": ["Phillips Curve", "money supply", "phillips curve"], "one_line_why": "Friedman explains inflation plainly."}


def test_taxonomy_loads_and_is_nonempty():
    assert {"fields", "topics", "schools", "eras", "regions", "format", "level"} <= TAX.keys()
    assert "nobel-lecture" in TAX["format"] and "austrian" in TAX["schools"]


def test_valid_output_has_no_errors():
    assert C._validate(good(), TAX) == []


def test_out_of_vocab_rejected_and_logged(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    o = good()
    o["topics"].append({"v": "made-up-topic", "c": 0.9})
    o["format"] = {"v": "vlog", "c": 0.9}
    assert len(C._validate(o, TAX)) == 2
    cleaned = C._clean(o, TAX, "x1")
    assert [t["v"] for t in cleaned["topics"]] == ["inflation"] and cleaned["format"] is None
    assert (tmp_path / "taxonomy_suggestions.jsonl").read_text().count("\n") == 2


def test_tags_normalised_and_low_confidence_hidden(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    v = C.visible(C._clean(good(), TAX, "x2"))
    assert v["tags"] == ["money supply", "phillips curve"]
    assert v["level"] is None and v["format"] == "lecture"   # 0.55 < SHOW_MIN


def test_overrides_win(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    (tmp_path / "overrides.yaml").write_text("x3:\n  schools: [austrian]\n  level: expert\n")
    out = C.apply_overrides("x3", C._clean(good(), TAX, "x3"))
    assert out["schools"] == [{"v": "austrian", "c": 1.0}] and out["level"] == {"v": "expert", "c": 1.0}


def test_single_facets_wrapped_in_list_are_accepted(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    o = good()
    o["format"] = [{"v": "podcast-episode", "c": 0.9}]
    o["level"] = [{"v": "intermediate", "c": 0.6}, {"v": "expert", "c": 0.3}]
    assert C._validate(o, TAX) == []
    cl = C._clean(o, TAX, "x4")
    assert cl["format"]["v"] == "podcast-episode" and cl["level"]["v"] == "intermediate"
    assert not (tmp_path / "taxonomy_suggestions.jsonl").exists()


def test_source_name_tags_dropped(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    o = good()
    o["tags"] = ["marginal-revolution", "Hoover Institution", "economic-growth"]
    cl = C._clean(o, TAX, "x5", {"Marginal Revolution", "Hoover Institution"})
    assert cl["tags"] == ["economic growth"]
