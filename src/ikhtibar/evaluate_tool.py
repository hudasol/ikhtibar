"""Evaluation of the checklist tool against preregistered scenarios, naive baselines and simulations.

Inputs
  data/evaluation/prereg/scenarios_prereg.json   written from the checklist YAML alone, before the engine was run
Outputs
  data/evaluation/results.json                   summary figures
  data/evaluation/misses.csv                     every item level disagreement with the preregistered expectation
  data/evaluation/simulation.json                monotonicity check and elicitation curve over random profiles
Run: python -m ikhtibar.evaluate_tool

Baselines (all use the same checklist conditions)
  closed_two_valued  missing or unknown answers count as "does not match" (a common checklist design)
  open_two_valued    missing or unknown answers count as "matches" (apply when unsure)
  always_applies     every item APPLIES
  structure_only     items with an always rule APPLY, every other item is UNKNOWN (answers ignored)
"""
import csv, json, random, itertools, collections
from pathlib import Path

from . import engine

ROOT = Path(__file__).resolve().parents[2]
EV = ROOT / "data" / "evaluation"
SEED = 20261028
STATES = ("APPLIES", "DOES_NOT_APPLY", "UNKNOWN")


# ------------------------------------------------------------ two valued baselines
def two_valued(cond, a, missing):
    (op, arg), = cond.items()
    if op == "always":
        return bool(arg)
    if op in ("eq", "in", "contains", "any_contains", "tri"):
        key = arg[0]
        if key not in a:
            return missing
        v = a[key]
        if op == "eq":
            return v == arg[1]
        if op == "in":
            return v in arg[1]
        if op == "contains":
            return arg[1] in v
        if op == "any_contains":
            return any(x in v for x in arg[1])
        return v in arg[1]  # tri: true list only
    if op == "not":
        return not two_valued(arg, a, missing)
    if op == "all":
        return all(two_valued(c, a, missing) for c in arg)
    if op == "any":
        return any(two_valued(c, a, missing) for c in arg)
    raise ValueError(op)


def baseline_predictions(name, checklist, answers, schema):
    try:
        a = engine.validate_answers(answers, schema)
    except engine.AnswerError:
        a = {}
    out = {}
    for it in checklist["items"]:
        c = it["applies_when"]
        if name == "closed_two_valued":
            out[it["id"]] = "APPLIES" if two_valued(c, a, False) else "DOES_NOT_APPLY"
        elif name == "open_two_valued":
            out[it["id"]] = "APPLIES" if two_valued(c, a, True) else "DOES_NOT_APPLY"
        elif name == "always_applies":
            out[it["id"]] = "APPLIES"
        elif name == "structure_only":
            out[it["id"]] = "APPLIES" if list(c.keys()) == ["always"] and c["always"] else "UNKNOWN"
    return out


def engine_predictions(answers, checklist, schema, rows):
    try:
        res = engine.run(answers, checklist, schema, rows)
    except engine.AnswerError as e:
        return None, "AnswerError: " + str(e)
    except Exception as e:  # a crash is a different outcome from a clean rejection
        return None, "CRASH " + type(e).__name__ + ": " + str(e)
    return {i["id"]: i["state"] for i in res["items"]}, ""


# ------------------------------------------------------------ scoring
def score(pred_by_scn, scenarios):
    n = ok = unsafe_excl = overclaim = unk = 0
    for s in scenarios:
        p = pred_by_scn[s["id"]]
        for iid, exp in s["expected"].items():
            got = p[iid]
            n += 1
            ok += got == exp
            unk += got == "UNKNOWN"
            unsafe_excl += (got == "DOES_NOT_APPLY" and exp != "DOES_NOT_APPLY")
            overclaim += (got == "APPLIES" and exp != "APPLIES")
    return {"item_decisions": n, "agree_with_expected": ok,
            "accuracy": round(100 * ok / n, 1),
            "wrongly_excluded": unsafe_excl,      # said DOES_NOT_APPLY where expected is APPLIES or UNKNOWN
            "wrongly_applied": overclaim,         # said APPLIES where expected is DOES_NOT_APPLY or UNKNOWN
            "unknown_returned": unk}


