# Handoff: what is done and what needs the author

State on 28 October 2026 (version 4.0). All tests, the content check and the secrets scan pass. Everything below that says "run" assumes `export PYTHONPATH=src`.

## Where things are

| Need | Path |
|---|---|
| Paper draft (LaTeX source, generated) | `paper/main.tmpl.tex` (edit this), `paper/main.tex` (generated); compile with `scripts/compile_paper.sh` |
| All evaluation numbers, with interpretation | `docs/EVALUATION.md` |
| Judgement calls | `docs/DECISIONS.md` |
| Limitations and plan, with status per item | `docs/GAP_ANALYSIS.md` |
| Data sheet | `docs/DATASHEET.md` |
| Rebuild every generated file | `python -m ikhtibar.build_all`, then `python scripts/build_paper.py` |
| Rerun an analysis | `python -m ikhtibar.baselines` (about three minutes), `evaluate_tool`, `robustness`, `coding_agreement`, `completeness`, `verify4` |

A test fails if a stored result file or the paper source is older than the table it describes, so after any change to the table run the analyses, the build, and the paper build before committing.

## Needs the author

1. **Label 100 rows by hand** (about one hour): fill `data/coding/phase4/human_gold_template.csv` (columns beginning YOUR_) and save it as `human_gold.csv` in the same folder. `python -m ikhtibar.coding_agreement` then adds agreement of every coder with a human. This is the single most valuable addition, because all current coders are language models.
2. **Download the blocked documents** listed in `docs/DOWNLOAD_LIST.md` (Canada Directive, ISO catalogue pages, SDAIA and NCA files, EU Official Journal pages) so the 32 unverified rows can be checked.
3. **Arrange a domain or legal reviewer** for the UAE rows and the gap analysis (Section 8 of the report). The paper must not be submitted as legal analysis without one.
4. **Apply licences.** Proposed: CC BY 4.0 for documents and data, MIT for code (`docs/LICENSING.md`). Add `LICENSE` files once chosen.
5. **Choose a venue and its template**, then port `paper/main.tmpl.tex`. Complete the affiliation, funding and acknowledgements in the author block (marked by a comment), and decide authorship.
6. **Check the reference metadata.** `data/paper/refs_candidates.csv` lists 61 works that were opened and read at abstract or landing page level, never in full text. Some authors, years and venues are blank where the page did not show them (see `data/paper/refs_notes.md`). Resolve these and read the works before submission.
7. **Decide about commit attribution.** Before your rule was applied, 21 commits carry an assistant co author trailer, and 25 commits (including most of those made on 28 October before the author name was corrected) show the assistant as the author name. They cannot be changed without rewriting published history, which your rules forbid, so they are left. Commits from this point use your name. Tell me if you want them handled another way.

## Still to do with web access (scheduled)

Retry the 47 unreadable rows of the fresh verification sample; widen the completeness reference list and read the six missed United States documents; recheck the status items still not re read (DoH Responsible AI revision, DIFC Regulation 10, EU, Saudi, Korea decree, Canada); add related work for the Gulf and for public sector assurance. After any of these, rerun the analyses and the builds as above.

## Claims the paper may make, and may not

May: binding test provisions are a minority in this evidence base under every assumption tested; the coding is regular and the document drives binding status; blind coders agree with each other; the tool never wrongly excluded an item in the preregistered scenarios; the measured error rate and coverage gap, with their intervals.

May not: that the table is complete or error free; that coder agreement is accuracy; that anything states what the UAE requires beyond what a retrieved source says; that the checklist is legally correct; that the unreadable verification rows were correct.
