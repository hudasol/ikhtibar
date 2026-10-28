#!/usr/bin/env python3
"""Draw the paper figures from the committed result files. Output: paper/figures/*.png (and a manifest with input hashes).
Run: python scripts/make_figures.py
Palette checked with a colour vision deficiency validator: purple (binding), rose (non binding), teal (ambiguous).
"""
import csv, json, hashlib, collections
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper" / "figures"
BIND, NONB, AMB = "#8C4A9E", "#E0527F", "#1F9BB5"
INK, MUTED, GRID = "#2B2B2B", "#6B6B6B", "#E6E1E4"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.dpi": 100, "savefig.dpi": 300})
J = lambda rel: json.loads((ROOT / rel).read_text(encoding="utf-8"))
G3 = {"mandatory": "binding", "conditional": "binding", "voluntary": "non", "guidance": "non", "ambiguous": "amb"}


def rows():
    with open(ROOT / "data" / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fig_pipeline():
    r = rows()
    n_all, n_test = len(r), sum(1 for x in r if x["row_type"] == "test")
    n_head = sum(1 for x in r if x["row_type"] == "test" and x["headline_include"] == "yes")
    fw = len({x["framework"] for x in r})
    fam = len({x["family"] for x in r})
    vf, cp, ag = J("data/verification/phase4/stats_p4.json"), J("data/completeness/recall.json"), J("data/coding/phase4/agreement.json")
    fig, ax = plt.subplots(figsize=(7.2, 2.6))
    ax.axis("off")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)

    def box(x, y, w, h, text, fc):
        ax.add_patch(plt.Rectangle((x, y), w, h, fc=fc, ec=MUTED, lw=0.8))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7, color=INK)

    def arrow(x0, y0, x1, y1):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))
    box(1, 14, 15, 12, f"Documents\n{fw} frameworks\n{fam} families", "#F8E3EC")
    box(21, 14, 17, 12, f"Provisions\n{n_all} rows\n(paraphrase,\nlocator, source)", "#F8E3EC")
    box(43, 14, 16, 12, f"Test provisions\n{n_test} rows\nheadline: {n_head}", "#F8E3EC")
    arrow(16, 20, 21, 20)
    arrow(38, 20, 43, 20)
    ev = [("Baselines", "predictability of\nthe codes"), ("Second codings", "two blind coders,\n120 rows"),
          ("Robustness", "alternative\nassumptions"), ("Verification", f"fresh sample,\n{vf['sampled']} rows"),
          ("Completeness", "independent\nreference list")]
    for k, (t, d) in enumerate(ev):
        y = 34 - k * 7.4
        ax.add_patch(plt.Rectangle((66, y - 3.2), 33.5, 6.4, fc="#E3F3F7", ec=MUTED, lw=0.8))
        ax.text(67, y, f"{t}: {d.replace(chr(10), ' ')}", ha="left", va="center", fontsize=6.1, color=INK)
        arrow(59, 20, 66, y)
    ax.text(1, 33, "Evidence base", fontsize=8, color=MUTED, weight="bold")
    ax.text(66, 38.4, "Evaluation of the evidence base", fontsize=8, color=MUTED, weight="bold")
    save(fig, "fig1_pipeline.png")


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0, c - h), min(1, c + h)


def fig_family():
    r = [x for x in rows() if x["row_type"] == "test" and x["headline_include"] == "yes"]
    by = collections.defaultdict(collections.Counter)
    for x in r:
        by[x["family"]][G3[x["binding_status"]]] += 1
    fams = sorted(by, key=lambda f: (-(by[f]["binding"] / sum(by[f].values())), -sum(by[f].values())))
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    y = np.arange(len(fams))[::-1]
    left = np.zeros(len(fams))
    for key, col, lab in (("binding", BIND, "Binding (mandatory or conditional)"), ("non", NONB, "Voluntary or guidance"), ("amb", AMB, "Ambiguous")):
        share = np.array([100 * by[f][key] / sum(by[f].values()) for f in fams])
        ax.barh(y, share, left=left, color=col, height=0.72, label=lab, edgecolor="white", linewidth=1)
        left += share
    for yy, f in zip(y, fams):
        ax.text(101, yy, f"n = {sum(by[f].values())}", va="center", fontsize=7, color=MUTED)
    ax.set_yticks(y)
    ax.set_yticklabels(fams)
    ax.set_xlim(0, 112)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Share of headline test provisions (%)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=3, frameon=False, fontsize=7)
    save(fig, "fig2_family.png")


