"""Merge the per topic time sensitive CSVs into data/time_sensitive.csv.

DIFC first round rows are superseded by time_difc_round2.csv (official host read in round 2).
"""
import csv, os, sys

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
