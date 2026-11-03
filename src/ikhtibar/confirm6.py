"""Registered primary analyses of phase 6 (see docs/PREREG_PHASE6.md). Frozen before the confirmation half is read.

Usage: python -m ikhtibar.confirm6 design | confirmation | all | old | new
`design` is the half on which thresholds were tuned; `confirmation` is the registered test; `all`, `old` and `new` are
exploratory. Output: data/phase6/results_<subset>.json. Seed 20261107, 4000 document cluster bootstrap draws.
"""
import sys, json, itertools, collections
from pathlib import Path
import numpy as np

from . import split6, specificity as sp

ROOT = Path(__file__).resolve().parents[2]
SEED, N_BOOT = 20261107, 4000
G = sp.GROUP


def wilson(k, n, z=1.96):
    if n == 0:
        return [float("nan")] * 2
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(100 * (c - h), 1), round(100 * (c + h), 1)]


def pick(subset):
    split = json.loads((ROOT / "data" / "phase6" / "split.json").read_text())["assignment"]
    keep = {"design": ("design",), "confirmation": ("confirmation_old", "confirmation_new"),
            "all": ("design", "confirmation_old", "confirmation_new"), "old": ("design", "confirmation_old"),
            "new": ("confirmation_new",)}[subset]
    return [r for r in split6.headline() if split[r["framework"]] in keep]


def stats_of(docs, lab, ttype):
    """docs: {doc: [row index]}; lab: list of group labels; returns the registered statistics."""
    ds = list(docs)
    multi = [d for d in ds if len(docs[d]) >= 2]
    mixed = sum(1 for d in multi if "binding" in {lab[i] for i in docs[d]} and "non_binding" in {lab[i] for i in docs[d]})
    conc = [np.mean([lab[a] == lab[b] for a, b in itertools.combinations(docs[d], 2)]) for d in multi]
    allr = [i for d in ds for i in docs[d]]
    chance = sum((sum(1 for i in allr if lab[i] == k) / len(allr)) ** 2 for k in ("binding", "non_binding", "ambiguous"))
    anyb = sum(1 for d in ds if any(lab[i] == "binding" for i in docs[d]))
    return {"n_docs": len(ds), "n_multi": len(multi), "mixed_share_multi": mixed / len(multi) if multi else float("nan"),
            "doc_concordance": float(np.mean(conc)) if conc else float("nan"), "chance": chance,
            "concordance_excess": (float(np.mean(conc)) - chance) if conc else float("nan"),
            "any_binding_docs": anyb / len(ds), "row_binding": float(np.mean([lab[i] == "binding" for i in allr])),
            "doc_weighted_binding": float(np.mean([np.mean([lab[i] == "binding" for i in docs[d]]) for d in ds]))}


def s1_gap(docs, lab, spec, ttype):
    """Binding minus non binding share of S1 rows, within test type, weighted by binding rows (as in specificity.py)."""
    ix = [i for d in docs for i in docs[d]]
    num = den = 0.0
    for t in sorted({ttype[i] for i in ix}):
        b = [i for i in ix if ttype[i] == t and lab[i] == "binding"]
        n = [i for i in ix if ttype[i] == t and lab[i] == "non_binding"]
        if b and n:
            num += len(b) * (np.mean([spec[i] == "S1" for i in b]) - np.mean([spec[i] == "S1" for i in n]))
            den += len(b)
    return (num / den if den else float("nan")), den


def main(subset):
    rows = pick(subset)
    A, B = sp.load_coder("A"), sp.load_coder("B")
    lab = [G[r["binding_status"]] for r in rows]
    ttype = [r["primary_test_type"] for r in rows]
    specs = {"A": [A[r["row_id"]] for r in rows], "B": [B[r["row_id"]] for r in rows]}
    docs = collections.defaultdict(list)
    for i, r in enumerate(rows):
        docs[r["framework"]].append(i)
    point = stats_of(docs, lab, ttype)
    gaps = {c: s1_gap(docs, lab, specs[c], ttype) for c in "AB"}
    rng = np.random.RandomState(SEED)
    names = list(docs)
    boot = collections.defaultdict(list)
    for _ in range(N_BOOT):
        pick_ = rng.randint(0, len(names), len(names))
        new, rl, rt, rs = {}, [], [], {"A": [], "B": []}
        for k, j in enumerate(pick_):
            idx = docs[names[j]]
            start = len(rl)
            for i in idx:
                rl.append(lab[i]); rt.append(ttype[i])
                for c in "AB":
                    rs[c].append(specs[c][i])
            new[f"{k}"] = list(range(start, start + len(idx)))
        s = stats_of(new, rl, rt)
        for k_, v in s.items():
            if k_ not in ("n_docs", "n_multi"):
                boot[k_].append(v)
        for c in "AB":
            g, d = s1_gap(new, rl, rs[c], rt)
            if d:
                boot["gap_" + c].append(g)
    ci = lambda v: [round(100 * float(np.nanpercentile(v, 2.5)), 1), round(100 * float(np.nanpercentile(v, 97.5)), 1)]
    out = {"subset": subset, "seed": SEED, "bootstrap": N_BOOT, "n_rows": len(rows), "n_docs": point["n_docs"],
           "n_multi_row_docs": point["n_multi"],
           "row_binding_pct": round(100 * point["row_binding"], 1), "row_binding_ci95": ci(boot["row_binding"]),
           "doc_weighted_binding_pct": round(100 * point["doc_weighted_binding"], 1),
           "doc_weighted_binding_ci95": ci(boot["doc_weighted_binding"]),
           "any_binding_docs_pct": round(100 * point["any_binding_docs"], 1),
           "any_binding_docs_wilson95": wilson(round(point["any_binding_docs"] * point["n_docs"]), point["n_docs"]),
           "mixed_share_multi_pct": round(100 * point["mixed_share_multi"], 1),
           "mixed_share_multi_wilson95": wilson(round(point["mixed_share_multi"] * point["n_multi"]), point["n_multi"]),
           "doc_concordance_pct": round(100 * point["doc_concordance"], 1), "chance_concordance_pct": round(100 * point["chance"], 1),
           "concordance_excess_pp": round(100 * point["concordance_excess"], 1),
           "concordance_excess_ci95": ci(boot["concordance_excess"]),
           "s1_gap_within_type_pp": {c: round(100 * gaps[c][0], 1) for c in "AB"},
           "s1_gap_binding_rows_compared": {c: gaps[c][1] for c in "AB"},
           "s1_gap_ci95": {c: ci(boot["gap_" + c]) for c in "AB"},
           "label_counts": dict(collections.Counter(lab))}
    # registered decisions (thresholds fixed in docs/PREREG_PHASE6.md)
    out["decisions"] = {
        "C1_documents_are_pure": bool(point["mixed_share_multi"] <= 0.25 and out["mixed_share_multi_wilson95"][1] <= 40.0),
        "C2_concordance_excess": bool(out["concordance_excess_ci95"][0] >= 20.0),
        "C3_minority_of_documents_binding": bool(out["any_binding_docs_wilson95"][1] < 50.0),
        "C4_minority_of_documents_weighted": bool(out["doc_weighted_binding_ci95"][1] < 50.0),
        "C4b_row_level_reported_not_decisive": bool(out["row_binding_ci95"][1] < 50.0),
        "C5_process_only_gap_direction": bool(all(gaps[c][0] > 0 for c in "AB")),
        "C5_process_only_gap_ci_excludes_zero": bool(all(out["s1_gap_ci95"][c][0] > 0 for c in "AB"))}
    (ROOT / "data" / "phase6" / f"results_{subset}.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv[1])
