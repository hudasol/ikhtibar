# SEC: Security and adversarial resilience testing

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Review code and dependencies, scan for vulnerabilities and test the deployment configuration (access control, secrets, logging).
- Run penetration tests against the application and interfaces around the model.
- For learned models, test AI specific attacks relevant to the system type, such as prompt injection, data poisoning, evasion, model extraction and data leakage.

## What to record

- Scope, method, tools and versions, dates, and who carried out the test.
- Findings with severity, status and retest evidence.
- Residual risk accepted and by whom.

## What a reviewer looks for

- Third party and open source components were covered.
- AI specific attacks were chosen for the actual threat model, not copied from a list.
- Fixes were retested before release.

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
| `UAE-AbuDhabi-DoH-007` | DoH Abu Dhabi Responsible AI Standard V1 (Oct 2025) | mandatory | Cl. 3.1.4.3.1 |
| `UAE-Federal-007` | UAE Federal Decree-Law No. 45 of 2021 (PDPL) | mandatory | Art. 20(1)(d) |
| `EU-AI-Act-030` | EU AI Act (Reg. (EU) 2024/1689, as amended by Reg. (EU) 2026 | conditional | Art. 15(5) |
| `China-026` | China - GB/T 45654-2025 Cybersecurity Technology: Basic Safe | voluntary | Sec. 5.1; App. B.2.2.1 |
| `Singapore-025` | Singapore AI Verify Testing Framework (for traditional and g | voluntary | Outcomes 5.2 and 5.9, p.47 and p.54 |
