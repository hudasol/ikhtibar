# Registration for the phase 6 primary analyses (3 November 2026)

Status: written and committed before the confirmation half of the documents was analysed. The commit that contains this file, `src/ikhtibar/confirm6.py`, `data/phase6/split.json` and `data/phase6/results_design.json` is the freeze point.

## Why there is a new primary analysis
The version 4.0 paper led with the share of binding rows (27.9% of 290). That figure depends on how many rows each document contributes: one long statute supplies many binding rows. The extended table (355 headline test rows from 101 documents, 21 families) allows a question that rows alone cannot answer: is force decided clause by clause or document by document? The old row share becomes a pilot result. The version 4.0 results are preserved at commit fa3e410.

## Design and confirmation
- Unit of the split: the document (`framework` field). Seed 20261106 (`python -m ikhtibar.split6`).
- Documents that hold any row of the frozen version 4.0 headline are split at random into two halves within each family: design (36 documents, 155 rows) and confirmation_old (35 documents). Documents whose headline rows all come from phase 5 (30 documents, 65 rows) are new to every earlier analysis and go to confirmation. Confirmation therefore has 65 documents and 200 rows.
- Design work (choosing statistics and thresholds) used only the design half. Nothing was computed on the confirmation half before this file was committed.
- Disclosure: aggregate figures over the whole extended table (24.8% binding, the process only gap of 17.2 points, and similar) were computed and reported earlier in phase 5, so the marginal shares of the confirmation half were not unseen in aggregate. The registered statistics below (document purity, document level shares, adjusted gaps by half) had not been computed for either half before the design run.

## Registered statistics and decision rules (all with a document cluster bootstrap, seed 20261107, 4000 draws)
- C1 Documents are pure. Among documents with at least two headline rows, the share holding both a binding and a non binding row is at most 25% and its upper 95% Wilson bound is at most 40%.
- C2 Force clusters in documents. The average within document concordance of binding status (three groups: binding, non binding, ambiguous) exceeds the concordance expected by chance (computed from the overall group shares) by at least 20 percentage points at the lower bound of the 95% interval. Tuning note: the design half gave an excess of 47.8 points with lower bound 28.3, so the threshold of 30 first thought of was lowered to 20 before confirmation.
- C3 Most documents contain no binding test provision. The upper 95% Wilson bound of the share of documents with any binding headline test row is below 50%.
- C4 Binding is a minority when each document counts once. The upper bound of the document weighted mean binding share is below 50%. The row level share is reported (C4b) but is not decisive, because in the design half a single long statute moved the row share above that of the document weighted share.
- C5 Binding provisions more often say only that testing happens. Difference in the share of specificity level S1 between binding and non binding rows, within test type, for each of the two blind coders. The finding is "direction supported" if both differences are positive and "supported" only if both 95% intervals exclude zero. The design half gave 20.4 and 12.2 points with intervals that include zero.

## Labels
Confirmatory: C1 to C5 on the confirmation half. Exploratory: every other number, including the same statistics on the design half, the old and new documents separately, and all earlier analyses (the baselines, the robustness checks, the completeness and extraction recall results, the verification samples). Earlier analyses were designed on the version 4.0 sample and are described as such.

## What would change the headline
If C1 or C2 fail on confirmation, the paper does not claim that force is decided at the document level. If C3 and C4 fail, it does not claim a minority of documents is binding. If C5 shows direction only, it says so.
