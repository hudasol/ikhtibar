# Evaluation of the evidence base and the checklist tool

This file is generated from the committed result files in `data/` (see `src/ikhtibar/eval_values.py`). Every number below is read from a result file. Tests check that the main result files agree with the current table (by hash for the baselines, by recomputation for the engine results, robustness, completeness and verification counts), but not every figure in every file is recomputed. It is research, not legal advice.

## What is measured, and what is not

The project makes five kinds of claim, and each is checked by a different method.

| Claim | Check | Section |
|---|---|---|
| Binding status and test type codes are regular, not arbitrary | Simple baselines predict the codes from the text | 1 |
| The checklist tool decides applicability correctly and safely | 94 scenarios written before the tool was run, four naive baselines, and a simulation | 2 |
| The coding can be repeated by someone else | Two blind second codings of 120 rows | 3 |
| The headline finding (binding test provisions are a minority) does not depend on coding choices | Sensitivity and bootstrap analysis | 4 |
| Table rows say what the sources say | Fresh independent verification of a random sample of 120 rows (readable rows only) | 5 |
| The table covers the relevant documents | Pilot recall against an independently built reference list | 6 |

Throughout, the labels are the analyst's own codes (made with AI assistance and then checked), so a high agreement or a high baseline score shows that the coding is regular, not that it is correct. Correctness of the rows is addressed only by section 5.

## 1. Baselines for the two codings

Population: 290 headline test rows from 71 documents in 16 families. Protocols: 10 times repeated stratified five fold cross validation, and leave one family out, which removes every document of a family from training. Intervals are bootstrap 95% intervals over rows (2000 resamples, fixed seed). The models use scikit-learn 1.9.1. Methods were chosen by the analyst, who had seen the table, and were committed together with the code.

### Binding status, five classes (mandatory, conditional, voluntary, guidance, ambiguous)

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 45.5 (39.7 to 51.4) | 12.5 | 0.0 | 45.5 (40.0 to 51.4) | 12.5 |
| Document prior (most common label in the same document) | 84.3 (80.2 to 88.2) | 81.9 | 0.774 | 45.5 (40.0 to 51.4) | 12.5 |
| Wording rule (shall, must versus should, may) | 58.3 (52.8 to 64.1) | 31.2 | 0.344 | 58.3 (52.8 to 64.1) | 31.2 |
| TF-IDF with logistic regression | 50.9 (45.0 to 56.5) | 21.6 | 0.125 | 46.9 (41.0 to 52.8) | 15.3 |
| TF-IDF with logistic regression plus document indicator | 79.1 (74.4 to 83.1) | 74.8 | 0.686 | 45.5 (40.0 to 51.4) | 12.5 |
| Frozen sentence embedding with logistic regression | 61.7 (56.7 to 66.8) | 46.2 | 0.419 | 49.3 (43.4 to 55.2) | 28.6 |
| Frozen sentence embedding with logistic regression plus document indicator | 82.9 (79.1 to 86.5) | 79.5 | 0.751 | 47.9 (42.1 to 53.8) | 18.6 |

### Binding status, three classes (binding, non binding, ambiguous)

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 60.0 (54.1 to 65.5) | 25.0 | 0.0 | 60.0 (54.1 to 65.5) | 25.0 |
| Document prior (most common label in the same document) | 89.6 (86.2 to 92.8) | 87.0 | 0.805 | 60.0 (54.1 to 65.5) | 25.0 |
| Wording rule (shall, must versus should, may) | 76.9 (72.1 to 82.1) | 60.8 | 0.554 | 76.9 (72.1 to 82.1) | 60.8 |
| TF-IDF with logistic regression | 64.9 (59.2 to 70.0) | 36.2 | 0.164 | 61.4 (55.5 to 66.6) | 28.4 |
| TF-IDF with logistic regression plus document indicator | 84.7 (80.7 to 88.2) | 80.6 | 0.698 | 60.0 (54.1 to 65.5) | 25.0 |
| Frozen sentence embedding with logistic regression | 73.5 (69.0 to 78.0) | 59.0 | 0.484 | 62.1 (56.6 to 67.6) | 42.3 |
| Frozen sentence embedding with logistic regression plus document indicator | 88.0 (84.7 to 91.1) | 84.5 | 0.773 | 61.7 (56.2 to 67.2) | 31.2 |

