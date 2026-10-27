"""Agreement between the original coding and two blind second coders (phase 4).

Inputs: data/evidence_table.csv (original codes), data/coding/phase4/coder2.csv and coder3.csv
Outputs: data/coding/phase4/agreement.json and disagreements.csv
Run: python -m ikhtibar.coding_agreement
Kappa is Cohen's kappa for pairs. Krippendorff's alpha (nominal) is computed over the three coders.
Optional: data/coding/phase4/human_gold.csv (filled template) adds agreement of every coder with a human.
"""
import csv, json, collections, itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "data" / "coding" / "phase4"
TO3 = {"mandatory": "binding", "conditional": "binding", "voluntary": "non_binding",
       "guidance": "non_binding", "ambiguous": "ambiguous"}


def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cohen(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def kripp_alpha_nominal(columns):
    """columns: list of equally long label lists (coders). No missing data."""
    n_items = len(columns[0])
    m = len(columns)
    coincid = collections.Counter()
    for i in range(n_items):
        vals = [col[i] for col in columns]
        for a, b in itertools.permutations(range(m), 2):
            coincid[(vals[a], vals[b])] += 1.0 / (m - 1)
    labels = sorted({v for col in columns for v in col})
    n_c = {c: sum(coincid[(c, k)] for k in labels) for c in labels}
    n = sum(n_c.values())
    do = sum(coincid[(a, b)] for a in labels for b in labels if a != b)
    de = sum(n_c[a] * n_c[b] for a in labels for b in labels if a != b) / (n - 1)
    return 1.0 if de == 0 else 1 - do / de


def bootstrap_ci(a, b, stat, reps=2000, seed=20261028):
    import random
    rng = random.Random(seed)
    n = len(a)
    vals = []
    for _ in range(reps):
        ix = [rng.randrange(n) for _ in range(n)]
        vals.append(stat([a[i] for i in ix], [b[i] for i in ix]))
    vals.sort()
    return [round(vals[int(0.025 * reps)], 3), round(vals[int(0.975 * reps) - 1], 3)]


def main():
    table = {r["row_id"]: r for r in read(ROOT / "data" / "evidence_table.csv")}
    c2 = {r["row_id"]: r for r in read(C / "coder2.csv")}
    c3 = {r["row_id"]: r for r in read(C / "coder3.csv")}
    ids = [r["row_id"] for r in read(C / "coding_input.csv")]
    assert set(ids) == set(c2) == set(c3), "coders did not code the same rows"
    orig_b = [table[i]["binding_status"] for i in ids]
    orig_t = [table[i]["primary_test_type"] for i in ids]
    out = {"n": len(ids), "fields": {}}
    dis = []
    coders = {"original": (orig_b, orig_t),
              "coder2": ([c2[i]["binding_status"].strip() for i in ids], [c2[i]["primary_test_type"].strip() for i in ids]),
              "coder3": ([c3[i]["binding_status"].strip() for i in ids], [c3[i]["primary_test_type"].strip() for i in ids])}
    gold_path = C / "human_gold.csv"
    if gold_path.exists():
        g = {r["row_id"]: r for r in read(gold_path) if r.get("YOUR_binding_status", "").strip()}
        out["human_gold_rows"] = len(g)
    fields = {"binding5": (0, lambda x: x), "binding3": (0, lambda x: TO3[x]), "test_type": (1, lambda x: x)}
    for fname, (idx, f) in fields.items():
        cols = {k: [f(v) for v in vals[idx]] for k, vals in coders.items()}
        res = {"pairs": {}}
        for a, b in itertools.combinations(cols, 2):
            po, k = cohen(cols[a], cols[b])
            res["pairs"][f"{a}|{b}"] = {
                "agreement_pct": round(100 * po, 1), "kappa": round(k, 3),
                "kappa_ci95": bootstrap_ci(cols[a], cols[b], lambda x, y: cohen(x, y)[1])}
        res["krippendorff_alpha_3_coders"] = round(kripp_alpha_nominal(list(cols.values())), 3)
        allsame = sum(1 for i in range(len(ids)) if len({cols[k][i] for k in cols}) == 1)
        res["all_three_agree_pct"] = round(100 * allsame / len(ids), 1)
        maj = []
        for i in range(len(ids)):
            cnt = collections.Counter([cols["coder2"][i], cols["coder3"][i]])
            maj.append(cols["coder2"][i] if cols["coder2"][i] == cols["coder3"][i] else None)
        both = [(o, m) for o, m in zip(cols["original"], maj) if m is not None]
        res["original_vs_agreed_blind_pairs"] = {
            "rows_where_blind_coders_agree": len(both),
            "original_matches_pct": round(100 * sum(o == m for o, m in both) / len(both), 1)}
        res["label_counts"] = {k: dict(collections.Counter(v)) for k, v in cols.items()}
        out["fields"][fname] = res
        if fname in ("binding5", "test_type"):
            for i, rid in enumerate(ids):
                vals = {k: cols[k][i] for k in cols}
                if len(set(vals.values())) > 1:
                    dis.append({"field": fname, "row_id": rid, "framework": table[rid]["framework"],
                                "original": vals["original"], "coder2": vals["coder2"], "coder3": vals["coder3"],
                                "coder2_note": c2[rid].get("note", ""), "coder3_note": c3[rid].get("note", "")})
    # who is the odd one out on binding5
    odd = collections.Counter()
    for d in dis:
        if d["field"] != "binding5":
            continue
        vals = [d["original"], d["coder2"], d["coder3"]]
        cnt = collections.Counter(vals)
        if len(cnt) == 2:
            lone = [k for k, v in zip(["original", "coder2", "coder3"], vals) if cnt[v] == 1][0]
            odd[lone] += 1
        else:
            odd["all_three_differ"] += 1
    out["binding5_odd_one_out"] = dict(odd)
    (C / "agreement.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    with open(C / "disagreements.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(dis[0].keys()))
        w.writeheader()
        w.writerows(dis)
    for fname, r in out["fields"].items():
        print(fname, {k: (v["agreement_pct"], v["kappa"]) for k, v in r["pairs"].items()}, "alpha", r["krippendorff_alpha_3_coders"],
              "all3", r["all_three_agree_pct"])
    print("odd one out", out["binding5_odd_one_out"], "disagreement rows", len(dis))


if __name__ == "__main__":
    main()
