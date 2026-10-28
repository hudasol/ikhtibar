#!/usr/bin/env python3
"""Phase 5: merge the full text claim checks and the newly read works into the reference files.

Inputs:  data/paper/refs_candidates.csv (record of what each work says and how much of it was read),
         data/paper/lit/claimcheck_{1,2,3}.csv (full text claim checks), data/paper/lit/new_{1,2}.csv (new works).
Outputs: data/paper/refs_candidates.csv (read level updated, new works appended, a verdict column added),
         data/paper/refs_curated.csv (structured BibTeX fields used to build paper/refs.bib).
Only bibliographic facts seen on a page that was opened are entered; anything else is left blank.
Run: python scripts/p5_merge_refs.py
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "data" / "paper" / "lit"
CAND = ROOT / "data" / "paper" / "refs_candidates.csv"
CUR = ROOT / "data" / "paper" / "refs_curated.csv"

NEW_KEYS = """minkova2023lowresource oneill2017classifying brandsma2025regulatory sleimi2020semantic hassani2025foodsafety
arnold2024agora guldimann2024complai metr2025common stelling2025evaluating marino2025airegbench guliani2026dejure
ariai2024legalsurvey bradner1997key reuel2024betterbench bean2025measuring weidinger2025toward rauh2024gaps raji2022outsider
lewis2025mapping nist2025tevv gartlehner2025swar pangakis2023automated flemyng2025position gallifant2024tripodllm
gebru2021datasheets nosek2018preregistration vanmiltenburg2021preregistering hofman2023preregistration li2020stop
alzubaidi2025evaluating peppin2025multilingual stelling2025mapping silva2024decoding""".split()

RENAME = {"alkhalifa2024falqs": "hofverberg2024falqs", "naser_cite": "naser2026cite"}

# key: (entrytype, dict of structured fields). Missing keys are filled from the candidate row as @misc.
S = {
 "chun2024comparative": ("misc", {"howpublished": "arXiv preprint arXiv:2410.21279"}),
 "du2025toward": ("misc", {"howpublished": "Doctoral dissertation, Lyceum of the Philippines University, Manila. arXiv:2508.00868"}),
 "roberts2023comparative": ("techreport", {"institution": "International Centre of Expertise in Montreal on AI (CEIMIA)"}),
 "almaamari2025between": ("misc", {"howpublished": "arXiv preprint arXiv:2503.05773"}),
 "raji2020closing": ("inproceedings", {"booktitle": "Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT*)"}),
 "mokander2023auditing": ("article", {"journal": "AI and Ethics", "doi": "10.1007/s43681-023-00289-2"}),
 "casper2024blackbox": ("inproceedings", {"booktitle": "Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT)", "doi": "10.1145/3630106.3659037", "author": "Casper, Stephen and Ezell, Carson and Siegmann, Charlotte and Kolt, Noam and Curtis, Taylor Lynn and Bucknall, Benjamin and others"}),
 "ojewale2024towards": ("misc", {"howpublished": "arXiv preprint arXiv:2402.17861", "year": "2024"}),
 "liang2023holistic": ("article", {"journal": "Transactions on Machine Learning Research", "author": "Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and others"}),
 "shevlane2023model": ("misc", {"howpublished": "arXiv preprint arXiv:2305.15324", "author": "Shevlane, Toby and Farquhar, Sebastian and Garfinkel, Ben and Phuong, Mary and Whittlestone, Jess and Leung, Jade and others"}),
 "phuong2024evaluating": ("misc", {"howpublished": "arXiv preprint arXiv:2403.13793", "author": "Phuong, Mary and Aitchison, Matthew and Catt, Elliot and Cogan, Sarah and Kaskasoli, Alexandre and Krakovna, Victoria and others"}),
 "perez2022red": ("misc", {"howpublished": "arXiv preprint arXiv:2202.03286"}),
 "weidinger2023sociotechnical": ("misc", {"howpublished": "arXiv preprint arXiv:2310.11986", "author": "Weidinger, Laura and Rauh, Maribeth and Marchal, Nahema and Manzini, Arianna and Hendricks, Lisa Anne and Mateos-Garcia, Juan and others"}),
 "feffer2024red": ("inproceedings", {"booktitle": "Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society", "volume": "7", "number": "1", "pages": "421--437", "doi": "10.1609/aies.v7i1.31647"}),
 "mokander2021conformity": ("article", {"journal": "Minds and Machines", "doi": "10.1007/s11023-021-09577-4"}),
 "gornet2024european": ("article", {"journal": "Internet Policy Review", "volume": "13", "number": "3", "doi": "10.14763/2024.3.1784"}),
 "wachter2024limitations": ("article", {"journal": "Yale Journal of Law \\& Technology", "volume": "26", "number": "3", "year": "2024"}),
 "veale2021demystifying": ("article", {"journal": "Computer Law Review International", "number": "4", "year": "2021", "note": "From page 97. Preprint arXiv:2107.03721"}),
 "lee2023aiverify": ("misc", {"author": "{Lee Kok Thong}, Josh", "howpublished": "Future of Privacy Forum blog, 6 June 2023"}),
 "harjani2025singapore": ("article", {"journal": "Issues in Science and Technology", "volume": "41", "number": "4", "pages": "27--29"}),
 "tabassi2023airmf": ("techreport", {"institution": "National Institute of Standards and Technology", "number": "NIST AI 100-1", "doi": "10.6028/NIST.AI.100-1", "year": "2023"}),
 "albous2025gcc": ("article", {"journal": "Journal of Artificial Intelligence Research", "volume": "82", "pages": "2389--2422"}),
 "alkhalifa2024falqs": ("misc", {"author": "Hofverberg, Elin", "howpublished": "In Custodia Legis, Law Library of Congress blog, 17 December 2024"}),
 "albous2025kuwaituae": ("article", {"journal": "Politics \\& Policy", "doi": "10.1111/polp.70084"}),
 "reisman2018aia": ("techreport", {"title": "Algorithmic Impact Assessments: A Practical Framework for Public Agency Accountability", "institution": "AI Now Institute"}),
 "metcalf2021aias": ("inproceedings", {"booktitle": "Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT)", "pages": "735--746", "doi": "10.1145/3442188.3445935"}),
 "brand2025sai": ("article", {"journal": "JeDEM: eJournal of eDemocracy and Open Government", "volume": "17", "number": "3", "pages": "106--140", "doi": "10.29379/jedem.v17i3.1049", "title": "Development of effective methods and tools for the auditing AI algorithms by Supreme Audit Institutions"}),
 "rekenkamer2022audit9": ("techreport", {"author": "{Netherlands Court of Audit}", "institution": "Netherlands Court of Audit (Algemene Rekenkamer)", "year": "2022"}),
 "zilka2023police": ("inproceedings", {"booktitle": "Proceedings of the 3rd ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization (EAAMO)", "doi": "10.1145/3617694.3623246"}),
 "dsit2025assurance": ("misc", {"author": "{UK Department for Science, Innovation and Technology}", "howpublished": "Policy paper, GOV.UK, 3 September 2025", "year": "2025"}),
 "gilardi2023chatgpt": ("article", {"journal": "Proceedings of the National Academy of Sciences", "doi": "10.1073/pnas.2305016120"}),
 "tornberg2023chatgpt": ("misc", {"howpublished": "arXiv preprint arXiv:2304.06588"}),
 "reiss2023testing": ("misc", {"howpublished": "arXiv preprint arXiv:2304.11085"}),
 "savelka2023can": ("inproceedings", {"booktitle": "Proceedings of the Sixth Workshop on Automated Semantic Analysis of Information in Legal Text (ASAIL)", "note": "arXiv:2306.13906"}),
 "tan2024large": ("misc", {"howpublished": "arXiv preprint arXiv:2402.13446"}),
 "ziems2024can": ("article", {"journal": "Computational Linguistics", "volume": "50", "number": "1", "pages": "238--266", "doi": "10.1162/coli_a_00502"}),
 "mchugh2012interrater": ("article", {"journal": "Biochemia Medica", "volume": "22", "number": "3", "pages": "276--282", "doi": "10.11613/BM.2012.031"}),
 "krippendorff2011computing": ("misc", {"author": "Krippendorff, Klaus", "howpublished": "Departmental Papers (ASC), University of Pennsylvania, paper 43"}),
 "bujang2017guidelines": ("article", {"journal": "Epidemiology, Biostatistics and Public Health", "volume": "14", "number": "2", "pages": "e12267", "doi": "10.2427/12267", "title": "Guidelines of the minimum sample size requirements for Cohen's Kappa"}),
 "wongpakaran2013comparison": ("article", {"journal": "BMC Medical Research Methodology", "volume": "13", "pages": "61", "doi": "10.1186/1471-2288-13-61"}),
 "fabrication2023chatgpt": ("article", {"author": "Walters, William H. and Wilder, Esther Isabelle", "journal": "Scientific Reports", "volume": "13", "pages": "14045", "doi": "10.1038/s41598-023-41032-5", "year": "2023"}),
 "chelli2024hallucination": ("article", {"journal": "Journal of Medical Internet Research", "volume": "26", "pages": "e53164", "doi": "10.2196/53164"}),
 "athaluri2023exploring": ("article", {"journal": "Cureus", "volume": "15", "number": "4", "pages": "e37432", "doi": "10.7759/cureus.37432"}),
 "naser_cite": ("misc", {"author": "Naser, M. Z.", "howpublished": "arXiv preprint arXiv:2603.03299", "year": "2026", "title": "How LLMs Cite and Why It Matters: A Cross-Model Audit of Reference Fabrication in AI-Assisted Academic Writing and Methods to Detect Phantom Citations"}),
 "spoor1996use": ("article", {"journal": "BMJ", "volume": "313", "number": "7053", "pages": "342", "doi": "10.1136/bmj.313.7053.342"}),
 "kastner2009capture": ("article", {"author": "Kastner, M. and Straus, S. E. and McKibbon, K. A. and Goldsmith, C. H.", "journal": "Journal of Clinical Epidemiology", "volume": "62", "number": "2", "pages": "149--157", "doi": "10.1016/j.jclinepi.2008.06.001"}),
 "stelfox2013capture": ("article", {"author": "Stelfox, H. T. and Foster, G. and Niven, D. and Kirkpatrick, A. W. and Goldsmith, C. H.", "journal": "The American Journal of Surgery", "volume": "206", "number": "3", "pages": "439--440", "doi": "10.1016/j.amjsurg.2012.11.017"}),
 "motschall2009number": ("misc", {"howpublished": "Cochrane Colloquium Abstracts, Singapore (poster)"}),
 # newly read works
 "minkova2023lowresource": ("inproceedings", {"booktitle": "Proceedings of the Natural Legal Language Processing Workshop 2023", "pages": "149--158"}),
 "oneill2017classifying": ("inproceedings", {"booktitle": "Proceedings of the 16th International Conference on Artificial Intelligence and Law (ICAIL)"}),
 "brandsma2025regulatory": ("misc", {"howpublished": "arXiv preprint arXiv:2505.00479"}),
 "sleimi2020semantic": ("misc", {"howpublished": "arXiv preprint arXiv:2001.11245"}),
 "hassani2025foodsafety": ("misc", {"howpublished": "arXiv preprint arXiv:2501.14683"}),
 "arnold2024agora": ("inproceedings", {"booktitle": "Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society", "volume": "7", "pages": "39--48"}),
 "guldimann2024complai": ("misc", {"howpublished": "arXiv preprint arXiv:2410.07959"}),
 "metr2025common": ("misc", {"author": "{METR}", "howpublished": "Report, March 2025 update (grey literature)"}),
 "stelling2025evaluating": ("misc", {"howpublished": "arXiv preprint arXiv:2512.01166"}),
 "marino2025airegbench": ("misc", {"howpublished": "arXiv preprint arXiv:2510.01474"}),
 "guliani2026dejure": ("misc", {"howpublished": "arXiv preprint arXiv:2604.02276"}),
 "ariai2024legalsurvey": ("misc", {"howpublished": "arXiv preprint arXiv:2410.21306"}),
 "bradner1997key": ("misc", {"howpublished": "RFC 2119 (BCP 14), Internet Engineering Task Force"}),
 "reuel2024betterbench": ("misc", {"howpublished": "arXiv preprint arXiv:2411.12990"}),
 "bean2025measuring": ("misc", {"author": "Bean, Andrew M. and Mahdi, Adam and others", "howpublished": "arXiv preprint arXiv:2511.04703"}),
 "weidinger2025toward": ("misc", {"howpublished": "arXiv preprint arXiv:2503.05336"}),
 "rauh2024gaps": ("inproceedings", {"booktitle": "Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society", "volume": "7", "pages": "1200--1217"}),
 "raji2022outsider": ("inproceedings", {"booktitle": "Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (AIES)", "pages": "557"}),
 "lewis2025mapping": ("misc", {"howpublished": "arXiv preprint arXiv:2503.05787"}),
 "nist2025tevv": ("misc", {"author": "{National Institute of Standards and Technology}", "howpublished": "Outline of proposed zero draft for public comment (NIST AI Standards Zero Drafts project)"}),
 "gartlehner2025swar": ("misc", {"author": "Gartlehner, Gerald and others", "howpublished": "medRxiv preprint, doi:10.1101/2025.03.20.25324350"}),
 "pangakis2023automated": ("misc", {"howpublished": "arXiv preprint arXiv:2306.00176"}),
 "flemyng2025position": ("article", {"author": "Flemyng, Ella and Noel-Storr, Anna and others", "journal": "JBI Evidence Synthesis", "volume": "23", "number": "11", "pages": "2162--2166"}),
 "gallifant2024tripodllm": ("misc", {"author": "Gallifant, Jack and Afshar, Majid and Ameen, Saleem and others", "howpublished": "medRxiv preprint, doi:10.1101/2024.07.24.24310930"}),
 "gebru2021datasheets": ("misc", {"howpublished": "arXiv preprint arXiv:1803.09010"}),
 "nosek2018preregistration": ("misc", {"howpublished": "Proceedings of the National Academy of Sciences, doi:10.1073/pnas.1708274114"}),
 "vanmiltenburg2021preregistering": ("misc", {"howpublished": "arXiv preprint arXiv:2103.06944"}),
 "hofman2023preregistration": ("misc", {"howpublished": "arXiv preprint arXiv:2311.18807"}),
 "li2020stop": ("article", {"journal": "ACM Transactions on Information Systems", "volume": "38", "number": "4"}),
 "alzubaidi2025evaluating": ("misc", {"howpublished": "arXiv preprint arXiv:2510.13430"}),
 "peppin2025multilingual": ("misc", {"howpublished": "arXiv preprint arXiv:2505.21344"}),
 "stelling2025mapping": ("misc", {"howpublished": "arXiv preprint arXiv:2504.15181"}),
 "silva2024decoding": ("misc", {"howpublished": "Student abstract, Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, vol. 7"}),
}
FIELDS = ["key", "entrytype", "author", "title", "journal", "booktitle", "institution", "howpublished", "year", "volume",
          "number", "pages", "doi", "note", "url"]


def main():
    cand = list(csv.DictReader(open(CAND, encoding="utf-8")))
    by = {r["key"]: r for r in cand}
    cols = list(cand[0].keys())
    if "claimcheck_verdict" not in cols:
        cols += ["claimcheck_verdict"]
    checks = {}
    for n in (1, 2, 3):
        for r in csv.DictReader(open(LIT / f"claimcheck_{n}.csv", encoding="utf-8")):
            checks[r["key"]] = r
    for k, c in checks.items():
        k = RENAME.get(k, k) if RENAME.get(k, k) in by else k
        by[k]["read_level"] = {"full_text": "full_text", "abstract_only": "abstract_page", "landing_only": "landing_page_only"}.get(c["read_level"], by[k]["read_level"])
        by[k]["claimcheck_verdict"] = c["verdict"]
    added = {}
    for n in (1, 2):
        for r in csv.DictReader(open(LIT / f"new_{n}.csv", encoding="utf-8")):
            if r["key"] in NEW_KEYS and r["key"] not in by:
                r["claimcheck_verdict"] = "not applicable (new work)"
                added[r["key"]] = r
    for k in NEW_KEYS:
        assert k in added or k in by, k
    rows = [by[r["key"]] for r in cand] + [added[k] for k in NEW_KEYS if k in added]
    # apply renames
    for r in rows:
        if r["key"] in RENAME:
            r["key"] = RENAME[r["key"]]
    for r in rows:
        r.setdefault("claimcheck_verdict", "")
    with open(CAND, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})
    inv = {v: k for k, v in RENAME.items()}
    out = []
    for r in rows:
        key = r["key"]
        old = inv.get(key, key)
        et, f = S.get(old, ("misc", {}))
        auth = f.get("author", r["authors"])
        year = f.get("year", r["year"])
        row = {c: "" for c in FIELDS}
        row.update({"key": key, "entrytype": et, "author": auth, "title": f.get("title", r["title"]), "year": year, "url": r["url"]})
        row.update({k: v for k, v in f.items() if k in FIELDS and k not in ("author", "title", "year")})
        out.append(row)
    with open(CUR, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out)
    print(len(rows), "references;", len(added), "added")


if __name__ == "__main__":
    main()
