"""Phase 5: the extended table next to the frozen version 4.0 numbers, and the out of sample replication.

Frozen numbers are read from data/phase5/frozen_v4/ (copies of the result files at commit fa3e410). Extended numbers are read
from the current result files. The out of sample sets are:
  new_all      every phase 5 headline test row (ids containing -P5-)
  new_second   the same without the 19 United States candidate rows (documents found through the second reference list)
Predictions are the ones fixed in docs/PREREG_PHASE5.md before extraction; each is scored hit or miss here.
Output: data/phase5/comparison.json. Run: python -m ikhtibar.phase5_compare   (needs the baselines libraries)
"""
import csv, json, collections, re
from pathlib import Path
import numpy as np
from .completeness import wilson
from . import baselines as B

ROOT = Path(__file__).resolve().parents[2]
F = ROOT / "data" / "phase5" / "frozen_v4"
SEED = 20261103
US_CAND = ("US-NIST-P5", "US-OMB-P5", "US-WH-P5")
BIND = ("mandatory", "conditional")
SECTOR_WORDS = re.compile(r"medical|device|SR 11-7|SR 26-2|Model Risk|CFPB|Consumer Financial|APRA|HKMA|Hong Kong Monetary|"
                          r"Central Bank|FAA|aviation|automated driving|PMDA|HSA|MDCG|DoD|Defense|Defence|Texas|NSW|Financial Services Agency|"
                          r"Ofcom|FCA|Good Machine Learning|MHRA|Health Canada|FDA", re.I)


