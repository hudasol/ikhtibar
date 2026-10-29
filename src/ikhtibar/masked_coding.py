"""Does the document name drive the blind binding status coding?

Two further blind coders recoded the same 120 sampled headline rows with the document name withheld
(data/coding/phase6). This module compares them with each other, with the two blind coders who saw the document
name (phase 4, B2 and B3) and with the original coding. Output: data/coding/phase6/masked_agreement.json.
Run: python -m ikhtibar.masked_coding
"""
import csv, json, collections
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
P4, P6 = ROOT / "data" / "coding" / "phase4", ROOT / "data" / "coding" / "phase6"
TO3 = {"mandatory": "binding", "conditional": "binding", "voluntary": "non_binding", "guidance": "non_binding",
       "ambiguous": "ambiguous"}


def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return {r["row_id"]: r for r in csv.DictReader(f)}


def kappa(a, b):
    labs = sorted(set(a) | set(b))
    ix = {l: i for i, l in enumerate(labs)}
    m = np.zeros((len(labs), len(labs)))
    for x, y in zip(a, b):
        m[ix[x], ix[y]] += 1
    n = m.sum()
    po = np.trace(m) / n
    pe = float((m.sum(1) * m.sum(0)).sum() / n ** 2)
    return float((po - pe) / (1 - pe)) if pe < 1 else 1.0


def compute():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        table = {r["row_id"]: r for r in csv.DictReader(f)}
    coders = {"M1": read(P6 / "masked_M1.csv"), "M2": read(P6 / "masked_M2.csv"),
              "B2": read(P4 / "coder2.csv"), "B3": read(P4 / "coder3.csv")}
    ids = sorted(coders["M1"])
    assert ids == sorted(coders["M2"]) == sorted(coders["B2"]) == sorted(coders["B3"]) and len(ids) == 120
    lab = {k: [v[i]["binding_status"] for i in ids] for k, v in coders.items()}
    lab["orig"] = [table[i]["binding_status"] for i in ids]
    lab3 = {k: [TO3[x] for x in v] for k, v in lab.items()}
    out = {"n": len(ids), "pairs": {}, "shares": {}}
    for a, b in (("M1", "M2"), ("B2", "B3"), ("M1", "B2"), ("M1", "B3"), ("M2", "B2"), ("M2", "B3"),
                 ("M1", "orig"), ("M2", "orig"), ("B2", "orig"), ("B3", "orig")):
        flips = sum(1 for x, y in zip(lab3[a], lab3[b]) if {x, y} == {"binding", "non_binding"})
        out["pairs"][f"{a}|{b}"] = {
            "agreement5_pct": round(100 * float(np.mean([x == y for x, y in zip(lab[a], lab[b])])), 1),
            "kappa5": round(kappa(lab[a], lab[b]), 3),
            "agreement3_pct": round(100 * float(np.mean([x == y for x, y in zip(lab3[a], lab3[b])])), 1),
            "kappa3": round(kappa(lab3[a], lab3[b]), 3),
            "binding_vs_nonbinding_flips": flips}
    for k, v in lab3.items():
        c = collections.Counter(v)
        out["shares"][k] = {g: round(100 * c[g] / len(v), 1) for g in ("binding", "non_binding", "ambiguous")}
    # masked coders against the majority of the three other codings is not computed; keep the design simple
    return out


def main():
    out = compute()
    (P6 / "masked_agreement.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for k, v in out["pairs"].items():
        print(k, v)
    print(out["shares"])


if __name__ == "__main__":
    main()
