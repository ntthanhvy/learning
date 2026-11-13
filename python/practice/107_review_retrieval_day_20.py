# Practice 107 — review day 20: retrieval across Days 104-106
# Run:  cd ~/learning/python && uv run python3 practice/107_review_retrieval_day_20.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 104, 105, and 106.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import locale
import shelve
import tempfile
import types
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Exercise 1 (Day 104 — types.SimpleNamespace: build one from keywords, and
# catch the AttributeError a missing attribute raises)
def make_namespace(**kwargs):
    """Return a types.SimpleNamespace built from the given keyword arguments."""
    # TODO: return types.SimpleNamespace(**kwargs)
    ...


def read_or_default(ns, name, default):
    """Return getattr(ns, name) if it exists, else default -- without ever
    letting an AttributeError escape this function."""
    # TODO: try:
    #           return getattr(ns, name)
    #       except AttributeError:
    #           return default
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 105 — locale: set en_US.UTF-8 and group a number with
# locale.format_string(), remembering grouping=True is required)
def grouped_number(n):
    """Set the en_US.UTF-8 locale (LC_ALL) and return locale.format_string()
    formatting n as "%d" with thousands grouping turned on."""
    # TODO: locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    #       return locale.format_string("%d", n, grouping=True)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 106 — shelve: a value survives a close/reopen round trip,
# and writeback=True fixes in-place mutation of a stored list)
def round_trip(path, key, value):
    """Open a shelf at path, store value under key, close it (use a `with`
    block), then open a brand-new shelf at the same path and return the
    value read back under that same key."""
    # TODO: with shelve.open(path) as db:
    #           db[key] = value
    #       with shelve.open(path) as db:
    #           return db[key]
    ...


def append_with_writeback(path, key, item):
    """Open the shelf at path with writeback=True, append item to the
    "tags" list inside the dict stored under key, close it, then open a
    plain (writeback=False) shelf at the same path and return the dict
    read back under that key -- proving the append really did persist
    this time."""
    # TODO: with shelve.open(path, writeback=True) as db:
    #           db[key]["tags"].append(item)
    #       with shelve.open(path) as db:
    #           return db[key]
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
    ns = make_namespace(name="Ada", age=30)
    if not (isinstance(ns, types.SimpleNamespace) and ns.name == "Ada" and ns.age == 30):
        return False
    present = read_or_default(ns, "name", "nobody")
    missing = read_or_default(ns, "nickname", "nobody")
    return present == "Ada" and missing == "nobody"


def _ex2():
    try:
        result = grouped_number(1234567)
    except locale.Error:
        return None  # environment lacks en_US.UTF-8 -- skip rather than fail
    return result == "1,234,567"


@dataclass
class Order:
    city: str
    amount: float


def _ex3():
    with tempfile.TemporaryDirectory() as tmp:
        shelf_path = tmp + "/recs"
        got = round_trip(shelf_path, "o1", Order("Hanoi", 120.0))
        if got != Order("Hanoi", 120.0):
            return False

        wb_path = tmp + "/wb"
        with shelve.open(wb_path) as db:
            db["rec"] = {"tags": ["a", "b"]}
        tags = append_with_writeback(wb_path, "rec", "c")
        return tags == {"tags": ["a", "b", "c"]}


_r2 = _ex2()
results = [
    check("Ex 1 (Day 104): SimpleNamespace built and AttributeError caught with a default", _ex1),
    True if _r2 is None else check("Ex 2 (Day 105): locale.format_string() groups thousands correctly", lambda: _r2),
    check("Ex 3 (Day 106): shelve round trip survives reopen; writeback=True persists a mutation", _ex3),
]
if _r2 is None:
    print("… (Ex 2 skipped — en_US.UTF-8 locale not installed in this environment)")

print("\nAll green — lesson 107 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
