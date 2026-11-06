# Practice 100 — timeit: benchmarking small code correctly
# Run:  cd ~/learning/python && uv run python3 practice/100_timeit_benchmarking.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import timeit


# ---------------------------------------------------------------------------
# Exercise 1 — time a snippet with timeit.timeit().
# Given a statement string and a number of repetitions, return the total
# elapsed seconds timeit.timeit() reports for running it that many times.
# (Just call timeit.timeit(stmt, number=number) and return the result.)
def time_snippet(stmt, number):
    # TODO: return timeit.timeit(stmt, number=number)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — use setup= so data construction isn't part of the timed total.
# Given a setup string (that defines a name) and a stmt string (that uses
# that name), time only stmt — not the setup — number times, and return the
# total elapsed seconds.
def time_with_setup(stmt, setup, number):
    # TODO: return timeit.timeit(stmt, setup=setup, number=number)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — compare two snippets and report which is faster.
# Given two statement strings (stmt_a, stmt_b) and a number of repetitions,
# time each one with timeit.timeit() and return "a" if stmt_a's total was
# strictly smaller, otherwise return "b".
def faster_of(stmt_a, stmt_b, number):
    # TODO: t_a = timeit.timeit(stmt_a, number=number)
    #       t_b = timeit.timeit(stmt_b, number=number)
    #       return "a" if t_a < t_b else "b"
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — trust the minimum of several repeated measurements.
# Given a statement string, a number of repetitions per measurement, and a
# repeat count, call timeit.repeat() with those settings and return the
# smallest total in the resulting list (the one closest to a noise-free
# run) — not the average, and not the last value.
def best_of_repeats(stmt, number, repeat):
    # TODO: totals = timeit.repeat(stmt, number=number, repeat=repeat)
    #       return min(totals)
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
    result = time_snippet("x = 1 + 1", 1000)
    return isinstance(result, float) and result >= 0


def _ex2():
    result = time_with_setup(
        "sorted(data)",
        "data = list(range(500, 0, -1))",
        200,
    )
    return isinstance(result, float) and result >= 0


def _ex3():
    # a trivial no-op beats a snippet that does real work, reliably enough
    # across repeated test runs to check the comparison logic itself.
    winner = faster_of("pass", "x = sum(range(10_000))", 200)
    return winner == "a"


def _ex4():
    totals = [timeit.repeat("x = 1 + 1", number=1000, repeat=5)]
    result = best_of_repeats("x = 1 + 1", 1000, 5)
    # the function's own answer must be a float no larger than every total
    # in an independently-taken sample of the same measurement.
    return isinstance(result, float) and all(result <= max(t) for t in totals)


results = [
    check("Ex 1: time_snippet() returns timeit's total elapsed seconds", _ex1),
    check("Ex 2: time_with_setup() excludes setup from the timed total", _ex2),
    check("Ex 3: faster_of() correctly names the faster snippet", _ex3),
    check("Ex 4: best_of_repeats() returns the minimum of repeat totals", _ex4),
]
print("\nAll green — lesson 100 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