def fig_specificity():
    s = J("data/specificity.json")
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.6), sharey=True)
    cols = {"S1": "#F2D1DE", "S2": "#E58BAA", "S3": "#B04A86", "S4": "#5A2A6E"}
    names = {"S1": "S1 process only", "S2": "S2 property named", "S3": "S3 method or metric", "S4": "S4 criterion set"}
    for ax, c in zip(axes, ("A", "B")):
        cnt = s["by_coder"][c]["counts"]
        groups = [("binding", "Binding"), ("non_binding", "Voluntary or\nguidance"), ("ambiguous", "Ambiguous")]
        bottom = np.zeros(3)
        for lv in ("S1", "S2", "S3", "S4"):
            v = np.array([100 * cnt[g][lv] / cnt[g]["n"] for g, _ in groups])
            ax.bar(range(3), v, bottom=bottom, color=cols[lv], width=0.62, edgecolor="white", linewidth=1, label=names[lv])
            for i, (vv, bb) in enumerate(zip(v, bottom)):
                if vv >= 5:
                    ax.text(i, bb + vv / 2, f"{vv:.0f}", ha="center", va="center", fontsize=7, color="white" if lv in ("S3", "S4") else INK)
            bottom += v
        ax.set_xticks(range(3))
        ax.set_xticklabels([f"{l}\n(n = {cnt[g]['n']})" for g, l in groups])
        ax.set_title(f"Coder {c}", fontsize=8, color=INK, loc="left")
    axes[0].set_ylabel("Share of provisions (%)")
    h, l = axes[1].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=4, frameon=False, fontsize=7)
    save(fig, "fig3_specificity.png")


def fig_baselines():
    b = J("data/baselines/results.json")
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.9))
    labels = {"majority": "Majority", "framework": "Document prior", "modal_rule": "Wording rule", "keyword_rule": "Keyword rule",
              "tfidf_lr": "TF-IDF", "tfidf_lr_fw": "TF-IDF + document", "embed_lr": "Embedding", "embed_lr_fw": "Embedding + document"}
    for ax, key, title in ((axes[0], "binding5", "Binding status (5 classes)"), (axes[1], "test_type", "Primary test type (15 classes)")):
        ms = [m for m in labels if m in b[key]["cv"]]
        y = np.arange(len(ms))[::-1]
        for yy, m in zip(y, ms):
            cv, lo = b[key]["cv"][m], b[key]["lofo"][m]
            ax.plot(cv["accuracy_ci95_doc"], [yy + 0.13] * 2, color=BIND, lw=1.2, alpha=0.5)
            ax.plot(lo["accuracy_ci95_doc"], [yy - 0.13] * 2, color=NONB, lw=1.2, alpha=0.5)
            ax.plot(cv["accuracy"], yy + 0.13, "o", color=BIND, ms=4.5, label="Cross validation" if m == ms[0] else None)
            ax.plot(lo["accuracy"], yy - 0.13, "s", color=NONB, ms=4.5, label="Leave one family out" if m == ms[0] else None)
        ax.set_yticks(y)
        ax.set_yticklabels([labels[m] for m in ms], fontsize=7)
        ax.set_xlim(0, 100)
        ax.set_xlabel("Accuracy (%), bars: 95% interval over documents")
        ax.set_title(title, fontsize=8, loc="left", color=INK)
        ax.xaxis.grid(True, color=GRID)
        ax.set_axisbelow(True)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, frameon=False, fontsize=7)
    fig.tight_layout()
    save(fig, "fig4_baselines.png")


