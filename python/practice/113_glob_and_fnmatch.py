# Practice 113 — glob & fnmatch: filename pattern matching
# Run:  cd ~/learning/python && uv run python3 practice/113_glob_and_fnmatch.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# This file builds its own small, temporary directory tree (cleaned up at the
# end) so the exercises have something real to search.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import shutil
import tempfile
from fnmatch import fnmatch
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 (Day 113 — Path.glob: top-level matches only, one directory deep)
def top_level_csvs(root):
    """Given a Path to a directory, return a sorted list of the *names*
    (strings, not full paths) of every *.csv file directly inside root —
    not inside any subdirectory of root."""
    # TODO: return sorted(p.name for p in root.glob("*.csv"))
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 113 — Path.rglob: the same pattern, every depth)
def all_csvs(root):
    """Given a Path to a directory, return a sorted list of every *.csv
    file's path *relative to root* (as strings), at any depth including
    nested subdirectories."""
    # TODO: return sorted(str(p.relative_to(root)) for p in root.rglob("*.csv"))
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 113 — fnmatch: filtering a plain list of name strings,
# no filesystem involved)
def matching_names(names, pattern):
    """Given a list of filename strings and a glob-style pattern, return a
    new list containing only the names that match the pattern according to
    fnmatch.fnmatch(), preserving input order."""
    # TODO: return [n for n in names if fnmatch(n, pattern)]
    ...


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _build_tree(tmp):
    root = Path(tmp) / "logs"
    (root / "archive").mkdir(parents=True)
    (root / "app.csv").write_text("a\n")
    (root / "2024.csv").write_text("b\n")
    (root / "notes.txt").write_text("c\n")
    (root / "archive" / "old.csv").write_text("d\n")
    return root


def _ex1(root):
    return top_level_csvs(root) == ["2024.csv", "app.csv"]


def _ex2(root):
    return all_csvs(root) == [
        "2024.csv",
        "app.csv",
        "archive/old.csv",
    ]


def _ex3():
    names = ["report_2024.csv", "report_2024.tmp", "README.md", "report_9.csv"]
    return matching_names(names, "report_*.csv") == [
        "report_2024.csv",
        "report_9.csv",
    ]


tmp_dir = tempfile.mkdtemp(prefix="py113_")
try:
    tree_root = _build_tree(tmp_dir)
    results = [
        check("Ex 1 (Day 113): Path.glob() stays one level deep", lambda: _ex1(tree_root)),
        check("Ex 2 (Day 113): Path.rglob() finds every depth", lambda: _ex2(tree_root)),
        check("Ex 3 (Day 113): fnmatch() filters a plain name list by wildcard pattern", _ex3),
    ]
finally:
    shutil.rmtree(tmp_dir, ignore_errors=True)

print("\nAll green — lesson 113 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
