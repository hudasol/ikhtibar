"""Merge the per topic time sensitive CSVs into data/time_sensitive.csv.

DIFC first round rows are superseded by time_difc_round2.csv (official host read in round 2).
"""
import csv, glob, os, sys

D = os.path.join(os.path.dirname(__file__), "..", "..", "data")
OUT_COLS = ["topic", "item", "our_value", "primary_value_seen", "locator_seen", "source_url",
            "access_path", "status", "retrieved_on", "conflict_or_note"]
TOPICS = [("EU Omnibus", "time_eu.csv"), ("DoH Responsible AI Standard", "time_doh.csv"),
          ("DIFC Regulation 10", "time_difc_round2.csv"), ("Saudi drafts", "time_saudi.csv")]


def rows():
    out = []
    for topic, fn in TOPICS:
        with open(os.path.join(D, "time_sensitive", fn), newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                r = {k: (v or "").replace("\u2014", ",").replace("\u2013", "-") for k, v in r.items()}
                out.append({
                    "topic": topic, "item": r["item"], "our_value": r.get("our_value", ""),
                    "primary_value_seen": r.get("primary_value", ""),
                    "locator_seen": r.get("locator_seen", ""), "source_url": r.get("source_url", ""),
                    "access_path": r.get("access_path", ""), "status": r.get("status", ""),
                    "retrieved_on": r.get("retrieval_date", ""), "conflict_or_note": r.get("note", "")})
    # phase 3 status checks (16 October 2026), already in the output column layout
    groups = {"g1": "Canada, US, ISO (phase 3)", "g2a": "EU AI Act text (phase 3)", "g2b": "EU codes, guidelines, standards (phase 3)",
              "g4": "UK and Singapore (phase 3)", "g5": "Japan, Korea, China (phase 3)", "g6": "Saudi and Gulf (phase 3)",
              "g7": "UAE (phase 3)"}
    for fn in sorted(glob.glob(os.path.join(D, "verification", "phase3", "p3ts_*.csv"))):
        g = os.path.basename(fn)[5:].split("_")[0]
        with open(fn, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                x = {c: (r.get(c) or "").replace("—", ",").replace("–", "-") for c in OUT_COLS}
                x["item"] = f"{x['topic']}: {x['item']}" if x["topic"] else x["item"]
                x["topic"] = groups.get(g, g)
                out.append(x)
    return out


def main():
    rs = rows()
    path = os.path.join(D, "time_sensitive.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        w.writerows(rs)
    print("wrote", path, len(rs), "rows")


if __name__ == "__main__":
    main()