### Primary test type, fifteen classes

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 20.0 (15.5 to 24.8) | 2.2 | 0.0 | 14.5 (10.7 to 18.6) | 1.8 |
| Document prior (most common label in the same document) | 27.8 (23.4 to 32.6) | 17.3 | 0.166 | 14.5 (10.7 to 18.6) | 1.8 |
| Keyword rule (taxonomy definitions) | 47.2 (41.4 to 53.1) | 43.9 | 0.414 | 47.2 (41.4 to 53.1) | 43.9 |
| TF-IDF with logistic regression | 29.9 (25.3 to 35.1) | 9.8 | 0.138 | 25.2 (20.3 to 30.3) | 7.0 |
| TF-IDF with logistic regression plus document indicator | 32.2 (27.3 to 37.2) | 15.4 | 0.195 | 22.8 (18.3 to 27.6) | 5.7 |
| Frozen sentence embedding with logistic regression | 61.2 (56.3 to 66.3) | 47.0 | 0.556 | 53.8 (48.3 to 59.7) | 38.5 |
| Frozen sentence embedding with logistic regression plus document indicator | 55.0 (50.2 to 60.3) | 44.4 | 0.486 | 51.4 (45.5 to 57.2) | 32.9 |

### Reading the results

- Binding status is largely a property of the document, in the sense that a document prior reaches 84.3% accuracy when other provisions of the same document were seen in training, against 45.5% for the majority class. This is close to tautological. When a whole family is held out, the document prior falls back to the majority rate (45.5%), because it has nothing to look up, and the wording rule is the better method.
- Learned wording models do little better than the majority class on binding status when families are held out (TF-IDF 46.9%, frozen sentence embedding 49.3%, against 45.5%), and the wording rule reaches 58.3%. Document level intervals overlap, so this ordering is suggestive. Wording carries some signal but much less than document identity.
- For test type, a frozen sentence embedding with logistic regression (61.2% under cross validation, 53.8% leaving a family out) beats a keyword rule built from the taxonomy definitions (47.2%), which beats TF-IDF (29.9%) and the majority class (20.0%). Test type is largely recoverable from the paraphrase text; the paraphrase was written by the analyst, so this shows regularity and not correctness.
- Limits of these baselines: intervals are bootstrap intervals over rows and ignore clustering by document, so they understate uncertainty. The keyword lexicon was written by an analyst who had seen the table. The text classified is the analyst's own paraphrase. The labels are the analyst's own codes.
- Any later classifier, or any language model coder, should be compared with the document prior, the wording rule and the embedding baseline, not with the majority class alone.

## 2. Evaluation of the checklist tool

The tool reads a set of answers about a system and returns, for each of 30 checklist items, APPLIES, DOES_NOT_APPLY or UNKNOWN. Missing answers never make a condition true or false.

Design. 94 scenarios were written from the checklist YAML alone by a separate author, with expected results from an independent oracle, and committed before the engine was run. 82 scenarios have a specified result, 12 are invalid inputs with no specified result, and each of ten stated assumptions (A1 to A10) marks the scenarios whose expectation depended on it. Five pairs of scenarios test monotonicity (adding an answer must not flip APPLIES to DOES_NOT_APPLY).

| Method | Item accuracy (%) | Scenarios matched exactly (%) | Wrongly excluded | Wrongly applied | Returned unknown |
|---|---|---|---|---|---|
| This engine (three valued) | 99.9 | 98.8 | 0 | 0 | 1062 |
| Two valued, missing answer counts as no | 56.8 | 4.9 | 1062 | 0 | 0 |
| Two valued, missing answer counts as yes | 57.0 | 4.9 | 45 | 1014 | 0 |
| Every item applies | 49.7 | 0.0 | 0 | 1238 | 0 |
| Answers ignored, unconditional items only | 83.0 | 17.1 | 0 | 0 | 1476 |

"Wrongly excluded" means the method said DOES_NOT_APPLY where the expected result was APPLIES or UNKNOWN. "Wrongly applied" means it said APPLIES where the expected result was DOES_NOT_APPLY or UNKNOWN.

Results.

