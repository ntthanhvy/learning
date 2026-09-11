# Practice 45 — review day 3: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/45_review_retrieval_day_3.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 4, 6, 9, 13,
# 20, and 36. Replace each `...` (or the marked TODO body) and re-run until
# every check prints ✓. Try each from memory before reopening the old lesson.
#
# Exercise 5 tests the same *rule* Day 20 taught (a blocking call inside
# async def never yields control back to the event loop) using plain
# asyncio functions timed against each other, rather than running a real
# FastAPI app, so this file stays standard-library-only.

import asyncio
import time
from collections import Counter
from functools import lru_cache
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 (Day 4 — functions, key=: sorted() calls key once per item)
# Sort `rows` (a list of dicts) by the "amount" field, descending, using
# sorted()'s key= argument — do not compare whole dicts directly.
def sort_by_amount_desc(rows):
    # TODO: return sorted(rows, key=lambda r: r["amount"], reverse=True)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 6 — with: __exit__ still runs on exception)
# Given a small custom context manager that appends to `log` on enter/exit,
# run `raiser()` inside a `with` block using that context manager, catch
# the exception it raises, and return `log` — proving __exit__ still ran
# even though the body raised.
class Tracker:
    def __init__(self, log):
        self.log = log

    def __enter__(self):
        self.log.append("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.log.append("exit")
        return True  # suppress the exception so the function can return cleanly


def with_survives_exception(log):
    def raiser():
        raise ValueError("boom")

    # TODO: with Tracker(log):
    #           raiser()
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 9 — modules: top-level code runs once, cached after that)
# Simulate "module top-level code" as a function that appends to `log` each
# time it actually runs, and a cache dict standing in for Python's own
# module cache. Calling `import_module` twice for the same name must only
# append to `log` on the FIRST call — the second must reuse the cache.
def import_module(name, log, cache):
    if name in cache:
        # TODO: already "imported" — do NOT run the module body again
        ...
    else:
        # TODO: run it for the first time, record it, and cache the result
        log.append(name)
        cache[name] = {"name": name}
        ...
    return cache[name]


# ---------------------------------------------------------------------------
# Exercise 4 (Day 13 — pathlib: / joins paths, the left operand decides)
# Build a Path for "data/raw/sales.csv" using ONLY the / operator, starting
# from Path("data") — no manual string concatenation.
def build_sales_path():
    # TODO: return Path("data") / "raw" / "sales.csv"
    ...


# ---------------------------------------------------------------------------
# Exercise 5 (Day 20 — async/await: a blocking call inside async def never
# yields control, silently serializing concurrent work)
# `good_task` awaits asyncio.sleep (yields control); `bad_task` calls the
# blocking time.sleep instead (never yields). Run THREE `good_task()` calls
# concurrently with asyncio.gather and return the elapsed time — it should
# be close to ONE task's duration, not three times that, because they
# overlap instead of serializing.
DELAY = 0.05


async def good_task():
    await asyncio.sleep(DELAY)


async def bad_task():
    time.sleep(DELAY)  # blocking — never yields control back to the loop


async def _time_three_concurrent(coro_fn):
    start = time.perf_counter()
    # TODO: await asyncio.gather(coro_fn(), coro_fn(), coro_fn())
    ...
    return time.perf_counter() - start


def three_concurrent_good_tasks_overlap():
    elapsed = asyncio.run(_time_three_concurrent(good_task))
    # overlapping: ~1x DELAY, not ~3x DELAY
    return elapsed < DELAY * 2


# ---------------------------------------------------------------------------
# Exercise 6 (Day 36 — functools: lru_cache is only safe on a pure function)
# slow_square must be decorated with @lru_cache so a repeat call with an
# argument already seen does NOT re-run the body (call_log stays length 1
# for two calls with the same argument).
call_log = []


# TODO: add @lru_cache(maxsize=None) directly above this def
def slow_square(n):
    call_log.append(n)
    return n * n


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex2_check():
    log = []
    with_survives_exception(log)
    return log == ["enter", "exit"]


def _ex3_check():
    log = []
    cache = {}
    import_module("parsing", log, cache)
    import_module("parsing", log, cache)
    return log == ["parsing"]


def _ex6_check():
    call_log.clear()
    slow_square(4)
    slow_square(4)
    slow_square(5)
    return call_log == [4, 5]


results = [
    check("Ex 1: sort_by_amount_desc orders rows by 'amount', descending",
          lambda: sort_by_amount_desc(
              [{"city": "Hanoi", "amount": 120}, {"city": "HCMC", "amount": 80},
               {"city": "Danang", "amount": 200}])
          == [{"city": "Danang", "amount": 200}, {"city": "Hanoi", "amount": 120},
              {"city": "HCMC", "amount": 80}]),
    check("Ex 2: with-block's __exit__ still runs even though the body raised",
          _ex2_check),
    check("Ex 3: a module's top-level code runs once, reused on the second import",
          _ex3_check),
    check("Ex 4: build_sales_path joins pieces with / into data/raw/sales.csv",
          lambda: build_sales_path() == Path("data") / "raw" / "sales.csv"),
    check("Ex 5: three good_task() calls run concurrently via asyncio.gather, not serially",
          three_concurrent_good_tasks_overlap),
    check("Ex 6: @lru_cache skips re-running slow_square for an argument already seen",
          _ex6_check),
]

# A quick, ungraded illustration companion to Exercise 1 — not itself checked,
# just confirms sorted()/Counter interplay from Day 4 still holds here too.
_counts = Counter(["Hanoi", "HCMC", "Hanoi"])
assert sorted(_counts.items(), key=lambda pair: pair[1], reverse=True)[0][0] == "Hanoi"

print("\nAll green — lesson 45 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
