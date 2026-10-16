"""Merge the two independent normative force codings and compute agreement.

Input: data/coding/coder_A.csv and coder_B.csv (codebook: data/coding/CODEBOOK_normative_force.md).
Output: data/coding/normative_force.csv (one row per coded row: both codes, the agreed code or DISPUTED)
and data/coding/normative_force_stats.json (agreement, Cohen's kappa, counts).
Run: python -m ikhtibar.normative
"""
import csv, json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "data" / "coding"
CODES = ["OBLIGATION_WORDING", "RECOMMENDS", "DESCRIBES"]


def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = collections.Counter(a for a, _ in pairs), collections.Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in CODES) / (n * n)
    return round(po, 3), round((po - pe) / (1 - pe), 3) if pe < 1 else 1.0


def main():
    a = {r["row_id"]: r for r in read(C / "coder_A.csv")}
    b = {r["row_id"]: r for r in read(C / "coder_B.csv")}
    ids = [r["row_id"] for r in read(C / "normative_force_input.csv")]
    assert set(ids) == set(a) == set(b), "coders did not code the same rows"
    out, pairs = [], []
    for i in ids:
        ca, cb = a[i]["normative_force"].strip(), b[i]["normative_force"].strip()
        assert ca in CODES and cb in CODES, i
        pairs.append((ca, cb))
        out.append({"row_id": i, "coder_A": ca, "coder_B": cb, "agreed": ca if ca == cb else "DISPUTED",
                    "confidence_A": a[i]["confidence"], "confidence_B": b[i]["confidence"]})
    with open(C / "normative_force.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    po, k = kappa(pairs)
    conf = collections.Counter((x, y) for x, y in pairs if x != y)
    S = {"n": len(ids), "observed_agreement": po, "cohens_kappa": k,
         "agreed_counts": dict(collections.Counter(r["agreed"] for r in out)),
         "coder_A_counts": dict(collections.Counter(x for x, _ in pairs)),
         "coder_B_counts": dict(collections.Counter(y for _, y in pairs)),
         "disagreements": {f"{x} vs {y}": n for (x, y), n in conf.most_common()}}
    (C / "normative_force_stats.json").write_text(json.dumps(S, indent=1), encoding="utf-8")
    print(json.dumps(S, indent=1))


if __name__ == "__main__":
    main()
