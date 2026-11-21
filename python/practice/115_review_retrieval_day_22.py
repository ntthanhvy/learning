# Practice 115 — review day 22: retrieval across Days 112-114
# Run:  cd ~/learning/python && uv run python3 practice/115_review_retrieval_day_22.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 112, 113, and 114.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import shlex
import tempfile
import threading
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 (Day 112 — threading.Lock: several threads safely bumping one
# shared counter, using `with lock:` so the final total is exactly right
# every time, not a near-miss from a lost update)
def run_locked_counter(num_threads, bumps_each):
    """Start `num_threads` threads that each increment a shared counter
    `bumps_each` times, protecting every read-then-write with a single
    shared threading.Lock via `with lock:`. Return the final counter
    value, which must equal num_threads * bumps_each exactly."""
    counter = 0
    lock = threading.Lock()

    def bump():
        nonlocal counter
        for _ in range(bumps_each):
            # TODO: protect this read-then-write with `with lock:`
            # with lock:
            #     counter += 1
            ...

    threads = [threading.Thread(target=bump) for _ in range(num_threads)]
    # TODO: start every thread, then join every thread, then return counter
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 113 — glob & fnmatch: Path.rglob() finding a pattern at
# every depth that a plain Path.glob() misses one level down)
def find_csvs(root):
    """Given a Path to a directory, return a sorted list of `.name` strings
    for every *.csv file at ANY depth under root (not just the top level) --
    use Path.rglob(), not glob()."""
    # TODO: return sorted(p.name for p in root.rglob("*.csv"))
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 114 — shlex: round-tripping a command string through
# split() and back through join())
def round_trip(command_line):
    """Given one command-line-shaped string, split it into an argv list
    with shlex.split(), then rebuild a shell-safe string from that list
    with shlex.join(). Return (argv, rebuilt) -- splitting `rebuilt` again
    must reproduce the same argv list exactly."""
    # TODO: argv = shlex.split(command_line)
    #       rebuilt = shlex.join(argv)
    #       return argv, rebuilt
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


def _ex1():
    total = run_locked_counter(4, 2000)
    return total == 8000


def _ex2():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "app.csv").write_text("a")
        (root / "notes.txt").write_text("b")
        nested = root / "archive"
        nested.mkdir()
        (nested / "old.csv").write_text("c")
        return find_csvs(root) == ["app.csv", "old.csv"]


def _ex3():
    argv, rebuilt = round_trip('cp "my file.txt" /tmp/backup --verbose')
    return (
        argv == ["cp", "my file.txt", "/tmp/backup", "--verbose"]
        and shlex.split(rebuilt) == argv
    )


if __name__ == "__main__":
    results = [
        check("Ex 1 (Day 112): threading.Lock keeps a multi-thread counter exact", _ex1),
        check("Ex 2 (Day 113): Path.rglob() finds a *.csv at every depth", _ex2),
        check("Ex 3 (Day 114): shlex.split()/join() round-trip an argv list", _ex3),
    ]

    print("\nAll green — lesson 115 done. 🎉" if all(results)
          else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
