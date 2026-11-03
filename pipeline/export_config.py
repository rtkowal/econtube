"""Export sources.yaml + site.yaml to data/*.json so the static site build needs only the stdlib."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
src = yaml.safe_load((ROOT / "sources.yaml").read_text())["sources"]
keep = ("id", "name", "url", "type", "language", "weight", "status", "notes")
(ROOT / "data/sources.json").write_text(json.dumps([{k: s[k] for k in keep if k in s} for s in src], ensure_ascii=False, indent=1))
(ROOT / "data/site.json").write_text(json.dumps(yaml.safe_load((ROOT / "site.yaml").read_text()) or {}, indent=1))
print("exported", len(src), "sources")
