"""Behaviour of the checklist tool on synthetic deployment archetypes.

Question answered: does the tool give materially different, sensible output for different kinds of deployment,
and how much does answering the questions reduce the unknown items? The archetypes are invented for this
analysis. They are not real systems and no real deployment is claimed. Output: data/evaluation/archetypes.json.
Run: python -m ikhtibar.archetypes
"""
import json
from pathlib import Path
from . import engine

ROOT = Path(__file__).resolve().parents[2]

# name, label, full answers
ARCHETYPES = [
    ("A1", "Internal document search assistant, federal entity",
     {"system_type": "genai_llm", "audience": "internal", "data_types": ["confidential_government"],
      "decision_impact": "none", "hosting": "uae_onprem", "acquisition": "vendor_product",
      "entity_zone": "federal_gov", "eu_market": "no"}),
    ("A2", "Public facing citizen chatbot, Dubai government",
     {"system_type": "genai_llm", "audience": "public_facing", "data_types": ["personal"],
      "decision_impact": "advisory", "hosting": "uae_cloud", "acquisition": "vendor_product",
      "entity_zone": "dubai_gov", "eu_market": "no"}),
    ("A3", "Clinical risk prediction model, Abu Dhabi health",
     {"system_type": "predictive_ml", "audience": "internal", "data_types": ["health", "sensitive_personal"],
      "decision_impact": "significant_support", "hosting": "uae_onprem", "acquisition": "mixed",
      "entity_zone": "health_abu_dhabi", "eu_market": "no"}),
    ("A4", "Automated benefit eligibility decision, Abu Dhabi government",
     {"system_type": "predictive_ml", "audience": "public_facing", "data_types": ["personal", "financial"],
      "decision_impact": "automated_significant", "hosting": "uae_onprem", "acquisition": "in_house",
      "entity_zone": "abu_dhabi_gov", "eu_market": "no"}),
    ("A5", "Face matching at a border checkpoint, federal entity",
     {"system_type": "computer_vision", "audience": "public_facing", "data_types": ["biometric", "personal"],
      "decision_impact": "critical", "hosting": "uae_onprem", "acquisition": "vendor_product",
      "entity_zone": "federal_gov", "eu_market": "no"}),
    ("A6", "Credit scoring model offered in the European market, financial centre firm",
     {"system_type": "predictive_ml", "audience": "public_facing", "data_types": ["financial", "personal"],
      "decision_impact": "automated_significant", "hosting": "foreign_cloud", "acquisition": "vendor_product",
      "entity_zone": "difc", "eu_market": "yes"}),
    ("A7", "Agent that takes actions on internal systems, Dubai government",
     {"system_type": "agentic", "audience": "internal", "data_types": ["personal"],
      "decision_impact": "significant_support", "hosting": "uae_cloud", "acquisition": "mixed",
      "entity_zone": "dubai_gov", "eu_market": "no"}),
    ("A8", "Rules based eligibility calculator (no learned model), federal entity",
     {"system_type": "rules_based", "audience": "public_facing", "data_types": ["personal"],
      "decision_impact": "significant_support", "hosting": "uae_onprem", "acquisition": "in_house",
      "entity_zone": "federal_gov", "eu_market": "no"}),
]
ORDER = ["system_type", "audience", "decision_impact", "data_types", "entity_zone", "acquisition", "hosting", "eu_market"]


def summary(ans):
    r = engine.run(ans)
    yes = {x["row_id"] for i in r["items"] for x in i["sources"] if x["binds_you"] == "YES"}
    return {**r["summary"], "rows_binding_you_yes": len(yes)}, r


def main():
    out = {"meta": {"note": "Synthetic archetypes; no real system is described.", "n_items": None},
           "archetypes": {}, "items_that_differ": {}}
    states = {}
    for aid, label, ans in ARCHETYPES:
        s, r = summary(ans)
        out["meta"]["n_items"] = sum(r["summary"].values())
        # answer curve: reveal questions one at a time in a fixed order
        curve = []
        part = {}
        for q in ORDER:
            part[q] = ans[q]
            cs, _ = summary(part)
            curve.append({"answered": len(part), "unknown": cs["UNKNOWN"], "applies": cs["APPLIES"],
                          "does_not_apply": cs["DOES_NOT_APPLY"]})
        out["archetypes"][aid] = {"label": label, "answers": ans, "full": s, "curve": curve,
                                  "baseline_zero_answers": summary({})[0]}
        states[aid] = {i["id"]: i["state"] for i in r["items"]}
    ids = sorted(states["A1"])
    varying = [i for i in ids if len({states[a][i] for a in states}) > 1]
    out["items_that_differ"] = {"n_varying": len(varying), "n_total": len(ids),
                                "constant_applies": sum(1 for i in ids if {states[a][i] for a in states} == {"APPLIES"}),
                                "constant_not_apply": sum(1 for i in ids if {states[a][i] for a in states} == {"DOES_NOT_APPLY"})}
    (ROOT / "data" / "evaluation" / "archetypes.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    for aid, v in out["archetypes"].items():
        print(aid, v["label"][:50], v["full"], [c["unknown"] for c in v["curve"]])
    print(out["items_that_differ"])


if __name__ == "__main__":
    main()
