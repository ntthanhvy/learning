# Practice 43 — review day: retrieval across six earlier lessons
# Run:  cd ~/learning/python && uv run python3 practice/43_review_retrieval.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 1-36.
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓. Try each from memory before reopening the old lesson.

from collections import defaultdict
from dataclasses import dataclass
from functools import wraps


# ---------------------------------------------------------------------------
# Exercise 1 (Day 1 — names, objects & mutability)
# Return a NEW list that is [1, 2, 3, 99] without changing `original` at all.
# (The bug this guards against: b = original; b.append(99) would mutate the
# one shared list instead of producing an independent copy.)
def append_without_mutating(original, value):
    # TODO: return a new list — e.g. original + [value], or original[:] then append
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 2 — comprehensions)
# Rewrite as a single list comprehension: double every number in nums that
# is greater than zero (skip zero and negative numbers).
def double_positives(nums):
    # TODO: return [n * 2 for n in nums if n > 0]
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 3 — dict/set grouping)
# Given a list of (category, amount) pairs, return a plain dict mapping each
# category to the sum of its amounts. Use collections.defaultdict — no
# manual "if key not in totals" check.
def totals_by_category(pairs):
    totals = defaultdict(float)
    # TODO: for cat, amt in pairs: totals[cat] += amt
    ...
    return dict(totals)


# ---------------------------------------------------------------------------
# Exercise 4 (Day 5 — generators)
# Write a generator function that yields the running sum of nums, one
# partial sum per element — e.g. running_sums([1, 2, 3]) yields 1, 3, 6.
# Must use `yield`, not return a list.
def running_sums(nums):
    total = 0
    # TODO: for n in nums: total += n; yield total
    ...


# ---------------------------------------------------------------------------
# Exercise 5 (Day 7 — dataclasses)
# Define a @dataclass named Point with int fields x and y. Do not write
# __init__/__repr__/__eq__ by hand — @dataclass generates all three.
# TODO: uncomment and fill in
# @dataclass
# class Point:
#     x: int
#     y: int
Point = None  # TODO: replace with the @dataclass-decorated class above


# ---------------------------------------------------------------------------
# Exercise 6 (Day 12 — decorators)
# Write a decorator `logged` that works on a function with ANY signature
# (accepts *args, **kwargs) and preserves the wrapped function's __name__
# via functools.wraps. It should just call the wrapped function and return
# its result unchanged (no printing needed for the check below).
def logged(func):
    # TODO:
    #     @wraps(func)
    #     def wrapper(*args, **kwargs):
    #         return func(*args, **kwargs)
    #     return wrapper
    ...


@logged
def add(a, b):
    """Add two numbers."""
    return a + b


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_no_mutation():
    original = [1, 2, 3]
    result = append_without_mutating(original, 99)
    return result == [1, 2, 3, 99] and original == [1, 2, 3]


def _ex5_point_fields_and_repr_and_eq():
    if Point is None:
        return False
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    return (
        p1.x == 1 and p1.y == 2
        and p1 == p2
        and p1 != p3
        and "Point" in repr(p1)
    )


def _ex6_decorator_preserves_name_and_result():
    return add(2, 3) == 5 and add.__name__ == "add"


results = [
    check("Ex 1: append_without_mutating leaves the original list untouched",
          _ex1_no_mutation),
    check("Ex 2: double_positives keeps only positives, doubled, in order",
          lambda: double_positives([-2, 0, 1, 3, -1, 4]) == [2, 6, 8]),
    check("Ex 2b: double_positives on an all-non-positive list is empty",
          lambda: double_positives([0, -1, -2]) == []),
    check("Ex 3: totals_by_category sums amounts per category",
          lambda: totals_by_category([("food", 10.0), ("food", 5.0), ("fuel", 20.0)])
          == {"food": 15.0, "fuel": 20.0}),
    check("Ex 4: running_sums is a real generator (not a list) yielding partial sums",
          lambda: list(running_sums([1, 2, 3])) == [1, 3, 6]),
    check("Ex 5: Point is a dataclass with working fields, __eq__ and __repr__",
          _ex5_point_fields_and_repr_and_eq),
    check("Ex 6: logged decorator forwards args/kwargs and keeps __name__",
          _ex6_decorator_preserves_name_and_result),
]
print("\nAll green — lesson 43 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
