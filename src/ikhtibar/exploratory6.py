"""Exploratory follow up to the registered phase 6 analyses (not registered; written after the confirmation result).

C2 failed on confirmation because chance concordance is high when most rows are non binding, so the excess over chance
is bounded. This module reports a prevalence adjusted within document agreement: kappa = (observed - chance) / (1 - chance)
for pairs of rows from the same document, with a document cluster bootstrap (seed 20261108). Output data/phase6/exploratory.json.
"""
import json, itertools, collections
import numpy as np
from . import confirm6, split6

SEED, N = 20261108, 4000


def kap(docs, lab):
    multi = [d for d in docs if len(docs[d]) >= 2]
    obs = np.mean([np.mean([lab[a] == lab[b] for a, b in itertools.combinations(docs[d], 2)]) for d in multi])
    allr = [i for d in docs for i in docs[d]]
    ch = sum((sum(1 for i in allr if lab[i] == k) / len(allr)) ** 2 for k in ("binding", "non_binding", "ambiguous"))
    return (obs - ch) / (1 - ch)


def main():
    out = {"seed": SEED, "note": "exploratory; not registered", "subsets": {}}
    for s in ("design", "confirmation", "old", "new", "all"):
        rows = confirm6.pick(s)
        lab = [confirm6.G[r["binding_status"]] for r in rows]
        docs = collections.defaultdict(list)
        for i, r in enumerate(rows):
            docs[r["framework"]].append(i)
        names = list(docs)
        rng = np.random.RandomState(SEED)
        bs = []
        for _ in range(N):
            new, rl = {}, []
            for k, j in enumerate(rng.randint(0, len(names), len(names))):
                st = len(rl)
                for i in docs[names[j]]:
                    rl.append(lab[i])
                new[k] = list(range(st, len(rl)))
            bs.append(kap(new, rl))
        out["subsets"][s] = {"pair_kappa": round(float(kap(docs, lab)), 3),
                             "ci95": [round(float(np.nanpercentile(bs, 2.5)), 3), round(float(np.nanpercentile(bs, 97.5)), 3)]}
    # families with and without any binding documents (all)
    rows = confirm6.pick("all")
    fam = collections.defaultdict(lambda: collections.defaultdict(bool))
    for r in rows:
        fam[r["family"]][r["framework"]] |= confirm6.G[r["binding_status"]] == "binding"
    out["family_documents"] = {f: {"documents": len(d), "with_binding": sum(d.values())} for f, d in sorted(fam.items())}
    json.dump(out, open("data/phase6/exploratory.json", "w"), indent=1, sort_keys=True)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
