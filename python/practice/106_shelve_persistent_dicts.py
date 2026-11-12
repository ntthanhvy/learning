# Practice 106 — shelve: a dict that survives the process ending
# Run:  cd ~/learning/python && uv run python3 practice/106_shelve_persistent_dicts.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import os
import shelve
import tempfile
from dataclasses import dataclass


@dataclass
class Order:
    city: str
    amount: float


# ---------------------------------------------------------------------------
# Exercise 1 — write a value, close the shelf, re-open it, read it back.
# Write roundtrip_value(path, key, value) that:
#   - opens the shelf at `path`, stores value under key, and closes it
#     (use a `with shelve.open(path) as db:` block)
#   - opens the shelf at `path` again (a fresh `with` block) and returns
#     db[key] from that second, separate open.
def roundtrip_value(path, key, value):
    # TODO:
    # with shelve.open(path) as db:
    #     db[key] = value
    # with shelve.open(path) as db:
    #     return db[key]
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — store a dataclass instance as a value and read it back intact.
# Write store_order(path, key, order) that opens the shelf at `path`, stores
# `order` under `key`, closes it, re-opens the shelf, and returns the value
# read back under `key` — should be an Order, equal to the original.
def store_order(path, key, order):
    # TODO:
    # with shelve.open(path) as db:
    #     db[key] = order
    # with shelve.open(path) as db:
    #     return db[key]
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — confirm a missing key raises KeyError, just like a plain dict.
# Write raises_keyerror(path, missing_key) that opens the shelf at `path`
# and returns True if db[missing_key] raises KeyError, False otherwise.
def raises_keyerror(path, missing_key):
    # TODO:
    # with shelve.open(path) as db:
    #     try:
    #         db[missing_key]
    #         return False
    #     except KeyError:
    #         return True
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — reproduce the writeback=True fix for in-place mutation.
# Write append_tag_with_writeback(path, key, tag) that:
#   - opens the shelf at `path` with writeback=True
#   - appends `tag` to the list stored under key (db[key] is a dict with a
#     "tags" list inside it, e.g. {"tags": ["a", "b"]})
#   - closes that shelf (so the change is written back on close)
#   - opens the shelf again (a fresh, plain open with no writeback=True) and
#     returns the "tags" list read back from under `key`
def append_tag_with_writeback(path, key, tag):
    # TODO:
    # with shelve.open(path, writeback=True) as db:
    #     db[key]["tags"].append(tag)
    # with shelve.open(path) as db:
    #     return db[key]["tags"]
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


def _with_tmp_shelf_path(fn):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "shelf")
        return fn(path)


def _ex1():
    def run(path):
        result = roundtrip_value(path, "greeting", "hello")
        return result == "hello"
    return _with_tmp_shelf_path(run)


def _ex2():
    def run(path):
        order = Order("Hanoi", 120.0)
        result = store_order(path, "o1", order)
        if result is None:
            return False
        return result == order and isinstance(result, Order)
    return _with_tmp_shelf_path(run)


def _ex3():
    def run(path):
        with shelve.open(path) as db:
            db["present"] = 1
        return raises_keyerror(path, "absent")
    return _with_tmp_shelf_path(run)


def _ex4():
    def run(path):
        with shelve.open(path) as db:
            db["rec"] = {"tags": ["a", "b"]}
        result = append_tag_with_writeback(path, "rec", "c")
        if result is None:
            return False
        return list(result) == ["a", "b", "c"]
    return _with_tmp_shelf_path(run)


results = [
    check("Ex 1: a value survives a close/reopen round trip", _ex1),
    check("Ex 2: a dataclass instance round-trips through a shelf", _ex2),
    check("Ex 3: a missing key raises KeyError, like a plain dict", _ex3),
    check("Ex 4: writeback=True persists in-place mutation of a value", _ex4),
]
print("\nAll green — lesson 106 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
