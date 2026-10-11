# FAIR: Fairness, bias and representativeness testing

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Decide which groups and attributes are relevant for the service (including language, nationality, age, gender and disability where lawful and appropriate) before testing.
- Compare error rates and outcomes across groups, with enough cases per group to say something.
- Check how well the data represents the groups affected, including under represented groups.

## What to record

- Group definitions, how group membership was obtained, and the legal basis for using it.
- Per group sample sizes, metrics and gaps, with uncertainty.
- Mitigations tried and the residual gaps accepted, with the decision maker named.

## What a reviewer looks for

- Small groups are flagged as underpowered, not reported as equal.
- The chosen fairness measure is justified for the decision, and trade offs between measures are stated.
- Proxy variables were considered.

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
| `UAE-AbuDhabi-DoH-008` | DoH Abu Dhabi Responsible AI Standard V1 (Oct 2025) | mandatory | Cl. 3.1.5.1.1-3.1.5.1.3 |
| `UAE-DIFC-ADGM-002` | DIFC Data Protection Regulations, Consolidated Version No. 2 | conditional | Reg. 10.2.2(d) |
| `Singapore-019` | Singapore AI Verify Testing Framework (for traditional and g | voluntary | Outcome 7.1 / Process 7.1.1, p.71 (technical testing, tradit |
| `UAE-Dubai-001` | Smart Dubai AI Ethics Principles & Guidelines (Guidelines ch | guidance | Guideline 1.1.1.1 |
| `UAE-Federal-018` | UAE AI Ethics: Principles & Guidelines (Dec 2022) | guidance | s3.1.2.2, pp.18-19 |
