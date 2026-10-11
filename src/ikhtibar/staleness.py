"""Flag evidence rows that are older than a chosen age or past their next_review_by date.

Offline only: this reads data/evidence_table.csv and never fetches anything. Re checking a source is a manual step
using the normal fetch route, and a blocked site stays blocked (mark the row unverified and list the document).

Examples
  python -m ikhtibar.staleness --max-age-days 180
  python -m ikhtibar.staleness --as-of 2027-04-01 --family Saudi --csv stale.csv
"""
import argparse, csv, datetime as dt, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def age_basis(row):
    return row.get("last_checked_on") or row["retrieved_on"]

def find_stale(rows, as_of, max_age_days=None, family=None):
    out = []
    for r in rows:
        if family and not r["family"].startswith(family):
            continue
        base = dt.date.fromisoformat(age_basis(r))
        age = (as_of - base).days
        due = dt.date.fromisoformat(r["next_review_by"])
        reasons = []
        if max_age_days is not None and age > max_age_days:
            reasons.append(f"older than {max_age_days} days")
        if as_of > due:
            reasons.append("past next_review_by")
        if reasons:
            out.append({"row_id": r["row_id"], "family": r["family"], "age_days": age, "basis_date": base.isoformat(),
                        "next_review_by": r["next_review_by"], "verification_status": r["verification_status"], "reason": "; ".join(reasons)})
    return sorted(out, key=lambda x: (-x["age_days"], x["row_id"]))

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--table", default=str(ROOT / "data" / "evidence_table.csv"))
    p.add_argument("--max-age-days", type=int, default=None, help="flag rows whose last check is older than this")
    p.add_argument("--as-of", default=None, help="date to measure from (YYYY-MM-DD); default today")
    p.add_argument("--family", default=None, help="only families starting with this prefix")
    p.add_argument("--csv", default=None, help="write flagged rows to this CSV")
    ns = p.parse_args(argv)
    as_of = dt.date.fromisoformat(ns.as_of) if ns.as_of else dt.date.today()
    rows = list(csv.DictReader(open(ns.table, encoding="utf-8", newline="")))
    res = find_stale(rows, as_of, ns.max_age_days, ns.family)
    print(f"as of {as_of.isoformat()}: {len(res)} of {len(rows)} rows flagged")
    for x in res[:40]:
        print(f"  {x['row_id']:28s} age {x['age_days']:4d} d  review by {x['next_review_by']}  [{x['verification_status']}]  {x['reason']}")
    if len(res) > 40:
        print(f"  ... {len(res) - 40} more (use --csv)")
    if ns.csv:
        with open(ns.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(res[0].keys()) if res else ["row_id"]); w.writeheader(); w.writerows(res)
    return 0

if __name__ == "__main__":
    sys.exit(main())
