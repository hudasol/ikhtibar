"""UAE Arabic check (phase 5, task 4).

Question answered: for UAE test rows that were read in English, does the Arabic original or official Arabic
version support the same clause, the same binding status and the same actor?

  inputs  python -m ikhtibar.uae_arabic inputs   -> data/uae_arabic/inputs/<group>.csv (row fields a reader needs)
  readers fresh agents read the Arabic text on official hosts and fill data/uae_arabic/raw/<group>.csv
  stats   python -m ikhtibar.uae_arabic          -> data/uae_arabic/stats.json, data/uae_arabic/differences.csv

Reader columns: row_id, arabic_found (yes, partial, no), arabic_url, arabic_title, arabic_locator,
supports_clause (yes, partial, no, not_checked), binding_arabic (mandatory, conditional, voluntary, guidance,
ambiguous, not_checked), same_actor (yes, no, not_checked), difference_note, read_basis (full text, summary only).
"""
import csv, json, sys, collections
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data" / "uae_arabic"
SEED = 20261103
BIND = {"mandatory", "conditional"}
GROUPS = {"doh_other": ("UAE-AbuDhabi-DoH", "UAE-AbuDhabi-Other"), "difc_adgm": ("UAE-DIFC-ADGM",),
          "dubai": ("UAE-Dubai",), "federal": ("UAE-Federal",)}


def rows():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def candidates(table):
    out = []
    for r in table:
        if not r["family"].startswith("UAE-") or r["row_type"] != "test":
            continue
        if r["language_read"].strip().lower().startswith("original arabic") or r["language_read"].strip().lower().startswith("arabic"):
            continue
        out.append(r)
    return out


def write_inputs():
    D.mkdir(parents=True, exist_ok=True)
    (D / "inputs").mkdir(exist_ok=True)
    cand = candidates(rows())
    for g, fams in GROUPS.items():
        sel = [r for r in cand if r["family"] in fams]
        with open(D / "inputs" / f"{g}.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["row_id", "framework", "clause_or_page", "requirement_paraphrase", "binding_status", "source_url"])
            for r in sel:
                w.writerow([r["row_id"], r["framework"], r["clause_or_page"], r["requirement_paraphrase"], r["binding_status"], r["source_url"]])
        print(g, len(sel))


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(100 * max(0.0, c - h), 1), round(100 * min(1.0, c + h), 1)]


def stats():
    table = {r["row_id"]: r for r in rows()}
    res = []
    for g in GROUPS:
        p = D / "raw" / f"{g}.csv"
        if p.exists():
            with open(p, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f):
                    r["group"] = g
                    if r.get("read_basis", "") == "not read":
                        r["arabic_found"] = "not_checked"   # a reader that read nothing has not shown that no Arabic version exists
                    res.append(r)
    cand = [r for g in GROUPS for r in (csv.DictReader(open(D / 'inputs' / f'{g}.csv', encoding='utf-8')) if (D / 'inputs' / f'{g}.csv').exists() else [])]
    read = [r for r in res if r["arabic_found"] in ("yes", "partial") and r["binding_arabic"] not in ("", "not_checked")]
    same = [r for r in read if r["binding_arabic"] == table[r["row_id"]]["binding_status"]]
    diff = [r for r in read if r["binding_arabic"] != table[r["row_id"]]["binding_status"]]
    flips = [r for r in read if (r["binding_arabic"] in BIND) != (table[r["row_id"]]["binding_status"] in BIND)]
    kinds = collections.Counter(f'{table[r["row_id"]]["binding_status"]}->{r["binding_arabic"]}' for r in diff)
    out = {"meta": {"seed": SEED, "candidate_rows": len(cand), "rows_returned": len(res),
                    "arabic_found": sum(r["arabic_found"] in ("yes", "partial") for r in res),
                    "arabic_not_found": sum(r["arabic_found"] == "no" for r in res),
                    "not_checked": sum(r["arabic_found"] == "not_checked" for r in res),
                    "read_with_status": len(read)},
           "binding_status_same": {"k": len(same), "n": len(read), "pct": round(100 * len(same) / len(read), 1) if read else None,
                                   "wilson_ci95": wilson(len(same), len(read))},
           "binding_status_differs": {"k": len(diff), "n": len(read), "pct": round(100 * len(diff) / len(read), 1) if read else None,
                                      "wilson_ci95": wilson(len(diff), len(read))},
           "binding_vs_nonbinding_flip": {"k": len(flips), "n": len(read), "pct": round(100 * len(flips) / len(read), 1) if read else None,
                                          "wilson_ci95": wilson(len(flips), len(read))},
           "clause_supported": {"yes": sum(r["supports_clause"] == "yes" for r in read), "partial": sum(r["supports_clause"] == "partial" for r in read),
                                "no": sum(r["supports_clause"] == "no" for r in read)},
           "actor_same_no": sum(r["same_actor"] == "no" for r in read),
           "difference_kinds": dict(kinds),
           "summary_only_rows": sum(r.get("read_basis", "").startswith("summary") for r in read)}
    (D / "stats.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if diff or any(r["supports_clause"] in ("no", "partial") or r["same_actor"] == "no" for r in read):
        with open(D / "differences.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["row_id", "framework", "english_binding", "arabic_binding", "supports_clause", "same_actor", "arabic_url", "arabic_locator", "difference_note"])
            for r in read:
                tb = table[r["row_id"]]["binding_status"]
                if r["binding_arabic"] != tb or r["supports_clause"] in ("no", "partial") or r["same_actor"] == "no":
                    w.writerow([r["row_id"], table[r["row_id"]]["framework"][:80], tb, r["binding_arabic"], r["supports_clause"], r["same_actor"], r["arabic_url"], r["arabic_locator"], r["difference_note"]])
    print(json.dumps(out, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "inputs":
        write_inputs()
    else:
        stats()


if __name__ == "__main__":
    main()
