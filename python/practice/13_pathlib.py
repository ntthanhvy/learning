# Practice 13 — pathlib
# Run:  cd ~/learning/python && uv run python3 practice/13_pathlib.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# This lesson needs real files on disk to check .exists()/.glob() honestly,
# so — same "write my own fixtures" approach Day 6/9/10's practice files
# used — this file builds a small throwaway directory with tempfile.mkdtemp()
# at startup and writes a few files into it below. Nothing here touches any
# existing fixture file, and nothing extra is added under practice/ itself.

import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Fixture setup — don't edit. Builds a scratch directory:
#   <tmp>/                  (empty at first — Ex 2 creates a file inside it)
#   <tmp>/reports/sales.csv
#   <tmp>/reports/notes.txt
#   <tmp>/reports/archive/old_sales.csv
_tmp = Path(tempfile.mkdtemp(prefix="py13_"))

_reports = _tmp / "reports"
_reports.mkdir(parents=True, exist_ok=True)
(_reports / "sales.csv").write_text("city,amount\nHanoi,100\n")
(_reports / "notes.txt").write_text("just a note, not a csv\n")

_archive = _reports / "archive"
_archive.mkdir(parents=True, exist_ok=True)
(_archive / "old_sales.csv").write_text("city,amount\nHue,50\n")


# ---------------------------------------------------------------------------
# Exercise 1 — join two path pieces with the / operator.
# Given a directory Path and a filename string, return the joined Path —
# do NOT use string concatenation (no "+", no f-strings for this).
def join_path(directory, filename):
    ...                              # TODO:
    # return directory / filename


# ---------------------------------------------------------------------------
# Exercise 2 — .exists() / .is_file() on a file this script creates itself.
# Create a file at (_tmp / "created_by_ex2.txt") with .write_text("hi\n"),
# then return a tuple (existed_before, is_file_after) where existed_before
# is whether the path existed BEFORE you created it, and is_file_after is
# whether .is_file() is True after you created it.
def create_and_check(tmp_dir):
    ...                              # TODO:
    # target = tmp_dir / "created_by_ex2.txt"
    # existed_before = target.exists()
    # target.write_text("hi\n")
    # is_file_after = target.is_file()
    # return (existed_before, is_file_after)


# ---------------------------------------------------------------------------
# Exercise 3 — .write_text() / .read_text() round trip.
# Write `content` to `path` with .write_text(), then read it back with
# .read_text() and return what you read — should equal `content` exactly.
def round_trip(path, content):
    ...                              # TODO:
    # path.write_text(content)
    # return path.read_text()


# ---------------------------------------------------------------------------
# Exercise 4 — .glob() pattern matching against the fixture directory.
# The fixture built _reports/sales.csv, _reports/notes.txt, and
# _reports/archive/old_sales.csv. Return a sorted list of `.name` strings
# for every *.csv file found DIRECTLY inside `reports_dir` (NOT its "archive"
# subfolder — plain .glob(), not .rglob()).
def csv_names_one_level(reports_dir):
    ...                              # TODO:
    # return sorted(p.name for p in reports_dir.glob("*.csv"))


# ---------------------------------------------------------------------------
# Exercise 5 — decompose a path into .name / .stem / .suffix.
# Given a Path, return a tuple (name, stem, suffix) — no string slicing.
def decompose(path):
    ...                              # TODO:
    # return (path.name, path.stem, path.suffix)


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: join_path() uses / to join a directory and a filename",
          lambda: join_path(Path("data"), "sales.csv") == Path("data/sales.csv")),
    check("Ex 2: create_and_check() creates a file and confirms it exists after",
          lambda: create_and_check(_tmp) == (False, True)),
    check("Ex 3: round_trip() writes then reads back the same text",
          lambda: round_trip(_tmp / "roundtrip.txt", "hello pathlib\n") == "hello pathlib\n"),
    check("Ex 4: csv_names_one_level() finds only the top-level *.csv, not archive/'s",
          lambda: csv_names_one_level(_reports) == ["sales.csv"]),
    check("Ex 5: decompose() splits a path into (name, stem, suffix)",
          lambda: decompose(Path("data/raw/sales.csv")) == ("sales.csv", "sales", ".csv")),
]

print("\nAll green — lesson 13 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