def evaluate_prereg():
    checklist, schema, rows = engine.load_checklist(), engine.load_schema(), engine.load_rows()
    d = json.loads((EV / "prereg" / "scenarios_prereg.json").read_text(encoding="utf-8"))
    specified = [s for s in d["scenarios"] if s.get("expected_status", "specified") == "specified"]
    unspecified = [s for s in d["scenarios"] if s.get("expected_status") == "unspecified"]
    items = [i["id"] for i in checklist["items"]]
    assert all(set(s["expected"]) == set(items) for s in d["scenarios"]), "scenario does not cover every item"

    eng, misses = {}, []
    for s in specified:
        pred, err = engine_predictions(s["answers"], checklist, schema, rows)
        if pred is None:
            # the engine rejected a scenario the preregistration expected to evaluate
            pred = {i: "ERROR" for i in items}
            misses.append({"scenario": s["id"], "item": "*", "expected": "evaluated", "got": "rejected: " + err,
                           "assumptions": ";".join(s.get("depends_on_assumption", [])), "tags": ";".join(s.get("tags", []))})
        eng[s["id"]] = pred
        for iid in items:
            if pred[iid] != s["expected"][iid]:
                misses.append({"scenario": s["id"], "item": iid, "expected": s["expected"][iid], "got": pred[iid],
                               "assumptions": ";".join(s.get("depends_on_assumption", [])),
                               "tags": ";".join(s.get("tags", []))})
    results = {"scenarios_total": len(d["scenarios"]), "scenarios_specified": len(specified),
               "scenarios_unspecified": len(unspecified), "items": len(items), "assumptions": d["assumptions"],
               "engine": score(eng, specified), "baselines": {}}
    exact = sum(1 for s in specified if all(eng[s["id"]][i] == s["expected"][i] for i in items))
    results["engine"]["scenarios_exact_match"] = exact
    results["engine"]["scenarios_exact_match_pct"] = round(100 * exact / len(specified), 1)
    for b in ("closed_two_valued", "open_two_valued", "always_applies", "structure_only"):
        preds = {s["id"]: baseline_predictions(b, checklist, s["answers"], schema) for s in specified}
        results["baselines"][b] = score(preds, specified)
        results["baselines"][b]["scenarios_exact_match_pct"] = round(100 * sum(
            1 for s in specified if all(preds[s["id"]][i] == s["expected"][i] for i in items)) / len(specified), 1)
    # scenarios whose expectation depended on a stated assumption
    dep = [s for s in specified if s.get("depends_on_assumption")]
    results["engine"]["scenarios_depending_on_assumptions"] = len(dep)
    results["engine"]["misses_in_assumption_dependent_scenarios"] = len({m["scenario"] for m in misses if m["assumptions"]})
    # unspecified (invalid input) behaviour
    unspec = []
    for s in unspecified:
        pred, err = engine_predictions(s["answers"], checklist, schema, rows)
        unspec.append({"scenario": s["id"], "description": s["description"], "answers": s["answers"],
                       "engine": ("crashed" if err.startswith("CRASH") else "rejected with a message") if pred is None else "accepted",
                       "message": err if pred is None else "",
                       "matches_lenient_expected": None if pred is None else
                       all(pred[i] == s["expected"][i] for i in items)})
    results["invalid_inputs"] = unspec
    # monotone pairs declared in the file
    mp = []
    for s in d["scenarios"]:
        pair = s.get("monotone_pair")
        if pair and s["id"] == pair.split("/")[0]:
            a_id, b_id = pair.split("/")
            sa = next(x for x in d["scenarios"] if x["id"] == a_id)
            sb = next(x for x in d["scenarios"] if x["id"] == b_id)
            pa, _ = engine_predictions(sa["answers"], checklist, schema, rows)
            pb, _ = engine_predictions(sb["answers"], checklist, schema, rows)
            if pa and pb:
                flips = [i for i in items if {pa[i], pb[i]} == {"APPLIES", "DOES_NOT_APPLY"}]
                mp.append({"pair": pair, "flips": flips})
    results["monotone_pairs_checked"] = mp
    return results, misses


# ------------------------------------------------------------ simulation over random profiles
def random_profile(schema, rng, full):
    a = {}
    for k, q in schema["questions"].items():
        vals = list(q["values"])
        if q["type"] == "multi":
            if "none" in vals and rng.random() < 0.15:
                a[k] = ["none"]
            else:
                pool = [v for v in vals if v != "none"]
                a[k] = sorted(rng.sample(pool, rng.randint(1, min(3, len(pool)))))
        else:
            a[k] = rng.choice(vals)
    return a


def simulate(n_profiles=3000):
    checklist, schema, rows = engine.load_checklist(), engine.load_schema(), engine.load_rows()
    rng = random.Random(SEED)
    keys = list(schema["questions"])
    items = [i["id"] for i in checklist["items"]]
    flips = 0
    checked = 0
    curve = collections.defaultdict(list)  # number of questions answered -> unknown counts
    applies_curve = collections.defaultdict(list)
    for _ in range(n_profiles):
        full = random_profile(schema, rng, True)
        order = keys[:]
        rng.shuffle(order)
        prev = None
        a = {}
        for step in range(len(order) + 1):
            if step:
                a[order[step - 1]] = full[order[step - 1]]
            res = engine.run(dict(a), checklist, schema, rows)
            st = {i["id"]: i["state"] for i in res["items"]}
            if prev is not None:
                checked += 1
                for i in items:
                    if {prev[i], st[i]} == {"APPLIES", "DOES_NOT_APPLY"}:
                        flips += 1
            prev = st
            curve[step].append(res["summary"]["UNKNOWN"])
            applies_curve[step].append(res["summary"]["APPLIES"])
    q = lambda xs: {"mean": round(sum(xs) / len(xs), 2), "min": min(xs), "max": max(xs)}
    # which questions can ever settle an item: from the items' to_settle lists
    settle = collections.Counter(k for it in checklist["items"] for k in it.get("to_settle", []))
    return {"profiles": n_profiles, "seed": SEED, "questions": len(keys), "items": len(items),
            "monotonicity_steps_checked": checked, "applies_to_not_apply_flips": flips,
            "unknown_items_by_questions_answered": {str(k): q(v) for k, v in sorted(curve.items())},
            "applies_items_by_questions_answered": {str(k): q(v) for k, v in sorted(applies_curve.items())},
            "items_by_question_in_to_settle": dict(settle)}


def main():
    EV.mkdir(parents=True, exist_ok=True)
    results, misses = evaluate_prereg()
    (EV / "results.json").write_text(json.dumps(results, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    with open(EV / "misses.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["scenario", "item", "expected", "got", "assumptions", "tags"])
        w.writeheader()
        w.writerows(misses)
    sim = simulate()
    (EV / "simulation.json").write_text(json.dumps(sim, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("engine", results["engine"])
    for b, v in results["baselines"].items():
        print(b, v)
    print("misses", len(misses), "scenarios with a miss", len({m['scenario'] for m in misses}))
    print("simulation flips", sim["applies_to_not_apply_flips"], "of", sim["monotonicity_steps_checked"], "steps")


if __name__ == "__main__":
    main()
