"""Extraction recall and precision (phase 5, task 2).

Question answered: of the test provisions a careful independent reader finds in a source document, how many are
rows in the evidence table (recall), and of the table rows for those documents, how many does the independent
reader also find (precision)?

Steps (the subagent steps are outside this script and leave files):
  sample    python -m ikhtibar.extraction_recall sample   -> data/extraction_recall/sample.json (seeded, stratified)
  extract   fresh readers see only the source address and the inclusion definition, never the table
            -> data/extraction_recall/raw/<doc_id>.csv
  match     an agent matches each independent provision to table rows; a second agent re checks a seeded 30%
            -> data/extraction_recall/matches.csv, data/extraction_recall/rematch.csv
  stats     python -m ikhtibar.extraction_recall          -> data/extraction_recall/stats.json
"""
import csv, json, sys, collections
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data" / "extraction_recall"
SEED = 20261103
N_DOCS = 14
BIND = {"mandatory", "conditional"}
GROUP = {"China": "China", "EU-AI-Act": "EU", "EU-GPAI-CoP": "EU", "EU-Standards": "EU", "ISO-IEC": "ISO",
         "Japan": "Japan", "Korea": "Korea", "Saudi": "Saudi", "Singapore": "Singapore",
         "UAE-AbuDhabi-DoH": "UAE", "UAE-DIFC-ADGM": "UAE", "UAE-Dubai": "UAE", "UAE-Federal": "UAE",
         "UK": "UK", "US-NIST": "US", "US-OMB": "US"}


def load_table():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def eligible_documents(rows):
    """Documents with at least one headline test row, whose rows were read from primary text in English."""
    docs = collections.defaultdict(list)
    for r in rows:
        if r["row_type"] == "test" and r["headline_include"] == "yes":
            docs[(r["family"], r["source_url"])].append(r)
    out = []
    for (fam, url), rs in docs.items():
        if fam == "ISO-IEC" or not url.startswith("http"):
            continue
        if any(r["evidence_grade"] != "primary text read" for r in rs):
            continue
        if any(("Chinese" in r["language_read"] or "Korean original not read" in r["language_read"]) for r in rs):
            continue
        out.append({"family": fam, "group": GROUP[fam], "source_url": url, "framework": rs[0]["framework"],
                    "n_rows": len(rs), "binding_rows": sum(r["binding_status"] in BIND for r in rs),
                    "row_ids": sorted(r["row_id"] for r in rs)})
    out.sort(key=lambda d: (d["family"], d["source_url"]))
    return out


def length_class(n):
    return "short" if n <= 2 else ("medium" if n <= 6 else "long")


def draw_sample(rows):
    docs = eligible_documents(rows)
    for d in docs:
        d["length_class"] = length_class(d["n_rows"])
    rng = np.random.RandomState(SEED)
    groups = collections.defaultdict(list)
    for d in docs:
        groups[d["group"]].append(d)
    taken_len = collections.Counter()
    chosen = []
    order = sorted(groups)
    pools = {g: [groups[g][i] for i in rng.permutation(len(groups[g]))] for g in order}
    while len(chosen) < N_DOCS and any(pools.values()):
        for g in order:
            if len(chosen) >= N_DOCS or not pools[g]:
                continue
            # prefer the length class taken least so far, then the seeded order
            pools[g].sort(key=lambda d: taken_len[d["length_class"]])
            d = pools[g].pop(0)
            taken_len[d["length_class"]] += 1
            chosen.append(d)
    ids = {f"X{i+1:02d}": d for i, d in enumerate(chosen)}
    return {"seed": SEED, "n_eligible": len(docs), "n_drawn": len(chosen),
            "method": "round robin over family groups in sorted order; inside a group a seeded permutation, preferring the length class chosen least often so far; length class from number of table rows (short 1 to 2, medium 3 to 6, long 7 or more)",
            "documents": {k: {kk: vv for kk, vv in v.items()} for k, v in ids.items()}}


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(100 * max(0.0, c - h), 1), round(100 * min(1.0, c + h), 1)]


