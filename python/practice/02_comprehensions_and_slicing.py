# Practice 2 — Comprehensions & slicing
# Run:  cd ~/learning/python && uv run python3 practice/02_comprehensions_and_slicing.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

# ---------------------------------------------------------------------------
# Exercise 1 — loop to comprehension.
# Rewrite this loop (empty list + append) as a one-line list comprehension.
# Same shape as the lesson's `taxed = [p * 1.1 for p in prices]` example.
prices = [120.0, 35.5, 99.9]
taxed_loop = []
for p in prices:
    taxed_loop.append(p * 1.1)

taxed = ...                    # TODO: [p * 1.1 for p in prices]

# ---------------------------------------------------------------------------
# Exercise 2 — add a filter.
# Build a list of only the sales greater than 50, using a comprehension
# with an `if` clause (the SQL WHERE part).
sales = [120.0, 35.5, 99.9, 10.0]
big_sales = ...                # TODO: [amount for amount in sales if amount > 50]

# ---------------------------------------------------------------------------
# Exercise 3 — dict comprehension shape.
# Build a dict mapping each name to its length: {name: len(name), ...}
# Curly braces + colon, same three slots as a list comprehension.
names = ["An", "Binh", "Chi"]
name_len = ...                 # TODO: {n: len(n) for n in names}

# ---------------------------------------------------------------------------
# Exercise 4 — slice with start:stop.
# Grab the middle three letters — indices 1, 2, 3 — remember stop is exclusive.
letters = ["a", "b", "c", "d", "e"]
middle = ...                   # TODO: letters[1:4]

# ---------------------------------------------------------------------------
# Exercise 5 — step and negative index.
# Reverse `letters` using a slice with step -1, and separately grab every
# second letter starting from the front using a slice with step 2.
reversed_letters = ...         # TODO: letters[::-1]
every_second = ...             # TODO: letters[::2]

# ---------------------------------------------------------------------------
# Exercise 6 — rewrite Day 1's clean() as a one-liner.
# Same job as Day 1 (strip the "name" field, return a NEW list, don't mutate
# `records` or its dicts) — but now as a single comprehension, no loop body.
def clean(records):
    # TODO: return [{**r, "name": r["name"].strip()} for r in records]
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


raw_records = [{"name": "  An  ", "amount": 120}, {"name": "Binh ", "amount": 35}]

results = [
    check("Ex 1: comprehension matches the loop's output",
          lambda: taxed == taxed_loop and len(taxed) == 3),
    check("Ex 2: filter keeps only sales over 50",
          lambda: big_sales == [120.0, 99.9]),
    check("Ex 3: dict comprehension maps each name to its length",
          lambda: name_len == {"An": 2, "Binh": 4, "Chi": 3}),
    check("Ex 4: slice[1:4] takes indices 1, 2, 3 — stop is exclusive",
          lambda: middle == ["b", "c", "d"]),
    check("Ex 5: step -1 reverses; step 2 takes every second item",
          lambda: reversed_letters == ["e", "d", "c", "b", "a"]
          and every_second == ["a", "c", "e"]),
    check("Ex 6: clean() returns stripped names and leaves raw_records intact",
          lambda: [r["name"] for r in clean(raw_records)] == ["An", "Binh"]
          and [r["name"] for r in raw_records] == ["  An  ", "Binh "]),
]
print("\nAll green — lesson 2 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
