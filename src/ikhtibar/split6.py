"""Seeded split of documents into a design half and a confirmation half (phase 6).

Documents (the `framework` field) that hold at least one row of the frozen version 4.0 headline are split at random
and stratified by family, half to design and half to confirmation. Documents whose headline rows all come from phase 5
are new to every earlier analysis and go to confirmation. Only the assignment is written here; no outcome is computed.
Run: python -m ikhtibar.split6
"""
import csv, json, random, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261106


def headline():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if r["row_type"] == "test" and r["headline_include"] == "yes"]


def main():
    rows = headline()
    docs = collections.defaultdict(list)
    for r in rows:
        docs[r["framework"]].append(r)
    rng = random.Random(SEED)
    split, by_family = {}, collections.defaultdict(list)
    for d in sorted(docs):
        rs = docs[d]
        if all(r["sample_type"] == "new_row_phase5" for r in rs):
            split[d] = "confirmation_new"
        else:
            by_family[rs[0]["family"]].append(d)
    toggle = 0
    for fam in sorted(by_family):
        ds = sorted(by_family[fam])
        rng.shuffle(ds)
        for i, d in enumerate(ds):
            # alternate, starting side alternates by family so odd families do not all favour one half
            split[d] = "design" if (i + toggle) % 2 == 0 else "confirmation_old"
        toggle += len(ds) % 2
    out = {"seed": SEED, "rule": "frozen documents split 50/50 within family; documents with only phase 5 rows go to confirmation",
           "n_documents": len(split), "assignment": split,
           "rows": {h: sum(len(docs[d]) for d in docs if split[d].startswith(h)) for h in ("design", "confirmation")}}
    (ROOT / "data" / "phase6" / "split.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(collections.Counter(split.values()), out["rows"])


if __name__ == "__main__":
    main()
