# Practice 3 — dict & set: grouping without pandas
# Run:  cd ~/learning/python && uv run python3 practice/03_dict_set_and_grouping.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from collections import defaultdict, Counter

# ---------------------------------------------------------------------------
# Exercise 1 — dict lookup with .get() and a default.
# Look up "kiwi" in `prices`. It isn't there, so use .get() with a fallback
# default of 0.0 instead of plain [] indexing (which would raise KeyError).
prices = {"apple": 3.5, "banana": 1.2, "pear": 2.0}
kiwi_price = ...                # TODO: prices.get("kiwi", 0.0)

# ---------------------------------------------------------------------------
# Exercise 2 — de-duplicate with a set.
# Build the set of distinct names from `raw_names` (a set collapses
# duplicates automatically — no loop needed).
raw_names = ["An", "Binh", "An", "Chi", "Binh"]
unique_names = ...              # TODO: set(raw_names)

# ---------------------------------------------------------------------------
# Exercise 3 — group rows by key with setdefault.
# Group `sales` amounts by "city": one dict, one list per distinct city,
# using by_city.setdefault(key, []).append(...) inside the loop.
sales = [
    {"city": "Hanoi", "amount": 120},
    {"city": "HCMC", "amount": 80},
    {"city": "Hanoi", "amount": 45},
]
by_city_setdefault = {}
# TODO: for row in sales:
#           by_city_setdefault.setdefault(row["city"], []).append(row["amount"])
...

# ---------------------------------------------------------------------------
# Exercise 4 — the same grouping with collections.defaultdict.
# Same result as Exercise 3, but using defaultdict(list) so no setdefault
# call is needed — accessing a missing key auto-creates an empty list.
by_city_defaultdict = defaultdict(list)
# TODO: for row in sales:
#           by_city_defaultdict[row["city"]].append(row["amount"])
...

# ---------------------------------------------------------------------------
# Exercise 5 — dict comprehension built from zip.
# Build a dict mapping each name to its age, pairing the two lists with zip.
names = ["An", "Binh", "Chi"]
ages = [30, 25, 41]
age_of = ...                    # TODO: {n: a for n, a in zip(names, ages)}

# ---------------------------------------------------------------------------
# Exercise 6 — count rows per key with collections.Counter.
# Count how many sales rows belong to each city — one call, no loop.
city_counts = ...               # TODO: Counter(row["city"] for row in sales)


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
    check("Ex 1: .get() returns the fallback default for a missing key",
          lambda: kiwi_price == 0.0),
    check("Ex 2: set collapses duplicate names",
          lambda: unique_names == {"An", "Binh", "Chi"}),
    check("Ex 3: setdefault groups amounts into one list per city",
          lambda: by_city_setdefault == {"Hanoi": [120, 45], "HCMC": [80]}),
    check("Ex 4: defaultdict(list) groups the same way as setdefault",
          lambda: dict(by_city_defaultdict) == {"Hanoi": [120, 45], "HCMC": [80]}),
    check("Ex 5: dict comprehension maps each name to its age via zip",
          lambda: age_of == {"An": 30, "Binh": 25, "Chi": 41}),
    check("Ex 6: Counter tallies rows per city",
          lambda: dict(city_counts) == {"Hanoi": 2, "HCMC": 1}),
]
print("\nAll green — lesson 3 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
