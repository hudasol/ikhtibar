"""Render the report, brief and summary tables from the data files.

Nothing in the generated documents is typed by hand when it is a number, a table or a row status.
Prose lives in docs_src/*.tmpl.md and uses {{key}} placeholders that this module fills.
Row identifiers written in backticks are checked against the table; an identifier whose row is
unverified or unverifiable gets a dagger (the dagger sign) and is excluded from the headline counts.
"""
import csv, collections, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA, DOCS, SRC = ROOT / "data", ROOT / "docs", ROOT / "docs_src"

DAG = "†"
UNRELIABLE = {"UNVERIFIED_BLOCKED", "UNVERIFIABLE_OTHER", "UNVERIFIED_SOURCE_NOT_READ", "ERROR_WITHDRAWN", "NEW_UNCHECKED"}

FAMS = ["EU-AI-Act", "EU-GPAI-CoP", "EU-Standards", "ISO-IEC", "US-NIST", "US-OMB", "UK", "Canada", "Singapore", "Japan",
        "Korea", "China", "UAE-Federal", "UAE-DIFC-ADGM", "UAE-Dubai", "UAE-AbuDhabi-DoH", "UAE-AbuDhabi-Other", "Saudi"]
FAM_LABEL = {
    "EU-AI-Act": "EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755", "EU-GPAI-CoP": "EU GPAI Code of Practice",
    "EU-Standards": "EU harmonised standards (JTC 21, EN 18286 citation)", "ISO-IEC": "ISO/IEC (catalogue level)",
    "US-NIST": "NIST (AI RMF, Playbook, 600-1, 800-2 draft)", "US-OMB": "US OMB M-25-21 and M-26-04",
    "UK": "UK (Playbook, ATRS, DSIT, AISI)", "Canada": "Canada Directive on Automated Decision-Making",
    "Singapore": "Singapore (AI Verify, Starter Kit, frameworks)", "Japan": "Japan (Act, plan, guidelines, Digital Agency DS-920, AISI)",
    "Korea": "South Korea AI Basic Act and Enforcement Decree", "China": "China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide)",
    "UAE-Federal": "UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL)",
    "UAE-DIFC-ADGM": "DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance)",
    "UAE-Dubai": "Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies)",
    "UAE-AbuDhabi-DoH": "Abu Dhabi DoH (health sector: Standard and Protocol)", "UAE-AbuDhabi-Other": "Abu Dhabi AI and Advanced Technology Council law",
    "Saudi": "Saudi Arabia (SDAIA, NCA draft, SFDA)"}
TYPES = ["PERF", "ROB", "FAIR", "SEC", "RED", "CSAFE", "PRIV", "TRANS", "OVER", "RISK", "DATA", "CONF", "REAL", "MON", "GATE"]
TYPE_NAME = {
    "PERF": "Performance and validity", "ROB": "Robustness and reliability", "FAIR": "Fairness and representativeness",
    "SEC": "Security and adversarial resilience", "RED": "Red teaming and dangerous capability evaluation",
    "CSAFE": "Content safety evaluation", "PRIV": "Privacy and data protection assessment",
    "TRANS": "Transparency, explainability and reproducibility", "OVER": "Human oversight validation",
    "RISK": "Risk, impact and compliance assessment", "DATA": "Data quality validation",
    "CONF": "Conformity assessment, independent review, certification", "REAL": "Real world, sandbox and pilot testing",
    "MON": "Post deployment monitoring and re assessment", "GATE": "Acceptance criteria and release decision"}
SYM = {"mandatory": "M", "conditional": "C", "voluntary": "V", "guidance": "G", "ambiguous": "A"}
RANK = {"mandatory": 5, "conditional": 4, "voluntary": 3, "guidance": 2, "ambiguous": 1}
RK = {"M": 4, "C": 3, "V": 2, "G": 1}