- The engine agreed with the preregistered expectation on 2457 of 2460 item decisions (99.9%), and matched 81 of 82 scenarios exactly (98.8%). It never wrongly excluded or wrongly applied an item (0 and 0).
- The two valued baselines score about 57% because they cannot express unknown, and they are unsafe in opposite ways: the closed version drops items the user cannot yet rule out, and the open version applies items that do not apply. The oracle uses three valued logic, so two valued designs are penalised by construction. The fairer comparison is the design that ignores the answers and returns UNKNOWN for conditional items (83.0% with no errors); the engine beats it because it uses the answers. The engine returns UNKNOWN in 1062 item decisions and states which answer would settle each one. The final figure is after two defects found by these scenarios were fixed.
- The first run, before any change, matched 2454 of 2460 decisions (99.8%) and 80 of 82 scenarios, but wrongly excluded 3 items (an empty list given for a multiple choice question was treated as a known answer that matched nothing) and crashed on 3 of the 12 invalid inputs (a list given for a single value question). These were reported in `data/evaluation/initial_run/`, fixed in the engine with tests, and the scenarios were rerun. The preregistered expectations were not edited.
- One scenario still disagrees (S43: an unknown inside a list of values). The oracle expected APPLIES under three valued OR; the engine returns UNKNOWN. The engine is deliberately conservative here, the specification was ambiguous (assumption A2), and the divergence is recorded in `docs/DECISIONS.md` rather than hidden.
- Of the 12 invalid inputs, 10 were rejected with a message that names the valid values, 2 were accepted and 0 crashed. The accepted case is a comma separated string for a multiple choice question, which the engine splits into a list by design (scenario S75); the preregistration had expected rejection or unknown, so this is a disagreement and is reported.
- The preregistration rests on the order of commits (the scenario file was committed before the harness that runs the engine) and on the author's report; there is no external timestamp.
- Simulation (a property that holds by construction of three valued logic, so it tests the implementation and not the design): 3000 random profiles were answered one question at a time in random order (24000 steps). No step flipped an item from APPLIES to DOES_NOT_APPLY or the reverse (0 flips).

What this does not show. The scenarios test whether the engine implements the checklist as written. They do not show that the checklist rules are legally correct, which needs a domain reviewer.

## 3. Coding reliability

Two blind coders, working only from the row text and a written codebook, recoded 120 randomly chosen headline test rows. Cells show percentage agreement with Cohen's kappa in brackets.

| Field | Original and blind coder 2: agreement % (kappa) | Original and blind coder 3 | Blind coder 2 and 3 | Krippendorff alpha, 3 coders |
|---|---|---|---|---|
| Binding status, five classes | 75.8 (0.636) | 77.5 (0.662) | 94.2 (0.905) | 0.729 |
| Binding status, three classes | 83.3 (0.664) | 83.3 (0.66) | 96.7 (0.919) | 0.736 |
| Primary test type | 78.3 (0.757) | 78.3 (0.758) | 90.0 (0.889) | 0.802 |

The two blind coders agree with each other closely (kappa 0.905 on five classes). Each agrees less with the original coding (kappa 0.636 to 0.662). In 24 of the 30 binding status disagreements where exactly one coder differs (one more row has three different codes), the original is the odd one out. The original coder used ambiguous on 20 of 120 rows, against 5 and 2 for the blind coders, and the dominant pattern is ambiguous in the original against guidance in both blind codings. Two causes are possible and cannot be separated here: the original coder read the whole document while the blind coders read one provision, and the written instructions differed (the blind codebook asks for ambiguous to be used sparingly). The blind coders also saw the analyst's paraphrase and the document name, so agreement is probably higher than it would be on raw text. For these reasons the original coding is not described as inaccurate, and agreement is not described as accuracy. A human second coding is still needed; a template of 100 rows is provided in `data/coding/phase4/human_gold_template.csv`, and the agreement script reads it when it is filled in.

## 4. Robustness of the headline finding

Claim under test: binding (mandatory or conditional) test provisions are a minority of test provisions. Headline: 81 of 290 (27.9%).

| Scenario | Binding share of test provisions (%) |
|---|---|
| Headline test rows as coded | 27.9 |
| Leave one family out, lowest (without EU-AI-Act) | 20.8 |
| Leave one family out, highest (without US-NIST) | 31.9 |
| Rows excluded from the headline added back, all counted binding | 32.8 |
| Rows excluded from the headline added back, all counted non binding | 26.0 |
| Ambiguous rows all counted binding | 40.0 |
| Both adjustments, most favourable to binding | 44.1 |
| Both adjustments, least favourable to binding | 26.0 |
| Each document weighted equally (mean over documents) | 25.5 |
| Document level bootstrap, 95% interval | 13.4 to 43.7 |

