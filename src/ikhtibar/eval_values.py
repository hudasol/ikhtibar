"""Values for docs/EVALUATION.md, read from the committed result files of phase 4 (nothing is typed by hand)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _j(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def _t(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in body]
    return "\n".join(out)


def _ci(x):
    return f"{x[0]} to {x[1]}"


def values():
    b, e, a = _j("data/baselines/results.json"), _j("data/evaluation/results.json"), _j("data/coding/phase4/agreement.json")
    rb, cp, vf = _j("data/robustness.json"), _j("data/completeness/recall.json"), _j("data/verification/phase4/stats_p4.json")
    sim = _j("data/evaluation/simulation.json")
    names = {"majority": "Majority class", "framework": "Document prior (most common label in the same document)",
             "modal_rule": "Wording rule (shall, must versus should, may)", "keyword_rule": "Keyword rule (taxonomy definitions)",
             "tfidf_lr": "TF-IDF with logistic regression", "tfidf_lr_fw": "TF-IDF with logistic regression plus document indicator"}
    v = {}

    def block(task, order):
        rows = []
        for m in order:
            c, l = b[task]["cv"][m], b[task]["lofo"][m]
            rows.append([names[m], f"{c['accuracy']} ({_ci(c['accuracy_ci95'])})", c["macro_f1"], c["kappa"],
                         f"{l['accuracy']} ({_ci(l['accuracy_ci95'])})", l["macro_f1"]])
        return _t(["Method", "Accuracy, repeated 5 fold CV (95% CI)", "Macro F1", "Kappa", "Accuracy, leave one family out (95% CI)", "Macro F1"], rows)

    v["bl_binding5"] = block("binding5", ["majority", "framework", "modal_rule", "tfidf_lr", "tfidf_lr_fw"])
    v["bl_binding3"] = block("binding3", ["majority", "framework", "modal_rule", "tfidf_lr", "tfidf_lr_fw"])
    v["bl_type"] = block("test_type", ["majority", "framework", "keyword_rule", "tfidf_lr", "tfidf_lr_fw"])
    v["bl_n"] = b["meta"]["n_rows"]
    v["bl_frameworks"] = b["meta"]["n_frameworks"]
    v["bl_families"] = b["meta"]["n_families"]
    v["bl_repeats"] = b["meta"]["repeats"]
    v["bl_fw5"] = b["binding5"]["cv"]["framework"]["accuracy"]
    v["bl_fw5_lofo"] = b["binding5"]["lofo"]["framework"]["accuracy"]
    v["bl_maj5"] = b["binding5"]["cv"]["majority"]["accuracy"]
    v["bl_tfidf5"] = b["binding5"]["cv"]["tfidf_lr"]["accuracy"]
    v["bl_kw"] = b["test_type"]["cv"]["keyword_rule"]["accuracy"]
    v["bl_tfidf_type"] = b["test_type"]["cv"]["tfidf_lr"]["accuracy"]
    v["bl_maj_type"] = b["test_type"]["cv"]["majority"]["accuracy"]
    v["bl_sklearn"] = b["meta"]["sklearn"]

    en = e["engine"]
    v["ev_scn"], v["ev_spec"], v["ev_unspec"] = e["scenarios_total"], e["scenarios_specified"], e["scenarios_unspecified"]
    v["ev_items"], v["ev_dec"] = e["items"], en["item_decisions"]
    v["ev_ok"], v["ev_acc"] = en["agree_with_expected"], en["accuracy"]
    v["ev_exact"], v["ev_exact_pct"] = en["scenarios_exact_match"], en["scenarios_exact_match_pct"]
    v["ev_unknown"] = en["unknown_returned"]
    v["ev_wex"], v["ev_wap"] = en["wrongly_excluded"], en["wrongly_applied"]
    lab = {"closed_two_valued": "Two valued, missing answer counts as no", "open_two_valued": "Two valued, missing answer counts as yes",
           "always_applies": "Every item applies", "structure_only": "Answers ignored, unconditional items only",
           }
    rows = [["This engine (three valued)", en["accuracy"], en["scenarios_exact_match_pct"], en["wrongly_excluded"], en["wrongly_applied"], en["unknown_returned"]]]
    for k, t in lab.items():
        x = e["baselines"][k]
        rows.append([t, x["accuracy"], x["scenarios_exact_match_pct"], x["wrongly_excluded"], x["wrongly_applied"], x["unknown_returned"]])
    v["ev_table"] = _t(["Method", "Item accuracy (%)", "Scenarios matched exactly (%)", "Wrongly excluded", "Wrongly applied", "Returned unknown"], rows)
    v["ev_sim_profiles"], v["ev_sim_steps"], v["ev_sim_flips"] = sim["profiles"], sim["monotonicity_steps_checked"], sim["applies_to_not_apply_flips"]
    v["ev_invalid_rejected"] = sum(x["engine"] == "rejected with a message" for x in e["invalid_inputs"])
    v["ev_invalid_crashed"] = sum(x["engine"] == "crashed" for x in e["invalid_inputs"])
    v["ev_invalid_n"] = len(e["invalid_inputs"])
    i0 = _j("data/evaluation/initial_run/results.json")
    v["ev0_acc"], v["ev0_ok"], v["ev0_wex"] = i0["engine"]["accuracy"], i0["engine"]["agree_with_expected"], i0["engine"]["wrongly_excluded"]
    v["ev0_exact"] = i0["engine"]["scenarios_exact_match"]
    v["ev0_crash"] = sum(x["engine"] == "crashed" for x in i0["invalid_inputs"])

    f = a["fields"]
    rows = []
    for lab_, k in (("Binding status, five classes", "binding5"), ("Binding status, three classes", "binding3"), ("Primary test type", "test_type")):
        p = f[k]["pairs"]
        rows.append([lab_, f"{p['original|coder2']['agreement_pct']} ({p['original|coder2']['kappa']})",
                     f"{p['original|coder3']['agreement_pct']} ({p['original|coder3']['kappa']})",
                     f"{p['coder2|coder3']['agreement_pct']} ({p['coder2|coder3']['kappa']})", f[k]["krippendorff_alpha_3_coders"]])
    v["ag_table"] = _t(["Field", "Original and blind coder 2: agreement % (kappa)", "Original and blind coder 3", "Blind coder 2 and 3", "Krippendorff alpha, 3 coders"], rows)
    v["ag_n"] = a["n"]
    v["ag_odd_original"] = a["binding5_odd_one_out"].get("original", 0)
    v["ag_odd_total"] = sum(a["binding5_odd_one_out"].values())
    v["ag_k_blind"] = f["binding5"]["pairs"]["coder2|coder3"]["kappa"]
    v["ag_k_orig"] = f["binding5"]["pairs"]["original|coder2"]["kappa"]
    ks = sorted([f["binding5"]["pairs"]["original|coder2"]["kappa"], f["binding5"]["pairs"]["original|coder3"]["kappa"]])
    v["ag_k_orig_range"] = f"{ks[0]} to {ks[1]}"

    ba, ex, am, xt = rb["base"], rb["excluded_bounds"], rb["ambiguous_bounds"], rb["extreme_bounds"]
    lo = rb["leave_one_family_out_range"]
    v["rb_n"], v["rb_pct"], v["rb_bind"], v["rb_amb"] = ba["n"], ba["binding_pct"], ba["binding"], ba["ambiguous"]
    rows = [["Headline test rows as coded", ba["binding_pct"]],
            [f"Leave one family out, lowest (without {lo['family_giving_min']})", lo["min_binding_pct"]],
            [f"Leave one family out, highest (without {lo['family_giving_max']})", lo["max_binding_pct"]],
            ["Rows excluded from the headline added back, all counted binding", ex["all_excluded_binding_pct"]],
            ["Rows excluded from the headline added back, all counted non binding", ex["all_excluded_non_binding_pct"]],
            ["Ambiguous rows all counted binding", am["ambiguous_all_binding_pct"]],
            ["Both adjustments, most favourable to binding", xt["most_favourable_to_binding_pct"]],
            ["Both adjustments, least favourable to binding", xt["least_favourable_to_binding_pct"]],
            ["Each document weighted equally (mean over documents)", rb["framework_weighted"]["mean_framework_binding_pct"]],
            ["Document level bootstrap, 95% interval", _ci(rb["framework_bootstrap"]["binding_pct_ci95"])]]
    v["rb_table"] = _t(["Scenario", "Binding share of test provisions (%)"], rows)
    v["rb_max"] = xt["most_favourable_to_binding_pct"]
    v["rb_docs"] = rb["framework_weighted"]["frameworks"]
    v["rb_docs_any"] = rb["framework_weighted"]["frameworks_with_any_binding_test_provision"]
    v["rb_docs_any_pct"] = rb["framework_weighted"]["frameworks_with_any_binding_pct"]
    v["rb_survives"] = "survives every scenario" if rb["claim_binding_is_minority"]["survives_every_scenario"] else "does NOT survive every scenario"

    v["cp_pos"], v["cp_in"], v["cp_rec"] = cp["confirmed_positive"], cp["confirmed_positive_in_table"], cp["recall_confirmed_pct"]
    v["cp_ci"], v["cp_unres"], v["cp_unres_in"] = _ci(cp["recall_confirmed_ci95"]), cp["unresolved"], cp["unresolved_in_table"]
    v["cp_lb"], v["cp_ref"], v["cp_out"] = cp["recall_lower_bound_pct"], cp["reference_candidates"], cp["out_of_frame"]
    v["cp_missed"] = "; ".join(m["title"] for m in cp["missed_confirmed"])

    v["vf_sampled"], v["vf_read"], v["vf_read_pct"] = vf["sampled"], vf["readable"], vf["readable_pct_of_sample"]
    v["vf_unread_pct"] = round(100 - vf["readable_pct_of_sample"], 1)
    v["vf_unread"], v["vf_pop"] = vf["unreadable"], vf["population_size"]
    v["vf_err_g"], v["vf_err_g_pct"], v["vf_err_g_ci"] = vf["errors_as_graded"], vf["error_rate_as_graded_pct"], _ci(vf["error_rate_as_graded_ci95"])
    v["vf_err_s"], v["vf_err_s_pct"], v["vf_err_s_ci"] = vf["errors_strict"], vf["error_rate_strict_pct"], _ci(vf["error_rate_strict_ci95"])
    v["vf_fault"], v["vf_fault_pct"], v["vf_fault_ci"] = vf["any_fault_strict"], vf["any_fault_strict_pct"], _ci(vf["any_fault_strict_ci95"])
    pp = vf["pooled_with_phase3_fresh_sample"]
    v["vf_pool"] = f"{pp['errors']} of {pp['readable']} ({pp['pct']}%, 95% interval {_ci(pp['ci95'])})"
    v["vf_err_rows"] = ", ".join(vf["error_rows_strict"])
    v["vf_bound_hi"] = vf["bounds_all_sampled_strict_error_pct"]["all_of_unreadable_in_error"]
    return v
