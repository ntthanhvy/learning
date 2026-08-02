# Practice 6 — Files, formats & context managers
# Run:  cd ~/learning/python && uv run python3 practice/06_files_formats_and_with.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# This file is self-contained: it creates its own scratch files in a temp
# directory (via tempfile), so it needs no external fixture to already exist,
# and cleans up after itself.

import csv
import json
import os
import tempfile

WORKDIR = tempfile.mkdtemp(prefix="py6_practice_")

# ---------------------------------------------------------------------------
# Exercise 1 — write then read a text file with `with`.
# Write the two lines in `lines` to a text file (one per line, each ending in
# "\n"), using `with open(path, "w") as f: ...`, then read the whole file
# back into `read_back` with `with open(path) as f: f.read()`.
text_path = os.path.join(WORKDIR, "notes.txt")
lines = ["first line", "second line"]
# TODO: with open(text_path, "w") as f:
#           for line in lines:
#               f.write(line + "\n")
...

read_back = ...                 # TODO: with open(text_path) as f: read_back = f.read()

# ---------------------------------------------------------------------------
# Exercise 2 — the leak-on-exception contrast, without a real crash-prone file.
# `FakeFile` below stands in for a real file object: `.close()` sets
# `.closed = True`. `leaky_use(fake, should_raise)` opens it, does some work,
# then calls `.close()` manually — if `should_raise` is True, an exception
# fires BEFORE the manual .close() line runs, so the file leaks (closed stays
# False). `safe_use(fake, should_raise)` should do the same work but use
# `fake` as a context manager (`with fake:`) so `.closed` becomes True
# EITHER WAY, exception or not — because FakeFile's __exit__ (already
# written for you below) always closes it.
class FakeFile:
    def __init__(self):
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True         # always runs, even if the with-body raised
        return False                # don't swallow the exception

    def close(self):
        self.closed = True


def leaky_use(fake, should_raise):
    # manual open/close pattern — no with statement
    try:
        if should_raise:
            raise ValueError("boom")
        fake.close()
    except ValueError:
        pass                        # exception caught here so the exercise can inspect fake.closed after
    return fake


def safe_use(fake, should_raise):
    ...                              # TODO:
    # try:
    #     with fake:
    #         if should_raise:
    #             raise ValueError("boom")
    # except ValueError:
    #     pass
    return fake


leaked = leaky_use(FakeFile(), should_raise=True)
saved = safe_use(FakeFile(), should_raise=True)

# ---------------------------------------------------------------------------
# Exercise 3 — csv.DictReader over a small CSV this script writes itself.
# Write `csv_rows` out as a CSV file (header + 3 rows) using csv.writer,
# then read it back with csv.DictReader into `read_rows`, a list of dicts.
csv_path = os.path.join(WORKDIR, "sales.csv")
csv_rows = [
    ["city", "amount"],
    ["Hanoi", "120"],
    ["HCMC", "80"],
    ["Danang", "200"],
]
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    for row in csv_rows:
        writer.writerow(row)

read_rows = ...                 # TODO:
# with open(csv_path) as f:
#     reader = csv.DictReader(f)
#     read_rows = [row for row in reader]

# ---------------------------------------------------------------------------
# Exercise 4 — json.dump then json.load, round-tripping a dict.
# Write `record` out to a JSON file with json.dump, then read it back with
# json.load into `loaded`. Types (int, list) should survive the round trip.
json_path = os.path.join(WORKDIR, "record.json")
record = {"city": "Hanoi", "amount": 120, "tags": ["retail", "q3"]}
...                              # TODO: with open(json_path, "w") as f: json.dump(record, f)

loaded = ...                    # TODO: with open(json_path) as f: loaded = json.load(f)

# ---------------------------------------------------------------------------
# Exercise 5 — lazily read the CSV into structured records (int amounts),
# via a generator function, chaining Day 5's generator idea onto Day 6's
# csv.DictReader. Write `read_sales(path)` as a generator function that opens
# the file, wraps it in csv.DictReader, and yields one
# {"city": ..., "amount": int(...)} dict per row.
def read_sales(path):
    ...                          # TODO:
    # with open(path) as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         yield {"city": row["city"], "amount": int(row["amount"])}


sales_records = ...              # TODO: list(read_sales(csv_path))


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


import types

results = [
    check("Ex 1: with-block writes lines then reads them back correctly",
          lambda: read_back == "first line\nsecond line\n"),
    check("Ex 2: with (safe_use) always closes even on exception, unlike manual close (leaky_use)",
          lambda: leaked.closed is False and saved.closed is True),
    check("Ex 3: csv.DictReader reads rows back as dicts keyed by column name",
          lambda: read_rows == [
              {"city": "Hanoi", "amount": "120"},
              {"city": "HCMC", "amount": "80"},
              {"city": "Danang", "amount": "200"},
          ]),
    check("Ex 4: json.dump/json.load round-trips the dict, types intact",
          lambda: loaded == record and isinstance(loaded["amount"], int)
          and isinstance(loaded["tags"], list)),
    check("Ex 5: read_sales() is a lazy generator yielding int-typed records",
          lambda: isinstance(read_sales(csv_path), types.GeneratorType)
          and sales_records == [
              {"city": "Hanoi", "amount": 120},
              {"city": "HCMC", "amount": 80},
              {"city": "Danang", "amount": 200},
          ]),
]
print("\nAll green — lesson 6 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
