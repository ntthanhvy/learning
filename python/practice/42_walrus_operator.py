# Practice 42 — the walrus operator: assignment expressions
# Run:  cd ~/learning/python && uv run python3 practice/42_walrus_operator.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import re


# ---------------------------------------------------------------------------
# Exercise 1 — while loop: use a walrus to avoid calling next_value() twice
# (once to prime the loop, once again at the end of the loop body).
# Collect values into a list until next_value() returns None, then return
# the list (not including the None).
def make_reader(values):
    it = iter(values)

    def next_value():
        return next(it, None)

    return next_value


def collect_until_none(values):
    next_value = make_reader(values)
    collected = []
    # TODO: rewrite this loop to use a walrus in the while condition, e.g.
    #     while (item := next_value()) is not None:
    #         collected.append(item)
    ...
    return collected


# ---------------------------------------------------------------------------
# Exercise 2 — comprehension: use a walrus so the filtered/computed value is
# only computed once per element instead of twice.
def square_if_over(nums, threshold):
    """Return the squares of every n in nums whose square exceeds threshold,
    computing each square only once per element (use a walrus in the `if`)."""
    # TODO: return [sq for n in nums if (sq := n * n) > threshold]
    try:
        ...
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Exercise 3 — if condition: use a walrus to bind and test a dict lookup's
# result in one line, instead of a separate lookup line before the if.
def price_or_default(catalog, sku, default):
    """Look up sku in catalog (a dict); return the price if found (not None),
    else default. Use a walrus: if (price := catalog.get(sku)) is not None."""
    # TODO: if (price := catalog.get(sku)) is not None:
    #           return price
    #       return default
    try:
        ...
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Exercise 4 — regex + walrus: Day 38's exact shape. Return the matched
# number as an int if pattern r"\d+" is found in text, else return None —
# in one `if` using a walrus, not two separate re.search() calls.
def first_number_or_none(text):
    # TODO: if (m := re.search(r"\d+", text)) is not None:
    #           return int(m.group())
    #       return None
    try:
        ...
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: while-walrus collects values until None, none lost",
          lambda: collect_until_none([1, 2, 3, None, 4]) == [1, 2, 3]),
    check("Ex 1b: while-walrus on an all-None reader collects nothing",
          lambda: collect_until_none([None]) == []),
    check("Ex 2: comprehension-walrus squares only the ones over threshold",
          lambda: square_if_over([1, 2, 3, 4, 5], 5) == [9, 16, 25]),
    check("Ex 2b: comprehension-walrus returns empty list when none qualify",
          lambda: square_if_over([1, 2], 100) == []),
    check("Ex 3: if-walrus returns the found price",
          lambda: price_or_default({"A1": 9.99}, "A1", 0.0) == 9.99),
    check("Ex 3b: if-walrus falls back to default when sku is missing",
          lambda: price_or_default({"A1": 9.99}, "Z9", 0.0) == 0.0),
    check("Ex 4: regex-walrus extracts the first number as an int",
          lambda: first_number_or_none("order id: 4471") == 4471),
    check("Ex 4b: regex-walrus returns None when there's no digit at all",
          lambda: first_number_or_none("no digits here") is None),
]
print("\nAll green — lesson 42 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
