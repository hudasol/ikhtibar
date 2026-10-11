# ROB: Robustness, reliability and fault testing

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Perturb inputs (noise, missing fields, formatting changes, paraphrases, scanned versus digital documents) and compare outputs.
- Run extreme and out of range values, and repeated runs of the same input to measure run to run stability.
- Inject faults (dependency down, slow response, malformed input) and observe fail safe behaviour.

## What to record

- Perturbation types and magnitudes, number of cases, and output change rates.
- Failure modes found, severity, and the mitigation or accepted risk for each.
- Fallback behaviour observed, and the time to recover.

## What a reviewer looks for

- A defined acceptable degradation, not just a list of tests run.
- Fallback to a human or manual process is tested, not assumed.
- Failures are traced to causes and either fixed or explicitly accepted by a named owner.

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
| `UAE-AbuDhabi-DoH-005` | DoH Abu Dhabi Responsible AI Standard V1 (Oct 2025) | mandatory | Cl. 3.1.2.1.3 |
| `EU-AI-Act-029` | EU AI Act (Reg. (EU) 2024/1689, as amended by Reg. (EU) 2026 | conditional | Art. 15(4) |
| `ISO-IEC-008` | ISO/IEC standards | voluntary | ISO/IEC 24029-2:2023 catalogue page |
| `Singapore-017` | Singapore AI Verify Testing Framework (for traditional and g | voluntary | Outcome 6.1 / Process 6.1.1, p.61 (technical testing) |
| `UAE-Federal-023` | UAE AI Ethics: Principles & Guidelines (Dec 2022) | guidance | s3.5.2.2, pp.32-33 |
