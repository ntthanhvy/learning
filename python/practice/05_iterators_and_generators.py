# Practice 5 — Iterators & generators: lazy pipelines
# Run:  cd ~/learning/python && uv run python3 practice/05_iterators_and_generators.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

# ---------------------------------------------------------------------------
# Exercise 1 — iter() and next() by hand.
# `letters` is a list. Get an iterator from it with iter(), then advance it
# twice with next() to pull the first two letters into `first` and `second`.
letters = ["a", "b", "c"]
letters_it = ...                # TODO: iter(letters)
first = ...                     # TODO: next(letters_it)
second = ...                    # TODO: next(letters_it)

# ---------------------------------------------------------------------------
# Exercise 2 — write a generator function.
# Write `countdown(n)` that yields n, n-1, ..., down to 1 (inclusive), one at
# a time, using a while loop and yield — no list built anywhere.
def countdown(n):
    ...                          # TODO: while n >= 1: yield n; n -= 1

# ---------------------------------------------------------------------------
# Exercise 3 — a generator expression.
# Given `nums`, build a generator expression (parentheses, not brackets)
# yielding each number's square. Don't call list() on it — leave it lazy.
nums = [1, 2, 3, 4, 5]
squares_gen = ...                # TODO: (n * n for n in nums)

# ---------------------------------------------------------------------------
# Exercise 4 — chain two generator functions into a pipeline.
# `parse(lines)` should yield each line split on "," as an
# {"city": ..., "amount": int(...)} dict. `positive_only(rows)` should yield
# only the rows whose "amount" is greater than 0. Wire them together into
# `pipeline` — nothing should run until something loops over it.
def parse(lines):
    ...                          # TODO: for line in lines: city, amount = line.split(","); yield {"city": city, "amount": int(amount)}

def positive_only(rows):
    ...                          # TODO: for row in rows: if row["amount"] > 0: yield row

raw_lines = ["Hanoi,120", "HCMC,-10", "Hanoi,45", "Danang,200"]
pipeline = ...                   # TODO: positive_only(parse(raw_lines))

# ---------------------------------------------------------------------------
# Exercise 5 — drive the pipeline and aggregate.
# Loop over `pipeline` and build `totals`, a plain dict mapping city -> sum
# of its positive amounts (use a plain dict + .get(city, 0), or defaultdict
# if you prefer — either is fine).
totals = {}
...                               # TODO: for row in pipeline: totals[row["city"]] = totals.get(row["city"], 0) + row["amount"]


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


import types

results = [
    check("Ex 1: iter()/next() pull items one at a time, in order",
          lambda: first == "a" and second == "b"),
    check("Ex 2: countdown(n) yields n down to 1 via yield",
          lambda: isinstance(countdown(3), types.GeneratorType)
          and list(countdown(3)) == [3, 2, 1]),
    check("Ex 3: squares_gen is a lazy generator expression, not a list",
          lambda: isinstance(squares_gen, types.GeneratorType)
          and list(squares_gen) == [1, 4, 9, 16, 25]),
    check("Ex 4: pipeline chains parse() and positive_only() lazily",
          lambda: isinstance(pipeline, types.GeneratorType)
          and list(positive_only(parse(raw_lines)))
          == [{"city": "Hanoi", "amount": 120},
              {"city": "Hanoi", "amount": 45},
              {"city": "Danang", "amount": 200}]),
    check("Ex 5: totals aggregates the pipeline's positive amounts per city",
          lambda: totals == {"Hanoi": 165, "Danang": 200}),
]
print("\nAll green — lesson 5 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
