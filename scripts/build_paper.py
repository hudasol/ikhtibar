"""Build paper/main.tex and paper/refs.bib from paper/main.tmpl.tex, the result files and data/paper/refs_candidates.csv.

Every number in the paper is read from a committed result file. Only works listed in refs_candidates.csv can be cited.
Run: PYTHONPATH=src python scripts/build_paper.py   (then: cd paper && pdflatex main && bibtex main && pdflatex main && pdflatex main)
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ikhtibar import eval_values, build_docs  # noqa: E402

PAPER = ROOT / "paper"


def tex(s):
    s = str(s)
    for a, b in (("\\", "\\textbackslash{}"), ("&", "\\&"), ("%", "\\%"), ("_", "\\_"), ("#", "\\#"), ("$", "\\$")):
        s = s.replace(a, b)
    return s.replace("`", "")


def j(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def bibtex_key_ok(rows):
    return {r["key"] for r in rows}


def make_bib(rows):
    """Write BibTeX from data/paper/refs_curated.csv (structured fields; only facts seen on opened pages)."""
    def esc(v):
        v = re.sub(r"(?<!\\)&", r"\\&", v)
        v = re.sub(r"(?<!\\)%", r"\\%", v)
        return v.replace("_", "\\_") if "http" not in v else v

    out = []
    for r in rows:
        fields = []
        for k in ("author", "title", "journal", "booktitle", "institution", "howpublished", "year", "volume",
                  "number", "pages", "doi", "note", "url"):
            v = (r.get(k) or "").strip()
            if not v:
                continue
            if k == "title":
                v = "{" + esc(v) + "}"
            elif k in ("doi", "url"):
                pass
            else:
                v = esc(v)
            fields.append((k, v))
        body = ",\n".join("  %s = {%s}" % (k, v) for k, v in fields)
        out.append("@%s{%s,\n%s\n}\n" % (r["entrytype"] or "misc", r["key"], body))
    return "\n".join(out)


def tabular(header, body, spec):
    lines = ["\\begin{tabular}{%s}" % spec, "\\toprule", " & ".join(header) + " \\\\", "\\midrule"]
    lines += [" & ".join(str(c) for c in r) + " \\\\" for r in body]
    lines += ["\\bottomrule", "\\end{tabular}"]
    return "\n".join(lines)


def tables(b, e, a, rb, vf):
    t = {}
    names = [("majority", "Majority class"), ("framework", "Document prior"), ("modal_rule", "Wording rule"),
             ("keyword_rule", "Keyword rule"), ("tfidf_lr", "TF-IDF, logistic regression"), ("tfidf_lr_fw", "TF-IDF plus document")]

    def cell(task, m, prot):
        x = b[task][prot].get(m)
        return "n/a" if x is None else "%.1f" % x["accuracy"]

    body = []
    for m, lab in names:
        row = [lab] + [cell("binding5", m, "cv"), cell("binding5", m, "lofo"), cell("binding3", m, "cv"),
                       cell("test_type", m, "cv"), cell("test_type", m, "lofo")]
        if all(c == "n/a" for c in row[1:]):
            continue
        body.append(row)
    t["tex_baselines"] = tabular(["Method", "Binding (5) CV", "Binding (5) LOFO", "Binding (3) CV", "Type CV", "Type LOFO"], body, "lrrrrr")

    en = e["engine"]
    lab = [("closed_two_valued", "Two valued, missing counts as no"), ("open_two_valued", "Two valued, missing counts as yes"),
           ("always_applies", "Every item applies"), ("structure_only", "Answers ignored")]
    body = [["Three valued engine", en["accuracy"], en["wrongly_excluded"], en["wrongly_applied"], en["unknown_returned"]]]
    for k, l in lab:
        x = e["baselines"][k]
        body.append([l, x["accuracy"], x["wrongly_excluded"], x["wrongly_applied"], x["unknown_returned"]])
    t["tex_tool"] = tabular(["Method", "Accuracy (\\%)", "Wrongly excluded", "Wrongly applied", "Unknown"], body, "lrrrr")

    f = a["fields"]
    body = []
    for l, k in (("Binding status (5)", "binding5"), ("Binding status (3)", "binding3"), ("Primary test type", "test_type")):
        p = f[k]["pairs"]
        body.append([l, "%.1f / %.2f" % (p["original|coder2"]["agreement_pct"], p["original|coder2"]["kappa"]),
                     "%.1f / %.2f" % (p["original|coder3"]["agreement_pct"], p["original|coder3"]["kappa"]),
                     "%.1f / %.2f" % (p["coder2|coder3"]["agreement_pct"], p["coder2|coder3"]["kappa"]),
                     "%.2f" % f[k]["krippendorff_alpha_3_coders"]])
    t["tex_agreement"] = tabular(["Field", "Orig.\\ and B2", "Orig.\\ and B3", "B2 and B3", "Alpha (3)"], body, "lrrrr")

    lo = rb["leave_one_family_out_range"]
    ex, am, xt = rb["excluded_bounds"], rb["ambiguous_bounds"], rb["extreme_bounds"]
    body = [["Headline test rows as coded", rb["base"]["binding_pct"]],
            ["Leave one family out, range", "%s to %s" % (lo["min_binding_pct"], lo["max_binding_pct"])],
            ["Excluded rows added back, all binding", ex["all_excluded_binding_pct"]],
            ["Ambiguous rows all binding", am["ambiguous_all_binding_pct"]],
            ["Both, most favourable to binding", xt["most_favourable_to_binding_pct"]],
            ["Each document weighted equally", rb["framework_weighted"]["mean_framework_binding_pct"]],
            ["Document level bootstrap, 95\\% interval", "%s to %s" % tuple(rb["framework_bootstrap"]["binding_pct_ci95"])]]
    t["tex_robust"] = tabular(["Scenario", "Binding share (\\%)"], body, "lr")

    def iv(x):
        return "%s to %s" % (x[0], x[1])
    body = [["Errors as graded by the verifier", "%d of %d" % (vf["errors_as_graded"], vf["readable"]), vf["error_rate_as_graded_pct"], iv(vf["error_rate_as_graded_ci95"])],
            ["Errors after strict grading", "%d of %d" % (vf["errors_strict"], vf["readable"]), vf["error_rate_strict_pct"], iv(vf["error_rate_strict_ci95"])],
            ["Any fault, including minor", "%d of %d" % (vf["any_fault_strict"], vf["readable"]), vf["any_fault_strict_pct"], iv(vf["any_fault_strict_ci95"])]]
    t["tex_verif"] = tabular(["Measure", "Rows", "Rate (\\%)", "95\\% interval"], body, "lrrr")
    return t


def render():
    """Return (main.tex text, refs.bib text, number of works cited)."""
    rows = list(csv.DictReader(open(ROOT / "data" / "paper" / "refs_candidates.csv", encoding="utf-8")))
    keys = bibtex_key_ok(rows)
    cur = list(csv.DictReader(open(ROOT / "data" / "paper" / "refs_curated.csv", encoding="utf-8")))
    assert {r["key"] for r in cur} == keys, "refs_curated.csv and refs_candidates.csv list different keys"
    bib = make_bib(cur)
    vals = {}
    vals.update({k: tex(v) for k, v in j("data/docs_values.json").items()})
    vals.update({k: tex(v) for k, v in eval_values.values().items() if not k.startswith(("bl_binding", "bl_type", "ev_table", "ag_table", "rb_table"))})
    vals.update({k: tex(v) for k, v in build_docs.madoun_values().items()})
    b, e, a = j("data/baselines/results.json"), j("data/evaluation/results.json"), j("data/coding/phase4/agreement.json")
    rb, vf = j("data/robustness.json"), j("data/verification/phase4/stats_p4.json")
    vals.update(tables(b, e, a, rb, vf))
    text = (PAPER / "main.tmpl.tex").read_text(encoding="utf-8")
    missing = set()

    def rep(m):
        k = m.group(1).strip()
        if k not in vals:
            missing.add(k)
            return "??"
        return str(vals[k])

    out = re.sub(r"\{\{([^}]+)\}\}", rep, text)
    if missing:
        raise SystemExit("placeholders without a value: " + ", ".join(sorted(missing)))
    cited = set()
    for m in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", out):
        cited |= {x.strip() for x in m.group(1).split(",")}
    bad = sorted(cited - keys)
    if bad:
        raise SystemExit("cited keys not in data/paper/refs_candidates.csv: " + ", ".join(bad))
    return out, bib, len(cited)


def main():
    out, bib, n = render()
    (PAPER / "refs.bib").write_text(bib, encoding="utf-8")
    (PAPER / "main.tex").write_text(out, encoding="utf-8")
    print("wrote paper/main.tex and paper/refs.bib;", n, "works cited")


if __name__ == "__main__":
    main()
