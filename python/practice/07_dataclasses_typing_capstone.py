# Practice 7 — Dataclasses, typing & an ETL capstone
# Run:  cd ~/learning/python && uv run python3 practice/07_dataclasses_typing_capstone.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# This is the capstone: it wires together Day 2 (comprehensions), Day 3
# (defaultdict grouping), Day 4 (key= sorting), Day 5 (generator functions),
# Day 6 (csv.DictReader / json.dump), and today's @dataclass + type hints
# into one small end-to-end ETL script. This file writes its own CSV fixture
# into a temp directory, so it needs no external file to already exist.

import csv
import json
import os
import tempfile
import types
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

WORKDIR = tempfile.mkdtemp(prefix="py7_practice_")

# ---------------------------------------------------------------------------
# Exercise 1 — define a @dataclass with a default field.
# Write a SalesRow dataclass with three fields:
#   city: str
#   amount: int
#   region: Optional[str] = None   (defaults to None when the caller omits it)
#
# TODO:
# @dataclass
# class SalesRow:
#     city: str
#     amount: int
#     region: Optional[str] = None


# ---------------------------------------------------------------------------
# Exercise 2 — extract(): a generator yielding SalesRow instances from a CSV.
# Write a fixture CSV (header + 4 rows, one row with a non-positive amount to
# be filtered out later), then write extract(path) as a generator function
# (Day 5 + Day 6's read_sales shape) that opens the file with `with`, wraps
# it in csv.DictReader, and yields one SalesRow per row (str -> int for
# amount).
csv_path = os.path.join(WORKDIR, "sales.csv")
csv_rows = [
    ["city", "amount"],
    ["Hanoi", "120"],
    ["HCMC", "80"],
    ["Hanoi", "45"],
    ["Danang", "-10"],
]
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    for row in csv_rows:
        writer.writerow(row)


def extract(path: str):
    ...                              # TODO:
    # with open(path) as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         yield SalesRow(city=row["city"], amount=int(row["amount"]))


# ---------------------------------------------------------------------------
# Exercise 3 — transform(): filter, group, and sort.
# Given an iterable of SalesRow, return a list of (city, total) tuples:
#   1. keep only rows with amount > 0            (Day 2 — list comprehension)
#   2. sum amount per city into a dict            (Day 3 — defaultdict(int))
#   3. sort the (city, total) pairs by total, descending  (Day 4 — key=)
def transform(rows):
    ...                              # TODO:
    # positive = [r for r in rows if r.amount > 0]
    # totals = defaultdict(int)
    # for r in positive:
    #     totals[r.city] += r.amount
    # return sorted(totals.items(), key=lambda pair: pair[1], reverse=True)


# ---------------------------------------------------------------------------
# Exercise 4 — load(): write the summary out as JSON.
# Given the list of (city, total) tuples from transform(), build a list of
# {"city": ..., "total": ...} dicts (Day 2 comprehension again) and write it
# to `path` with json.dump (Day 6).
json_path = os.path.join(WORKDIR, "summary.json")


def load(totals, path: str) -> None:
    ...                              # TODO:
    # summary = [{"city": city, "total": total} for city, total in totals]
    # with open(path, "w") as f:
    #     json.dump(summary, f)


# ---------------------------------------------------------------------------
# Exercise 5 — run(): wire extract -> transform -> load, then read the JSON
# back to prove the pipeline actually ran end to end.
def run(src_csv: str, dest_json: str) -> None:
    ...                              # TODO:
    # rows = extract(src_csv)
    # totals = transform(rows)
    # load(totals, dest_json)


run(csv_path, json_path)

loaded_summary = None
if os.path.exists(json_path):
    with open(json_path) as f:
        try:
            loaded_summary = json.load(f)
        except json.JSONDecodeError:
            loaded_summary = None


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _make_sales_row():
    # Exercises 2-5 all depend on SalesRow existing; build one defensively so
    # a missing Exercise 1 fails its own check instead of crashing every
    # later one with a NameError.
    try:
        return SalesRow(city="Hanoi", amount=120)
    except Exception:
        return None


results = [
    check("Ex 1: SalesRow is a dataclass with city, amount, and a region default of None",
          lambda: (lambda r: r is not None
                   and r == SalesRow(city="Hanoi", amount=120)
                   and r.region is None
                   and "SalesRow(city='Hanoi'" in repr(r))(_make_sales_row())),
    check("Ex 2: extract() is a lazy generator yielding SalesRow instances from the CSV",
          lambda: isinstance(extract(csv_path), types.GeneratorType)
          and list(extract(csv_path)) == [
              SalesRow(city="Hanoi", amount=120),
              SalesRow(city="HCMC", amount=80),
              SalesRow(city="Hanoi", amount=45),
              SalesRow(city="Danang", amount=-10),
          ]),
    check("Ex 3: transform() filters non-positive amounts, groups by city, sorts by total desc",
          lambda: transform(list(extract(csv_path))) == [("Hanoi", 165), ("HCMC", 80)]),
    check("Ex 4: load() writes the summary as JSON matching transform()'s totals",
          lambda: (lambda: (
              load(transform(list(extract(csv_path))), json_path),
              json.load(open(json_path)) == [
                  {"city": "Hanoi", "total": 165},
                  {"city": "HCMC", "total": 80},
              ],
          )[1])()),
    check("Ex 5: run() wires extract -> transform -> load into one working ETL script",
          lambda: loaded_summary == [
              {"city": "Hanoi", "total": 165},
              {"city": "HCMC", "total": 80},
          ]),
]
print("\nAll green — lesson 7 done, Phase 1 complete! 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