The claim survives every scenario. Even when every excluded row and every ambiguous row is counted as binding, the binding share is 44.1%. The share is also not driven by a few long documents: of 71 documents, 21 (29.6%) contain any binding test provision. The conclusion that binding provisions are a minority is supported, but the size of the minority depends on coding choices and should be quoted with the interval, not as one number.

## 5. Fresh independent verification

120 rows were drawn at random (fixed seed) from the 485 rows that earlier checks had marked as verified and readable. A verifier who saw only the row and the rules reread the primary source. A source can be read only when the session can fetch it, and 26 of 120 rows (21.7%) could not be read in this session, mostly because of a session level domain allowlist, not because the sites refused. The error rates below therefore describe the 94 readable rows only.

| Measure | Rows | Rate | 95% interval (Wilson) |
|---|---|---|---|
| Errors, as graded by the verifier | 4 of 94 | 4.3% | 1.7 to 10.4 |
| Errors, after the lead applied the rubric strictly | 6 of 94 | 6.4% | 3.0 to 13.2 |
| Any fault, including minor | 20 of 94 | 21.3% | 14.2 to 30.6 |

Rows with a strict error: EU-AI-Act-004, Korea-002, Korea-003, UAE-DIFC-ADGM-010, UK-004, US-NIST-033. Only 17 of 26 sampled European Union rows could be read, and that family supplies a large share of the binding rows, so the rate says little about the rows behind the headline. It is also a rate among rows that earlier checks had already passed. The phase 3 fresh sample (drawn before the corrections) is reported separately because it was drawn at a different time: 3 errors in 23 verifiable rows (13.0%, 95% interval 4.5% to 32.1%); the phase 3 recheck of rows phase 2 had left open found 15 in 142 (10.6%). The true error rate of the whole table is plausibly higher than the readable subset of this sample suggests. Accepted corrections were applied to the table and listed in `data/verification/phase4/patches_p4.json`. If every unreadable row were an error, the rate for the sample could be as high as 26.7%, so the rate describes readable rows and must not be extended to the rest without saying so. The unreadable rows are listed for manual checking.

## 6. Completeness pilot

A separate agent built a reference list of 82 candidate documents without seeing the table, and the matches were made by hand. 3 candidates were outside the stated frame. Of 19 candidates confirmed to contain a testing provision, 13 are in the table: recall 68.4% (95% interval 46.0 to 84.6). A further 58 candidates could not be confirmed either way, of which 30 are in the table, so the most pessimistic recall is 55.8%. Missed documents (all United States federal): NIST AI 200-2 ipd, The TEVV-Athlon Framework for Evaluating AI Systems; NIST AI 700-2 ARIA Pilot Evaluation Report (ARIA 0.1); ARIA Program Evaluation Design Document; NIST SP 800-218A Secure Software Development Practices for Generative AI and Dual-Use Foundation Models; M-25-22 Driving Efficient Acquisition of Artificial Intelligence in Government; America's AI Action Plan. Of the 28 unresolved candidates not in the table, 6 are UAE instruments. Matching was done by hand by the author of the table. After the benchmark was scored, the six confirmed misses were read from official hosts (6 of 6 readable) and 19 candidate rows were drafted from them in `data/completeness/us_docs_candidate_rows.csv`. Those rows are not in the table and were not used to change the recall figure, because they have not been independently verified; adding them unverified would also raise recall by construction.

This is a pilot, not a population estimate. The reference list was built under the same tool limits as the table, so the two are not independent of search behaviour, and the interval is wide because the count is small.

## 7. What these results allow

- The table can be described as a documented, partly independently checked evidence base. It can not be described as complete or error free.
- The headline that binding test provisions are a minority is robust to the coding choices tested here.
- The checklist tool implements its specification safely (it never excluded an item it should not), with one documented conservative divergence. Its legal correctness has not been reviewed.
- Open items that need the author or an outside reviewer are listed in `docs/GAP_ANALYSIS.md`.
