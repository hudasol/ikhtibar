#!/usr/bin/env python3
"""Task 3d: seeded fresh verification sample of existing rows from the families least covered by earlier fresh samples.

Frame: rows of the table (not phase 5 rows) never drawn in a fresh independent sample (phase 2, 3 or 4), in the
families where earlier fresh draws covered at most a quarter of the rows. Seed 20261103. 30 rows, allocated in
proportion to family size (at least 2 per family), split across three input files for three fresh verifiers.
Output: data/verification/phase5/sample_p5.json and inputs/p5v_<k>.csv
"""
import csv, json, random, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SEED, N = 20261103, 30
COLS = ["row_id", "family", "framework", "clause_or_page", "requirement_paraphrase", "binding_status", "what_is_tested",
        "who_tests", "source_url", "retrieved_on"]


def main():
    rows = [r for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8")) if "-P5-" not in r["row_id"]]
    fresh = lambda r: bool(r["p4_sample"]) or r["p3_sample"] == "fresh_random_seed_20261016" or r["sample_type"] == "fresh_random_seed_20261012"
    by = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        by[r["family"]][0] += 1
        by[r["family"]][1] += fresh(r)
    fams = sorted(f for f, (n, k) in by.items() if k / n <= 0.25 and n >= 5)
    frame = [r for r in rows if r["family"] in fams and not fresh(r)]
    rng = random.Random(SEED)
    tot = len(frame)
    alloc = {f: max(2, round(N * sum(1 for r in frame if r["family"] == f) / tot)) for f in fams}
    pick = []
    for f in fams:
        pool = sorted([r for r in frame if r["family"] == f], key=lambda r: r["row_id"])
        pick += rng.sample(pool, min(alloc[f], len(pool)))
    rng.shuffle(pick)
    (ROOT / "data" / "verification" / "phase5" / "inputs").mkdir(parents=True, exist_ok=True)
    for k in range(3):
        with open(ROOT / "data" / "verification" / "phase5" / "inputs" / f"p5v_{k+1}.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f); w.writerow(COLS)
            for r in pick[k::3]:
                w.writerow([r[c] for c in COLS])
    out = {"seed": SEED, "families": fams, "frame_size": tot, "allocation": alloc, "sample": sorted(r["row_id"] for r in pick),
           "family_fresh_share_before": {f: round(by[f][1] / by[f][0], 3) for f in fams}}
    (ROOT / "data" / "verification" / "phase5" / "sample_p5.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(len(pick), "rows from", fams, "frame", tot)


if __name__ == "__main__":
    main()
