# Data sheet for the Ikhtibar evidence table

Following the questions of the datasheets for datasets proposal, answered briefly. Research, not legal advice.

**Purpose.** To record what published documents say about testing AI systems before deployment, coded by binding force and test type, and to support a checklist tool and a gap analysis for UAE government deployment.

**Composition.** One row per provision (`data/evidence_table.csv`). Each row has a document and family label, a locator (clause or page), a short paraphrase, a binding status (mandatory, conditional, voluntary, guidance, ambiguous), a row type (test, enabler, context), a primary test type from a fifteen type taxonomy, the source address, the retrieval date, the language read, and a verification status with notes. Row counts and splits are in `docs/REPORT.md` and `data/stats.json`. The table contains no personal data. Quotations are short and attributed.

**Collection.** Documents were located and read with standard search and fetch tools. Only primary documents from governments, national institutes and standards bodies are rows. Documents that could not be read are listed (`docs/DOWNLOAD_LIST.md`) and their rows are excluded from headline counts. No workaround was used when a site refused a fetch.

**Coding.** Binding status, row type and test type were assigned by language model agents under written rules and then checked. Normative force of non binding rows was double coded. A blind recoding of 120 rows is in `data/coding/phase4/`. No human gold labels exist yet.

**Verification.** Each row has a verification status. Fresh random samples were checked by independent verifiers (phase 3 and phase 4). Error rates, intervals and unreadable fractions are in `docs/EVALUATION.md`.

**Known limitations.** Coverage is incomplete (pilot recall 68.4% on confirmed candidates); English language sources dominate; Arabic originals were read for part of the UAE sources; several documents were revised during the work; applicability rules in the checklist are proposals.

**Uses.** Appropriate: comparing the force and type of testing provisions across documents, finding gaps to investigate, designing a test plan. Not appropriate: stating what the law requires of a particular organisation, or ranking jurisdictions by the number of rows.

**Maintenance.** Rows carry retrieval dates and `python -m ikhtibar.staleness` lists rows older than a chosen age. Changes are made by commit, with corrections recorded in patch files with a reason.

**Licence.** All rights reserved (`LICENSE`). Contact the author before reuse (`docs/LICENSING.md`).
