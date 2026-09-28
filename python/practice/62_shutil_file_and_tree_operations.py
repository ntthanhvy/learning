# Practice 62 — shutil: copying, moving & removing whole file trees
# Run:  cd ~/learning/python && uv run python3 practice/62_shutil_file_and_tree_operations.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import shutil
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 — copy a single file, leaving the original untouched.
# Write copy_file(src, dst) that copies src to dst using shutil, preserving
# content. Return value is ignored by the checks below.
def copy_file(src, dst):
    # TODO: shutil.copy(src, dst)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — copy a whole directory tree.
# Write copy_tree(src_dir, dst_dir) that recursively copies src_dir (and
# everything inside it, including subdirectories) to dst_dir. dst_dir does
# NOT exist yet when this is called.
def copy_tree(src_dir, dst_dir):
    # TODO: shutil.copytree(src_dir, dst_dir)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — move a directory to a new location.
# Write move_tree(src_dir, dst_dir) that moves src_dir (and everything
# inside it) to dst_dir. After this runs, src_dir must no longer exist.
def move_tree(src_dir, dst_dir):
    # TODO: shutil.move(src_dir, dst_dir)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — remove a directory tree entirely.
# Write remove_tree(path) that deletes path and everything inside it.
def remove_tree(path):
    # TODO: shutil.rmtree(path)
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
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / "report.csv"
        dst = Path(d) / "backup" / "report.csv"
        dst.parent.mkdir()
        src.write_text("city,amount\nHanoi,120\n")
        copy_file(src, dst)
        return (
            dst.exists()
            and dst.read_text() == src.read_text()
            and src.exists()  # original untouched
        )


def _ex2():
    with tempfile.TemporaryDirectory() as d:
        src_dir = Path(d) / "raw"
        (src_dir / "nested").mkdir(parents=True)
        (src_dir / "a.txt").write_text("a")
        (src_dir / "nested" / "b.txt").write_text("b")
        dst_dir = Path(d) / "raw_backup"
        copy_tree(src_dir, dst_dir)
        return (
            (dst_dir / "a.txt").read_text() == "a"
            and (dst_dir / "nested" / "b.txt").read_text() == "b"
            and (src_dir / "a.txt").exists()  # original tree untouched
        )


def _ex3():
    with tempfile.TemporaryDirectory() as d:
        src_dir = Path(d) / "processed"
        src_dir.mkdir()
        (src_dir / "out.txt").write_text("done")
        dst_dir = Path(d) / "archive" / "processed"
        (Path(d) / "archive").mkdir()
        move_tree(src_dir, dst_dir)
        return (
            not src_dir.exists()
            and (dst_dir / "out.txt").read_text() == "done"
        )


def _ex4():
    with tempfile.TemporaryDirectory() as d:
        scratch = Path(d) / "scratch"
        (scratch / "nested").mkdir(parents=True)
        (scratch / "nested" / "tmp.txt").write_text("x")
        remove_tree(scratch)
        return not scratch.exists() and Path(d).exists()  # parent survives


results = [
    check("Ex 1: copy_file copies content, leaves the original in place", _ex1),
    check("Ex 2: copy_tree recursively copies a nested directory", _ex2),
    check("Ex 3: move_tree relocates a directory, removing the source", _ex3),
    check("Ex 4: remove_tree deletes a directory and everything inside it", _ex4),
]
print("\nAll green — lesson 62 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
