"""Record which model ran each coder, extractor and verifier (phase 5).

Appends one row per run to data/model_identity_log.csv. The identifier is whatever the agent reported about
itself, together with the identifier the session was configured with; where an agent could not report it, the
field says so. Run: python -m ikhtibar.model_identity RUN_ID TASK ROLE REPORTED [NOTE]
"""
import csv, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "data" / "model_identity_log.csv"
FIELDS = ["run_id", "task", "role", "reported_by_agent", "session_configured", "recorded_on", "note"]
CONFIGURED = "identifier withheld"


def append(run_id, task, role, reported, note=""):
    new = not LOG.exists()
    with open(LOG, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(FIELDS)
        w.writerow([run_id, task, role, reported or "agent could not report it", CONFIGURED,
                    datetime.date.today().isoformat(), note])


if __name__ == "__main__":
    a = sys.argv[1:]
    append(a[0], a[1], a[2], a[3] if len(a) > 3 else "", a[4] if len(a) > 4 else "")
