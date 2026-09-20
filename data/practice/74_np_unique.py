# Practice 74 — np.unique(): sorted, richer, and a stricter cousin of Series.unique()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/74_np_unique.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")

# ---------------------------------------------------------------------------
# Exercise 1 — np.unique() on the `order_id`-ordered `amount` column comes
# back SORTED, while Series.unique() keeps first-appearance (raw row) order
# -- the two genuinely differ here since the raw amounts are not already
# sorted. Fill in the literal string "amount" for the column name (not just
# any placeholder -- this checks the literal column name itself, to avoid a
# freebie pass).
ex1_column = ...
try:
    amt = pd.to_numeric(df[ex1_column], errors="coerce").dropna()
    ex1_appearance_order = amt.unique().tolist()
    ex1_sorted_order = np.unique(amt.to_numpy()).tolist()
except Exception:
    ex1_appearance_order = None
    ex1_sorted_order = None

# ---------------------------------------------------------------------------
# Exercise 2 — use return_counts= to confirm how many rows each customer
# has. Fill in the literal boolean True for return_counts= (not just any
# truthy placeholder -- a bare unfilled "..." is ALSO truthy in Python, so
# this checks the literal value itself, to avoid a freebie pass).
ex2_return_counts = ...
try:
    ex2_vals, ex2_counts = np.unique(df["customer"].to_numpy(), return_counts=ex2_return_counts)
    ex2_count_map = dict(zip(ex2_vals.tolist(), ex2_counts.tolist()))
except Exception:
    ex2_count_map = None

# ---------------------------------------------------------------------------
# Exercise 3 — plain factorize() and np.unique(return_inverse=True) give
# DIFFERENT codes on data where first-appearance order and sorted order
# diverge; factorize(sort=True) matches np.unique() instead. Fill in the
# literal boolean True for factorize's sort= keyword (not just any
# placeholder -- checks the literal value, to avoid a freebie pass).
s = pd.Series(["Chi", "An", "Chi", "Binh", "An"])
ex3_sort_value = ...
try:
    codes_default, _ = pd.factorize(s)
    codes_sorted, _ = pd.factorize(s, sort=ex3_sort_value)
    _, codes_np = np.unique(s.to_numpy(), return_inverse=True)
    ex3_default_differs_from_np = codes_default.tolist() != codes_np.tolist()
    ex3_sorted_matches_np = codes_sorted.tolist() == codes_np.tolist()
except Exception:
    ex3_default_differs_from_np = None
    ex3_sorted_matches_np = None

# ---------------------------------------------------------------------------
# Exercise 4 — np.unique() raises TypeError on an object array mixing a
# real None with strings (it must sort to work); Series.unique() survives
# the identical data untouched. Fill in the literal string "TypeError" for
# the exception class name expected (not just any placeholder -- checks the
# literal value, to avoid a freebie pass).
mixed = pd.Series(["b", "a", None, "a"])
ex4_exception_name = ...
try:
    np.unique(mixed.to_numpy())
    ex4_raised_name = None
except Exception as e:
    ex4_raised_name = type(e).__name__
try:
    ex4_series_unique_ok = mixed.unique() is not None
except Exception:
    ex4_series_unique_ok = False

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
    check("Exercise 1: np.unique() is sorted, differs from Series.unique()'s appearance order",
          lambda: ex1_column == "amount"
          and ex1_appearance_order == [120.0, 35.5, 99.9, 180.0, 42.0]
          and ex1_sorted_order == [35.5, 42.0, 99.9, 120.0, 180.0]),
    check("Exercise 2: return_counts= gives correct per-customer row counts",
          lambda: ex2_return_counts is True and ex2_count_map == {"An": 3, "Binh": 2, "Chi": 1}),
    check("Exercise 3: factorize() default differs from np.unique(); sort=True matches it",
          lambda: ex3_sort_value is True and ex3_default_differs_from_np is True and ex3_sorted_matches_np is True),
    check("Exercise 4: np.unique() raises TypeError on mixed None/str; Series.unique() survives",
          lambda: ex4_exception_name == "TypeError" and ex4_raised_name == "TypeError" and ex4_series_unique_ok is True),
]

print("\nAll green — lesson 74 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
