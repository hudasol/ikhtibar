# PRIV: Privacy and data protection assessment or testing

> PROPOSAL. This template was written by the maintainer from the retrieved sources. It is not a requirement of any authority and no authority has reviewed it. Adapt it to your entity and tier.

## What to run

- Complete a data protection impact assessment where the processing is high risk, and record the legal basis and scope check.
- Test for leakage of training or personal data in outputs, membership inference where relevant, and re identification risk in any released data.
- Check data minimisation, retention and access controls in the live configuration.

## What to record

- Data map, legal basis and scope analysis, including whether the entity and the data are within the law that applies.
- Test method and results for leakage and re identification.
- Actions taken and residual risk with sign off.

## What a reviewer looks for

- The scope question (which law applies to this entity and data) was answered by someone qualified to answer it.
- Tests used realistic prompts and data.

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
| `UAE-DIFC-ADGM-006` | ADGM Data Protection Regulations 2021 (via ODP Guidance Part | conditional | Guidance para. 3.1 (DPR s.34(1)) |
| `UAE-Federal-005` | UAE Federal Decree-Law No. 45 of 2021 (PDPL) | conditional | Art. 21 |
| `UK-009` | UK AI Playbook for the UK Government (GDS, published 2025-02 | conditional | Using AI safely and responsibly > Data protection and privac |
| `US-NIST-033` | US NIST AI 600-1 Generative AI Profile (July 2024) | guidance | MS-2.10-001, p.36 |
| `Saudi-005` | SDAIA AI Ethics Principles (Version 1.0, September 2023, rea | ambiguous | Principle 2, Deploy and Monitor item 3, p. 17 |