def fig_robust():
    rb = J("data/robustness.json")
    lo = rb["leave_one_family_out_range"]
    items = [("Headline rows as coded", rb["base"]["binding_pct"], None),
             ("Leave one family out (range)", None, (lo["min_binding_pct"], lo["max_binding_pct"])),
             ("Excluded rows added back as binding", rb["excluded_bounds"]["all_excluded_binding_pct"], None),
             ("Ambiguous rows counted as binding", rb["ambiguous_bounds"]["ambiguous_all_binding_pct"], None),
             ("Both of the above (most favourable)", rb["extreme_bounds"]["most_favourable_to_binding_pct"], None),
             ("Each document weighted equally", rb["framework_weighted"]["mean_framework_binding_pct"], None),
             ("Document bootstrap, 95% interval", None, tuple(rb["framework_bootstrap"]["binding_pct_ci95"]))]
    fig, ax = plt.subplots(figsize=(6.2, 2.7))
    y = np.arange(len(items))[::-1]
    for yy, (lab, pt, rng) in zip(y, items):
        if pt is not None:
            ax.plot(pt, yy, "o", color=BIND, ms=5.5)
            ax.text(pt + 1.2, yy + 0.05, f"{pt:.1f}", va="center", fontsize=7, color=INK)
        else:
            ax.plot(rng, [yy, yy], color=NONB, lw=3, solid_capstyle="round")
            ax.text(rng[1] + 1.2, yy, f"{rng[0]:.1f} to {rng[1]:.1f}", va="center", fontsize=7, color=INK)
    ax.axvline(50, color=MUTED, lw=0.8, ls=":")
    ax.text(50.8, y[0] + 0.45, "half", fontsize=7, color=MUTED)
    ax.set_yticks(y)
    ax.set_yticklabels([i[0] for i in items])
    ax.set_xlim(0, 62)
    ax.set_xlabel("Binding share of test provisions (%)")
    ax.xaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    save(fig, "fig5_robustness.png")


def fig_archetypes():
    a = J("data/evaluation/archetypes.json")
    fig, ax = plt.subplots(figsize=(5.2, 2.7))
    cols = [BIND, NONB, AMB, "#B8860B", "#4D4D4D", "#7A3B3B", "#2E7D32", "#C46FA8"]
    marks = ["o", "s", "^", "D", "v", "P", "X", "*"]
    for (aid, v), c, m in zip(sorted(a["archetypes"].items()), cols, marks):
        xs = [0] + [p["answered"] for p in v["curve"]]
        ys = [v["baseline_zero_answers"]["UNKNOWN"]] + [p["unknown"] for p in v["curve"]]
        ax.plot(xs, ys, marker=m, ms=3.5, lw=1.1, color=c, label=aid)
    ax.set_xlabel("Questions answered (fixed order)")
    ax.set_ylabel("Items still unknown (of 30)")
    ax.yaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    ax.legend(ncol=4, frameon=False, fontsize=7, loc="upper right")
    save(fig, "fig6_archetypes.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fig_pipeline(); fig_family(); fig_specificity(); fig_baselines(); fig_robust(); fig_archetypes()
    srcs = ["data/evidence_table.csv", "data/specificity.json", "data/baselines/results.json", "data/robustness.json",
            "data/evaluation/archetypes.json", "data/verification/phase4/stats_p4.json", "data/completeness/recall.json",
            "data/coding/phase4/agreement.json"]
    h = hashlib.sha256()
    for s in srcs:
        h.update((ROOT / s).read_bytes())
    (OUT / "manifest.json").write_text(json.dumps({"inputs": srcs, "inputs_sha256": h.hexdigest(),
                                                   "files": sorted(p.name for p in OUT.glob("*.png"))}, indent=1) + "\n")
    print("figures written")


if __name__ == "__main__":
    main()
