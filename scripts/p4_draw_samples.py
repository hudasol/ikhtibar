"""Draw the seeded phase 4 samples: verification sample, coding sample, human gold template.
Deterministic: python scripts/p4_draw_samples.py
"""
import csv, json, random, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEED = 20261028
rows = list(csv.DictReader(open(ROOT / "data/evidence_table.csv", encoding="utf-8")))

# 1. Verification sample: rows with a readable source and a completed check.
readable = sorted(
    r["row_id"] for r in rows
    if r["verification_status"] in ("VERIFIED", "VERIFIED_CORRECTED") and r["access_path"] != "none"
)
rng = random.Random(SEED)
ver = sorted(rng.sample(readable, 120))
byid = {r["row_id"]: r for r in rows}
ver_sorted = sorted(ver, key=lambda i: (byid[i]["family"], i))
chunks = [ver_sorted[i::6] for i in range(6)]  # interleave so each verifier sees mixed families
cols = ["row_id", "framework", "clause_or_page", "requirement_paraphrase", "binding_status",
        "what_is_tested", "who_tests", "source_url", "retrieved_on"]
out = ROOT / "data/verification/phase4/inputs"
for k, ch in enumerate(chunks, 1):
    with open(out / f"v4_{k}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for i in ch:
            w.writerow({c: byid[i][c] for c in cols})
json.dump({"seed": SEED, "population_size": len(readable), "sample": ver_sorted,
           "chunks": chunks}, open(ROOT / "data/verification/phase4/sample_p4.json", "w"), indent=1, sort_keys=True)

# 2. Coding sample: headline test rows.
tests = sorted(r["row_id"] for r in rows if r["row_type"] == "test" and r["headline_include"] == "yes")
rng = random.Random(SEED + 1)
cod = sorted(rng.sample(tests, 120))
rng.shuffle(cod)
ccols = ["row_id", "framework", "clause_or_page", "requirement_paraphrase"]
cdir = ROOT / "data/coding/phase4"
with open(cdir / "coding_input.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ccols)
    w.writeheader()
    for i in cod:
        w.writerow({c: byid[i][c] for c in ccols})
json.dump({"seed": SEED + 1, "population_size": len(tests), "sample_in_order": cod},
          open(cdir / "sample_coding.json", "w"), indent=1, sort_keys=True)

# 3. Human gold template: first 100 of the shuffled coding sample.
with open(cdir / "human_gold_template.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["row_id", "framework", "clause_or_page", "requirement_paraphrase",
                "YOUR_binding_status", "YOUR_primary_test_type", "YOUR_note"])
    for i in cod[:100]:
        r = byid[i]
        w.writerow([i, r["framework"], r["clause_or_page"], r["requirement_paraphrase"], "", "", ""])
print("verification population", len(readable), "sample", len(ver), "coding population", len(tests))
print(collections.Counter(byid[i]["family"] for i in ver).most_common(8))
