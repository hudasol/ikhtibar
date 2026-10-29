# Licence decision and licence record

**Decision (author, standing):** no open licence. All rights are reserved. Anyone who wishes to use, modify, distribute or sell the work should contact the author first. The `LICENSE` file records this. The open licence table below is the earlier proposal and is kept only for reference; it is not in force. Research, not legal advice; ask a lawyer or the university or employer if either could have a claim on the work.

## Earlier proposal (not adopted)

| Part | Proposed licence | Reason |
|---|---|---|
| Documents, tables and data (`docs/`, `data/`, `templates/`, `examples/`, `README.md`) | Creative Commons Attribution 4.0 International (CC BY 4.0) | Allows reuse and adaptation with attribution, which suits a research record that others may extend. It is a common licence for open research outputs. |
| Code (`src/`, `scripts/`, `tests/`, `.github/`) | MIT Licence | Short and permissive, compatible with the PyYAML dependency (MIT), and easy for public sector and student readers to adopt. Apache 2.0 is an alternative if an explicit patent grant matters; it is also compatible with the dependencies. |

Third party material: the evidence table paraphrases public documents and quotes only short attributed fragments. The documents themselves remain under their publishers' terms. The licences above cover the author's paraphrases, analysis and code only. A repository check (`scripts/check_content.py`) fails on long quotations and document binaries.

## Licence record for libraries and data

| Item | Use | Licence | Cost |
|---|---|---|---|
| Python standard library | All code | PSF Licence | Free |
| PyYAML 6.0.3 | Reads `data/checklist.yaml` and `data/answers_schema.yaml` in the build scripts | MIT | Free |
| pytest 9.1.1 | Optional test runner (tests also run under `unittest`) | MIT | Free |
| detect-secrets 1.5.0 | Optional extra secrets scan, run locally | Apache 2.0 | Free |
| GitHub Actions | CI on a public repository | Service terms; free for public repositories | Free |
| Public source documents cited in the table | Read only; not redistributed | Each publisher's own terms | Free to read |

No dataset is bundled. No paid service, subscription or paid API is used or required.

## Things the author must confirm

1. That the all rights reserved notice in `LICENSE` is what you want for a conference submission, since some venues ask for a data availability statement.
2. That no employer or university terms apply to the work.
3. Whether CC BY 4.0 attribution wording should name the author in a particular form.
