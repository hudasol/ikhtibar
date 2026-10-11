# PERF: Performance and validity evaluation

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Define the task, the unit of evaluation and the metrics before looking at results.
- Run the system on a held out test set drawn from data that resembles deployment conditions, and on a separate set of known hard cases.
- Report the metric with an uncertainty estimate (confidence interval or repeated runs), not a single point value.

## What to record

- Test data source, version, size, date range, and how it was kept apart from training data.
- Metric definitions, thresholds fixed in advance, and who approved them.
- Results per metric, per important slice, and the failure examples reviewed.
- Model or system version identifier, configuration, and random seeds.

## What a reviewer looks for

- Thresholds were set before testing and are tied to the stakes of the decision.
- The test set matches the real population and language, and there is no leakage from training data.
- Uncertainty is stated and weak slices are reported rather than averaged away.
- The metric measures what the service needs (a benchmark that predicts the outcome of interest).

## Evidence record (fill in)

| Field | Entry |
|---|---|
| System and version | |
| Test date and tester | |
| Data used (source, version) | |
| Acceptance criteria (fixed before testing) | |
| Result | |
| Findings and closure | |
| Open items marked UNKNOWN | |
| Approver | |

## Source rows that motivate this template

Selected by script from verified rows; these are examples, not a complete list. Statuses are the source's own.

| Row | Framework | Source status | Clause |
|---|---|---|---|
| `UAE-AbuDhabi-DoH-003` | DoH Abu Dhabi Responsible AI Standard V1 (Oct 2025) | mandatory | Cl. 3.1.3.1.1 |
| `EU-AI-Act-016` | EU AI Act (Reg. (EU) 2024/1689, as amended by Reg. (EU) 2026 | conditional | Art. 9(6) |
| `US-OMB-003` | US OMB Memorandum M-25-21 (3 April 2025) - federal agency us | conditional | s.4(b)(i), p.15-16 |
| `EU-Standards-005` | EU harmonised standards work (CEN-CENELEC JTC 21) | voluntary | JTC 21 standards feed: prEN 18281, 18282 |
| `Singapore-023` | Singapore AI Verify Testing Framework (for traditional and g | voluntary | Outcome 3.12, p.27 |
