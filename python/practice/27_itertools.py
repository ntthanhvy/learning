# Practice 27 — itertools: chaining, grouping & combining
# Run:  cd ~/learning/python && uv run python3 practice/27_itertools.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from itertools import chain, groupby, islice, product

# ---------------------------------------------------------------------------
# Exercise 1 — chain two lists into one pass.
# jan_sales and feb_sales are separate lists of raw "city,amount" strings.
# Use itertools.chain to build one iterable visiting jan_sales' items first,
# then feb_sales' items, with no new list built by hand (don't use +).
jan_sales = ["Hanoi,120", "HCMC,80"]
feb_sales = ["Hanoi,45", "Danang,200"]
chained = ...                    # TODO: chain(jan_sales, feb_sales)

# ---------------------------------------------------------------------------
# Exercise 2 — group pre-sorted rows by key with groupby.
# `sorted_rows` is already sorted by "city" (groupby requires that — it only
# merges consecutive matching keys). Build `totals`, a plain dict mapping
# city -> sum of amounts in that city's group.
sorted_rows = [
    {"city": "Danang", "amount": 200},
    {"city": "Hanoi", "amount": 120},
    {"city": "Hanoi", "amount": 45},
    {"city": "HCMC", "amount": 80},
]
totals = {}
# TODO: for city, group in groupby(sorted_rows, key=lambda r: r["city"]):
#           totals[city] = sum(r["amount"] for r in group)
...

# ---------------------------------------------------------------------------
# Exercise 3 — see groupby's sorted-input requirement break on unsorted data.
# `unsorted_rows` has two separate "Hanoi" runs, not adjacent. Run the same
# groupby pattern as Exercise 2 and count how many total groups come out
# (should be 3, not 2, because groupby never merges non-adjacent runs).
unsorted_rows = [
    {"city": "Hanoi", "amount": 120},
    {"city": "HCMC", "amount": 80},
    {"city": "Hanoi", "amount": 45},
]
group_count = ...                # TODO: sum(1 for _ in groupby(unsorted_rows, key=lambda r: r["city"]))

# ---------------------------------------------------------------------------
# Exercise 4 — islice an infinite generator.
# `counter()` below yields 0, 1, 2, ... forever and never stops on its own.
# Use islice to pull exactly the first four values into a list, `first_four`.
def counter():
    n = 0
    while True:
        yield n
        n += 1

first_four = ...                 # TODO: list(islice(counter(), 4))

# ---------------------------------------------------------------------------
# Exercise 5 — every combination with product.
# Build every (size, color) combination as a list of tuples, in the order
# product() naturally produces them (all colors for "S" first, then "M").
sizes = ["S", "M"]
colors = ["red", "blue"]
combos = ...                     # TODO: list(product(sizes, colors))


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
    check("Ex 1: chain visits jan_sales then feb_sales lazily, no new list",
          lambda: list(chained) == ["Hanoi,120", "HCMC,80", "Hanoi,45", "Danang,200"]),
    check("Ex 2: groupby on pre-sorted rows sums amounts per city",
          lambda: totals == {"Danang": 200, "Hanoi": 165, "HCMC": 80}),
    check("Ex 3: groupby on unsorted rows produces 3 groups, not 2",
          lambda: group_count == 3),
    check("Ex 4: islice pulls exactly the first four values from an infinite generator",
          lambda: first_four == [0, 1, 2, 3]),
    check("Ex 5: product builds every (size, color) combination",
          lambda: combos == [("S", "red"), ("S", "blue"), ("M", "red"), ("M", "blue")]),
]
print("\nAll green — lesson 27 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
