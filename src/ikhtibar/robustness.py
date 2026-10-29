"""Robustness of the headline binding split (phase 4).

Headline claim under test: among test provisions, binding text (mandatory or conditional) is a minority.
Scenarios, all computed from data/evidence_table.csv:
  base                  headline test rows (row_type test, headline_include yes)
  leave_one_family_out  drop each family in turn
  excluded_bounds       the test rows excluded from the headline are added back: all binding (best case for the
                        claim "binding is common") or all non binding
  ambiguous_bounds      ambiguous rows counted all as binding, or all as non binding
  extreme_bounds        both of the above together, in each direction
  framework_weighted    every framework (document) gets equal weight, which removes the effect of document length
  framework_bootstrap   percentile interval for the binding share when frameworks are resampled with replacement
  document_level        share of frameworks that contain at least one binding test provision
Output: data/robustness.json. Run: python -m ikhtibar.robustness
"""
import csv, random, json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BIND = {"mandatory", "conditional"}
SEED = 20261028


def load():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r["row_type"] == "test"]


def share(rows):
    n = len(rows)
    b = sum(r["binding_status"] in BIND for r in rows)
    a = sum(r["binding_status"] == "ambiguous" for r in rows)
    return {"n": n, "binding": b, "mandatory": sum(r["binding_status"] == "mandatory" for r in rows), "ambiguous": a, "non_binding": n - b - a,
            "binding_pct": round(100 * b / n, 1) if n else None}


def pct(x, n):
    return round(100 * x / n, 1)


