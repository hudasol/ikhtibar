"""Paper values for phase 6 (registered primary analyses), read from data/phase6/*.json. Keys start with p6_."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _j(name):
    return json.loads((ROOT / "data" / "phase6" / name).read_text(encoding="utf-8"))


def _ci(x):
    return "%s to %s" % (x[0], x[1])


def values():
    v = {}
    sp = json.loads((ROOT / "data" / "phase6" / "split.json").read_text())
    v["p6_split_seed"] = sp["seed"]
    ex = _j("exploratory.json")
    for tag, f in (("c", "confirmation"), ("d", "design"), ("o", "old"), ("n", "new"), ("a", "all")):
        r = _j(f"results_{f}.json")
        v[f"p6_{tag}_rows"], v[f"p6_{tag}_docs"], v[f"p6_{tag}_multi"] = r["n_rows"], r["n_docs"], r["n_multi_row_docs"]
        v[f"p6_{tag}_mixed"], v[f"p6_{tag}_mixed_ci"] = r["mixed_share_multi_pct"], _ci(r["mixed_share_multi_wilson95"])
        v[f"p6_{tag}_conc"], v[f"p6_{tag}_chance"] = r["doc_concordance_pct"], r["chance_concordance_pct"]
        v[f"p6_{tag}_excess"], v[f"p6_{tag}_excess_ci"] = r["concordance_excess_pp"], _ci(r["concordance_excess_ci95"])
        v[f"p6_{tag}_anyb"], v[f"p6_{tag}_anyb_ci"] = r["any_binding_docs_pct"], _ci(r["any_binding_docs_wilson95"])
        v[f"p6_{tag}_anyb_k"] = round(r["any_binding_docs_pct"] * r["n_docs"] / 100)
        v[f"p6_{tag}_docw"], v[f"p6_{tag}_docw_ci"] = r["doc_weighted_binding_pct"], _ci(r["doc_weighted_binding_ci95"])
        v[f"p6_{tag}_rowb"], v[f"p6_{tag}_rowb_ci"] = r["row_binding_pct"], _ci(r["row_binding_ci95"])
        v[f"p6_{tag}_mixed_k"] = round(r["mixed_share_multi_pct"] * r["n_multi_row_docs"] / 100)
        for c in "AB":
            v[f"p6_{tag}_gap{c}"], v[f"p6_{tag}_gap{c}_ci"] = r["s1_gap_within_type_pp"][c], _ci(r["s1_gap_ci95"][c])
        v[f"p6_{tag}_gap_nb"] = int(r["s1_gap_binding_rows_compared"]["A"])
        v[f"p6_{tag}_kappa"], v[f"p6_{tag}_kappa_ci"] = ex["subsets"][f]["pair_kappa"], _ci(ex["subsets"][f]["ci95"])
        if tag == "c":
            d = r["decisions"]
            word = lambda b: "passed" if b else "failed"
            v["p6_C1"], v["p6_C2"], v["p6_C3"], v["p6_C4"] = (word(d["C1_documents_are_pure"]), word(d["C2_concordance_excess"]),
                                                              word(d["C3_minority_of_documents_binding"]),
                                                              word(d["C4_minority_of_documents_weighted"]))
            v["p6_C5"] = ("supported" if d["C5_process_only_gap_ci_excludes_zero"] else
                          "direction supported, interval includes zero" if d["C5_process_only_gap_direction"] else "not supported")
            v["p6_n_pass"] = sum(1 for k in ("C1_documents_are_pure", "C2_concordance_excess",
                                             "C3_minority_of_documents_binding", "C4_minority_of_documents_weighted") if d[k])
    # round kappa display
    return v
