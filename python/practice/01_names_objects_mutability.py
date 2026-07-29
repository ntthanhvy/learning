# Practice 1 — Names, objects & mutability
# Run:  cd ~/learning/python && uv run python3 practice/01_names_objects_mutability.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓. Exercises 1 and 2 want you to PREDICT the answer before running —
# write down what you expect, then see if the check agrees.
import copy

# ---------------------------------------------------------------------------
# Exercise 1 — predict, then fill in.
# Two names, one list. What does `first` hold after the append?
# Set `predicted_first` to the list you expect — don't run it first, guess.
first = [1, 2, 3]
second = first
second.append(4)

predicted_first = ...          # TODO: [1, 2, 3] or [1, 2, 3, 4]?

# ---------------------------------------------------------------------------
# Exercise 2 — predict, then fill in.
# Same shape, but with a string instead of a list. Strings are immutable.
word = "hello"
echo = word
word = word.upper()

predicted_echo = ...           # TODO: "hello" or "HELLO"?

# ---------------------------------------------------------------------------
# Exercise 3 — identity vs equality.
# Build `same_object` so it is the SAME object as `base` (not just equal),
# and `equal_only` so it is a DIFFERENT object with equal contents.
base = [10, 20]
same_object = ...              # TODO: alias it
equal_only = ...               # TODO: a separate list with the same contents

# ---------------------------------------------------------------------------
# Exercise 4 — a safe copy.
# Copy `prices` so that appending to the copy leaves `prices` untouched.
prices = [120.0, 35.5, 99.9]
prices_copy = ...              # TODO: make a real copy, not an alias
try:
    prices_copy.append(0.0)
except Exception:
    pass

# ---------------------------------------------------------------------------
# Exercise 5 — the shallow-copy limit.
# `list(rows)` copies the OUTER list only. Make `deep_rows` a copy that is
# independent all the way down, so mutating a nested list can't reach `rows`.
rows = [["An", 120], ["Binh", 35]]
deep_rows = ...                # TODO: independent at every level
try:
    deep_rows[0].append("VN")
except Exception:
    pass

# ---------------------------------------------------------------------------
# Exercise 6 — fix the mutable default argument.
# `add_item` accumulates across calls because its default list is created once,
# at definition time. Rewrite the body so each call with no basket starts fresh.
def add_item(item, basket=None):
    # TODO: if no basket was passed, build a NEW empty list here.
    ...
    basket.append(item)
    return basket

# ---------------------------------------------------------------------------
# Exercise 7 — stop mutating the caller's data.
# `clean` currently strips names IN PLACE, destroying the raw records.
# Rewrite it to return a NEW list of new dicts, leaving `records` untouched.
# Plain `for` loops are fine — comprehensions are Day 2.
def clean(records):
    # TODO: build and return a new list; do not mutate `records` or its dicts.
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
    check("Ex 1: aliasing — append through `second` is visible through `first`",
          lambda: predicted_first == first == [1, 2, 3, 4]),
    check("Ex 2: immutability — rebinding `word` left `echo` alone",
          lambda: predicted_echo == echo == "hello"),
    check("Ex 3: `same_object` is base; `equal_only` merely equals it",
          lambda: same_object is base
          and equal_only is not base and equal_only == base),
    check("Ex 4: appending to the copy left `prices` at 3 items",
          lambda: len(prices) == 3 and len(prices_copy) == 4),
    check("Ex 5: deep copy — mutating `deep_rows[0]` did not reach `rows`",
          lambda: rows[0] == ["An", 120] and deep_rows[0] == ["An", 120, "VN"]),
    check("Ex 6: two separate calls each start from an empty basket",
          lambda: add_item("apple") == ["apple"] and add_item("banana") == ["banana"]),
    check("Ex 7: clean() returns stripped names and leaves raw_records intact",
          lambda: [r["name"] for r in clean(raw_records)] == ["An", "Binh"]
          and [r["name"] for r in raw_records] == ["  An  ", "Binh "]),
]
print("\nAll green — lesson 1 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
