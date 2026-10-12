# Practice 75 — review day 12: retrieval across Days 72-74
# Run:  cd ~/learning/python && uv run python3 practice/75_review_retrieval_day_12.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 72, 73, and 74.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import configparser
import pickle
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Order:
    city: str
    amount: float


# ---------------------------------------------------------------------------
# Exercise 1 (Day 72 — pickle: round-trip a dataclass instance through
# pickle.dumps()/loads() and confirm the restored copy is equal to the
# original but is NOT the same object)
def roundtrip_equal_but_new(order):
    """Return a tuple (equal, same) where:
    equal is True if pickle.loads(pickle.dumps(order)) == order
    same is True if that round-tripped copy IS the original object
    (this should come back False — pickle always builds a new object)."""
    # TODO: restored = pickle.loads(pickle.dumps(order))
    #       return (restored == order, restored is order)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 73 — concurrent.futures: ThreadPoolExecutor.map() runs
# several slow I/O-bound calls concurrently instead of one after another)
def slow_call(n):
    time.sleep(0.3)
    return n * n


def concurrent_calls(items):
    """Run slow_call across `items` using ThreadPoolExecutor(max_workers=
    len(items)).map(), inside a `with` block, and return the results as a
    list (map() returns an iterator — wrap it in list())."""
    # TODO: with ThreadPoolExecutor(max_workers=len(items)) as pool:
    #           return list(pool.map(slow_call, items))
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 74 — uuid & configparser: write a ConfigParser section to
# a file, then read a typed int AND a non-"True" boolean spelling back)
def write_and_read_settings(path):
    """Build a configparser.ConfigParser(), set:
      config["database"] = {"port": "5432"}
      config["app"] = {"debug": "yes"}        (note: "yes", not "True")
    Write it to `path` by opening it "w" and calling config.write(f).
    Then build a FRESH ConfigParser, read the file back with
    reader.read(path), and return a tuple:
      (reader.getint("database", "port"), reader.getboolean("app", "debug"))
    """
    # TODO: config = configparser.ConfigParser()
    #       config["database"] = {"port": "5432"}
    #       config["app"] = {"debug": "yes"}
    #       with open(path, "w") as f:
    #           config.write(f)
    #       reader = configparser.ConfigParser()
    #       reader.read(path)
    #       return (reader.getint("database", "port"),
    #               reader.getboolean("app", "debug"))
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
    order = Order("Da Nang", 42.0)
    result = roundtrip_equal_but_new(order)
    if result is None:
        return False
    equal, same = result
    return equal is True and same is False


def _ex2_correctness():
    items = [1, 2, 3]
    result = concurrent_calls(items)
    if result is None:
        return False
    return result == [1, 4, 9]


def _ex2_speed():
    items = [0, 1, 2, 3, 4]
    start = time.perf_counter()
    for n in items:
        slow_call(n)
    sequential_elapsed = time.perf_counter() - start

    start = time.perf_counter()
    concurrent_calls(items)
    concurrent_elapsed = time.perf_counter() - start

    # five 0.3s calls: sequential ~1.5s, concurrent ~0.3s -- concurrent
    # should be well under half the sequential time.
    return concurrent_elapsed < (sequential_elapsed / 2)


def _ex3():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "settings.ini"
        result = write_and_read_settings(path)
    if result is None:
        return False
    port, debug = result
    return port == 5432 and isinstance(port, int) and debug is True


results = [
    check("Ex 1 (Day 72): a pickled copy round-trips equal but is a new object", _ex1),
    check("Ex 2a (Day 73): concurrent_calls() matches the plain-loop result", _ex2_correctness),
    check("Ex 2b (Day 73): ThreadPoolExecutor.map() is meaningfully faster", _ex2_speed),
    check("Ex 3 (Day 74): getint() and getboolean() read typed values back", _ex3),
]

print("\nAll green — lesson 75 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
