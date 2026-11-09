# Practice 103 — review day 19: retrieval across Days 100-102
# Run:  cd ~/learning/python && uv run python3 practice/103_review_retrieval_day_19.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 100, 101, and 102.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import array
import importlib
import importlib.util
import timeit


# ---------------------------------------------------------------------------
# Exercise 1 (Day 100 — timeit: use setup= so the timed total excludes data
# construction, and read the minimum out of a timeit.repeat() list)
def time_sorted(data_setup, number):
    """Time "sorted(data)" using timeit.timeit(), with data_setup as the
    setup= code that builds `data` once, excluded from the timed total.
    Return the total elapsed seconds as a float."""
    # TODO: return timeit.timeit("sorted(data)", setup=data_setup, number=number)
    ...


def best_of_repeats(stmt, setup, number, repeat):
    """Call timeit.repeat(stmt, setup=setup, number=number, repeat=repeat)
    and return the minimum value from the resulting list — the trustworthy
    statistic, since it sits closest to a noise-free run."""
    # TODO: totals = timeit.repeat(stmt, setup=setup, number=number, repeat=repeat)
    #       return min(totals)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 101 — importlib: load a module by a runtime string name,
# and check importability first with find_spec() instead of catching an
# exception)
def load_and_call(module_name, func_name, *args):
    """Load module_name with importlib.import_module(), look up func_name
    on it with getattr(), and call it with *args. Return the result."""
    # TODO: mod = importlib.import_module(module_name)
    #       func = getattr(mod, func_name)
    #       return func(*args)
    ...


def importable(module_name):
    """Return True if module_name could be imported (find_spec() is not
    None), False otherwise -- without ever raising an exception, and
    without actually importing the module's code."""
    # TODO: return importlib.util.find_spec(module_name) is not None
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 102 — array: build a typed array and catch the TypeError
# a mismatched-type value raises on append)
def build_typed(typecode, values):
    """Return the array.array built from typecode and values."""
    # TODO: return array.array(typecode, values)
    ...


def try_append(arr, value):
    """Try appending value to a *copy* of arr (array.array(arr.typecode,
    arr), so the caller's array is never mutated). Return True if it
    succeeds, False if it raises TypeError."""
    # TODO: copy = array.array(arr.typecode, arr)
    #       try:
    #           copy.append(value)
    #           return True
    #       except TypeError:
    #           return False
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
    total = time_sorted("data = list(range(1000, 0, -1))", number=100)
    if not (isinstance(total, float) and total > 0):
        return False
    best = best_of_repeats("sorted(data)", "data = list(range(500, 0, -1))", number=50, repeat=3)
    return isinstance(best, float) and best > 0


def _ex2():
    result = load_and_call("statistics", "mean", [1, 2, 3, 4])
    return result == 2.5 and importable("os") is True and importable("definitely_not_a_real_module_xyz") is False


def _ex3():
    arr = build_typed("i", [1, 2, 3])
    if not (isinstance(arr, array.array) and arr.typecode == "i" and list(arr) == [1, 2, 3]):
        return False
    ok_int = try_append(arr, 4)
    ok_float = try_append(arr, 3.5)
    unchanged = list(arr) == [1, 2, 3]
    return ok_int is True and ok_float is False and unchanged


results = [
    check("Ex 1 (Day 100): timeit setup= excludes construction; repeat() min is trustworthy", _ex1),
    check("Ex 2 (Day 101): import_module()/getattr() dispatch and find_spec() check cleanly", _ex2),
    check("Ex 3 (Day 102): build_typed() works and try_append() reports True/False, never raises", _ex3),
]

print("\nAll green — lesson 103 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
