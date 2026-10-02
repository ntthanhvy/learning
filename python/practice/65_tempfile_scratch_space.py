# Practice 65 — tempfile: scratch space that cleans itself up
# Run:  cd ~/learning/python && uv run python3 practice/65_tempfile_scratch_space.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 — stage a file inside a TemporaryDirectory() and hand back
# what was written, from INSIDE the with block (the directory is gone the
# moment the block exits, so reading it after exiting would fail).
# Write stage_and_read(content) that creates a TemporaryDirectory(), writes
# `content` to a file named "staged.csv" inside it, reads that file back,
# and returns the text it read.
def stage_and_read(content):
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           p = Path(tmp_dir) / "staged.csv"
    #           p.write_text(content)
    #           return p.read_text()
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — write with NamedTemporaryFile(delete=False), then clean up
# by hand. Write write_named_temp(content) that opens a NamedTemporaryFile
# in text mode with delete=False, writes `content`, and returns the file's
# path (f.name) as a string. The file must still exist on disk after this
# function returns (delete=False keeps it there until Exercise 3 removes it).
def write_named_temp(content):
    # TODO: with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
    #           f.write(content)
    #           return f.name
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — clean up a NamedTemporaryFile(delete=False) path by hand.
# Write cleanup_named_temp(path) that deletes the file at `path` and
# returns True if it no longer exists afterward.
def cleanup_named_temp(path):
    # TODO: Path(path).unlink()
    #       return not Path(path).exists()
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — stage several files in one temporary directory, then
# aggregate them (the shape a real ETL staging step takes).
# Write stage_and_sum(amounts) that creates ONE TemporaryDirectory(),
# writes each amount in `amounts` to its own file inside it (one int per
# file, as text), then reads every file back and returns the sum of all
# the values — all from inside the same with block.
def stage_and_sum(amounts):
    # TODO: with tempfile.TemporaryDirectory() as tmp_dir:
    #           tmp_path = Path(tmp_dir)
    #           for i, amount in enumerate(amounts):
    #               (tmp_path / f"{i}.txt").write_text(str(amount))
    #           return sum(int(p.read_text()) for p in tmp_path.iterdir())
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
    return stage_and_read("id,amount\n1,10\n") == "id,amount\n1,10\n"


def _ex2_and_3():
    path = write_named_temp("hello scratch")
    if path is None or not Path(path).exists():
        return False
    if Path(path).read_text() != "hello scratch":
        return False
    return cleanup_named_temp(path) is True


def _ex4():
    return stage_and_sum([10, 20, 30]) == 60


def _ex_no_collision():
    # Two separate TemporaryDirectory() calls must never hand back the same
    # path -- the whole point of letting tempfile pick the name.
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        return a != b


results = [
    check("Ex 1: stage_and_read writes and reads back inside the with block", _ex1),
    check("Ex 2+3: NamedTemporaryFile(delete=False) then manual cleanup", _ex2_and_3),
    check("Ex 4: stage_and_sum stages several files in one dir and aggregates", _ex4),
    check("Bonus: two TemporaryDirectory() calls never collide on a name", _ex_no_collision),
]
print("\nAll green — lesson 65 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
