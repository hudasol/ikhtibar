"""Baselines for the two codings that drive the headline findings.

Question answered: how well can the analyst's binding status code and primary test type code be predicted
from the text of the paraphrase, by methods that are much simpler than the analyst's reading of the document?
This is a construct validity check, not an accuracy claim. The labels are the analyst's own (AI assisted)
codes, so a high score shows that the coding is regular and predictable, not that it is right.

Population: headline test rows (row_type == test and headline_include == yes).
Methods, chosen by the analyst who had seen the table and committed with the code (the keyword lexicon was not written blind):
  majority      most frequent label in the training part
  framework     most frequent label among training rows of the same framework (document level prior)
  modal_rule    binding status only: wording rule (shall, must, required versus should, may, recommend)
  keyword_rule  test type only: keyword lexicon taken from the taxonomy definitions, first match wins
  tfidf_lr      TF-IDF (words, 1 to 2 grams) with logistic regression, C = 1
  tfidf_lr_fw   as tfidf_lr plus a one hot framework indicator
  embed_lr      frozen sentence embedding (all-MiniLM-L6-v2, 384 dimensions, no fine tuning) with logistic regression;
                the regularisation strength is chosen by three fold cross validation inside each training part
  embed_lr_fw   as embed_lr plus a one hot framework indicator
Embeddings are cached in data/baselines/embeddings_minilm_l6_v2.npy (keyed by a hash of the paraphrases) so that
the run does not need the embedding library once the cache exists.
Protocols: repeated stratified five fold cross validation (10 repeats), and leave one family out (the family
column), which removes every document of the family from training.
Run: python -m ikhtibar.baselines  (needs scikit-learn, see requirements-baselines.txt)
"""
import csv, json, re, hashlib, collections
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "baselines"
SEED = 20261028
N_REPEATS = 10
N_FOLDS = 5
N_BOOT = 2000

BINDING = ["mandatory", "conditional", "voluntary", "guidance", "ambiguous"]
TO3 = {"mandatory": "binding", "conditional": "binding", "voluntary": "non_binding",
       "guidance": "non_binding", "ambiguous": "ambiguous"}

STRONG = re.compile(r"\b(shall|must|is required|are required|required to|requires? that|obliged|obliges|"
                    r"obligation|mandatory|mandates?|has to|have to|prohibit\w*|may not|must not)\b", re.I)
WEAK = re.compile(r"\b(should|may|recommend\w*|encourag\w*|consider\w*|suggest\w*|advis\w*|expected|"
                  r"good practice|voluntar\w*|optional|can|could|aims? to|guidance)\b", re.I)

# Lexicon from the taxonomy definitions (Section 4 of the report). Order is the precedence. Not tuned on data.
LEXICON = [
    ("RED", r"red[ -]?team|dangerous capabilit|misuse|jailbreak|adversarial (testing|probing)|systemic risk"),
    ("CSAFE", r"refusal|harmful (output|content)|question bank|content safety|unsafe (output|content)"),
    ("FAIR", r"fair\w*|bias\w*|discriminat\w*|represent(ative|ativeness)|protected (group|characteristic)"),
    ("PRIV", r"privacy|data protection impact|personal data|re[- ]?identif\w*|leakage"),
    ("SEC", r"secur\w*|penetration|vulnerabilit\w*|cyber\w*|attack\w*|threat model"),
    ("ROB", r"robust\w*|resilien\w*|reliab\w*|fault|perturb\w*|fail[- ]?safe|repeat(ed)? runs?|edge cases?"),
    ("OVER", r"human oversight|human review|override|escalat\w*|human in the loop|human intervention"),
    ("TRANS", r"explainab\w*|transparen\w*|interpretab\w*|label(l)?ing|disclos\w*|reproducib\w*"),
    ("DATA", r"training data|data quality|dataset|data governance|provenance|corpus"),
    ("MON", r"monitor\w*|post[- ]?(market|deployment)|incident|re[- ]?assess\w*|re[- ]?test\w*"),
    ("REAL", r"pilot|sandbox|real[- ]world (test|condition)|live trial|field test"),
    ("CONF", r"conformity|certif\w*|third[- ]party|independent (review|audit|assessment)|audit\w*|notified body|filing"),
    ("GATE", r"threshold|acceptance criteri\w*|go or no[- ]go|release decision|approval|sign[- ]?off"),
    ("RISK", r"risk assessment|impact assessment|risk (tier|classification|management)|assess\w* (the )?risks?"),
]
LEX = [(c, re.compile(p, re.I)) for c, p in LEXICON]