def doc_bootstrap(per_doc, key_num, key_den, n_boot=4000):
    rng = np.random.RandomState(SEED + 1)
    ids = sorted(per_doc)
    vals = []
    for _ in range(n_boot):
        pick = [ids[i] for i in rng.randint(0, len(ids), len(ids))]
        num = sum(per_doc[i][key_num] for i in pick)
        den = sum(per_doc[i][key_den] for i in pick)
        if den:
            vals.append(100 * num / den)
    return [round(float(np.percentile(vals, 2.5)), 1), round(float(np.percentile(vals, 97.5)), 1)]


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def stats():
    sample = json.load(open(D / "sample.json", encoding="utf-8"))
    docs = sample["documents"]
    cov = json.load(open(D / "coverage.json", encoding="utf-8"))
    raw = {}
    for did in docs:
        p = D / "raw" / f"{did}.csv"
        if p.exists():
            raw[did] = read_csv(p)
    matches = read_csv(D / "matches.csv")
    table = {r["row_id"]: r for r in load_table()}
    rematch = read_csv(D / "rematch.csv") if (D / "rematch.csv").exists() else []
    per_doc = {}
    missed, found_force = [], collections.Counter()
    for did, d in docs.items():
        if did not in raw:
            continue
        ind = raw[did]
        m = {r["indep_id"]: r for r in matches if r["doc_id"] == did}
        n_ind = len(ind)
        n_found = sum(1 for r in ind if m.get(r["indep_id"], {}).get("matched", "no") in ("yes", "partial"))
        matched_rows = {rid for r in m.values() for rid in r.get("table_row_ids", "").split(";") if rid.strip()}
        tbl_rows = [rid for rid in d["row_ids"]]
        n_tbl = len(tbl_rows)
        n_tbl_found = sum(1 for rid in tbl_rows if rid in matched_rows)
        per_doc[did] = {"coverage": cov.get(did, {}).get("read", "unknown"), "precision_basis": bool(cov.get(did, {}).get("precision_basis")), "family": d["family"], "group": d["group"], "length_class": d["length_class"],
                        "n_independent": n_ind, "n_independent_in_table": n_found,
                        "n_table_rows": n_tbl, "n_table_rows_found_independently": n_tbl_found}
        for r in ind:
            mm = m.get(r["indep_id"], {})
            if mm.get("matched", "no") == "no":
                missed.append({"doc_id": did, "family": d["family"], "source_url": d["source_url"], **r})
    tot = collections.Counter()
    for v in per_doc.values():
        for k in ("n_independent", "n_independent_in_table", "n_table_rows", "n_table_rows_found_independently"):
            tot[k] += v[k]
    ptot = collections.Counter()
    for v in per_doc.values():
        if v["precision_basis"]:
            for k in ("n_table_rows", "n_table_rows_found_independently"):
                ptot[k] += v[k]
    byfam = {}
    for g in sorted({v["group"] for v in per_doc.values()}):
        a = sum(v["n_independent_in_table"] for v in per_doc.values() if v["group"] == g)
        b = sum(v["n_independent"] for v in per_doc.values() if v["group"] == g)
        c = sum(v["n_table_rows_found_independently"] for v in per_doc.values() if v["group"] == g)
        e = sum(v["n_table_rows"] for v in per_doc.values() if v["group"] == g)
        byfam[g] = {"documents": sum(1 for v in per_doc.values() if v["group"] == g), "recall_n": b, "recall_hits": a,
                    "recall_pct": round(100 * a / b, 1) if b else None, "precision_n": e, "precision_hits": c,
                    "precision_pct": round(100 * c / e, 1) if e else None}
    # binding status of missed provisions versus matched provisions (as judged by the independent reader)
    def force(r):
        return r.get("independent_force", "").strip().lower()
    ind_all = [(did, r) for did, rs in raw.items() for r in rs]
    matched_force = [force(r) for did, r in ind_all if matches_status(matches, did, r["indep_id"])]
    missed_force = [force(r) for did, r in ind_all if not matches_status(matches, did, r["indep_id"])]
    def share(lst):
        return round(100 * sum(1 for x in lst if x == "binding") / len(lst), 1) if lst else None
    out = {"meta": {"seed": SEED, "documents_sampled": len(docs), "documents_with_raw": len(raw),
                    "n_eligible": sample["n_eligible"], "sampling_method": sample["method"],
                    "second_check": "agent re checked a seeded 30 percent of matches"},
           "per_document": per_doc,
           "recall": {"hits": tot["n_independent_in_table"], "n": tot["n_independent"],
                      "pct": round(100 * tot["n_independent_in_table"] / tot["n_independent"], 1) if tot["n_independent"] else None,
                      "wilson_row_ci95": wilson(tot["n_independent_in_table"], tot["n_independent"]),
                      "doc_bootstrap_ci95": doc_bootstrap(per_doc, "n_independent_in_table", "n_independent") if per_doc else None},
           "precision": {"basis": "only documents whose whole text the reader reached (coverage.json precision_basis)",
                         "documents": sum(1 for v in per_doc.values() if v["precision_basis"]),
                         "hits": ptot["n_table_rows_found_independently"], "n": ptot["n_table_rows"],
                         "pct": round(100 * ptot["n_table_rows_found_independently"] / ptot["n_table_rows"], 1) if ptot["n_table_rows"] else None,
                         "wilson_row_ci95": wilson(ptot["n_table_rows_found_independently"], ptot["n_table_rows"]),
                         "doc_bootstrap_ci95": doc_bootstrap({k: v for k, v in per_doc.items() if v["precision_basis"]}, "n_table_rows_found_independently", "n_table_rows") if sum(1 for v in per_doc.values() if v["precision_basis"]) > 1 else None},
           "by_group": byfam,
           "force_of_independent_provisions": {"matched_n": len(matched_force), "matched_binding_pct": share(matched_force),
                                               "missed_n": len(missed_force), "missed_binding_pct": share(missed_force)},
           "rematch_agreement": rematch_agreement(matches, rematch)}
    (D / "stats.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if missed:
        keys = sorted({k for r in missed for k in r})
        with open(D / "missed_candidates.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(missed)
    print(json.dumps({k: out[k] for k in ("recall", "precision", "force_of_independent_provisions", "rematch_agreement")}, indent=1))


def matches_status(matches, did, iid):
    for r in matches:
        if r["doc_id"] == did and r["indep_id"] == iid:
            return r["matched"] in ("yes", "partial")
    return False


def rematch_agreement(matches, rematch):
    if not rematch:
        return None
    base = {(r["doc_id"], r["indep_id"]): r["matched"] for r in matches}
    n = agree = 0
    for r in rematch:
        k = (r["doc_id"], r["indep_id"])
        if k in base:
            n += 1
            agree += (base[k] in ("yes", "partial")) == (r["matched"] in ("yes", "partial"))
    return {"n": n, "agree": agree, "agree_pct": round(100 * agree / n, 1) if n else None}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        s = draw_sample(load_table())
        D.mkdir(parents=True, exist_ok=True)
        (D / "sample.json").write_text(json.dumps(s, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        for k, d in s["documents"].items():
            print(k, d["family"], d["length_class"], d["n_rows"], d["source_url"][:90])
        return
    stats()


if __name__ == "__main__":
    main()