def j(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def share_block(rows):
    n = len(rows)
    k = sum(r["binding_status"] in BIND for r in rows)
    docs = collections.defaultdict(list)
    for r in rows:
        docs[r["framework"]].append(r["binding_status"] in BIND)
    per_doc = [100 * np.mean(v) for v in docs.values()]
    rng = np.random.RandomState(SEED)
    names = list(docs)
    boots = []
    for _ in range(4000):
        pick = rng.randint(0, len(names), len(names))
        kk = sum(sum(docs[names[i]]) for i in pick)
        nn = sum(len(docs[names[i]]) for i in pick)
        boots.append(100 * kk / nn if nn else 0)
    return {"n": n, "binding": k, "binding_pct": round(100 * k / n, 1) if n else None, "wilson_ci95": wilson(k, n),
            "mandatory": sum(r["binding_status"] == "mandatory" for r in rows),
            "ambiguous": sum(r["binding_status"] == "ambiguous" for r in rows),
            "documents": len(docs), "mean_document_share_pct": round(float(np.mean(per_doc)), 1) if per_doc else None,
            "document_bootstrap_ci95": [round(float(np.percentile(boots, 2.5)), 1), round(float(np.percentile(boots, 97.5)), 1)]}


def spec_gap(rows, A):
    """Difference in the share coded S1 (process only) between binding and non binding rows, coder A."""
    ids = [r for r in rows if r["row_id"] in A]
    b = [A[r["row_id"]] == "S1" for r in ids if r["binding_status"] in BIND]
    nb = [A[r["row_id"]] == "S1" for r in ids if r["binding_status"] in ("voluntary", "guidance")]
    if not b or not nb:
        return {"binding_n": len(b), "non_binding_n": len(nb), "difference_pp": None}
    d = 100 * (np.mean(b) - np.mean(nb))
    docs = collections.defaultdict(list)
    for r in ids:
        docs[r["framework"]].append(r)
    names = list(docs)
    rng = np.random.RandomState(SEED)
    bs = []
    for _ in range(4000):
        pick = [x for i in rng.randint(0, len(names), len(names)) for x in docs[names[i]]]
        pb = [A[r["row_id"]] == "S1" for r in pick if r["binding_status"] in BIND]
        pn = [A[r["row_id"]] == "S1" for r in pick if r["binding_status"] in ("voluntary", "guidance")]
        if pb and pn:
            bs.append(100 * (np.mean(pb) - np.mean(pn)))
    return {"binding_n": len(b), "non_binding_n": len(nb), "binding_s1_pct": round(100 * float(np.mean(b)), 1),
            "non_binding_s1_pct": round(100 * float(np.mean(nb)), 1), "difference_pp": round(float(d), 1),
            "difference_ci95_doc_cluster_pp": [round(float(np.percentile(bs, 2.5)), 1), round(float(np.percentile(bs, 97.5)), 1)] if bs else None}


def oos_baselines(old, new):
    """Train on the pre-existing headline rows, test on the new rows (documents unseen)."""
    allr = old + new
    texts = [r["requirement_paraphrase"] for r in allr]
    fws = [r["framework"] for r in allr]
    y = [r["binding_status"] for r in allr]
    tr, te = list(range(len(old))), list(range(len(old), len(allr)))
    X, _ = B.load_embeddings([r["requirement_paraphrase"] for r in B.load_rows()])
    out = {}
    # embedding rows are indexed by the order of B.load_rows(); map our rows to that order
    order = {r["row_id"]: i for i, r in enumerate(B.load_rows())}
    B.EMB["x"] = X[[order[r["row_id"]] for r in allr]]
    for name, fn in (("majority", B.method_majority), ("framework", B.method_framework), ("modal_rule", B.method_modal_rule),
                     ("tfidf_lr", B.method_tfidf_lr), ("embed_lr", B.method_embed_lr)):
        pred = fn(texts, fws, y, tr, te, "binding")
        ok = [pred[k] == y[i] for k, i in enumerate(te)]
        k = sum(ok)
        docs = collections.defaultdict(list)
        for kk, i in enumerate(te):
            docs[fws[i]].append(ok[kk])
        out[name] = {"accuracy_pct": round(100 * k / len(te), 1), "n": len(te), "wilson_ci95": wilson(k, len(te)),
                     "documents": len(docs)}
    return out


def score(o):
    """Score each preregistered prediction (docs/PREREG_PHASE5.md) as hit, miss or not tested. Ranges are copied from that file."""
    P = []

    def add(n, text, value, ok, note=""):
        P.append({"id": n, "prediction": text, "observed": value, "result": "not tested" if ok is None else ("hit" if ok else "miss"), "note": note})
    ns, na = o["sets"]["new_second_list"], o["sets"]["new_all"]
    add("1a", "binding share on new documents between 15% and 40%", f"{ns['binding_pct']}% on {ns['n']} rows (second list); {na['binding_pct']}% on {na['n']} rows (all new)",
        15 <= ns["binding_pct"] <= 40 and 15 <= na["binding_pct"] <= 40)
    sec, oth = o["sector_vs_other_new"]["sector"], o["sector_vs_other_new"]["other"]
    add("1b", "sector regulator documents have a higher binding share than national frameworks and standards",
        f"sector {sec['binding_pct']}% of {sec['n']} rows; other {oth['binding_pct']}% of {oth['n']} rows", sec["binding_pct"] > oth["binding_pct"])
    g = o["process_only_gap_coderA"]["new_second_list"]
    add("2", "process only gap positive and between 5 and 30 points (coder A, new documents)",
        f"{g.get('difference_pp')} points ({g.get('binding_n')} binding rows)", g.get("difference_pp") is not None and 5 <= g["difference_pp"] <= 30,
        "interval expected to include zero; direction is the test")
    bo = o["baselines_out_of_sample_second_list"]
    add("3", "document prior within 10 points of the majority rate and not above the wording rule by more than 10 points (new documents)",
        f"document prior {bo['framework']['accuracy_pct']}%, majority {bo['majority']['accuracy_pct']}%, wording rule {bo['modal_rule']['accuracy_pct']}%",
        abs(bo["framework"]["accuracy_pct"] - bo["majority"]["accuracy_pct"]) <= 10 and bo["framework"]["accuracy_pct"] - bo["modal_rule"]["accuracy_pct"] <= 10)
    add("4", "wording rule accuracy between 45% and 65% on new rows", f"{bo['modal_rule']['accuracy_pct']}%", 45 <= bo["modal_rule"]["accuracy_pct"] <= 65)
    u = o["unseen_families_new"]
    add("5", "binding share below 25% in families not in the frozen table (International, Other jurisdictions)",
        f"{u['binding_pct']}% of {u['n']} rows", u["binding_pct"] < 25)
    cp = json.loads((ROOT / "data" / "completeness" / "recall_p5.json").read_text(encoding="utf-8"))
    r = cp["confirmed_positive_strict"]["pct"]
    add("6", "recall lower than the frozen 68.4%, expected range 30% to 65%", f"{r}% strict ({cp['confirmed_positive_lenient']['pct']}% counting partial matches)",
        30 <= r <= 65, "lower than 68.4%: yes" if r < 68.4 else "not lower than 68.4%")
    ex = json.loads((ROOT / "data" / "extraction_recall" / "stats.json").read_text(encoding="utf-8"))
    add("7a", "extraction recall between 55% and 85%", f"{ex['recall']['pct']}%", 55 <= ex["recall"]["pct"] <= 85)
    add("7b", "extraction precision between 75% and 95%", f"{ex['precision']['pct']}% on {ex['precision']['n']} rows from {ex['precision']['documents']} documents",
        75 <= ex["precision"]["pct"] <= 95, "precision measured on only three documents read whole")
    f = ex["force_of_independent_provisions"]
    add("7c", "missed provisions are more often non binding than extracted ones", f"binding share: missed {f['missed_binding_pct']}%, matched {f['matched_binding_pct']}%",
        f["missed_binding_pct"] < f["matched_binding_pct"])
    add("8", "UAE Arabic agreement at least 80%", "not tested: the search budget was used up before any Arabic original could be read", None)
    v = json.loads((ROOT / "data" / "verification" / "phase5" / "stats_p5.json").read_text(encoding="utf-8"))
    nr = v["new_rows"]
    add("9", "strict error rate on new rows between 4% and 15%", f"{nr['error_rate_pct']}% ({nr['errors']} of {nr['readable']} readable rows, extracted rows); "
        f"{v['pooled']['new_rows_only']['pct']}% with the US candidate rows", 4 <= nr["error_rate_pct"] <= 15)
    bl = json.loads((ROOT / "data" / "baselines" / "results.json").read_text(encoding="utf-8"))["binding5"]["gcv"]
    best = max(bl[m]["accuracy"] for m in ("tfidf_lr", "embed_lr", "tfidf_lr_fw", "embed_lr_fw"))
    fail = {
        "finding1_fails": bool(ns["binding_pct"] >= 50 and ns["n"] >= 30 and ns["documents"] >= 8) or o["extended"]["base"]["binding_pct"] >= 50,
        "finding2_fails": (g.get("difference_pp") is not None and g["difference_pp"] <= 0),
        "finding3_fails": best - bl["majority"]["accuracy"] > 10 or bo["framework"]["accuracy_pct"] > bo["majority"]["accuracy_pct"],
        "best_learned_grouped_cv": best, "majority_grouped_cv": bl["majority"]["accuracy"],
    }
    return {"scored": P, "hits": sum(1 for x in P if x["result"] == "hit"), "misses": sum(1 for x in P if x["result"] == "miss"),
            "not_tested": sum(1 for x in P if x["result"] == "not tested"), "failure_criteria": fail}


def main():
    rows = [r for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8"))
            if r["row_type"] == "test" and r["headline_include"] == "yes"]
    old = [r for r in rows if "-P5-" not in r["row_id"]]
    new_all = [r for r in rows if "-P5-" in r["row_id"]]
    new_sec = [r for r in new_all if not r["row_id"].startswith(US_CAND)]
    sets = {"frozen_rows_in_extended_table": old, "extended": rows, "new_all": new_all, "new_second_list": new_sec}
    out = {"seed": SEED, "sets": {k: share_block(v) for k, v in sets.items()}}
    fz_stats, ex_stats = j(F / "data_stats.json"), j(ROOT / "data" / "stats.json")
    fz_rob, ex_rob = j(F / "data_robustness.json"), j(ROOT / "data" / "robustness.json")
    out["frozen_v4"] = {"headline_test_rows": fz_stats["test_rows_headline"], "binding_headline": fz_stats["binding_headline"],
                        "base": fz_rob["base"], "leave_one_family_out_range": fz_rob["leave_one_family_out_range"],
                        "framework_bootstrap": fz_rob["framework_bootstrap"], "extreme_bounds": fz_rob["extreme_bounds"]}
    out["extended"] = {"headline_test_rows": ex_stats["test_rows_headline"], "binding_headline": ex_stats["binding_headline"],
                       "base": ex_rob["base"], "leave_one_family_out_range": ex_rob["leave_one_family_out_range"],
                       "framework_bootstrap": ex_rob["framework_bootstrap"], "extreme_bounds": ex_rob["extreme_bounds"]}
    # specificity
    A = {}
    for part in (1, 2, 3):
        p = ROOT / "data" / "coding" / "phase5" / f"spec_A_{part}.csv"
        if p.exists():
            for r in csv.DictReader(open(p, encoding="utf-8")):
                A[r["row_id"]] = r["specificity"].strip()
    out["process_only_gap_coderA"] = {"frozen_published": j(F / "data_specificity.json").get("headline_gap_note", None),
                                      "old_rows": spec_gap(old, A), "extended": spec_gap(rows, A),
                                      "new_all": spec_gap(new_all, A), "new_second_list": spec_gap(new_sec, A)}
    # sector regulators versus national frameworks and standards among the new rows
    sect = [r for r in new_sec if SECTOR_WORDS.search(r["framework"])]
    oth = [r for r in new_sec if not SECTOR_WORDS.search(r["framework"])]
    out["sector_vs_other_new"] = {"sector": share_block(sect), "other": share_block(oth)}
    unseen = [r for r in new_sec if r["family"] in ("International", "Other-Jurisdictions")]
    out["unseen_families_new"] = share_block(unseen)
    out["baselines_out_of_sample"] = oos_baselines(sorted(old, key=lambda r: r["row_id"]), sorted(new_all, key=lambda r: r["row_id"]))
    out["baselines_out_of_sample_second_list"] = oos_baselines(sorted(old, key=lambda r: r["row_id"]), sorted(new_sec, key=lambda r: r["row_id"]))
    out["predictions"] = score(out)
    (ROOT / "data" / "phase5" / "comparison.json").write_text(json.dumps(out, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("sets", "sector_vs_other_new", "unseen_families_new", "baselines_out_of_sample_second_list")}, indent=1)[:6000])


if __name__ == "__main__":
    main()