def load_rows():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    rows = [r for r in rows if r["row_type"] == "test" and r["headline_include"] == "yes"]
    rows.sort(key=lambda r: r["row_id"])
    return rows


def input_hash(rows):
    h = hashlib.sha256()
    for r in rows:
        h.update("\x1f".join([r["row_id"], r["binding_status"], r["primary_test_type"], r["framework"],
                              r["family"], r["requirement_paraphrase"]]).encode("utf-8") + b"\x1e")
    return h.hexdigest()


def macro_f1(y, p, labels=None):
    labels = labels if labels is not None else sorted(set(y))
    f1s = []
    for c in labels:
        tp = sum(1 for a, b in zip(y, p) if a == c and b == c)
        fp = sum(1 for a, b in zip(y, p) if a != c and b == c)
        fn = sum(1 for a, b in zip(y, p) if a == c and b != c)
        f1s.append(0.0 if tp == 0 else 2 * tp / (2 * tp + fp + fn))
    return float(np.mean(f1s))


def accuracy(y, p):
    return float(np.mean([a == b for a, b in zip(y, p)]))


def cohen_kappa(y, p):
    n = len(y)
    po = accuracy(y, p)
    cy, cp = collections.Counter(y), collections.Counter(p)
    pe = sum(cy[k] * cp[k] for k in set(cy) | set(cp)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


# ---------------------------------------------------------------- methods
def majority(train_y):
    return collections.Counter(train_y).most_common(1)[0][0]


def method_majority(texts, fws, y, tr, te, task):
    m = majority([y[i] for i in tr])
    return [m for _ in te]


def method_framework(texts, fws, y, tr, te, task):
    by = collections.defaultdict(list)
    for i in tr:
        by[fws[i]].append(y[i])
    g = majority([y[i] for i in tr])
    return [majority(by[fws[i]]) if fws[i] in by else g for i in te]


def method_modal_rule(texts, fws, y, tr, te, task):
    """Binding status only. Wording decides binding versus non binding; ties inside a group take the most
    frequent training label of that group."""
    cnt = collections.Counter(y[i] for i in tr)
    bind = "mandatory" if cnt["mandatory"] >= cnt["conditional"] else "conditional"
    nonb = "guidance" if cnt["guidance"] >= cnt["voluntary"] else "voluntary"
    out = []
    for i in te:
        s, w = bool(STRONG.search(texts[i])), bool(WEAK.search(texts[i]))
        out.append("ambiguous" if (s and w) else bind if s else nonb)
    return out


def method_keyword_rule(texts, fws, y, tr, te, task):
    out = []
    for i in te:
        lab = "PERF"
        for c, rx in LEX:
            if rx.search(texts[i]):
                lab = c
                break
        out.append(lab)
    return out


def _tfidf_lr(texts, fws, y, tr, te, with_fw):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from scipy.sparse import hstack, csr_matrix
    vec = TfidfVectorizer(ngram_range=(1, 2), lowercase=True, sublinear_tf=True)
    xtr = vec.fit_transform([texts[i] for i in tr])
    xte = vec.transform([texts[i] for i in te])
    if with_fw:
        names = sorted(set(fws[i] for i in tr))
        ix = {n: k for k, n in enumerate(names)}

        def oh(idx):
            m = np.zeros((len(idx), len(names)))
            for r, i in enumerate(idx):
                if fws[i] in ix:
                    m[r, ix[fws[i]]] = 1.0
            return csr_matrix(m)
        xtr, xte = hstack([xtr, oh(tr)]).tocsr(), hstack([xte, oh(te)]).tocsr()
    ytr = [y[i] for i in tr]
    if len(set(ytr)) == 1:
        return [ytr[0]] * len(te)
    clf = LogisticRegression(C=1.0, max_iter=5000)
    clf.fit(xtr, ytr)
    return list(clf.predict(xte))


EMB = {"x": None}


def _embed_lr(texts, fws, y, tr, te, with_fw):
    from sklearn.linear_model import LogisticRegressionCV
    X = EMB["x"]
    xtr, xte = X[tr], X[te]
    if with_fw:
        names = sorted(set(fws[i] for i in tr))
        ix = {n: k for k, n in enumerate(names)}

        def oh(idx):
            m = np.zeros((len(idx), len(names)))
            for r, i in enumerate(idx):
                if fws[i] in ix:
                    m[r, ix[fws[i]]] = 1.0
            return m
        xtr, xte = np.hstack([xtr, oh(tr)]), np.hstack([xte, oh(te)])
    ytr = [y[i] for i in tr]
    if len(set(ytr)) == 1:
        return [ytr[0]] * len(te)
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        clf = LogisticRegressionCV(Cs=[0.1, 1.0, 10.0, 100.0], cv=3, max_iter=5000)
        clf.fit(xtr, ytr)
    return list(clf.predict(xte))


def method_embed_lr(texts, fws, y, tr, te, task):
    return _embed_lr(texts, fws, y, tr, te, False)


def method_embed_lr_fw(texts, fws, y, tr, te, task):
    return _embed_lr(texts, fws, y, tr, te, True)


def load_embeddings(texts):
    """Return the cached embedding matrix, or compute it with the embedding library and cache it."""
    key = hashlib.sha256("\x1e".join(texts).encode("utf-8")).hexdigest()
    cache = OUT / "embeddings_minilm_l6_v2.npy"
    meta = OUT / "embeddings_minilm_l6_v2.json"
    if cache.exists() and meta.exists() and json.loads(meta.read_text())["texts_sha256"] == key:
        return np.load(cache), key
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    x = model.encode(texts, batch_size=32, normalize_embeddings=True, show_progress_bar=False)
    OUT.mkdir(parents=True, exist_ok=True)
    np.save(cache, x.astype("float32"))
    meta.write_text(json.dumps({"model": "sentence-transformers/all-MiniLM-L6-v2", "texts_sha256": key,
                                "n": len(texts), "dim": int(x.shape[1])}, indent=1) + "\n")
    return x, key


def method_tfidf_lr(texts, fws, y, tr, te, task):
    return _tfidf_lr(texts, fws, y, tr, te, False)


def method_tfidf_lr_fw(texts, fws, y, tr, te, task):
    return _tfidf_lr(texts, fws, y, tr, te, True)


METHODS = {
    "binding": [("majority", method_majority), ("framework", method_framework),
                ("modal_rule", method_modal_rule), ("tfidf_lr", method_tfidf_lr),
                ("tfidf_lr_fw", method_tfidf_lr_fw), ("embed_lr", method_embed_lr),
                ("embed_lr_fw", method_embed_lr_fw)],
    "test_type": [("majority", method_majority), ("framework", method_framework),
                  ("keyword_rule", method_keyword_rule), ("tfidf_lr", method_tfidf_lr),
                  ("tfidf_lr_fw", method_tfidf_lr_fw), ("embed_lr", method_embed_lr),
                  ("embed_lr_fw", method_embed_lr_fw)],
}


# ---------------------------------------------------------------- protocols
def folds_stratified(y, seed):
    rng = np.random.RandomState(seed)
    order = rng.permutation(len(y))
    order = sorted(order, key=lambda i: y[i])  # stable: shuffled within label
    assign = {int(i): k % N_FOLDS for k, i in enumerate(order)}
    return [([i for i in range(len(y)) if assign[i] != f], [i for i in range(len(y)) if assign[i] == f])
            for f in range(N_FOLDS)]


def run_repeated_cv(method, texts, fws, y, task):
    preds = []
    for rep in range(N_REPEATS):
        p = [None] * len(y)
        for tr, te in folds_stratified(y, SEED + rep):
            for i, lab in zip(te, method(texts, fws, y, tr, te, task)):
                p[i] = lab
        preds.append(p)
    return preds  # list of prediction vectors, one per repeat


def folds_grouped(fws, seed):
    """Document grouped folds: all rows of a document stay together; documents are shuffled and
    placed greedily into the currently smallest fold, so rows of one document never straddle train and test."""
    rng = np.random.RandomState(seed)
    docs = sorted(set(fws))
    rng.shuffle(docs)
    size = {d: sum(1 for f in fws if f == d) for d in docs}
    docs.sort(key=lambda d: -size[d])  # stable after shuffle: ties stay shuffled
    load = [0] * N_FOLDS
    assign = {}
    for d in docs:
        k = int(np.argmin(load))
        assign[d] = k
        load[k] += size[d]
    return [([i for i in range(len(fws)) if assign[fws[i]] != f], [i for i in range(len(fws)) if assign[fws[i]] == f])
            for f in range(N_FOLDS)]


def run_grouped_cv(method, texts, fws, y, task):
    preds = []
    for rep in range(N_REPEATS):
        p = [None] * len(y)
        for tr, te in folds_grouped(fws, SEED + 100 + rep):
            for i, lab in zip(te, method(texts, fws, y, tr, te, task)):
                p[i] = lab
        preds.append(p)
    return preds


def run_lofo(method, texts, fws, y, fams, task):
    p = [None] * len(y)
    for fam in sorted(set(fams)):
        te = [i for i in range(len(y)) if fams[i] == fam]
        tr = [i for i in range(len(y)) if fams[i] != fam]
        for i, lab in zip(te, method(texts, fws, y, tr, te, task)):
            p[i] = lab
    return [p]


def summarise(y, pred_list, rng, fws=None):
    labels = sorted(set(y))
    accs = [accuracy(y, p) for p in pred_list]
    f1s = [macro_f1(y, p, labels) for p in pred_list]
    n = len(y)
    ba, bf = [], []
    for _ in range(N_BOOT):
        ix = rng.randint(0, n, n)
        yy = [y[i] for i in ix]
        ba.append(np.mean([accuracy(yy, [p[i] for i in ix]) for p in pred_list]))
        bf.append(np.mean([macro_f1(yy, [p[i] for i in ix], sorted(set(yy))) for p in pred_list]))
    q = lambda a: [round(100 * float(np.percentile(a, 2.5)), 1), round(100 * float(np.percentile(a, 97.5)), 1)]
    extra = {}
    if fws is not None:
        # cluster bootstrap: resample documents (frameworks) with replacement and keep all their rows
        docs = sorted(set(fws))
        by = {d: [i for i in range(n) if fws[i] == d] for d in docs}
        cb = []
        for _ in range(N_BOOT):
            pick = rng.randint(0, len(docs), len(docs))
            ix = [i for k in pick for i in by[docs[k]]]
            yy = [y[i] for i in ix]
            cb.append(np.mean([accuracy(yy, [p[i] for i in ix]) for p in pred_list]))
        extra["accuracy_ci95_doc"] = q(cb)
    return {**extra, "accuracy": round(100 * float(np.mean(accs)), 1), "accuracy_ci95": q(ba),
            "macro_f1": round(100 * float(np.mean(f1s)), 1), "macro_f1_ci95": q(bf),
            "kappa": round(float(np.mean([cohen_kappa(y, p) for p in pred_list])), 3)}


def per_class(y, p):
    out = {}
    for c in sorted(set(y)):
        tp = sum(1 for a, b in zip(y, p) if a == c and b == c)
        fp = sum(1 for a, b in zip(y, p) if a != c and b == c)
        fn = sum(1 for a, b in zip(y, p) if a == c and b != c)
        out[c] = {"n": tp + fn, "f1": round(100 * (0.0 if tp == 0 else 2 * tp / (2 * tp + fp + fn)), 1)}
    return out


def main():
    import sklearn
    rows = load_rows()
    texts = [r["requirement_paraphrase"] for r in rows]
    fws = [r["framework"] for r in rows]
    fams = [r["family"] for r in rows]
    EMB["x"], emb_key = load_embeddings(texts)
    result = {"meta": {"n_rows": len(rows), "seed": SEED, "repeats": N_REPEATS, "folds": N_FOLDS,
                       "bootstrap": N_BOOT, "sklearn": sklearn.__version__, "numpy": np.__version__,
                       "input_sha256": input_hash(rows), "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
                       "embedding_texts_sha256": emb_key, "n_families": len(set(fams)),
                       "n_frameworks": len(set(fws))}}
    y5 = [r["binding_status"] for r in rows]
    y3 = [TO3[v] for v in y5]
    ytt = [r["primary_test_type"] for r in rows]
    result["binding5"] = {"label_counts": dict(collections.Counter(y5)), "cv": {}, "gcv": {}, "lofo": {}}
    result["binding3"] = {"label_counts": dict(collections.Counter(y3)), "cv": {}, "gcv": {}, "lofo": {}}
    result["test_type"] = {"label_counts": dict(collections.Counter(ytt)), "cv": {}, "gcv": {}, "lofo": {}}
    confusion = {}
    for task, y, key in (("binding", y5, "binding5"), ("test_type", ytt, "test_type")):
        for mname, fn in METHODS[task]:
            rng = np.random.RandomState(SEED + 7)
            cv = run_repeated_cv(fn, texts, fws, y, task)
            lo = run_lofo(fn, texts, fws, y, fams, task)
            gc = run_grouped_cv(fn, texts, fws, y, task)
            result[key]["gcv"][mname] = summarise(y, gc, np.random.RandomState(SEED + 7), fws)
            result[key]["cv"][mname] = summarise(y, cv, rng, fws)
            result[key]["lofo"][mname] = summarise(y, lo, rng, fws)
            if task == "binding":
                m3 = lambda ps: [[TO3[a] for a in p] for p in ps]
                result["binding3"]["cv"][mname] = summarise(y3, m3(cv), np.random.RandomState(SEED + 7), fws)
                result["binding3"]["lofo"][mname] = summarise(y3, m3(lo), np.random.RandomState(SEED + 7), fws)
                result["binding3"]["gcv"][mname] = summarise(y3, m3(gc), np.random.RandomState(SEED + 7), fws)
            if mname == "tfidf_lr":
                result[key]["lofo_per_class_tfidf_lr"] = per_class(y, lo[0])
                cm = collections.Counter(zip(y, lo[0]))
                confusion[key] = {f"{a}|{b}": v for (a, b), v in sorted(cm.items())}
                if task == "binding":
                    result[key]["lofo_by_family_tfidf_lr"] = {
                        fam: {"n": sum(1 for f in fams if f == fam),
                              "accuracy": round(100 * float(np.mean(
                                  [a == b for a, b, f in zip(y, lo[0], fams) if f == fam])), 1)}
                        for fam in sorted(set(fams))}
    result["lofo_confusion_tfidf_lr"] = confusion
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, sort_keys=True)
        f.write("\n")
    for t in ("binding5", "binding3", "test_type"):
        print(t, "CV  ", {k: (v["accuracy"], v["macro_f1"]) for k, v in result[t]["cv"].items()})
        print(t, "GCV ", {k: (v["accuracy"], v["macro_f1"]) for k, v in result[t]["gcv"].items()})
        print(t, "LOFO", {k: (v["accuracy"], v["macro_f1"]) for k, v in result[t]["lofo"].items()})


if __name__ == "__main__":
    main()
