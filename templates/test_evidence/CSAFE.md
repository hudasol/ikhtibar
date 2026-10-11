# CSAFE: Content safety evaluation

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Build question banks for harmful content categories relevant to the service and a separate bank of legitimate requests to detect over refusal.
- Measure harmful output rate and refusal rate, in each language the service supports.
- Re run after prompt, model or filter changes.

## What to record

- Bank composition, size, languages, and how it was built and protected from leakage into tuning.
- Rates per category with uncertainty, against thresholds set in advance.

## What a reviewer looks for

- Banks cover the languages and dialects used by the audience.
- Over refusal is measured as well as harm.
- Thresholds were set before the run.

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
| `China-024` | China - GB/T 45654-2025 Cybersecurity Technology: Basic Safe | voluntary | Sec. 5.2a; App. B.2.2.2 |
