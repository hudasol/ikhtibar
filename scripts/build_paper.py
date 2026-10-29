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
             ("keyword_rule", "Keyword rule"), ("tfidf_lr", "TF-IDF, logistic regression"), ("tfidf_lr_fw", "TF-IDF plus document"),
             ("embed_lr", "Embedding, logistic regression"), ("embed_lr_fw", "Embedding plus document")]

    def cell(task, m, prot):
        x = b[task][prot].get(m)
        return "n/a" if x is None else "%.1f" % x["accuracy"]

    body = []
    for m, lab in names:
        row = [lab] + [cell("binding5", m, "cv"), cell("binding5", m, "gcv"), cell("binding5", m, "lofo"),
                       cell("binding3", m, "gcv"), cell("test_type", m, "gcv"), cell("test_type", m, "lofo")]
        if all(c == "n/a" for c in row[1:]):
            continue
        body.append(row)
    t["tex_baselines"] = tabular(["Method", "B5 row", "B5 doc", "B5 LOFO", "B3 doc", "Type doc", "Type LOFO"], body, "lrrrrrr")

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
            ["Document level bootstrap, 95\\% interval", "%s to %s" % tuple(rb["framework_bootstrap"]["binding_pct_ci95"])],
            ["Without ISO and IEC catalogue rows", rb["access_sensitivity"]["without_iso_catalogue_rows"]["binding_pct"]],
            ["Without machine translated rows", rb["access_sensitivity"]["without_translated_rows"]["binding_pct"]],
            ["Most favourable assumptions with document resampling, 95\\% interval", "%s to %s" % tuple(rb["favourable_with_sampling"]["binding_pct_ci95"])]]
    t["tex_robust"] = tabular(["Scenario", "Binding share (\\%)"], body, "lr")

    def iv(x):
        return "%s to %s" % (x[0], x[1])
    body = [["Errors as graded by the verifier", "%d of %d" % (vf["errors_as_graded"], vf["readable"]), vf["error_rate_as_graded_pct"], iv(vf["error_rate_as_graded_ci95"])],
            ["Errors after strict grading", "%d of %d" % (vf["errors_strict"], vf["readable"]), vf["error_rate_strict_pct"], iv(vf["error_rate_strict_ci95"])],
            ["Any fault, including minor", "%d of %d" % (vf["any_fault_strict"], vf["readable"]), vf["any_fault_strict_pct"], iv(vf["any_fault_strict_ci95"])]]
    t["tex_verif"] = tabular(["Measure", "Rows", "Rate (\\%)", "95\\% interval"], body, "lrrr")
    return t


G3 = {"mandatory": "b", "conditional": "b", "voluntary": "n", "guidance": "n", "ambiguous": "a"}


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, 100 * (c - h)), min(100.0, 100 * (c + h)))


def evidence_rows():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if r["row_type"] == "test" and r["headline_include"] == "yes"]


