# RED: Red teaming and dangerous capability evaluation

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Plan the red team scope from the misuse and failure scenarios of the deployment, including tool use for agentic systems.
- Use testers who were not involved in building the system, with domain knowledge relevant to the service.
- Record attempts, not only successes, so the effort is visible.

## What to record

- Scenarios, tester roles and independence, attack strategies tried, number of attempts.
- Successful attacks with reproduction steps, severity and the fix or accepted risk.
- Residual risk statement and re test plan after changes.

## What a reviewer looks for

- Independence of the testers from the developers.
- Coverage of the whole workflow, not only the model.
- Findings drive changes and re testing, rather than ending in a report.

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
| `Singapore-016` | Singapore AI Verify Testing Framework (for traditional and g | voluntary | Outcome 4.1 / Process 4.1.1, p.29 (technical testing, genera |
| `UK-024` | UK AI Security Institute (AISI) | voluntary | AI Safety Institute approach to evaluations (published 2024- |
| `ISO-IEC-015` | ISO/IEC standards | guidance | ISO/IEC AWI TS 42119-7 catalogue page |
| `Japan-020` | Japan AISI - Guide to Red Teaming Methodology on AI Safety v | guidance | Sec. 5.1 and 6.1 |
| `US-NIST-027` | US NIST AI 600-1 Generative AI Profile (July 2024) | guidance | GV-1.3-003, p.15 |
