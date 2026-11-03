#!/usr/bin/env python3
"""Phase 5: bring the primary test type of the new rows onto the table's code list.

The extraction brief listed a code set that differs from the table's (ROBU, SAFE, OTHER are not table codes). Mapping: ROBU -> ROB.
For rows whose extractor code is not a table code after that mapping, the code agreed by both blind coders is used;
where the coders disagree, the first coder's code (C2) is used and the row is flagged in the reason. Output:
data/verification/phase5/patches_p5_types.json. Run once after the blind coding; the file is committed.
"""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VALID = {"PERF", "NONE", "RISK", "CONF", "MON", "SEC", "TRANS", "RED", "GATE", "ROB", "FAIR", "REAL", "OVER", "PRIV", "DATA", "CSAFE"}


def main():
    t = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8")) if "-P5-" in r["row_id"]}
    c2 = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data" / "coding" / "phase5" / "newrows" / "bind_C2.csv", encoding="utf-8"))}
    c3 = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data" / "coding" / "phase5" / "newrows" / "bind_C3.csv", encoding="utf-8"))}
    out = []
    for rid, r in t.items():
        cur = r["primary_test_type"]
        cur = {"ROBU": "ROB"}.get(cur, cur)
        if cur in VALID:
            if cur != r["primary_test_type"]:
                out.append({"row_id": rid, "field": "primary_test_type", "op": "set", "value": cur, "source": "p5_types",
                            "reason": "Extractor code ROBU mapped to the table code ROB."})
            continue
        a, b = c2[rid]["primary_test_type"].strip(), c3[rid]["primary_test_type"].strip()
        if a == b and a in VALID:
            new, why = a, "Extractor code outside the table code list; both blind coders agree."
        else:
            new = a if a in VALID else (b if b in VALID else "NONE")
            why = f"Extractor code outside the table code list; blind coders differ ({a} versus {b}), first coder used."
        out.append({"row_id": rid, "field": "primary_test_type", "op": "set", "value": new, "source": "p5_types", "reason": why})
    (ROOT / "data" / "verification" / "phase5" / "patches_p5_types.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(len(out), "type patches")


if __name__ == "__main__":
    main()
