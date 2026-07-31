# Practice 4 — Functions that pull their weight
# Run:  cd ~/learning/python && uv run python3 practice/04_functions_args_and_key.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from collections import Counter

# ---------------------------------------------------------------------------
# Exercise 1 — a function with a default argument.
# Write `discount(price, rate=0.1)` returning price * (1 - rate), so calling
# it with just a price uses a 10% discount by default.
def discount(price, rate=0.1):
    ...                          # TODO: return price * (1 - rate)

# ---------------------------------------------------------------------------
# Exercise 2 — call a function with keyword arguments.
# Call `discount` passing rate=0.5 and price=200, as keyword arguments in
# that order (name=value), overriding the default rate.
half_off = ...                  # TODO: discount(rate=0.5, price=200)

# ---------------------------------------------------------------------------
# Exercise 3 — write a lambda.
# Write a lambda that takes one number `n` and returns its square (n * n).
square = ...                    # TODO: lambda n: n * n

# ---------------------------------------------------------------------------
# Exercise 4 — sort a list of dicts with key=.
# Sort `sales` by "amount", ascending, using sorted(..., key=...) with a
# lambda that pulls out row["amount"].
sales = [
    {"city": "Hanoi", "amount": 120},
    {"city": "HCMC", "amount": 80},
    {"city": "Danang", "amount": 200},
]
by_amount = ...                 # TODO: sorted(sales, key=lambda row: row["amount"])

# ---------------------------------------------------------------------------
# Exercise 5 — find the max of a list with key=.
# Find the single row in `sales` with the largest "amount", using
# max(..., key=...).
biggest_sale = ...              # TODO: max(sales, key=lambda row: row["amount"])

# ---------------------------------------------------------------------------
# Exercise 6 — sort a Counter's items by count.
# `city_counts` tallies how many times each city appears. Build a sorted
# list of (city, count) pairs, largest count first: sorted(..., key=...,
# reverse=True) on city_counts.items(), keying by the count (index 1).
city_counts = Counter(["Hanoi", "HCMC", "Hanoi", "Hanoi", "HCMC", "Danang"])
ranked_cities = ...              # TODO: sorted(city_counts.items(), key=lambda pair: pair[1], reverse=True)


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
    check("Ex 1: discount() applies a 10% default rate when omitted",
          lambda: discount(100) == 90.0),
    check("Ex 2: keyword arguments match by name, not position",
          lambda: half_off == 100.0),
    check("Ex 3: lambda squares its argument",
          lambda: square(5) == 25 and square(3) == 9),
    check("Ex 4: sorted(..., key=...) orders rows by amount, ascending",
          lambda: by_amount == [sales[1], sales[0], sales[2]]),
    check("Ex 5: max(..., key=...) finds the row with the largest amount",
          lambda: biggest_sale == sales[2]),
    check("Ex 6: sorting Counter.items() by count, descending",
          lambda: ranked_cities == [("Hanoi", 3), ("HCMC", 2), ("Danang", 1)]),
]
print("\nAll green — lesson 4 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
