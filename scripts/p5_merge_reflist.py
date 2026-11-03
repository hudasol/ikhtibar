#!/usr/bin/env python3
"""Task 3b: merge the six area reference lists (built blind to the table by separate agents) into one list.

Inputs (kept in data/completeness/p5/raw/): A.csv ... F.csv and the matching *.searches.csv logs.
Outputs: data/completeness/reference_list_p5.csv (global ids N001..., duplicate URLs or titles merged and
recorded in the column duplicate_of), data/completeness/p5/search_log.csv (every search and fetch).
Run: python scripts/p5_merge_reflist.py
"""
import csv, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "completeness" / "p5" / "raw"
OUT = ROOT / "data" / "completeness"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def key_url(u):
    u = (u or "").lower().split("#")[0].rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", u)


def main():
    rows, seen_url, seen_title = [], {}, {}
    n = 0
    for a in "ABCDEF":
        with open(RAW / f"{a}.csv", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                n += 1
                nid = f"N{n:03d}"
                dup = ""
                ku, kt = key_url(r["official_url"]), norm(r["title"])
                if ku and ku in seen_url:
                    dup = seen_url[ku]
                elif kt in seen_title:
                    dup = seen_title[kt]
                else:
                    if ku: seen_url[ku] = nid
                    seen_title[kt] = nid
                rows.append({"ref_id": nid, "area": a, "area_ref_id": r["ref_id"], "jurisdiction": r["jurisdiction"],
                             "issuer": r["issuer"], "title": r["title"], "year_or_date": r["year_or_date"],
                             "instrument_type": r["instrument_type"], "official_url": r["official_url"],
                             "has_testing_provision": r["has_testing_provision"],
                             "provision_locator_or_evidence": r["provision_locator_or_evidence"],
                             "access_status": r["access_status"], "discovered_via": r["discovered_via"],
                             "notes": r["notes"], "duplicate_of": dup})
    with open(OUT / "reference_list_p5.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
    logs = []
    for a in "ABCDEF":
        with open(RAW / f"{a}.csv.searches.csv", encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f)
            for r in rd:
                r["area"] = a; logs.append(r)
    cols = ["area"] + [c for c in logs[0].keys() if c != "area"]
    allcols = list(dict.fromkeys(cols + [c for r in logs for c in r.keys()]))
    with open(OUT / "p5" / "search_log.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=allcols, restval="", lineterminator="\n"); w.writeheader(); w.writerows(logs)
    uniq = [r for r in rows if not r["duplicate_of"]]
    print(len(rows), "listed;", len(uniq), "unique;", len(logs), "log rows")


if __name__ == "__main__":
    main()
