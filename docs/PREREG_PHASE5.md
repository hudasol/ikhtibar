# Preregistration for phase 5 (3 November 2026)

Committed before any new row is extracted or any new document is read for phase 5. Predictions are made from the frozen version 4.0 data only (commit fa3e410, local tag `v4.0-paper-frozen`, remote branch `frozen/v4.0-paper`). Hits and misses will be reported in the paper and in `docs/MORNING_NOTE.md`, including misses.

## What will be added

New in scope documents found through a second, independent reference list (task 3b) and read in phase 5. New rows carry ids of the form `<family>-P5-<nn>`. The 19 United States candidate rows are verified and added as a separate group. The new documents are the out of sample set; all comparisons below are made on the new documents only, and again on the extended table next to the frozen numbers.

## Predictions

Headline unit: rows with row_type test that pass the same verification screen as the frozen headline.

1. **Binding share on new documents.** Frozen share 27.9% of 290 rows (81 binding); leave one family out range 20.8% to 31.9%; mean over documents 25.5%; document bootstrap interval 13.4% to 43.7% (`data/robustness.json`). Prediction for new documents pooled: a binding share between 15% and 40%. A new document that is a statute or regulation will have a higher share than guidance, so a second prediction is that new documents from sector regulators (for example medical devices, finance, aviation) have a higher share than new national frameworks or standards.
2. **Direction of the process only gap.** In the frozen data binding rows are more often process only (S1) than non binding rows by 17.2 percentage points for coder A (interval 5.3 to 27.2 over documents). Prediction: the difference is positive on the new documents, and its size lies between 5 and 30 points. Because the new set will be small, its interval is expected to include zero; the direction is the test.
3. **Document prior baseline.** On a new document of an already seen family the document prior has no row of that document in training, so it cannot look the document up. Prediction: it will fall to the majority class rate of the new rows (within 10 points of it) and will not beat the wording rule by more than 10 points. Under row level cross validation (a leak) it would do far better; that is not the test.
4. **Wording rule.** Prediction: accuracy on new rows for binding status in five classes between 45% and 65%, close to the frozen grouped value (55.6%), and not clearly above the majority class.
5. **Families not yet in the table.** For jurisdictions or instrument types with no row in the frozen table (for example Australia, India, Brazil, the Council of Europe convention, OECD and G7 instruments, United Nations documents) the prediction is that binding provisions are rarer than in the whole frozen sample: below 25% binding, with the Council of Europe Framework Convention as the likeliest source of binding text, and OECD, G7 and United Nations instruments almost entirely non binding.
6. **Completeness.** Prediction: recall of the frozen table against the new reference list is lower than the frozen estimate of 68.4% (19 confirmed items), because the new list targets gaps (sector rules, standards, other jurisdictions) that the frozen search did not cover. Expected range 30% to 65%. Misses are expected to be sector instruments and instruments in jurisdictions not covered, not main national frameworks.
7. **Extraction recall (task 2).** Prediction: extraction recall between 55% and 85% over sampled documents, and precision between 75% and 95%. Missed provisions are expected to be more often non binding and more often general statements than extracted rows, so that the frozen headline binding share is, if anything, slightly overstated.
8. **UAE Arabic check (task 4).** Prediction: binding status agrees between English and Arabic readings for at least 80% of the rows that can be re read in Arabic; differences are mostly ambiguous versus another class and not mandatory versus non binding.
9. **Verification error rate.** Prediction: the strict error rate on new rows lies between 4% and 15%, similar to the frozen random samples (6.4% and 13.0%).

## What counts as the finding failing to replicate

- Finding 1 (binding provisions are a minority) fails if the pooled share on at least 30 new test rows from at least 8 new documents is 50% or more, or if the share on the extended table exceeds 50% in the base scenario.
- Finding 2 (binding provisions are more often process only) fails if the difference on the new documents is zero or negative, or if on the extended table the document level interval for the type adjusted difference no longer excludes zero.
- Finding 3 (binding status is a property of the document, weakly predictable from wording) fails if a learned text model beats the majority class by more than 10 points under grouped cross validation on the extended table, or if the document prior beats the majority class on new documents.
- A prediction that falls outside its stated range is recorded as a miss, whatever the reason, and discussed afterwards without changing the prediction.

## Rules fixed in advance

All seeds are recorded in the result files. Every new coder, extractor and verifier run records its model identity (name and version when the agent can report it, otherwise the fact that it could not). Rows are not edited after seeing results except through the patch process in `data/patches.json`. Rows that cannot be read are reported separately and excluded from headline counts, as before. This is research analysis and not legal advice.