def compute():
    tests = load()
    head = [r for r in tests if r["headline_include"] == "yes"]
    excl = [r for r in tests if r["headline_include"] != "yes"]
    out = {"base": share(head)}
    b = out["base"]

    # leave one family out
    lofo = {}
    for fam in sorted({r["family"] for r in head}):
        lofo[fam] = share([r for r in head if r["family"] != fam])
        lofo[fam]["dropped_rows"] = sum(r["family"] == fam for r in head)
    out["leave_one_family_out"] = lofo
    pcts = [v["binding_pct"] for v in lofo.values()]
    out["leave_one_family_out_range"] = {"min_binding_pct": min(pcts), "max_binding_pct": max(pcts),
                                         "family_giving_max": max(lofo, key=lambda k: lofo[k]["binding_pct"]),
                                         "family_giving_min": min(lofo, key=lambda k: lofo[k]["binding_pct"])}

    # excluded rows: all binding, all non binding
    e = len(excl)
    ex_b = sum(r["binding_status"] in BIND for r in excl)
    out["excluded_rows"] = {"n": e, "coded_binding_in_table": ex_b}
    n_all = b["n"] + e
    out["excluded_bounds"] = {
        "all_excluded_binding_pct": pct(b["binding"] + e, n_all),
        "all_excluded_non_binding_pct": pct(b["binding"], n_all),
        "as_coded_pct": pct(b["binding"] + ex_b, n_all)}

    # ambiguous
    out["ambiguous_bounds"] = {
        "ambiguous_all_binding_pct": pct(b["binding"] + b["ambiguous"], b["n"]),
        "ambiguous_all_non_binding_pct": pct(b["binding"], b["n"])}

    # extreme
    out["extreme_bounds"] = {
        "most_favourable_to_binding_pct": pct(b["binding"] + b["ambiguous"] + e, n_all),
        "least_favourable_to_binding_pct": pct(b["binding"], n_all)}

    # framework weighting and document level
    byfw = collections.defaultdict(list)
    for r in head:
        byfw[r["framework"]].append(r)
    fw_share = {fw: sum(r["binding_status"] in BIND for r in rs) / len(rs) for fw, rs in byfw.items()}
    out["framework_weighted"] = {
        "frameworks": len(byfw),
        "mean_framework_binding_pct": round(100 * sum(fw_share.values()) / len(fw_share), 1),
        "frameworks_with_any_binding_test_provision": sum(v > 0 for v in fw_share.values()),
        "frameworks_with_any_binding_pct": pct(sum(v > 0 for v in fw_share.values()), len(fw_share)),
        "frameworks_majority_binding": sum(v > 0.5 for v in fw_share.values()),
        "frameworks_all_binding": sum(v == 1 for v in fw_share.values())}
    fams = collections.defaultdict(list)
    for r in head:
        fams[r["family"]].append(r)
    fam_share = {f: sum(r["binding_status"] in BIND for r in rs) / len(rs) for f, rs in fams.items()}
    out["family_weighted"] = {"families": len(fams),
                              "mean_family_binding_pct": round(100 * sum(fam_share.values()) / len(fam_share), 1),
                              "families_with_any_binding": sum(v > 0 for v in fam_share.values())}

    # cluster bootstrap by framework
    rng = random.Random(SEED)
    keys = sorted(byfw)
    vals = []
    for _ in range(5000):
        samp = [rng.choice(keys) for _ in keys]
        rows = [r for k in samp for r in byfw[k]]
        vals.append(100 * sum(r["binding_status"] in BIND for r in rows) / len(rows))
    vals.sort()
    out["framework_bootstrap"] = {"reps": 5000, "binding_pct_ci95": [round(vals[124], 1), round(vals[4874], 1)],
                                  "seed": SEED}

    # sensitivity to access type: rows read from catalogue pages or through machine translation
    trans = lambda r: r["evidence_grade"] == "read via unofficial/machine translation"
    iso = lambda r: r["family"] == "ISO-IEC"
    out["access_sensitivity"] = {
        "without_iso_catalogue_rows": share([r for r in head if not iso(r)]),
        "without_translated_rows": share([r for r in head if not trans(r)]),
        "without_either": share([r for r in head if not iso(r) and not trans(r)]),
        "n_translated_headline": sum(trans(r) for r in head), "n_iso_headline": sum(iso(r) for r in head)}

    # combined worst case with sampling uncertainty: resample documents (all test rows), count excluded rows and
    # ambiguous rows as binding inside each resample, take the upper end
    rng = random.Random(SEED + 5)
    fwk = sorted({r["framework"] for r in tests})
    byf = {f: [r for r in tests if r["framework"] == f] for f in fwk}
    fav = []
    for _ in range(5000):
        rs = [r for f in (rng.choice(fwk) for _ in fwk) for r in byf[f]]
        nb = sum((r["binding_status"] in BIND) or r["binding_status"] == "ambiguous" or r["headline_include"] != "yes" for r in rs)
        fav.append(100 * nb / len(rs))
    fav.sort()
    out["favourable_with_sampling"] = {"reps": 5000, "binding_pct_ci95": [round(fav[124], 1), round(fav[4874], 1)],
                                       "median_pct": round(fav[2500], 1), "share_of_resamples_at_or_above_50": round(100 * sum(v >= 50 for v in fav) / len(fav), 1)}

    # does the claim survive every scenario?
    claim = {"statement": "binding (mandatory or conditional) test provisions are a minority (below 50%)",
             "base": b["binding_pct"] < 50,
             "all_leave_one_family_out": all(p < 50 for p in pcts),
             "excluded_all_binding": out["excluded_bounds"]["all_excluded_binding_pct"] < 50,
             "ambiguous_all_binding": out["ambiguous_bounds"]["ambiguous_all_binding_pct"] < 50,
             "extreme_most_favourable": out["extreme_bounds"]["most_favourable_to_binding_pct"] < 50,
             "framework_bootstrap_upper": out["framework_bootstrap"]["binding_pct_ci95"][1] < 50,
             "framework_weighted_mean": out["framework_weighted"]["mean_framework_binding_pct"] < 50}
    claim["survives_every_scenario"] = all(v for k, v in claim.items() if k not in ("statement",))
    out["claim_binding_is_minority"] = claim
    return out


def main():
    out = compute()
    (ROOT / "data" / "robustness.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("base", "leave_one_family_out_range", "excluded_bounds", "ambiguous_bounds",
                                          "extreme_bounds", "framework_weighted", "framework_bootstrap",
                                          "claim_binding_is_minority")}, indent=1))


if __name__ == "__main__":
    main()
