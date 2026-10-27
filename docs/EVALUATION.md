# Evaluation of the evidence base and the checklist tool

This file is generated from the committed result files in `data/` (see `src/ikhtibar/eval_values.py`). Every number below is read from a result file, and a test fails if a result file is older than the table it describes. It is research, not legal advice.

## What is measured, and what is not

The project makes five kinds of claim, and each is checked by a different method.

| Claim | Check | Section |
|---|---|---|
| Binding status and test type codes are regular, not arbitrary | Simple baselines predict the codes from the text | 1 |
| The checklist tool decides applicability correctly and safely | 94 scenarios written before the tool was run, four naive baselines, and a simulation | 2 |
| The coding can be repeated by someone else | Two blind second codings of 120 rows | 3 |
| The headline finding (binding test provisions are a minority) does not depend on coding choices | Sensitivity and bootstrap analysis | 4 |
| Table rows say what the sources say | Fresh independent verification of a random sample of 120 rows | 5 |
| The table covers the relevant documents | Pilot recall against an independently built reference list | 6 |

Throughout, the labels are the analyst's own codes (made with AI assistance and then checked), so a high agreement or a high baseline score shows that the coding is regular, not that it is correct. Correctness of the rows is addressed only by section 5.

## 1. Baselines for the two codings

Population: 290 headline test rows from 71 documents in 16 families. Protocols: 10 times repeated stratified five fold cross validation, and leave one family out, which removes every document of a family from training. Intervals are bootstrap 95% intervals over rows (2000 resamples, fixed seed). The models use scikit-learn 1.9.1. Methods and cut offs were fixed before any result was seen.

### Binding status, five classes (mandatory, conditional, voluntary, guidance, ambiguous)

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 45.5 (39.7 to 51.4) | 12.5 | 0.0 | 45.5 (40.0 to 51.4) | 12.5 |
| Document prior (most common label in the same document) | 84.3 (80.2 to 88.2) | 81.9 | 0.774 | 45.5 (40.0 to 51.4) | 12.5 |
| Wording rule (shall, must versus should, may) | 58.3 (52.8 to 64.1) | 31.2 | 0.344 | 58.3 (52.8 to 64.1) | 31.2 |
| TF-IDF with logistic regression | 50.5 (44.7 to 56.2) | 21.1 | 0.117 | 47.2 (41.7 to 52.8) | 16.0 |
| TF-IDF with logistic regression plus document indicator | 79.1 (74.4 to 83.1) | 74.8 | 0.686 | 45.5 (40.0 to 51.4) | 12.5 |

### Binding status, three classes (binding, non binding, ambiguous)

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 60.0 (54.1 to 65.5) | 25.0 | 0.0 | 60.0 (54.1 to 65.5) | 25.0 |
| Document prior (most common label in the same document) | 89.6 (86.2 to 92.8) | 87.0 | 0.805 | 60.0 (54.1 to 65.5) | 25.0 |
| Wording rule (shall, must versus should, may) | 76.9 (72.1 to 82.1) | 60.8 | 0.554 | 76.9 (72.1 to 82.1) | 60.8 |
| TF-IDF with logistic regression | 64.6 (58.9 to 69.8) | 35.6 | 0.154 | 61.7 (55.9 to 66.9) | 29.1 |
| TF-IDF with logistic regression plus document indicator | 84.7 (80.8 to 88.2) | 80.6 | 0.699 | 60.0 (54.1 to 65.5) | 25.0 |

### Primary test type, fifteen classes

| Method | Accuracy, repeated 5 fold CV (95% CI) | Macro F1 | Kappa | Accuracy, leave one family out (95% CI) | Macro F1 |
|---|---|---|---|---|---|
| Majority class | 20.0 (15.5 to 24.8) | 2.2 | 0.0 | 14.5 (10.7 to 18.6) | 1.8 |
| Document prior (most common label in the same document) | 27.8 (23.4 to 32.6) | 17.3 | 0.166 | 14.5 (10.7 to 18.6) | 1.8 |
| Keyword rule (taxonomy definitions) | 47.2 (41.4 to 53.1) | 43.9 | 0.414 | 47.2 (41.4 to 53.1) | 43.9 |
| TF-IDF with logistic regression | 30.0 (25.3 to 35.2) | 9.8 | 0.139 | 25.2 (20.3 to 30.3) | 7.0 |
| TF-IDF with logistic regression plus document indicator | 32.2 (27.5 to 37.3) | 15.4 | 0.195 | 22.8 (17.9 to 27.6) | 5.7 |

### Reading the results

