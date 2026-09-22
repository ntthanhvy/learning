# Practice 56 — the operator module
# Run:  cd ~/learning/python && uv run python3 practice/56_operator_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from collections import namedtuple
from functools import reduce
from operator import attrgetter, itemgetter, methodcaller, mul


# ---------------------------------------------------------------------------
# Exercise 1 — sort a list of dicts by one field.
# Return `rows` sorted by the "amount" field, ascending, using itemgetter
# (not a lambda).
def sort_by_amount(rows):
    # TODO: return sorted(rows, key=itemgetter("amount"))
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — sort by two fields at once.
# Return `rows` sorted by "city" first, then "amount" second (both ascending),
# using a single multi-key itemgetter call.
def sort_by_city_then_amount(rows):
    # TODO: return sorted(rows, key=itemgetter("city", "amount"))
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — sort namedtuples by field, with attrgetter.
# `points` is a list of Point(x, y) namedtuples. Return them sorted by the
# "x" field, ascending, using attrgetter (not itemgetter — these are objects,
# not dicts).
Point = namedtuple("Point", ["x", "y"])


def sort_points_by_x(points):
    # TODO: return sorted(points, key=attrgetter("x"))
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — case-insensitive sort with methodcaller.
# Return `words` sorted case-insensitively (as if every word were lowercase),
# but with the ORIGINAL casing preserved in the output, using methodcaller.
def sort_case_insensitive(words):
    # TODO: return sorted(words, key=methodcaller("lower"))
    ...


# ---------------------------------------------------------------------------
# Exercise 5 — a product with reduce + operator.mul.
# Return the product of every number in `nums`, using functools.reduce
# paired with operator.mul (not a lambda, not a manual loop).
def product(nums):
    # TODO: return reduce(mul, nums)
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


_sales = [
    {"city": "Hanoi", "amount": 120},
    {"city": "Danang", "amount": 200},
    {"city": "HCMC", "amount": 80},
]

_multi = [
    {"city": "Hanoi", "amount": 120},
    {"city": "Hanoi", "amount": 80},
    {"city": "Danang", "amount": 200},
]

_points = [Point(3, 1), Point(1, 2), Point(2, 0)]

_words = ["banana", "Apple", "cherry"]

results = [
    check("Ex 1: sort_by_amount sorts ascending by the amount field",
          lambda: sort_by_amount(_sales) == sorted(_sales, key=lambda r: r["amount"])),
    check("Ex 2: sort_by_city_then_amount sorts by city, then amount",
          lambda: sort_by_city_then_amount(_multi)
          == sorted(_multi, key=lambda r: (r["city"], r["amount"]))),
    check("Ex 3: sort_points_by_x sorts namedtuples by their x field",
          lambda: sort_points_by_x(_points) == sorted(_points, key=lambda p: p.x)),
    check("Ex 4: sort_case_insensitive orders case-blind but keeps original casing",
          lambda: sort_case_insensitive(_words) == ["Apple", "banana", "cherry"]),
    check("Ex 5: product multiplies every number together",
          lambda: product([1, 2, 3, 4]) == 24 and product([5]) == 5),
]
print("\nAll green — lesson 56 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
