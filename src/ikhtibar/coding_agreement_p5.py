"""Agreement on the phase 5 new rows: the table coding (extractor, after verifier corrections) against two blind coders.

Inputs: data/evidence_table.csv (rows with -P5- ids), data/coding/phase5/newrows/bind_C2.csv and bind_C3.csv
(codebook: data/coding/phase4/CODEBOOK.md; coders saw framework, locator and paraphrase only).
Output: data/coding/phase5/newrows/agreement_p5.json. Run: python -m ikhtibar.coding_agreement_p5
Note: the table codes of these rows were set by the extractor and then corrected where a fresh verifier found a fault, so they are not
independent of the verifier; the two coders are independent of both.
"""
import csv, json, collections, itertools
from pathlib import Path
import numpy as np
from .completeness import wilson

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "data" / "coding" / "phase5" / "newrows"
SEED = 20261103
G3 = {"mandatory": "binding", "conditional": "binding", "voluntary": "non_binding", "guidance": "non_binding", "ambiguous": "ambiguous"}


def kappa(a, b):
    n = len(a)
    cats = sorted(set(a) | set(b))
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def pair(a, b, rng):
    n = len(a)
    k = sum(x == y for x, y in zip(a, b))
    bs = []
    for _ in range(2000):
        ix = rng.randint(0, n, n)
        bs.append(kappa([a[i] for i in ix], [b[i] for i in ix]))
    return {"n": n, "agree": k, "agree_pct": round(100 * k / n, 1), "wilson_ci95": wilson(k, n), "kappa": round(kappa(a, b), 3),
            "kappa_ci95": [round(float(np.percentile(bs, 2.5)), 3), round(float(np.percentile(bs, 97.5)), 3)]}


def main():
    t = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8")) if "-P5-" in r["row_id"]}
    c2 = {r["row_id"]: r for r in csv.DictReader(open(N / "bind_C2.csv", encoding="utf-8"))}
    c3 = {r["row_id"]: r for r in csv.DictReader(open(N / "bind_C3.csv", encoding="utf-8"))}
    ids = sorted(t)
    assert ids == sorted(c2) == sorted(c3)
    rng = np.random.RandomState(SEED)
    codes = {"original": {i: t[i] for i in ids}, "C2": c2, "C3": c3}
    out = {"n": len(ids), "seed": SEED, "binding5": {}, "binding3": {}, "binding_vs_nonbinding_flips": {}, "test_type": {}}
    for (x, X), (y, Y) in itertools.combinations(codes.items(), 2):
        key = f"{x}|{y}"
        a5, b5 = [X[i]["binding_status"] for i in ids], [Y[i]["binding_status"] for i in ids]
        out["binding5"][key] = pair(a5, b5, rng)
        out["binding3"][key] = pair([G3[v] for v in a5], [G3[v] for v in b5], rng)
        out["binding_vs_nonbinding_flips"][key] = sum(1 for p, q in zip(a5, b5) if G3[p] != G3[q] and "ambiguous" not in (G3[p], G3[q]))
        ta = [X[i]["primary_test_type"] for i in ids]
        tb = [Y[i]["primary_test_type"] for i in ids]
        out["test_type"][key] = pair(ta, tb, rng)
    out["label_shares_pct"] = {k: {c: round(100 * v / len(ids), 1) for c, v in collections.Counter(G3[V[i]["binding_status"]] for i in ids).items()}
                               for k, V in codes.items()}
    dis = [i for i in ids if len({t[i]["binding_status"], c2[i]["binding_status"], c3[i]["binding_status"]}) > 1]
    out["rows_with_any_binding_disagreement"] = len(dis)
    with open(N / "disagreements_p5.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["row_id", "original", "C2", "C3", "framework"])
        for i in dis:
            w.writerow([i, t[i]["binding_status"], c2[i]["binding_status"], c3[i]["binding_status"], t[i]["framework"][:80]])
    (N / "agreement_p5.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for k in out["binding5"]:
        print(k, "5-class", out["binding5"][k]["agree_pct"], out["binding5"][k]["kappa"], "3-class", out["binding3"][k]["agree_pct"], out["binding3"][k]["kappa"],
              "flips", out["binding_vs_nonbinding_flips"][k], "type", out["test_type"][k]["agree_pct"])


if __name__ == "__main__":
    main()