def read_csv(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct(a, b, d=0):
    return f"{100 * a / b:.{d}f}%" if b else "n/a"


def load():
    rows = read_csv(DATA / "evidence_table.csv")
    return rows, {r["row_id"]: r for r in rows}


def md_table(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in body]
    return "\n".join(out)


def tag(rid, by):
    r = by.get(rid)
    if r is None:
        return rid + " (MISSING)"
    return f"`{rid}`" + (DAG if r["headline_include"] != "yes" else "")


def dagger_pass(text, by):
    """Add the dagger to unreliable row ids written as `ID` and fail on unknown ids."""
    unknown = []

    def rep(m):
        rid = m.group(1)
        if rid not in by:
            unknown.append(rid)
            return m.group(0)
        d = DAG if by[rid]["headline_include"] != "yes" else ""
        return f"`{rid}`{d}"

    out = re.sub(r"`([A-Za-z][A-Za-z0-9-]*-\d{2,3})`" + f"(?:{DAG})?", rep, text)
    if unknown:
        raise SystemExit("unknown row ids in prose: " + ", ".join(sorted(set(unknown))))
    return out


def cited_ids(text):
    return sorted(set(re.findall(r"`([A-Za-z][A-Za-z0-9-]*-\d{2,3})`", text)))


def describe(cond):
    if not isinstance(cond, dict) or not cond:
        return "always"
    (op, arg), = cond.items()
    if op == "always":
        return "always"
    if op == "eq":
        return f"{arg[0]} = {arg[1]}"
    if op == "in":
        return f"{arg[0]} in {{{', '.join(arg[1])}}}"
    if op == "tri":
        return f"{arg[0]} in {{{', '.join(arg[1])}}}"
    if op in ("contains",):
        return f"{arg[0]} includes {arg[1]}"
    if op == "any_contains":
        return f"{arg[0]} includes any of {{{', '.join(arg[1])}}}"
    return json.dumps(cond)


def build_values(rows, by, stats, tsens, uae_log, uae_src):
    T_all = [r for r in rows if r["row_type"] == "test"]
    T = [r for r in T_all if r["headline_include"] == "yes"]
    E = [r for r in T_all if r["headline_include"] != "yes"]
    v = {}
    n = len(T)
    bc = collections.Counter(r["binding_status"] for r in T)
    ba = collections.Counter(r["binding_status"] for r in T_all)
    mc, vg, am = bc["mandatory"] + bc["conditional"], bc["voluntary"] + bc["guidance"], bc["ambiguous"]
    v.update(n_rows=len(rows), n_phase1=391, n_new=len(rows) - 391, n_test_all=len(T_all), n_test_head=n, n_test_excl=len(E),
             n_enabler=sum(r["row_type"] == "enabler" for r in rows), n_context=sum(r["row_type"] == "context" for r in rows),
             n_rowtype_test=len(T_all),
             head_mc=mc, head_vg=vg, head_am=am, head_mc_pct=pct(mc, n), head_vg_pct=pct(vg, n), head_am_pct=pct(am, n),
             head_m=bc["mandatory"], head_c=bc["conditional"], head_v=bc["voluntary"], head_g=bc["guidance"],
             all_mc=ba["mandatory"] + ba["conditional"], all_vg=ba["voluntary"] + ba["guidance"], all_am=ba["ambiguous"],
             all_mc_pct=pct(ba["mandatory"] + ba["conditional"], len(T_all)),
             all_vg_pct=pct(ba["voluntary"] + ba["guidance"], len(T_all)),
             all_am_pct=pct(ba["ambiguous"], len(T_all)))
    # status census
    vs = collections.Counter(r["verification_status"] for r in rows)
    v["n_unreliable_rows"] = sum(1 for r in rows if r["headline_include"] != "yes")
    v["n_blocked"], v["n_unverifiable_other"] = vs["UNVERIFIED_BLOCKED"], vs["UNVERIFIABLE_OTHER"]
    v["canada_rows"] = sum(1 for r in rows if r["family"] == "Canada")
    v["canada_unrel"] = sum(1 for r in rows if r["family"] == "Canada" and r["headline_include"] != "yes")
    v["n_not_read"] = vs["UNVERIFIED_SOURCE_NOT_READ"]
    v["n_not_rechecked"] = vs["NOT_RECHECKED"]
    v["n_verified_any"] = vs["VERIFIED"] + vs["VERIFIED_CORRECTED"] + vs["VERIFIED_NOTE_ONLY"]
    v["n_withdrawn"] = vs["ERROR_WITHDRAWN"]

    # evidence base
    lines = []
    for f in FAMS:
        rs = [r for r in rows if r["family"] == f]
        if not rs:
            continue
        g = collections.Counter(r["evidence_grade"] for r in rs)
        un = sum(1 for r in rs if r["headline_include"] != "yes")
        lines.append([FAM_LABEL[f], len(rs), sum(1 for r in T if r["family"] == f), g["primary text read"], g["catalogue-level only"],
                      g["read via unofficial/machine translation"], un])
    tot = collections.Counter(r["evidence_grade"] for r in rows)
    lines.append(["**Total**", f"**{len(rows)}**", f"**{n}**", f"**{tot['primary text read']}**", f"**{tot['catalogue-level only']}**",
                  f"**{tot['read via unofficial/machine translation']}**", f"**{v['n_unreliable_rows']}**"])
    v["evidence_base"] = md_table(["Family", "Rows", "Headline test rows", "Primary text read", "Catalogue only",
                                   "Unofficial or machine translation", "Unverified or unverifiable"], lines)

    # by family
    lines = []
    for f in FAMS:
        c = collections.Counter(SYM[r["binding_status"]] for r in T if r["family"] == f)
        k = sum(c.values())
        ex = sum(1 for r in E if r["family"] == f)
        if not k and not ex:
            continue
        lines.append([FAM_LABEL[f], k, c["M"], c["C"], c["V"], c["G"], c["A"], f"{c['M'] + c['C']} of {k}", ex])
    c = collections.Counter(SYM[r["binding_status"]] for r in T)
    lines.append(["**All**", f"**{n}**", f"**{c['M']}**", f"**{c['C']}**", f"**{c['V']}**", f"**{c['G']}**", f"**{c['A']}**",
                  f"**{c['M'] + c['C']} of {n}**", f"**{len(E)}**"])
    v["by_family"] = md_table(["Family", "Headline test rows", "M", "C", "V", "G", "A", "Binding where triggered (M+C)",
                               "Test rows excluded as unverified"], lines)
    # binding by family sentence (computed)
    fam_mc = [(f, sum(1 for r in T if r["family"] == f and r["binding_status"] in ("mandatory", "conditional"))) for f in FAMS]
    fam_mc = sorted([(f, k) for f, k in fam_mc if k], key=lambda x: -x[1])
    v["binding_by_family"] = ", ".join(f"{FAM_LABEL[f]} ({k})" for f, k in fam_mc)
    exm = collections.Counter(r["family"] for r in E if r["binding_status"] in ("mandatory", "conditional"))
    v["excluded_binding_by_family"] = ", ".join(f"{FAM_LABEL[f]} ({k})" for f, k in exm.most_common())

    # by type
    lines = []
    for t in TYPES:
        rs = [r for r in T if r["primary_test_type"] == t]
        c = collections.Counter(SYM[r["binding_status"]] for r in rs)
        fm = sorted(set(r["family"] for r in rs if r["binding_status"] in ("mandatory", "conditional")))
        lines.append([t, TYPE_NAME[t], len(rs), c["M"], c["C"], c["V"], c["G"], c["A"], ", ".join(fm) if fm else "none"])
    v["by_type"] = md_table(["Code", "Test type", "Headline test rows", "M", "C", "V", "G", "A", "Families with M or C rows"], lines)
    for t in ("RED", "OVER", "CSAFE", "REAL"):
        rs = [r for r in T if r["primary_test_type"] == t]
        v[f"n_{t}"] = len(rs)
        v[f"n_{t}_binding"] = sum(1 for r in rs if r["binding_status"] in ("mandatory", "conditional"))
        b_ids = [r["row_id"] for r in rs if r["binding_status"] in ("mandatory", "conditional")]
        v[f"{t}_binding_ids"] = ", ".join(f"`{i}`" for i in b_ids) if b_ids else "none"
        ex = [r["row_id"] for r in E if r["primary_test_type"] == t and r["binding_status"] in ("mandatory", "conditional")]
        v[f"{t}_excluded_binding_ids"] = ", ".join(f"`{i}`" for i in ex) if ex else "none"
        v[f"n_{t}_all"] = sum(1 for r in T_all if r["primary_test_type"] == t)
        v[f"{t}_ids"] = ", ".join(f"`{r['row_id']}` ({r['binding_status']})" for r in rs) if rs else "none"
    # matrix
    hdr = ["Family"] + TYPES
    mx = []
    for f in FAMS:
        if not any(r["family"] == f for r in T):
            continue
        cells = []
        for t in TYPES:
            cell = [r for r in T if r["family"] == f and r["primary_test_type"] == t]
            if not cell:
                cells.append(".")
                continue
            un = [SYM[r["binding_status"]] for r in cell if r["binding_status"] != "ambiguous"]
            a = sum(1 for r in cell if r["binding_status"] == "ambiguous")
            s = (max(un, key=lambda x: RK[x]) if un else "A") + str(len(cell))
            if un and a:
                s += f"+a{a}"
            cells.append(s)
        mx.append([f] + cells)
    v["matrix"] = md_table(hdr, mx)
    v["_matrix_rows"], v["_matrix_hdr"] = mx, hdr
    empty_cols = [t for t in TYPES if not any(r["primary_test_type"] == t for r in T)]
    v["empty_type_columns"] = ", ".join(empty_cols) if empty_cols else "none"

    # verification
    ver = stats["verification"]

    def vrow(name, d):
        return [name, d["n_checked_rows"] if "n_checked_rows" in d else d["n"], d["PASS"], d["MINOR"], d["ERROR"],
                d["UNVERIFIED_BLOCKED"], d["UNVERIFIABLE_OTHER"], d["verifiable"],
                f"{d['error_rate_pct']}% ({d['error_ci95_pct'][0]} to {d['error_ci95_pct'][1]})"]
    vh = ["Sample", "Rows checked", "PASS", "MINOR", "ERROR", "Blocked", "Unverifiable", "Verifiable", "Error rate (Wilson 95%)"]
    vr = [vrow("Rows cited in report prose, brief and checklist (phase 1 citations)", ver["cited_rows"]),
          vrow("Fresh seeded random sample (seed 20261012)", ver["fresh_random_sample"]),
          vrow("Targeted rows", ver["targeted_other"]),
          vrow("New UAE rows added in phase 2", ver["new_uae_rows"]),
          vrow("**All rows checked in phase 2**", ver["all_checked_this_round"]),
          vrow("All rows checked, excluding new UAE rows", ver["all_checked_excluding_new_rows"]),
          vrow("Phase 1 provisional rows (re verified)", ver["phase1_provisional_rows"])]
    v["verification_table"] = md_table(vh, vr)
    # phase 3
    v3 = stats["verification_p3"]
    v["p3_verification_table"] = md_table(vh, [
        vrow("Phase 3 re-check of 175 open rows, as graded by research agents", v3["recheck_as_graded_by_agents"]),
        vrow("Same rows, re-graded by the lead analyst against the rubric", v3["recheck_by_research_agents"]),
        vrow("**Fresh random sample (seed 20261016), independent verifiers**", v3["fresh_random_seed_20261016"]),
        vrow("New phase 3 rows, independent verifiers", v3["new_rows_phase3"]),
        vrow("**All rows checked by phase 3 independent verifiers**", v3["final_independent_all"])])
    for key, d in [("p3r", v3["recheck_by_research_agents"]), ("p3a", v3["recheck_as_graded_by_agents"]),
                   ("p3f", v3["fresh_random_seed_20261016"]), ("p3n", v3["new_rows_phase3"]), ("p3x", v3["final_independent_all"])]:
        v.update({f"{key}_n": d["n"], f"{key}_pass": d["PASS"], f"{key}_minor": d["MINOR"], f"{key}_err": d["ERROR"],
                  f"{key}_blocked": d["UNVERIFIED_BLOCKED"], f"{key}_unverif": d["UNVERIFIABLE_OTHER"],
                  f"{key}_verifiable": d["verifiable"], f"{key}_rate": d["error_rate_pct"],
                  f"{key}_lo": d["error_ci95_pct"][0], f"{key}_hi": d["error_ci95_pct"][1], f"{key}_fault": d["any_fault_rate_pct"]})
    v["p3_regraded"] = v3["n_regraded_minor_to_error"]
    v["n_local_pdf"] = sum(1 for r in rows if r["access_path"].startswith("standard_fetch_saved_pdf"))
    # normative force of non-binding test rows (two independent coders), headline rows only
    nf_path = DATA / "coding" / "normative_force.csv"
    if nf_path.exists():
        nf = {r["row_id"]: r["agreed"] for r in read_csv(nf_path)}
        ns = json.loads((DATA / "coding" / "normative_force_stats.json").read_text(encoding="utf-8"))
        H = [r for r in T if r["binding_status"] in ("voluntary", "guidance", "ambiguous")]
        coded = [r for r in H if r["row_id"] in nf]
        cc = collections.Counter(nf[r["row_id"]] for r in coded)
        v.update(nf_n=len(coded), nf_uncoded=len(H) - len(coded), nf_obl=cc["OBLIGATION_WORDING"], nf_rec=cc["RECOMMENDS"],
                 nf_des=cc["DESCRIBES"], nf_dis=cc["DISPUTED"], nf_kappa=ns["cohens_kappa"], nf_agree=round(100 * ns["observed_agreement"], 1),
                 nf_total_coded=ns["n"])
        v["nf_summary"] = (f"Of {len(coded)} such headline rows, {cc['RECOMMENDS']} recommend a test, {cc['DESCRIBES']} only describe "
                           f"testing practice, {cc['OBLIGATION_WORDING']} use obligation wording in a document that is not binding or whose "
                           f"force is unclear, and {cc['DISPUTED']} were disputed between the coders (agreement {v['nf_agree']}%, "
                           f"Cohen's kappa {ns['cohens_kappa']}).")
        lines = []
        for fam in FAMS:
            fr = [r for r in coded if r["family"] == fam]
            if fr:
                c2 = collections.Counter(nf[r["row_id"]] for r in fr)
                mc2 = sum(1 for r in T if r["family"] == fam and r["binding_status"] in ("mandatory", "conditional"))
                lines.append([FAM_LABEL.get(fam, fam), mc2, c2["OBLIGATION_WORDING"], c2["RECOMMENDS"], c2["DESCRIBES"], c2["DISPUTED"]])
        v["nf_table"] = md_table(["Family", "Required (mandatory or conditional)", "Obligation wording, not binding",
                                  "Recommended", "Described only", "Disputed"], lines)
        v["nf_obligation_ids"] = ", ".join(f"`{r['row_id']}`" for r in coded if nf[r["row_id"]] == "OBLIGATION_WORDING") or "none"
        v["nf_disputed_ids"] = ", ".join(f"`{r['row_id']}`" for r in coded if nf[r["row_id"]] == "DISPUTED") or "none"
    v["n_superseded"] = vs["SUPERSEDED"]
    v["n_new_p3"] = sum(1 for r in rows if r["sample_type"] == "new_row_phase3")
    v["n_new_unchecked"] = vs["NEW_UNCHECKED"]
    a = ver["all_checked_this_round"]
    v.update(ver_all_n=a["n_checked_rows"], ver_all_verifiable=a["verifiable"], ver_all_err=a["ERROR"], ver_all_rate=a["error_rate_pct"],
             ver_all_lo=a["error_ci95_pct"][0], ver_all_hi=a["error_ci95_pct"][1], ver_all_fault=a["any_fault_rate_pct"],
             ver_all_blocked=a["UNVERIFIED_BLOCKED"], ver_all_unverif=a["UNVERIFIABLE_OTHER"], ver_all_pass=a["PASS"], ver_all_minor=a["MINOR"])
    c = ver["cited_rows"]
    v.update(cited_n=c["n"], cited_err=c["ERROR"], cited_rate=c["error_rate_pct"], cited_verifiable=c["verifiable"],
             cited_lo=c["error_ci95_pct"][0], cited_hi=c["error_ci95_pct"][1],
             cited_blocked=c["UNVERIFIED_BLOCKED"], cited_unverif=c["UNVERIFIABLE_OTHER"], cited_pass=c["PASS"], cited_minor=c["MINOR"])
    f = ver["fresh_random_sample"]
    v.update(fresh_n=f["n"], fresh_err=f["ERROR"], fresh_rate=f["error_rate_pct"], fresh_verifiable=f["verifiable"],
             fresh_lo=f["error_ci95_pct"][0], fresh_hi=f["error_ci95_pct"][1], fresh_blocked=f["UNVERIFIED_BLOCKED"],
             fresh_unverif=f["UNVERIFIABLE_OTHER"], fresh_pass=f["PASS"], fresh_minor=f["MINOR"])
    nw = ver["new_uae_rows"]
    v.update(new_n=nw["n"], new_err=nw["ERROR"], new_rate=nw["error_rate_pct"], new_lo=nw["error_ci95_pct"][0], new_hi=nw["error_ci95_pct"][1])
    pv = ver["phase1_provisional_rows"]
    v.update(prov_n=pv["n"], prov_err=pv["ERROR"], prov_rate=pv["error_rate_pct"], prov_blocked=pv["UNVERIFIED_BLOCKED"],
             prov_unverif=pv["UNVERIFIABLE_OTHER"], prov_verifiable=pv["verifiable"], prov_pass=pv["PASS"], prov_minor=pv["MINOR"])

    # provisional rows table (ids by final status)
    ids = pv["ids_by_final_status"]
    lines = []
    for st in ("VERIFIED", "VERIFIED_CORRECTED", "UNVERIFIABLE_OTHER", "UNVERIFIED_BLOCKED"):
        xs = ids.get(st, [])
        if xs:
            lines.append([st, len(xs), ", ".join(f"`{i}`" for i in xs)])
    for st, xs in ids.items():
        if st not in ("VERIFIED", "VERIFIED_CORRECTED", "UNVERIFIABLE_OTHER", "UNVERIFIED_BLOCKED") and xs:
            lines.append([st, len(xs), ", ".join(f"`{i}`" for i in xs)])
    v["provisional_table"] = md_table(["Final status", "Rows", "Row identifiers"], lines)

    # named earlier unverifiable rows
    named = ["Canada-002", "Canada-009", "Canada-014", "EU-AI-Act-034", "EU-AI-Act-044", "EU-AI-Act-068", "Saudi-008", "Singapore-014", "UK-009"]
    lines = []
    for i in named:
        r = by[i]
        lines.append([f"`{i}`", r["verification_status"], r["block_type"] or "none", "yes" if r["headline_include"] == "yes" else "no",
                      (r["document_to_download"] or r["verification_note"])[:140]])
    v["named_rows_table"] = md_table(["Row", "Final status", "Block type", "In headline counts", "What resolves it"], lines)
    v["named_resolved"] = ", ".join(f"`{i}`" for i in named if by[i]["verification_status"] in ("VERIFIED", "VERIFIED_CORRECTED", "VERIFIED_NOTE_ONLY"))
    v["named_open"] = ", ".join(f"`{i}`" for i in named if by[i]["headline_include"] != "yes")

    # unverified by family + block type
    bt = collections.Counter(r["block_type"] or "none" for r in rows if r["headline_include"] != "yes")
    v["block_types_text"] = ", ".join(f"{k}: {x}" for k, x in bt.most_common())
    lines = []
    for fam in FAMS:
        rs = [r for r in rows if r["family"] == fam and r["headline_include"] != "yes"]
        if rs:
            c = collections.Counter(r["verification_status"] for r in rs)
            other = len(rs) - c["UNVERIFIED_BLOCKED"] - c["UNVERIFIABLE_OTHER"] - c["UNVERIFIED_SOURCE_NOT_READ"] - c["ERROR_WITHDRAWN"]
            lines.append([FAM_LABEL.get(fam, fam), len(rs), c["UNVERIFIED_BLOCKED"], c["UNVERIFIABLE_OTHER"],
                          c["UNVERIFIED_SOURCE_NOT_READ"] + c["ERROR_WITHDRAWN"], other])
    v["unverified_by_family"] = md_table(["Family", "Rows", "Blocked", "Readable but passage not located", "Source not read or withdrawn",
                                          "Other (superseded, portal or secondary only, awaiting check)"], lines)
    # sensitivity
    sens = collections.Counter(r["binding_status"] for r in T_all)
    v["sensitivity_text"] = (f"If the {len(E)} excluded test rows were counted, the split would be {sens['mandatory'] + sens['conditional']} "
                             f"mandatory or conditional ({v['all_mc_pct']}), {sens['voluntary'] + sens['guidance']} voluntary or guidance "
                             f"({v['all_vg_pct']}) and {sens['ambiguous']} ambiguous ({v['all_am_pct']}) of {len(T_all)}.")

    # phase 1 comparison figures kept as reported then
    v.update(p1_tests=234, p1_mc=73, p1_vg=142, p1_am=19, p1_rows=391, p1_test_all=237, p1_sample=40, p1_verifiable=32, p1_err=1,
             p1_rate="3.1%", p1_lo=0.6, p1_hi=15.7)

    # UAE logs
    zones = ["UAE federal", "Abu Dhabi", "Dubai"]
    lines = []
    for z in zones:
        lg = [r for r in uae_log if r["zone"] == z]
        sr = [r for r in uae_src if r["zone"] == z]
        oc = collections.Counter(r["outcome"] for r in lg)
        lang = collections.Counter(r["language"][:2] for r in lg)
        rc = collections.Counter(r["reading_class"] for r in sr)
        ms = sum(1 for r in sr if r["machine_summary_of_arabic"] == "yes")
        lines.append([z, len(lg), f"{lang['en']} / {lang['ar']}", oc["found"], oc["not_found"], oc["blocked"], oc["partial_locator_only"],
                      len(sr), rc["english_original"], rc["arabic_original"], ms, rc["not_read"]])
    v["uae_search_table"] = md_table(["Zone", "Searches and fetches logged", "English / Arabic queries", "Found", "Not found", "Blocked",
                                      "Locator only", "Sources listed", "English read", "Arabic wording obtained", "of which English rendering by fetch tool",
                                      "Not read"], lines)
    v["n_uae_logs"], v["n_uae_sources"] = len(uae_log), len(uae_src)
    v["n_uae_ar_queries"] = sum(1 for r in uae_log if r["language"].startswith("ar"))
    v["n_uae_not_found"] = sum(1 for r in uae_log if r["outcome"] == "not_found")
    v["n_uae_arabic_read"] = sum(1 for r in uae_src if r["reading_class"] == "arabic_original")
    v["n_uae_machine"] = sum(1 for r in uae_src if r["machine_summary_of_arabic"] == "yes")

    # time sensitive
    st = collections.Counter(r["status"] for r in tsens)
    v["time_status_text"] = ", ".join(f"{k}: {x}" for k, x in sorted(st.items()))
    lines = []
    for r in tsens:
        if r["item"].startswith("UAE-"):
            continue
        lines.append([r["topic"], r["item"], r["status"], r["retrieved_on"]])
    v["time_table"] = md_table(["Topic", "Item", "Status", "Retrieved on"], lines)
    # staleness
    ages = [r["next_review_by"] for r in rows if r["next_review_by"]]
    v["earliest_review"] = min(ages) if ages else "n/a"
    return v


def checklist_section(rows, by):
    cl = json.loads((DATA / "checklist.json").read_text(encoding="utf-8"))
    lines, csv_rows = [], []
    phases = cl["phases"]
    cur = None
    for it in cl["items"]:
        if it["phase"] != cur:
            cur = it["phase"]
            pname = phases.get(cur, cur) if isinstance(phases, dict) else cur
            lines.append([f"**{cur}**", f"**{pname}**", "", "", ""])
        ids = it["rows"]
        rel = [i for i in ids if by[i]["headline_include"] == "yes"]
        strongest = max((by[i]["binding_status"] for i in rel), key=lambda s: RANK[s]) if rel else "none reliable"
        fam_best = {}
        for i in rel:
            b = by[i]["binding_status"]
            if b in ("mandatory", "conditional"):
                f = by[i]["family"]
                if f not in fam_best or RANK[b] > RANK[fam_best[f]]:
                    fam_best[f] = b
        binders = sorted(fam_best)
        st = ("binding in some cited sources: " + ", ".join(f"{f} ({SYM[fam_best[f]]})" for f in binders)) if binders \
            else f"not binding in the reliable cited rows ({strongest})"
        cites = ", ".join(f"`{i}`" + (DAG if by[i]["headline_include"] != "yes" else "") for i in ids)
        lines.append([it["id"], it["text"], describe(it["applies_when"]), cites, st])
        csv_rows.append({"item": it["id"], "phase": it["phase"], "check": it["text"], "applies_when": describe(it["applies_when"]),
                         "rows": ";".join(ids), "unreliable_rows_excluded_from_trace": ";".join(i for i in ids if i not in rel),
                         "strongest_status_reliable_rows": strongest, "binding_families": ";".join(binders)})
    table = md_table(["#", "Check", "Applies when (proposal)", "Motivating rows", "Binding trace"], lines)
    return table, csv_rows, len(cl["items"])


def write_summary_csvs(rows, v):
    DOCS.mkdir(exist_ok=True)
    with open(DOCS / "coverage_matrix.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(v["_matrix_hdr"])
        w.writerows(v["_matrix_rows"])
    T = [r for r in rows if r["row_type"] == "test" and r["headline_include"] == "yes"]
    with open(DOCS / "summary_by_family.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["family", "test_rows_headline", "mandatory", "conditional", "voluntary", "guidance", "ambiguous"])
        for fam in FAMS:
            c = collections.Counter(r["binding_status"] for r in T if r["family"] == fam)
            if sum(c.values()):
                w.writerow([fam, sum(c.values()), c["mandatory"], c["conditional"], c["voluntary"], c["guidance"], c["ambiguous"]])
    with open(DOCS / "summary_by_test_type.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["test_type", "test_rows_headline", "mandatory", "conditional", "voluntary", "guidance", "ambiguous"])
        for t in TYPES:
            c = collections.Counter(r["binding_status"] for r in T if r["primary_test_type"] == t)
            w.writerow([t, sum(c.values()), c["mandatory"], c["conditional"], c["voluntary"], c["guidance"], c["ambiguous"]])


def render(template_name, values, by):
    text = (SRC / template_name).read_text(encoding="utf-8")

    def rep(m):
        k = m.group(1).strip()
        if k not in values:
            raise SystemExit(f"{template_name}: placeholder {{{{{k}}}}} has no value")
        return str(values[k])

    out = re.sub(r"\{\{([^}]+)\}\}", rep, text)
    return dagger_pass(out, by)


OUTPUTS = [("REPORT.tmpl.md", "docs/REPORT.md"), ("EXECUTIVE_BRIEF.tmpl.md", "docs/EXECUTIVE_BRIEF.md"),
           ("READING_LIST.tmpl.md", "docs/READING_LIST.md"), ("UAE_COVERAGE.tmpl.md", "docs/UAE_COVERAGE.md"),
           ("TIME_SENSITIVE.tmpl.md", "docs/TIME_SENSITIVE.md"), ("README.tmpl.md", "README.md")]


def render_all(write_support=True):
    """Return {relative output path: text}. When write_support is true also write the generated CSV tables."""
    rows, by = load()
    stats = json.loads((DATA / "stats.json").read_text(encoding="utf-8"))
    tsens = read_csv(DATA / "time_sensitive.csv")
    log = read_csv(DATA / "uae_search_log.csv")
    src = read_csv(DATA / "uae_sources.csv")
    v = build_values(rows, by, stats, tsens, log, src)
    table, csv_rows, n_items = checklist_section(rows, by)
    v["checklist"], v["n_checklist_items"] = table, n_items
    cited = set()
    for tn in ("REPORT.tmpl.md", "EXECUTIVE_BRIEF.tmpl.md"):
        cited |= set(cited_ids((SRC / tn).read_text(encoding="utf-8")))
    cited |= {i for r in csv_rows for i in r["rows"].split(";")}
    unk = sorted(i for i in cited if i not in by)
    if unk:
        raise SystemExit("cited ids missing from table: " + ", ".join(unk))
    cs = collections.Counter(by[i]["verification_status"] for i in cited)
    unrel = sum(1 for i in cited if by[i]["headline_include"] != "yes")
    v.update(cited_total=len(cited), cited_ok=sum(1 for i in cited if by[i]["headline_include"] == "yes" and by[i]["verification_status"] != "NOT_RECHECKED"), cited_unrel=unrel, cited_notre=cs["NOT_RECHECKED"])
    out = {}
    pub = {k: x for k, x in v.items() if not k.startswith("_")}
    allv = {**pub, **extra_values(rows, by, log, src, tsens)}
    for tmpl, dest in OUTPUTS:
        if (SRC / tmpl).exists():
            out[dest] = render(tmpl, allv, by)
    out["data/docs_values.json"] = json.dumps(pub, indent=1, ensure_ascii=False)
    out["data/cited_coverage.json"] = json.dumps({"cited": sorted(cited), "by_status": dict(sorted(cs.items()))}, indent=1)
    if write_support:
        DOCS.mkdir(exist_ok=True)
        with open(DOCS / "assurance_checklist.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
            w.writeheader()
            w.writerows(csv_rows)
        write_summary_csvs(rows, v)
    return out


def main():
    for rel, text in render_all().items():
        (ROOT / rel).write_text(text, encoding="utf-8")
        print("wrote", rel)


def madoun_values():
    from . import engine
    ans = json.loads((ROOT / "examples" / "madoun_answers.json").read_text(encoding="utf-8"))
    res = engine.run(ans)["summary"]
    return {"madoun_applies": res["APPLIES"], "madoun_not": res["DOES_NOT_APPLY"], "madoun_unknown": res["UNKNOWN"]}


def extra_values(rows, by, log, src, tsens):
    """Large tables used by the coverage and time sensitive documents."""
    ev = {}
    ev.update(madoun_values())
    ev["brief_time"] = "\n".join([
        "- **EU Omnibus (Regulation (EU) 2026/1744):** identity, 27 July 2026 entry into force and the 2 August 2027 sandbox date are confirmed. The Annex III date (2 December 2027) and Annex I date (2 August 2028) are confirmed at recital level only; the operative Article 113 text is still to be read.",
        "- **DoH Responsible AI Standard:** V1, October 2025, revision due October 2026. Whether it has been revised is open (listing pages unreadable).",
        "- **DIFC Regulation 10:** the Commissioner has published an accreditation and certification framework; amendments after Version No. 2 are unchecked.",
        "- **Saudi drafts:** none can be called final from the evidence retrieved; the NCA document is a draft and SDAIA 2025 documents were blocked."])
    lines = []
    for r in src:
        lines.append([r["zone"], r["title"][:90], r["issuer"][:50], r["language_read"][:70], r["reading_class"],
                      r["machine_summary_of_arabic"], "yes" if r["blocked"].startswith("yes") else "no", r["url"]])
    ev["uae_sources_table"] = md_table(["Zone", "Title", "Issuer", "Language read (as recorded)", "Class", "English rendering by fetch tool",
                                        "Blocked", "URL"], lines)
    lines = [[r["zone"], r["query"][:110], r["language"], r["tool"], r["outcome"]] for r in log if r["outcome"] in ("not_found", "blocked")]
    ev["uae_notfound_table"] = md_table(["Zone", "Query or target", "Language", "Tool", "Outcome"], lines)
    lines = [[r["topic"], r["item"], r["our_value"][:80], r["primary_value_seen"][:120], r["locator_seen"][:60], r["status"], r["retrieved_on"], r["access_path"][:60]]
            for r in tsens]
    ev["time_full_table"] = md_table(["Topic", "Item", "Our value", "Primary value seen", "Locator", "Status", "Retrieved on", "Access path"], lines)
    return ev


if __name__ == "__main__":
    main()
