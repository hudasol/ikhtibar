"""Command line interface: python -m ikhtibar.cli --help"""
import argparse, json, sys
from . import engine

def build_parser():
    p = argparse.ArgumentParser(prog="ikhtibar", description="Return the applicable checklist items for a described AI system, with source traces. Research aid, not legal advice.")
    p.add_argument("--answers", help="JSON file of answers (keys as in --list-questions)")
    p.add_argument("--system-type"); p.add_argument("--audience"); p.add_argument("--data-types", help="comma separated")
    p.add_argument("--decision-impact"); p.add_argument("--hosting"); p.add_argument("--acquisition")
    p.add_argument("--entity-zone"); p.add_argument("--eu-market")
    p.add_argument("--format", choices=["text", "json", "markdown"], default="text")
    p.add_argument("--only", choices=["APPLIES", "DOES_NOT_APPLY", "UNKNOWN"], help="show only items in this state")
    p.add_argument("--list-questions", action="store_true")
    p.add_argument("--data-dir", help="directory with checklist.json, answers_schema.json, evidence_table.csv")
    return p

def collect_answers(ns):
    ans = {}
    if ns.answers:
        ans.update(json.load(open(ns.answers, encoding="utf-8")))
    for k in ["system_type", "audience", "data_types", "decision_impact", "hosting", "acquisition", "entity_zone", "eu_market"]:
        v = getattr(ns, k)
        if v is not None:
            ans[k] = v
    return ans

def render_text(res, only=None):
    L = [res["disclaimer"], "", "Answers used: " + json.dumps(res["answers_used"], ensure_ascii=False), "Summary: " + ", ".join(f"{k} {v}" for k, v in res["summary"].items()), ""]
    for it in res["items"]:
        if only and it["state"] != only:
            continue
        L.append(f"[{it['state']}] {it['id']}  {it['text']}")
        L.append(f"    reason: {it['why']}")
        if it["state"] == "UNKNOWN" and it["to_settle"]:
            L.append("    would settle it: answer " + ", ".join(it["to_settle"]))
        if it["templates"]:
            L.append("    test evidence templates (proposals): " + ", ".join(it["templates"]))
        for s in it["sources"]:
            flag = "" if s["verification_status"].startswith("VERIFIED") else f" [{s['verification_status']}]"
            L.append(f"    - {s['row_id']}{flag}: {s['source_binding_status']}; binds you: {s['binds_you']} ({s['binds_you_reason']})")
        L.append("")
    for n in res["notes"]:
        L.append("Note: " + n)
    return "\n".join(L)

def render_markdown(res, only=None):
    L = [f"> {res['disclaimer']}", "", f"Answers used: `{json.dumps(res['answers_used'], ensure_ascii=False)}`", "",
         "Summary: " + ", ".join(f"{k} {v}" for k, v in res["summary"].items()), "",
         "| Item | State | Needs answer | Sources (binds you) |", "|---|---|---|---|"]
    for it in res["items"]:
        if only and it["state"] != only:
            continue
        src = "; ".join(f"`{s['row_id']}` ({s['binds_you']})" for s in it["sources"])
        L.append(f"| {it['id']} {it['text']} | {it['state']} | {', '.join(it['to_settle']) or '-'} | {src} |")
    return "\n".join(L)

def main(argv=None):
    ns = build_parser().parse_args(argv)
    kw = {}
    if ns.data_dir:
        from pathlib import Path
        d = Path(ns.data_dir)
        kw = {"checklist": engine.load_checklist(d / "checklist.json"), "schema": engine.load_schema(d / "answers_schema.json"), "rows": engine.load_rows(d / "evidence_table.csv")}
    schema = kw.get("schema") or engine.load_schema()
    if ns.list_questions:
        for k, q in schema["questions"].items():
            print(f"{k}: {q['ask']}  ({q['type']})")
            for v, d in q["values"].items():
                print(f"    {v}: {d}")
        return 0
    try:
        res = engine.run(collect_answers(ns), **kw)
    except engine.AnswerError as e:
        print("error:", e, file=sys.stderr)
        return 2
    if ns.format == "json":
        print(json.dumps(res, indent=1, ensure_ascii=False))
    elif ns.format == "markdown":
        print(render_markdown(res, ns.only))
    else:
        print(render_text(res, ns.only))
    return 0

if __name__ == "__main__":
    sys.exit(main())
