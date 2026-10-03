# Practice 66 — csv.DictWriter: the write side of Day 6's DictReader
# Run:  cd ~/learning/python && uv run python3 practice/66_csv_dictwriter.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import csv
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 — writeheader() + writerows(), then read the result back with
# Day 6's csv.DictReader to confirm it round-trips.
# Write write_and_read(rows, fieldnames) that:
#   - creates a TemporaryDirectory() (Day 65) and a path inside it, "out.csv"
#   - opens that path for writing with newline="" (see Exercise 2 below for
#     why this matters)
#   - builds a csv.DictWriter(f, fieldnames=fieldnames), calls writeheader(),
#     then writerows(rows)
#   - reopens the same path for reading, wraps it in csv.DictReader, and
#     returns the rows read back as a list of dicts
# All from inside the same with tempfile.TemporaryDirectory() block.
def write_and_read(rows, fieldnames):
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           path = Path(tmp_dir) / "out.csv"
    #           with open(path, "w", newline="") as f:
    #               writer = csv.DictWriter(f, fieldnames=fieldnames)
    #               writer.writeheader()
    #               writer.writerows(rows)
    #           with open(path) as f:
    #               reader = csv.DictReader(f)
    #               return [row for row in reader]
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — the newline="" gotcha. Write write_raw_lines(rows, fieldnames)
# that does the exact same write as Exercise 1 (DictWriter + writeheader +
# writerows) into a TemporaryDirectory(), but returns the file's RAW bytes
# (read with Path(path).read_bytes()) so the check below can confirm the
# line endings are not doubled. Must still open with newline="" to pass —
# the whole point of this exercise is to prove that detail matters, not to
# skip it.
def write_raw_lines(rows, fieldnames):
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           path = Path(tmp_dir) / "out.csv"
    #           with open(path, "w", newline="") as f:
    #               writer = csv.DictWriter(f, fieldnames=fieldnames)
    #               writer.writeheader()
    #               writer.writerows(rows)
    #           return path.read_bytes()
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — extrasaction="ignore" for a dict with an extra key that isn't
# in fieldnames. Write write_with_extra(rows, fieldnames) that writes `rows`
# (one of which has a key not present in `fieldnames`) using
# DictWriter(f, fieldnames=fieldnames, extrasaction="ignore"), then reads
# the result back with csv.DictReader and returns the rows as a list of
# dicts. Without extrasaction="ignore" this would raise ValueError instead.
def write_with_extra(rows, fieldnames):
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           path = Path(tmp_dir) / "out.csv"
    #           with open(path, "w", newline="") as f:
    #               writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    #               writer.writeheader()
    #               writer.writerows(rows)
    #           with open(path) as f:
    #               reader = csv.DictReader(f)
    #               return [row for row in reader]
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    rows = [
        {"city": "Hanoi", "amount": 120},
        {"city": "Hue", "amount": 45},
    ]
    result = write_and_read(rows, ["city", "amount"])
    return result == [
        {"city": "Hanoi", "amount": "120"},
        {"city": "Hue", "amount": "45"},
    ]


def _ex2():
    rows = [{"city": "Hanoi", "amount": 120}]
    raw = write_raw_lines(rows, ["city", "amount"])
    if raw is None:
        return False
    # csv's own line ending is \r\n; newline="" must keep it that way,
    # not double it into \r\r\n.
    return b"\r\r\n" not in raw and b"\r\n" in raw


def _ex3():
    rows = [
        {"city": "Hanoi", "amount": 120, "note": "q3"},  # "note" is not in fieldnames
        {"city": "Hue", "amount": 45, "note": "q3"},
    ]
    result = write_with_extra(rows, ["city", "amount"])
    return result == [
        {"city": "Hanoi", "amount": "120"},
        {"city": "Hue", "amount": "45"},
    ]


results = [
    check("Ex 1: writeheader()+writerows() round-trips through DictReader", _ex1),
    check("Ex 2: newline=\"\" keeps csv's own line endings from doubling", _ex2),
    check("Ex 3: extrasaction=\"ignore\" drops a key not in fieldnames", _ex3),
]
print("\nAll green — lesson 66 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
