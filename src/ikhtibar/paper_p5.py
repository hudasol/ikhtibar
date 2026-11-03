"""Values for the phase 5 paper sections, read from committed result files (nothing typed by hand).

Sources: data/extraction_recall/stats.json, data/phase5/comparison.json, data/completeness/recall_p5.json,
data/verification/phase5/stats_p5.json, data/coding/phase5/newrows/agreement_p5.json, data/uae_arabic/stats.json,
data/model_identity_log.csv and the frozen copies in data/phase5/frozen_v4/.
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _j(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def _ci(x):
    return f"{x[0]} to {x[1]}" if x and x[0] is not None else "not defined"


def values():
    ex, cm = _j("data/extraction_recall/stats.json"), _j("data/phase5/comparison.json")
    cp, vf = _j("data/completeness/recall_p5.json"), _j("data/verification/phase5/stats_p5.json")
    ag = _j("data/coding/phase5/newrows/agreement_p5.json")
    fz = cm["frozen_v4"]
    cov = _j("data/extraction_recall/coverage.json")
    v = {}
    # extraction recall
    v["p5_ex_sampled"] = ex["meta"]["documents_sampled"]
    v["p5_ex_read"] = ex["meta"]["documents_with_raw"]
    v["p5_ex_elig"] = ex["meta"]["n_eligible"]
    v["p5_ex_n"], v["p5_ex_hits"], v["p5_ex_recall"] = ex["recall"]["n"], ex["recall"]["hits"], ex["recall"]["pct"]
    v["p5_ex_ci_row"], v["p5_ex_ci_doc"] = _ci(ex["recall"]["wilson_row_ci95"]), _ci(ex["recall"]["doc_bootstrap_ci95"])
    v["p5_ex_prec"], v["p5_ex_prec_n"], v["p5_ex_prec_docs"] = ex["precision"]["pct"], ex["precision"]["n"], ex["precision"]["documents"]
    v["p5_ex_prec_ci"] = _ci(ex["precision"]["wilson_row_ci95"])
    v["p5_ex_rm"], v["p5_ex_rm_n"] = ex["rematch_agreement"]["agree_pct"], ex["rematch_agreement"]["n"]
    f = ex["force_of_independent_provisions"]
    v["p5_ex_f_matched"], v["p5_ex_f_missed"], v["p5_ex_f_mn"], v["p5_ex_f_xn"] = f["matched_binding_pct"], f["missed_binding_pct"], f["matched_n"], f["missed_n"]
    pd = ex["per_document"]
    v["p5_ex_nist_recall"] = round(100 * pd["X07"]["n_independent_in_table"] / pd["X07"]["n_independent"], 1)
    v["p5_ex_nist_n"] = pd["X07"]["n_independent"]
    v["p5_ex_excl"] = sum(1 for c in cov.values() if c.get("read") == "none")
    v["p5_ex_whole"] = sum(1 for c in cov.values() if c.get("precision_basis"))
    # frozen versus extended
    S = cm["sets"]
    v["p5_fz_n"], v["p5_fz_k"], v["p5_fz_pct"] = fz["base"]["n"], fz["base"]["binding"], fz["base"]["binding_pct"]
    v["p5_ex_tab_n"], v["p5_ex_tab_k"], v["p5_ex_tab_pct"] = cm["extended"]["base"]["n"], cm["extended"]["base"]["binding"], cm["extended"]["base"]["binding_pct"]
    v["p5_fz_lofo"] = f"{fz['leave_one_family_out_range']['min_binding_pct']} to {fz['leave_one_family_out_range']['max_binding_pct']}"
    v["p5_ex_lofo"] = f"{cm['extended']['leave_one_family_out_range']['min_binding_pct']} to {cm['extended']['leave_one_family_out_range']['max_binding_pct']}"
    v["p5_fz_boot"], v["p5_ex_boot"] = _ci(fz["framework_bootstrap"]["binding_pct_ci95"]), _ci(cm["extended"]["framework_bootstrap"]["binding_pct_ci95"])
    v["p5_fz_ext_hi"], v["p5_ex_ext_hi"] = fz["extreme_bounds"]["most_favourable_to_binding_pct"], cm["extended"]["extreme_bounds"]["most_favourable_to_binding_pct"]
    v["p5_fz_docmean"] = S["frozen_rows_in_extended_table"]["mean_document_share_pct"]
    v["p5_ex_docmean"] = S["extended"]["mean_document_share_pct"]
    for key, name in (("new_all", "na"), ("new_second_list", "ns")):
        b = S[key]
        v[f"p5_{name}_n"], v[f"p5_{name}_k"], v[f"p5_{name}_pct"] = b["n"], b["binding"], b["binding_pct"]
        v[f"p5_{name}_ci"], v[f"p5_{name}_docs"] = _ci(b["wilson_ci95"]), b["documents"]
        v[f"p5_{name}_docci"], v[f"p5_{name}_docmean"] = _ci(b["document_bootstrap_ci95"]), b["mean_document_share_pct"]
        v[f"p5_{name}_amb"] = b["ambiguous"]
    sv, ot, un = cm["sector_vs_other_new"]["sector"], cm["sector_vs_other_new"]["other"], cm["unseen_families_new"]
    v["p5_sec_n"], v["p5_sec_pct"], v["p5_sec_k"] = sv["n"], sv["binding_pct"], sv["binding"]
    v["p5_oth_n"], v["p5_oth_pct"], v["p5_oth_k"] = ot["n"], ot["binding_pct"], ot["binding"]
    v["p5_un_n"], v["p5_un_pct"], v["p5_un_k"] = un["n"], un["binding_pct"], un["binding"]
    g = cm["process_only_gap_coderA"]
    for key, name in (("extended", "ext"), ("new_second_list", "ns"), ("new_all", "na")):
        x = g[key]
        v[f"p5_gap_{name}"] = x.get("difference_pp")
        v[f"p5_gap_{name}_ci"] = _ci(x.get("difference_ci95_doc_cluster_pp"))
        v[f"p5_gap_{name}_nb"] = x.get("binding_n")
    sp = _j("data/specificity.json")["adjusted"]["A"]
    sf = _j("data/phase5/frozen_v4/data_specificity.json")["adjusted"]["A"]
    for pre, d in (("ex", sp), ("fz", sf)):
        v[f"p5_{pre}_adj_type"] = d["test_type|S1_process_only"]["difference_pp"]
        v[f"p5_{pre}_adj_type_ci"] = _ci(d["test_type|S1_process_only"]["ci95_doc_cluster_pp"])
        v[f"p5_{pre}_adj_fam"] = d["family|S1_process_only"]["difference_pp"]
        v[f"p5_{pre}_adj_fam_ci"] = _ci(d["family|S1_process_only"]["ci95_doc_cluster_pp"])
    ob = cm["baselines_out_of_sample_second_list"]
    for m in ("majority", "framework", "modal_rule", "tfidf_lr", "embed_lr"):
        v[f"p5_oos_{m}"] = ob[m]["accuracy_pct"]
    v["p5_oos_n"], v["p5_oos_docs"] = ob["majority"]["n"], ob["majority"]["documents"]
    bl = _j("data/baselines/results.json")["binding5"]["gcv"]
    bf = _j("data/phase5/frozen_v4/data_baselines_results.json")["binding5"]["gcv"]
    for m in ("majority", "framework", "modal_rule", "embed_lr"):
        v[f"p5_g_{m}"], v[f"p5_gf_{m}"] = bl[m]["accuracy"], bf[m]["accuracy"]
    lf = _j("data/baselines/results.json")["binding5"]["lofo"]
    lff = _j("data/phase5/frozen_v4/data_baselines_results.json")["binding5"]["lofo"]
    v["p5_lofo_embed"], v["p5_lofof_embed"], v["p5_lofo_maj"], v["p5_lofof_maj"] = lf["embed_lr"]["accuracy"], lff["embed_lr"]["accuracy"], lf["majority"]["accuracy"], lff["majority"]["accuracy"]
    pr = cm["predictions"]
    v["p5_pred_hits"], v["p5_pred_miss"], v["p5_pred_nt"] = pr["hits"], pr["misses"], pr["not_tested"]
    v["p5_pred_n"] = len(pr["scored"])
    fc = pr["failure_criteria"]
    v["p5_fail1"] = "did not" if not fc["finding1_fails"] else "did"
    v["p5_fail2"] = "did not" if not fc["finding2_fails"] else "did"
    v["p5_fail3"] = "did not" if not fc["finding3_fails"] else "did"
    v["p5_best_learned"], v["p5_maj_g"] = fc["best_learned_grouped_cv"], fc["majority_grouped_cv"]
    # completeness
    v["p5_cp_n"], v["p5_cp_yes"] = cp["instruments"], cp["has_testing_yes"]
    s, l = cp["confirmed_positive_strict"], cp["confirmed_positive_lenient"]
    v["p5_cp_strict"], v["p5_cp_strict_k"], v["p5_cp_strict_ci"] = s["pct"], s["hits"], _ci(s["wilson_ci95"])
    v["p5_cp_len"], v["p5_cp_len_k"], v["p5_cp_len_ci"] = l["pct"], l["hits"], _ci(l["wilson_ci95"])
    v["p5_cp_missed"] = len(cp["missed_confirmed"])
    ug = cp["by_group"].get("UAE and Gulf", {}).get("confirmed_positive_strict", {})
    v["p5_cp_uae"], v["p5_cp_uae_n"], v["p5_cp_uae_k"] = ug.get("pct"), ug.get("n"), ug.get("hits")
    ug2 = cp["by_group"].get("US and Canada", {}).get("confirmed_positive_strict", {})
    v["p5_cp_us"], v["p5_cp_us_n"] = ug2.get("pct"), ug2.get("n")
    v["p5_cp_read"] = cp["access"].get("read", 0)
    # verification
    e, n_, u_, po = vf["existing_sample"], vf["new_rows"], vf["us_candidate_rows"], vf["pooled"]
    v["p5_vf_ex_n"], v["p5_vf_ex_read"], v["p5_vf_ex_blocked"] = e["n"], e["readable"], e["n"] - e["readable"]
    v["p5_vf_nw_n"], v["p5_vf_nw_err"], v["p5_vf_nw_pct"] = n_["n"], n_["errors"], n_["error_rate_pct"]
    v["p5_vf_nw_ci"] = _ci(n_["error_rate_ci95"])
    v["p5_vf_nw_fault"], v["p5_vf_nw_fault_pct"] = n_["any_fault"], n_["any_fault_pct"]
    v["p5_vf_us_n"], v["p5_vf_us_err"] = u_["n"], u_["errors"]
    for k, nm in (("frozen_phase3_and_4", "fz"), ("plus_phase5_existing_sample", "ex"), ("plus_phase5_existing_and_new_rows", "all"), ("new_rows_only", "new")):
        v[f"p5_vf_p_{nm}"], v[f"p5_vf_p_{nm}_ci"] = po[k]["pct"], _ci(po[k]["ci95"])
        v[f"p5_vf_p_{nm}_e"], v[f"p5_vf_p_{nm}_n"] = po[k]["errors"], po[k]["readable"]
    # coding agreement on new rows
    v["p5_ag_n"] = ag["n"]
    v["p5_ag_b5_c2"], v["p5_ag_k5_c2"] = ag["binding5"]["original|C2"]["agree_pct"], ag["binding5"]["original|C2"]["kappa"]
    v["p5_ag_b5_c3"], v["p5_ag_k5_c3"] = ag["binding5"]["original|C3"]["agree_pct"], ag["binding5"]["original|C3"]["kappa"]
    v["p5_ag_b5_cc"], v["p5_ag_k5_cc"] = ag["binding5"]["C2|C3"]["agree_pct"], ag["binding5"]["C2|C3"]["kappa"]
    v["p5_ag_t_c2"], v["p5_ag_t_cc"] = ag["test_type"]["original|C2"]["agree_pct"], ag["test_type"]["C2|C3"]["agree_pct"]
    v["p5_ag_flips"] = max(ag["binding_vs_nonbinding_flips"].values())
    # uae arabic
    ua = _j("data/uae_arabic/stats.json")
    v["p5_ua_n"] = ua["meta"].get("rows_in_scope", "")
    v["p5_ua_checked"] = ua["binding_status_same"]["n"] + ua["binding_status_differs"]["n"]
    # model identity
    rows = list(csv.DictReader(open(ROOT / "data" / "model_identity_log.csv", encoding="utf-8")))
    v["p5_mi_runs"] = len(rows)
    v["p5_mi_reported"] = sum(1 for r in rows if r["reported_by_agent"] and not r["reported_by_agent"].startswith("agent could not"))
    v["p5_mi_unreported"] = v["p5_mi_runs"] - v["p5_mi_reported"]
    return v