- Binding status is largely a property of the document, not of the sentence. The document prior reaches 84.3% accuracy when documents are seen in training, against 45.5% for the majority class. When a whole family is held out, the document prior falls back to the majority rate (45.5%), because it has nothing to look up.
- A bag of words model does little better than the majority class on binding status (50.5%). Wording alone is a weak signal, which is why the coding reads each provision in the context of its document.
- For test type, a keyword rule built from the taxonomy definitions (47.2%) beats TF-IDF with logistic regression (30.0%) and the majority class (20.0%). With 290 rows and fifteen classes, a learned model has too little data. This is a modest baseline, not evidence that test type is easy to code.
- The best baseline is therefore not a trained model. Any later classifier, or any language model coder, should be compared with the document prior and the keyword rule, not with the majority class alone.

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
- The two valued baselines look acceptable on accuracy alone but are unsafe: the closed version drops items the user cannot yet rule out, and the open version applies items that do not apply. The engine returns UNKNOWN in 1062 item decisions instead, and states which answer would settle each one.
- The first run, before any change, matched 2454 of 2460 decisions (99.8%) and 80 of 82 scenarios, but wrongly excluded 3 items (an empty list given for a multiple choice question was treated as a known answer that matched nothing) and crashed on 3 of the 12 invalid inputs (a list given for a single value question). These were reported in `data/evaluation/initial_run/`, fixed in the engine with tests, and the scenarios were rerun. The preregistered expectations were not edited.
- One scenario still disagrees (S43: an unknown inside a list of values). The oracle expected APPLIES under three valued OR; the engine returns UNKNOWN. The engine is deliberately conservative here, the specification was ambiguous (assumption A2), and the divergence is recorded in `docs/DECISIONS.md` rather than hidden.
- Of the 12 invalid inputs, 10 were rejected with a message that names the valid values and 0 crashed.
- Simulation: 3000 random profiles were answered one question at a time in random order (24000 steps). No step flipped an item from APPLIES to DOES_NOT_APPLY or the reverse (0 flips).

What this does not show. The scenarios test whether the engine implements the checklist as written. They do not show that the checklist rules are legally correct, which needs a domain reviewer.

## 3. Coding reliability

Two blind coders, working only from the row text and a written codebook, recoded 120 randomly chosen headline test rows. Cells show percentage agreement with Cohen's kappa in brackets.

| Field | Original and blind coder 2: agreement % (kappa) | Original and blind coder 3 | Blind coder 2 and 3 | Krippendorff alpha, 3 coders |
|---|---|---|---|---|
| Binding status, five classes | 75.8 (0.636) | 77.5 (0.662) | 94.2 (0.905) | 0.729 |
| Binding status, three classes | 83.3 (0.664) | 83.3 (0.66) | 96.7 (0.919) | 0.736 |
| Primary test type | 78.3 (0.757) | 78.3 (0.758) | 90.0 (0.889) | 0.802 |

The two blind coders agree with each other closely (kappa 0.905 on five classes). Each agrees less with the original coding (kappa 0.636 to 0.662). In 24 of the 31 binding status disagreements where exactly one coder differs, the original is the odd one out. The dominant pattern is the original coder coding a provision as ambiguous where both blind coders code it as guidance. This is an information difference, not a pure error: the original coder read the whole document, and the blind coders saw one provision. For that reason the original coding is not described as inaccurate, and the blind agreement is not described as accuracy either. A human second coding is still needed; a template of 100 rows is provided in `data/coding/phase4/human_gold_template.csv`, and the agreement script reads it when it is filled in.

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

120 rows were drawn at random (fixed seed) from the 485 rows that earlier checks had marked as verified and readable. A verifier who saw only the row and the rules re read the primary source. A source can be read only when the session can fetch it, and 47 of 120 rows (39.2%) could not be read in this session, mostly because of a session level domain allowlist, not because the sites refused. The error rates below therefore describe the 73 readable rows only.

| Measure | Rows | Rate | 95% interval (Wilson) |
|---|---|---|---|
| Errors, as graded by the verifier | 3 of 73 | 4.1% | 1.4 to 11.4 |
| Errors, after the lead applied the rubric strictly | 5 of 73 | 6.8% | 3.0 to 15.1 |
| Any fault, including minor | 15 of 73 | 20.5% | 12.9 to 31.2 |
| Strict errors pooled with the phase 3 fresh sample | 8 of 96 (8.3%, 95% interval 4.3 to 15.6) | | |

Rows with a strict error: Korea-002, Korea-003, UAE-DIFC-ADGM-010, UK-004, US-NIST-033. Accepted corrections were applied to the table and listed in `data/verification/phase4/patches_p4.json`. If every unreadable row were an error, the rate for the sample could be as high as 43.3%, so the rate describes readable rows and must not be extended to the rest without saying so. The unreadable rows are listed for manual checking.

## 6. Completeness pilot

A separate agent built a reference list of 82 candidate documents without seeing the table, and the matches were made by hand. 3 candidates were outside the stated frame. Of 19 candidates confirmed to contain a testing provision, 13 are in the table: recall 68.4% (95% interval 46.0 to 84.6). A further 58 candidates could not be confirmed either way, of which 30 are in the table, so the most pessimistic recall is 55.8%. Missed documents: NIST AI 200-2 ipd, The TEVV-Athlon Framework for Evaluating AI Systems; NIST AI 700-2 ARIA Pilot Evaluation Report (ARIA 0.1); ARIA Program Evaluation Design Document; NIST SP 800-218A Secure Software Development Practices for Generative AI and Dual-Use Foundation Models; M-25-22 Driving Efficient Acquisition of Artificial Intelligence in Government; America's AI Action Plan.

This is a pilot, not a population estimate. The reference list was built under the same tool limits as the table, so the two are not independent of search behaviour, and the interval is wide because the count is small.

## 7. What these results allow

- The table can be described as a documented, partly independently checked evidence base. It can not be described as complete or error free.
- The headline that binding test provisions are a minority is robust to the coding choices tested here.
- The checklist tool implements its specification safely (it never excluded an item it should not), with one documented conservative divergence. Its legal correctness has not been reviewed.
- Open items that need the author or an outside reviewer are listed in `docs/GAP_ANALYSIS.md`.
