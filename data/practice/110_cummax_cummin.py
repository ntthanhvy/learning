# Practice 110 — Series.cummax() / Series.cummin(): the running best-so-far,
#                and the NumPy function that doesn't exist
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/110_cummax_cummin.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: basic cummax()/cummin() running best-so-far on a
# plain Series. [3, 1, 4, 1, 5, 9, 2, 6] -> cummax ends at 9 (the max),
# cummin ends at 1 (the min) -- the last value always matches the plain
# max()/min().
s = pd.Series([3, 1, 4, 1, 5, 9, 2, 6])

# ex1_cummax = s.cummax()
ex1_cummax = ...
# ex1_cummin = s.cummin()
ex1_cummin = ...
try:
    ex1_cummax_ok = ex1_cummax.tolist() == [3, 3, 4, 4, 5, 9, 9, 9]
    ex1_cummin_ok = ex1_cummin.tolist() == [3, 1, 1, 1, 1, 1, 1, 1]
    ex1_last_matches_max = bool(ex1_cummax.iloc[-1] == s.max())
    ex1_last_matches_min = bool(ex1_cummin.iloc[-1] == s.min())
except Exception:
    ex1_cummax_ok = False
    ex1_cummin_ok = False
    ex1_last_matches_max = False
    ex1_last_matches_min = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: groupby(...).cummax() tracks each group's own
# running best independently. An: [10, 30, 15] -> running best [10, 30, 30].
# Binh: [5, 20] -> running best [5, 20].
df = pd.DataFrame({
    "customer": ["An", "An", "Binh", "Binh", "An"],
    "amount": [10, 30, 5, 20, 15],
})


def running_best(frame):
    # Return a Series: frame.groupby("customer")["amount"].cummax()
    #   return frame.groupby("customer")["amount"].cummax()
    ...


# ex2_running_best = running_best(df)
ex2_running_best = ...
try:
    ex2_values_ok = ex2_running_best.tolist() == [10, 30, 5, 20, 30]
except Exception:
    ex2_values_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: default skipna=True resumes tracking right after a
# NaN; skipna=False poisons every row from the first NaN onward.
s2 = pd.Series([3.0, np.nan, 1.0, 5.0, np.nan, 2.0])

# ex3_default = s2.cummax()
ex3_default = ...
# ex3_no_skip = s2.cummax(skipna=False)
ex3_no_skip = ...
try:
    ex3_default_resumes = ex3_default.tolist()[2] == 3.0  # resumes after the NaN at index 1
    ex3_no_skip_poisoned = pd.isna(ex3_no_skip.iloc[2]) and pd.isna(ex3_no_skip.iloc[-1])
except Exception:
    ex3_default_resumes = False
    ex3_no_skip_poisoned = False

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
    check("Exercise 1: cummax()/cummin() produce the correct running best-so-far, ending at max()/min()",
          lambda: ex1_cummax_ok is True and ex1_cummin_ok is True
          and ex1_last_matches_max is True and ex1_last_matches_min is True),
    check("Exercise 2: groupby(...).cummax() tracks each group's own running best independently",
          lambda: ex2_values_ok is True),
    check("Exercise 3: default skipna=True resumes after a NaN; skipna=False poisons every row after it",
          lambda: ex3_default_resumes is True and ex3_no_skip_poisoned is True),
]

print("\nAll green — lesson 110 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
