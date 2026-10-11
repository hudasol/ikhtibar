"""Merge the UAE discovery logs and source lists into data/uae_search_log.csv and data/uae_sources.csv.

Adds a zone column and a normalised reading class. The original free text columns are kept.
Reading class is derived from the recorded language_read text:
  english_original       English text of the official publication was read
  arabic_original        Arabic wording was obtained, possibly only in part (see language_read)
  not_read               the document was not read
Whenever the fetch tool answered in English about an Arabic page, the entry is flagged
machine_summary_of_arabic = yes: the English rendering is the fetch tool's, not an official translation.
"""
import csv, os

D = os.path.join(os.path.dirname(__file__), "..", "..", "data")
ZONES = [("federal", "UAE federal"), ("abudhabi", "Abu Dhabi"), ("dubai", "Dubai")]


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def classify(lr, note=""):
    t = (lr or "").lower()
    if t.startswith("not read") or t.startswith("not opened") or t in ("none", ""):
        return "not_read", "no"
    if "arabic" in t or "mixed" in t:
        machine = "yes" if any(k in t for k in ("summary", "summarised", "tool", "garbled", "ocr")) else "no"
        return "arabic_original", machine
    return "english_original", "no"


def main():
    logs, srcs = [], []
    for key, zone in ZONES:
        for r in read(os.path.join(D, "uae_discovery", f"search_log_{key}.csv")):
            r["zone"] = zone
            logs.append(r)
        for r in read(os.path.join(D, "uae_discovery", f"sources_{key}.csv")):
            r["zone"] = zone
            tk = [k for k in r if k.startswith("testing_content")][0]
            bk = [k for k in r if k.startswith("blocked")][0]
            r["testing_content"] = r.pop(tk)
            r["blocked"] = r.pop(bk)
            r["reading_class"], r["machine_summary_of_arabic"] = classify(r["language_read"])
            srcs.append(r)
    lc = ["zone", "query", "language", "tool", "site_scope", "outcome", "urls_opened", "note"]
    sc = ["zone", "url", "title", "issuer", "version_or_date", "language_available", "language_read",
          "reading_class", "machine_summary_of_arabic", "translation_flag", "testing_content", "blocked", "note"]
    for name, cols, rows in (("uae_search_log.csv", lc, logs), ("uae_sources.csv", sc, srcs)):
        with open(os.path.join(D, name), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print("wrote", name, len(rows))


if __name__ == "__main__":
    main()
