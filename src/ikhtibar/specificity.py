"""How specific are the testing provisions, and are binding provisions more specific than the rest?

Question answered: the paper states that binding text seldom says how to test. This module turns that
statement into a measurement. Two blind coders (language model instances) coded every headline test row on a
four level scale (S1 process only, S2 property named, S3 method or metric named, S4 criterion set) from the
paraphrase alone, without seeing the binding status (data/coding/phase5/CODEBOOK_SPECIFICITY.md).
Outputs data/specificity.json: coder agreement, level counts by binding group for each coder, and differences
between binding and non binding provisions with document level (framework) cluster bootstrap intervals.
Run: python -m ikhtibar.specificity
"""
import csv, json, collections
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
P5 = ROOT / "data" / "coding" / "phase5"
SEED = 20261028
N_BOOT = 4000
LEVELS = ["S1", "S2", "S3", "S4"]
GROUP = {"mandatory": "binding", "conditional": "binding", "voluntary": "non_binding",
         "guidance": "non_binding", "ambiguous": "ambiguous"}


def load_coder(tag):
    out = {}
    for part in (1, 2):
        with open(P5 / f"spec_{tag}_{part}.csv", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                out[r["row_id"]] = r["specificity"].strip()
    return out


def cohen_kappa(a, b, weights=None):
    k = len(LEVELS)
    ix = {l: i for i, l in enumerate(LEVELS)}
    m = np.zeros((k, k))
    for x, y in zip(a, b):
        m[ix[x], ix[y]] += 1
    n = m.sum()
    w = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            w[i, j] = 0.0 if i == j else (1.0 if weights is None else abs(i - j) / (k - 1))
    e = np.outer(m.sum(1), m.sum(0)) / n
    return float(1 - (w * m).sum() / (w * e).sum())


def main():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        table = {r["row_id"]: r for r in csv.DictReader(f)}
    A, B = load_coder("A"), load_coder("B")
    ids = sorted(A)
    assert ids == sorted(B), "coders cover different rows"
    for i in ids:
        assert table[i]["row_type"] == "test" and table[i]["headline_include"] == "yes"
    a = [A[i] for i in ids]
    b = [B[i] for i in ids]
    grp = [GROUP[table[i]["binding_status"]] for i in ids]
    fw = [table[i]["framework"] for i in ids]
    n = len(ids)
    lv = {l: k for k, l in enumerate(LEVELS)}

    rng = np.random.RandomState(SEED)
    boot_k, boot_kw = [], []
    for _ in range(N_BOOT):
        ix = rng.randint(0, n, n)
        boot_k.append(cohen_kappa([a[i] for i in ix], [b[i] for i in ix]))
        boot_kw.append(cohen_kappa([a[i] for i in ix], [b[i] for i in ix], weights="linear"))
    q = lambda v: [round(float(np.percentile(v, 2.5)), 3), round(float(np.percentile(v, 97.5)), 3)]
    agreement = {
        "n": n,
        "exact_pct": round(100 * float(np.mean([x == y for x, y in zip(a, b)])), 1),
        "within_one_pct": round(100 * float(np.mean([abs(lv[x] - lv[y]) <= 1 for x, y in zip(a, b)])), 1),
        "kappa": round(cohen_kappa(a, b), 3), "kappa_ci95": q(boot_k),
        "kappa_linear_weighted": round(cohen_kappa(a, b, "linear"), 3), "kappa_linear_weighted_ci95": q(boot_kw),
        "label_counts": {"A": dict(collections.Counter(a)), "B": dict(collections.Counter(b))},
    }

    def share(labels, mask, levels):
        idx = [i for i in range(n) if mask[i]]
        return float(np.mean([labels[i] in levels for i in idx])) if idx else float("nan")

    docs = sorted(set(fw))
    by_doc = {d: [i for i in range(n) if fw[i] == d] for d in docs}
    comp = {}
    coders = {"A": a, "B": b,
              "lower": [min(x, y) for x, y in zip(a, b)],     # the less specific of the two codes
              "upper": [max(x, y) for x, y in zip(a, b)]}     # the more specific of the two codes
    for cname, labs in coders.items():
        table_counts = {}
        for g in ("binding", "non_binding", "ambiguous"):
            idx = [i for i in range(n) if grp[i] == g]
            table_counts[g] = {"n": len(idx), **{l: sum(1 for i in idx if labs[i] == l) for l in LEVELS}}
        res = {"counts": table_counts, "differences": {}}
        mb = [g == "binding" for g in grp]
        mn = [g == "non_binding" for g in grp]
        for name, lvls in (("S1_process_only", ("S1",)), ("S3_or_S4_method_or_criterion", ("S3", "S4")),
                           ("S4_criterion_set", ("S4",))):
            d0 = share(labs, mb, lvls) - share(labs, mn, lvls)
            rng2 = np.random.RandomState(SEED + 1)
            bs = []
            for _ in range(N_BOOT):
                pick = rng2.randint(0, len(docs), len(docs))
                ix = [i for k in pick for i in by_doc[docs[k]]]
                mbb = [grp[i] == "binding" for i in ix]
                mnn = [grp[i] == "non_binding" for i in ix]
                if not any(mbb) or not any(mnn):
                    continue
                lab2 = [labs[i] for i in ix]
                bs.append(float(np.mean([l in lvls for l, m in zip(lab2, mbb) if m]))
                          - float(np.mean([l in lvls for l, m in zip(lab2, mnn) if m])))
            res["differences"][name] = {
                "binding_pct": round(100 * share(labs, mb, lvls), 1),
                "non_binding_pct": round(100 * share(labs, mn, lvls), 1),
                "difference_pp": round(100 * d0, 1),
                "difference_ci95_doc_cluster_pp": [round(100 * float(np.percentile(bs, 2.5)), 1),
                                                   round(100 * float(np.percentile(bs, 97.5)), 1)]}
        comp[cname] = res
    # adjusted differences: compare binding with non binding rows inside the same stratum (test type, or family),
    # weighting each stratum by its number of binding rows, so that the comparison is not driven by the mix of types
    ttype = [table[i]["primary_test_type"] for i in ids]
    famv = [table[i]["family"] for i in ids]

    def strat_diff(labs, lvls, strata, ix):
        num, den = 0.0, 0
        for s_ in sorted(set(strata[i] for i in ix)):
            sb = [i for i in ix if strata[i] == s_ and grp[i] == "binding"]
            sn = [i for i in ix if strata[i] == s_ and grp[i] == "non_binding"]
            if not sb or not sn:
                continue
            db = np.mean([labs[i] in lvls for i in sb]) - np.mean([labs[i] in lvls for i in sn])
            num += len(sb) * db
            den += len(sb)
        return (num / den) if den else float("nan"), den

    adjusted = {}
    for cname in ("A", "B"):
        labs = coders[cname]
        adjusted[cname] = {}
        for sname, strata in (("test_type", ttype), ("family", famv)):
            for name, lvls in (("S1_process_only", ("S1",)), ("S3_or_S4_method_or_criterion", ("S3", "S4"))):
                d0, used = strat_diff(labs, lvls, strata, list(range(n)))
                rng3 = np.random.RandomState(SEED + 2)
                bs = []
                for _ in range(N_BOOT):
                    pick = rng3.randint(0, len(docs), len(docs))
                    ix = [i for k in pick for i in by_doc[docs[k]]]
                    d, u = strat_diff(labs, lvls, strata, ix)
                    if u:
                        bs.append(d)
                adjusted[cname][f"{sname}|{name}"] = {
                    "difference_pp": round(100 * d0, 1), "binding_rows_compared": used,
                    "ci95_doc_cluster_pp": [round(100 * float(np.percentile(bs, 2.5)), 1),
                                            round(100 * float(np.percentile(bs, 97.5)), 1)]}
    # binding rows by family, for the discussion
    fam = collections.defaultdict(lambda: collections.Counter())
    for i in range(n):
        if grp[i] == "binding":
            fam[table[ids[i]]["family"]][a[i]] += 1
    out = {"meta": {"n_rows": n, "seed": SEED, "bootstrap": N_BOOT, "levels": LEVELS,
                    "coders": "two blind language model instances, paraphrase only, binding status hidden"},
           "agreement": agreement, "by_coder": comp, "adjusted": adjusted,
           "binding_by_family_coder_A": {k: dict(v) for k, v in sorted(fam.items())}}
    (ROOT / "data" / "specificity.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(json.dumps(agreement, indent=1))
    for c, r in comp.items():
        print(c, r["counts"])
        for k, v in r["differences"].items():
            print("  ", k, v)


if __name__ == "__main__":
    main()
