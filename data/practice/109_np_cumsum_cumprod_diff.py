# Practice 109 — np.cumsum(), np.cumprod(), np.diff(): running totals,
#                products, and differences, one array layer down
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/109_np_cumsum_cumprod_diff.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: basic cumsum()/cumprod() running totals on a plain
# array. [1, 2, 3, 4] -> cumsum [1, 3, 6, 10], cumprod [1, 2, 6, 24].
arr = np.array([1, 2, 3, 4])

# ex1_cumsum = np.cumsum(arr)
ex1_cumsum = ...
# ex1_cumprod = np.cumprod(arr)
ex1_cumprod = ...
try:
    ex1_cumsum_ok = ex1_cumsum.tolist() == [1, 3, 6, 10]
    ex1_cumprod_ok = ex1_cumprod.tolist() == [1, 2, 6, 24]
except Exception:
    ex1_cumsum_ok = False
    ex1_cumprod_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.cumsum() on a Series with a NaN matches
# Series.cumsum() exactly (dispatch, Series back, resumes after the NaN).
# np.diff() on that same Series comes back one element shorter and is NOT
# a Series.
s = pd.Series([1.0, np.nan, 3.0, 4.0])


def matches_series_cumsum(values):
    # Return True if np.cumsum(values) equals values.cumsum() exactly,
    # comparing with .equals() (NaN-aware) and confirming the result is
    # still a pandas Series.
    #   result = np.cumsum(values)
    #   return isinstance(result, pd.Series) and result.equals(values.cumsum())
    ...


# ex2_cumsum_matches = matches_series_cumsum(s)
ex2_cumsum_matches = ...
# ex2_diff_result = np.diff(s)
ex2_diff_result = ...
try:
    ex2_diff_is_not_series = not isinstance(ex2_diff_result, pd.Series)
    ex2_diff_is_shorter = len(ex2_diff_result) == len(s) - 1
except Exception:
    ex2_diff_is_not_series = False
    ex2_diff_is_shorter = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: an int8 array's cumprod() result upgrades to
# int64 (platform default), to guard against overflowing the narrow type.
small_ints = np.array([10, 10, 10], dtype=np.int8)

# ex3_result = np.cumprod(small_ints)
ex3_result = ...
try:
    ex3_dtype_is_int64 = ex3_result.dtype == np.int64
    ex3_values_correct = ex3_result.tolist() == [10, 100, 1000]
except Exception:
    ex3_dtype_is_int64 = False
    ex3_values_correct = False

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
    check("Exercise 1: np.cumsum()/np.cumprod() produce the correct running totals",
          lambda: ex1_cumsum_ok is True and ex1_cumprod_ok is True),
    check("Exercise 2: np.cumsum() matches Series.cumsum(); np.diff() is shorter and not a Series",
          lambda: ex2_cumsum_matches is True and ex2_diff_is_not_series is True and ex2_diff_is_shorter is True),
    check("Exercise 3: an int8 array's cumprod() result upgrades to int64",
          lambda: ex3_dtype_is_int64 is True and ex3_values_correct is True),
]

print("\nAll green — lesson 109 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
