# Practice 108 — Series.mode(): the most-frequent value, and why it can
#                hand back more than one
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/108_mode.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .mode() on the real orders_raw.csv customer column
# returns a one-row Series whose single value matches value_counts()'s own
# top entry (An: 3 orders, Binh: 2, Chi: 1 -- no tie).
orders = pd.read_csv("practice/data/orders_raw.csv")

# ex1_mode_result = orders["customer"].mode()
ex1_mode_result = ...
try:
    ex1_len_is_one = len(ex1_mode_result) == 1
    ex1_top_value = ex1_mode_result.iloc[0]
    ex1_matches_value_counts = ex1_top_value == orders["customer"].value_counts().index[0]
except Exception:
    ex1_len_is_one = False
    ex1_matches_value_counts = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: a two-way tie ("a" and "b" both occur twice, "c"
# occurs once) returns BOTH tied values as separate rows in the same call.
tied = pd.Series(["a", "b", "a", "b", "c"])


def top_values(values):
    # Return values.mode() -- one line, no loop.
    #   return values.mode()
    ...


# ex2_result = top_values(tied)
ex2_result = ...
try:
    ex2_len_is_two = len(ex2_result) == 2
    ex2_has_both = set(ex2_result.tolist()) == {"a", "b"}
except Exception:
    ex2_len_is_two = False
    ex2_has_both = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: dropna=False lets NaN win outright when NaN is
# genuinely the most frequent entry; the default dropna=True excludes NaN
# from the count entirely, so a real value wins instead.
with_nan = pd.Series([1, 1, 2, np.nan, np.nan, np.nan])

# ex3_default = with_nan.mode()
ex3_default = ...
# ex3_keep_nan = with_nan.mode(dropna=False)
ex3_keep_nan = ...
try:
    ex3_default_is_real_value = bool(ex3_default.iloc[0] == 1.0)
    ex3_keep_nan_is_nan = bool(pd.isna(ex3_keep_nan.iloc[0]))
except Exception:
    ex3_default_is_real_value = False
    ex3_keep_nan_is_nan = False

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
    check("Exercise 1: .mode() on customer returns a one-row Series matching value_counts()'s top",
          lambda: ex1_len_is_one is True and ex1_matches_value_counts is True),
    check("Exercise 2: a two-way tie returns both tied values as separate rows in the same call",
          lambda: ex2_len_is_two is True and ex2_has_both is True),
    check("Exercise 3: dropna=False lets NaN win outright; default dropna=True excludes it",
          lambda: ex3_default_is_real_value is True and ex3_keep_nan_is_nan is True),
]

print("\nAll green — lesson 108 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
