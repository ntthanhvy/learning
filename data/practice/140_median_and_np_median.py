# Practice 140 — Series.median() and np.median(): the sorted-middle value,
# and the NaN-propagation trap std() doesn't have
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/140_median_and_np_median.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: an odd-count Series's .median() matches np.median()
# on the same values. An even-count Series's .median() equals the average of
# its two sorted middle values.
s_odd = pd.Series([2, 4, 4, 5, 5, 7, 9])
s_even = pd.Series([1, 2, 3, 4])


def odd_series_median():
    # Return s_odd.median().
    #   return s_odd.median()
    ...


def odd_np_median():
    # Return np.median(s_odd.to_numpy()).
    #   return np.median(s_odd.to_numpy())
    ...


def even_series_median():
    # Return s_even.median().
    #   return s_even.median()
    ...


ex1_odd_series = odd_series_median()
ex1_odd_np = odd_np_median()
ex1_even = even_series_median()
try:
    ex1_odd_matches = abs(float(ex1_odd_series) - float(ex1_odd_np)) < 1e-9
    ex1_even_is_2_5 = abs(float(ex1_even) - 2.5) < 1e-9
except Exception:
    ex1_odd_matches = False
    ex1_even_is_2_5 = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: on a Series with one NaN mixed in, Series.median()
# and np.nanmedian() both return the same real number, while plain
# np.median() on the identical values returns NaN.
s_with_na = pd.Series([2, 4, 4, 4, 5, 5, 7, 9, np.nan])


def series_median_with_na():
    # Return s_with_na.median().
    #   return s_with_na.median()
    ...


def np_median_with_na():
    # Return np.median(s_with_na.to_numpy()).
    #   return np.median(s_with_na.to_numpy())
    ...


def np_nanmedian_with_na():
    # Return np.nanmedian(s_with_na.to_numpy()).
    #   return np.nanmedian(s_with_na.to_numpy())
    ...


ex2_series_median = series_median_with_na()
ex2_np_median = np_median_with_na()
ex2_np_nanmedian = np_nanmedian_with_na()
try:
    ex2_np_median_is_nan = pd.isna(ex2_np_median)
    ex2_series_matches_nanmedian = abs(float(ex2_series_median) - float(ex2_np_nanmedian)) < 1e-9
except Exception:
    ex2_np_median_is_nan = False
    ex2_series_matches_nanmedian = False

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
    check("Exercise 1: odd-count .median() matches np.median(); even-count .median() is 2.5",
          lambda: ex1_odd_matches is True and ex1_even_is_2_5 is True),
    check("Exercise 2: plain np.median() with a NaN is NaN; Series.median() matches np.nanmedian()",
          lambda: ex2_np_median_is_nan is True and ex2_series_matches_nanmedian is True),
]

print("\nAll green — lesson 140 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
