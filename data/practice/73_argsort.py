# Practice 73 — argsort(): positions, not values — and a stale docstring to catch
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/73_argsort.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
# Coerce "amount" to numeric (the "unknown" string becomes NaN) -- NOT dropped here on
# purpose, since this lesson's whole point is how argsort() handles that NaN.
amt = pd.to_numeric(df["amount"], errors="coerce")

# ---------------------------------------------------------------------------
# Exercise 1 — use argsort() + .iloc[] to read out the two smallest `amount`
# rows' order_ids, ascending. Confirm it matches what nsmallest(2) would give
# (Lesson 10). Fill in the literal integer 2 for how many smallest rows to
# take from the argsort order (not just any placeholder -- this checks the
# literal value itself, to avoid a freebie pass).
ex1_n = ...
try:
    ex1_order_ids = df.iloc[amt.argsort().iloc[:ex1_n]]["order_id"].tolist()
except Exception:
    ex1_order_ids = None

# ---------------------------------------------------------------------------
# Exercise 2 — confirm no -1 EVER appears in argsort()'s raw output, even
# though `amt` contains a real NaN (order_id 4). This is the exact
# stale-docstring claim from the lesson: help(pd.Series.argsort) says "-1
# indicating nan values," but current pandas never actually emits -1. Fill
# in the literal integer -1 for the sentinel value the docstring claims to
# use (not just any placeholder -- checks the literal value being searched
# for, to avoid a freebie pass).
ex2_sentinel = ...
try:
    ex2_has_sentinel = bool((amt.argsort().to_numpy() == ex2_sentinel).any())
except Exception:
    ex2_has_sentinel = None

# ---------------------------------------------------------------------------
# Exercise 3 — argsort() has no ascending= keyword at all; passing one
# raises TypeError. Fill in the literal boolean False for ascending= (not
# just any falsy placeholder -- a bare "..." left unfilled is ALSO falsy in
# some truthiness checks, so this checks the literal value itself, to avoid
# a freebie pass).
ex3_ascending_value = ...
try:
    amt.argsort(ascending=ex3_ascending_value)
    ex3_raised = False
except TypeError:
    ex3_raised = True
except Exception:
    ex3_raised = False

# ---------------------------------------------------------------------------
# Exercise 4 — get a DESCENDING order via negation (no ascending= keyword
# exists), and confirm the largest-amount row (order_id 5, amount 180.0)
# comes out first. Fill in the literal string "order_id" for the column to
# read back out.
ex4_column = ...
try:
    ex4_desc_order = (-amt).argsort()
    ex4_first_row_value = df.iloc[ex4_desc_order.iloc[0]][ex4_column]
except Exception:
    ex4_first_row_value = None

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
    check("Exercise 1: two smallest amounts' order_ids via argsort() match nsmallest(2)",
          lambda: ex1_n == 2 and ex1_order_ids == [2, 6]),
    check("Exercise 2: no -1 sentinel ever appears in argsort()'s output, despite a real NaN",
          lambda: ex2_sentinel == -1 and ex2_has_sentinel is False),
    check("Exercise 3: argsort(ascending=...) raises TypeError -- no such keyword exists",
          lambda: ex3_ascending_value is False and ex3_raised is True),
    check("Exercise 4: descending via negation puts the largest amount (order_id 5) first",
          lambda: ex4_column == "order_id" and ex4_first_row_value == 5),
]

print("\nAll green — lesson 73 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
