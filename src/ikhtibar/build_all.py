"""Run every generator in dependency order: python -m ikhtibar.build_all"""
from . import (build_table, stats, build_checklist, build_templates, build_example, downloads,
               build_time, build_uae_logs, build_docs, normative)

STEPS = [("evidence table", build_table.main), ("statistics", stats.main), ("checklist", build_checklist.main),
         ("test evidence templates", build_templates.main), ("worked example", build_example.main),
         ("download list", downloads.main), ("time sensitive records", build_time.main),
         ("UAE search records", build_uae_logs.main), ("normative force coding", normative.main),
         ("documents", build_docs.main)]


def main():
    for name, fn in STEPS:
        print("==", name)
        fn()


if __name__ == "__main__":
    main()
