# Practice 121 — tracemalloc: watching where memory actually goes
# Run:  cd ~/learning/python && uv run python3 practice/121_tracemalloc.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import inspect

import tracemalloc


# ---------------------------------------------------------------------------
# Exercise 1 — take a before/after snapshot pair and read the top diff line.
# Write snapshot_growth(fn) that: starts tracing if it isn't already, takes
# a snapshot, calls fn() (ignoring its return value), takes a second
# snapshot, and returns the .lineno of the top entry of
# second.compare_to(first, "lineno")[0].traceback[0].
def snapshot_growth(fn):
    # TODO: if not tracemalloc.is_tracing(): tracemalloc.start()
    # before = tracemalloc.take_snapshot()
    # fn()
    # after = tracemalloc.take_snapshot()
    # top = after.compare_to(before, "lineno")[0]
    # return top.traceback[0].lineno
    pass


def _line_marker():
    return [i for i in range(10000)]  # noqa: this line's number is the answer


# ---------------------------------------------------------------------------
# Exercise 2 — confirm a leaking accumulator's growth scales with call count.
# Write leaked_length(call_count) that calls add_item(i, ...) in a fresh
# accumulator function `call_count` times (reusing the SAME default-arg
# function object across all calls, the Day 1 trap) and returns
# len(add_item.__defaults__[0]) afterward.
def add_item(item, basket=[]):
    basket.append(item)
    return basket


def leaked_length(call_count):
    # TODO: call add_item(i) for i in range(call_count), then return
    # len(add_item.__defaults__[0])
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — read current/peak memory before and after reset_peak().
# Write peak_equals_current_after_reset() that: ensures tracing is on,
# allocates something sizeable, reads (current, peak) once, calls
# tracemalloc.reset_peak(), reads (current2, peak2) again, and returns
# True only if peak2 == current2 (reset_peak's documented effect).
def peak_equals_current_after_reset():
    # TODO: if not tracemalloc.is_tracing(): tracemalloc.start()
    # _ = [0] * 1_000_000
    # current, peak = tracemalloc.get_traced_memory()
    # tracemalloc.reset_peak()
    # current2, peak2 = tracemalloc.get_traced_memory()
    # return peak2 == current2
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
    # _line_marker's body is one real statement, one line below its own `def` —
    # computed relative to the function's own source line, not hardcoded, so
    # this check stays correct no matter where the file gets edited above it.
    expected_line = inspect.getsourcelines(_line_marker)[1] + 1
    line = snapshot_growth(_line_marker)
    return line == expected_line


def _ex2():
    add_item.__defaults__[0].clear()
    return leaked_length(500) == 500


def _ex3():
    return peak_equals_current_after_reset() is True


results = [
    check("Ex 1: snapshot_growth reports the top allocating line number", _ex1),
    check("Ex 2: leaked_length confirms the shared default keeps growing", _ex2),
    check("Ex 3: peak_equals_current_after_reset resets the running peak", _ex3),
]
print("\nAll green — lesson 121 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