def evidence_all():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def extra_tables():
    t = {}
    rows = evidence_rows()
    fam = {}
    for r in rows:
        d = fam.setdefault(r["family"], {"b": 0, "n": 0, "a": 0, "docs": set()})
        d[G3[r["binding_status"]]] += 1
        d["docs"].add(r["framework"])
    order = sorted(fam, key=lambda f: (-fam[f]["b"] / sum(fam[f][k] for k in "bna"), f))
    body = []
    for f in order:
        d = fam[f]
        n = d["b"] + d["n"] + d["a"]
        lo, hi = wilson(d["b"], n)
        body.append([tex(f), len(d["docs"]), n, d["b"], d["n"], d["a"], "%.0f (%.0f to %.0f)" % (100 * d["b"] / n, lo, hi)])
    N = sum(x[2] for x in body)
    B = sum(x[3] for x in body)
    lo, hi = wilson(B, N)
    body.append(["All headline rows", sum(x[1] for x in body), N, B, sum(x[4] for x in body), sum(x[5] for x in body),
                 "%.0f (%.0f to %.0f)" % (100 * B / N, lo, hi)])
    t["tex_family"] = tabular(["Family", "Docs", "Rows", "Binding", "Vol./guid.", "Ambig.", "Binding \\% (95\\% CI)"], body, "lrrrrrr")

    tp = {}
    for r in rows:
        d = tp.setdefault(r["primary_test_type"], {"b": 0, "n": 0, "a": 0})
        d[G3[r["binding_status"]]] += 1
    body = []
    for c in build_docs.TYPES:
        d = tp.get(c, {"b": 0, "n": 0, "a": 0})
        n = d["b"] + d["n"] + d["a"]
        body.append([c, tex(build_docs.TYPE_NAME[c]), n, d["b"], d["n"], d["a"]])
    t["tex_types"] = tabular(["Code", "Test type", "Rows", "Binding", "Vol./guid.", "Ambig."], body, "llrrrr")
    import re as _re
    defs = {}
    for line in (ROOT / "docs_src" / "REPORT.tmpl.md").read_text(encoding="utf-8").splitlines():
        mm = _re.match(r"\| ([A-Z]{2,5}) \| [^|]+ \| ([^|]+) \|", line)
        if mm:
            defs[mm.group(1)] = mm.group(2).strip()
    t["tex_taxonomy"] = tabular(["Code", "Test type", "Definition"], [[c, tex(build_docs.TYPE_NAME[c]), tex(defs.get(c, ""))] for c in build_docs.TYPES], "lp{3.4cm}p{7.6cm}")

    sp = j("data/specificity.json")["by_coder"]
    body = []
    for c in "AB":
        for g, lab in (("binding", "Binding"), ("non_binding", "Voluntary or guidance"), ("ambiguous", "Ambiguous")):
            x = sp[c]["counts"][g]
            body.append(["Coder " + c, lab, x["S1"], x["S2"], x["S3"], x["S4"], x["n"]])
    t["tex_spec"] = tabular(["Coder", "Binding status", "S1", "S2", "S3", "S4", "n"], body, "llrrrrr")

    v = j("data/verification/phase4/stats_p4.json")
    ev = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data/evidence_table.csv", encoding="utf-8"))}
    et = {}
    for f in sorted((ROOT / "data/verification/phase4").glob("v4*res*.csv")):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r["verdict"] == "ERROR" or (r["row_id"] in v["error_rows_strict"] and r["error_type"] != "none"):
                et[r["row_id"]] = r["error_type"].replace("_", " ")
    body = [[tex(rid), tex(ev[rid]["family"]), tex(et.get(rid, "see file")), tex(v["row_verdicts"][rid]["as_graded"].lower())] for rid in v["error_rows_strict"]]
    t["tex_errors"] = tabular(["Row", "Family", "Error type", "As graded"], body, "llll")

    ar = j("data/evaluation/archetypes.json")["archetypes"]
    body = []
    for k, x in ar.items():
        f = x["full"]
        s = f.get("summary", f)
        body.append([k, tex(x["label"]), s.get("APPLIES", "?"), s.get("DOES_NOT_APPLY", "?"), s.get("UNKNOWN", "?"), f.get("rows_binding_you_yes", "?")])
    t["tex_arch"] = tabular(["Id", "Profile", "Appl.", "Not", "Unkn.", "YES"], body, "lp{7.6cm}rrrr")
    return t


def author_block():
    import os
    if os.environ.get("IKHTIBAR_ANON"):
        return "\\author{Anonymous submission}\n\\date{}"
    return "\\author{Huda Mueen\\\\Independent researcher, United Arab Emirates}\n\\date{}"


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
    vals.update(extra_tables())
    for k in list(vals):
        if k.startswith("sp_") and isinstance(vals[k], str):
            vals[k] = re.sub(r"(?<![\w.])-(?=\d)", "$-$", vals[k])
    vals["author_block"] = author_block()
    allrows = evidence_all()
    vals["n_docs_total"] = len({r["framework"] for r in allrows})
    vals["n_fam_total"] = len({r["family"] for r in allrows})
    tmpl = (PAPER / "main.tmpl.tex").read_text(encoding="utf-8")
    ck = set()
    for m in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", tmpl):
        ck |= {x.strip() for x in m.group(1).split(",")}
    vals["n_full"] = sum(1 for r in rows if r["key"] in ck and r["read_level"] == "full_text")
    vals["n_cited"] = len(ck)
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
