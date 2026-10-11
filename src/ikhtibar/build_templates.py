"""Render templates/test_evidence/<CODE>.md from data/test_templates.yaml and the evidence table.
Source rows listed under each template are chosen by script: verified headline test rows with that primary type,
at most one per family, ordered by binding strength then row id."""
import csv
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data"
RANK = {"mandatory": 0, "conditional": 1, "voluntary": 2, "guidance": 3, "ambiguous": 4}

def main():
    T = yaml.safe_load(open(D / "test_templates.yaml", encoding="utf-8"))
    rows = list(csv.DictReader(open(D / "evidence_table.csv", encoding="utf-8", newline="")))
    out = ROOT / "templates" / "test_evidence"
    out.mkdir(parents=True, exist_ok=True)
    for code, t in T.items():
        cand = [r for r in rows if r["primary_test_type"] == code and r["row_type"] == "test" and r["headline_include"] == "yes"
                and r["verification_status"].startswith("VERIFIED")]
        cand.sort(key=lambda r: (RANK[r["binding_status"]], r["row_id"]))
        seen, pick = set(), []
        for r in cand:
            if r["family"] in seen: continue
            seen.add(r["family"]); pick.append(r)
            if len(pick) == 5: break
        L = [f"# {code}: {t['name']}", "",
             "> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.", "",
             "## What to run", ""] + [f"- {x}" for x in t["what_to_run"]] + ["", "## What to record", ""] + [f"- {x}" for x in t["record"]] + \
            ["", "## What a reviewer looks for", ""] + [f"- {x}" for x in t["reviewer_looks_for"]] + ["", "## Evidence record (fill in)", "",
             "| Field | Entry |", "|---|---|", "| System and version | |", "| Test date and tester | |", "| Data used (source, version) | |",
             "| Acceptance criteria (fixed before testing) | |", "| Result | |", "| Findings and closure | |", "| Open items marked UNKNOWN | |", "| Approver | |", "",
             "## Source rows that motivate this template", "",
             "Selected by script from verified rows; these are examples, not a complete list. Statuses are the source's own."]
        L += ["", "| Row | Framework | Source status | Clause |", "|---|---|---|---|"]
        for r in pick:
            L.append(f"| `{r['row_id']}` | {r['framework'][:60]} | {r['binding_status']} | {r['clause_or_page'][:60]} |")
        if not pick:
            L.append("| (no verified row of this primary type in the current table) | | | |")
        (out / f"{code}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("templates written:", len(T))

if __name__ == "__main__":
    main()
