# Practice 69 — statistics: summary numbers without pandas
# Run:  cd ~/learning/python && uv run python3 practice/69_statistics_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import statistics
from collections import defaultdict


# ---------------------------------------------------------------------------
# Exercise 1 — mean() vs median() on a list with one outlier.
# Write mean_and_median(data) that returns a tuple
# (statistics.mean(data), statistics.median(data)).
def mean_and_median(data):
    # TODO: return (statistics.mean(data), statistics.median(data))
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — mode() on repeated category labels.
# Write most_common_city(cities) that returns statistics.mode(cities) —
# the single most frequently occurring string in the list.
def most_common_city(cities):
    # TODO: return statistics.mode(cities)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — stdev() reveals spread that mean() alone hides.
# Write spread(data) that returns statistics.stdev(data).
def spread(data):
    # TODO: return statistics.stdev(data)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — per-group aggregation: group rows by "city" (Day 3's
# defaultdict pattern), then compute each group's mean "amount".
# Write mean_by_city(rows) where each row is a dict like
# {"city": "Hanoi", "amount": 20}. Return a dict mapping each city name to
# the mean of its amounts, e.g. {"Hanoi": 22.5, "Hue": 40.0}.
def mean_by_city(rows):
    # TODO: grouped = defaultdict(list)
    #       for row in rows:
    #           grouped[row["city"]].append(row["amount"])
    #       return {city: statistics.mean(amounts) for city, amounts in grouped.items()}
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
    data = [20, 25, 22, 21, 500]
    result = mean_and_median(data)
    if result is None:
        return False
    mean_val, median_val = result
    return abs(mean_val - 117.6) < 1e-9 and median_val == 22


def _ex2():
    cities = ["Hanoi", "Hue", "Hanoi", "Danang", "Hanoi"]
    return most_common_city(cities) == "Hanoi"


def _ex3():
    tight = [48, 50, 52, 49, 51]
    wide = [10, 90, 50, 95, 5]
    tight_stdev = spread(tight)
    wide_stdev = spread(wide)
    if tight_stdev is None or wide_stdev is None:
        return False
    return tight_stdev < 5 and wide_stdev > 30


def _ex4():
    rows = [
        {"city": "Hanoi", "amount": 20},
        {"city": "Hanoi", "amount": 25},
        {"city": "Hue", "amount": 40},
    ]
    result = mean_by_city(rows)
    if result is None:
        return False
    return abs(result["Hanoi"] - 22.5) < 1e-9 and abs(result["Hue"] - 40.0) < 1e-9


results = [
    check("Ex 1: mean() is pulled by the outlier, median() mostly ignores it", _ex1),
    check("Ex 2: mode() finds the most frequent category label", _ex2),
    check("Ex 3: stdev() tells apart two same-shape, differently-spread lists", _ex3),
    check("Ex 4: grouping by key, then mean() per group", _ex4),
]
print("\nAll green — lesson 69 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
