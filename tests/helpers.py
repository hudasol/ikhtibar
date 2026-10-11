import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))


def rows():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def by_id():
    return {r["row_id"]: r for r in rows()}


def stats():
    return json.loads((ROOT / "data" / "stats.json").read_text(encoding="utf-8"))
