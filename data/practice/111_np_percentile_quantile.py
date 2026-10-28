# Practice 111 — np.percentile() and np.quantile(): same math, two scales,
#               and a NaN trap pandas doesn't have
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/111_np_percentile_quantile.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.percentile() (0-100 scale) and np.quantile()
# (0-1 scale) compute the identical value for matching q. Multiple q values
# at once return an array, in the same order as the input list.
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# ex1_pct50 = np.percentile(arr, 50)
ex1_pct50 = ...
# ex1_q50 = np.quantile(arr, 0.5)
ex1_q50 = ...
# ex1_multi = np.percentile(arr, [25, 50, 75])
ex1_multi = ...
try:
    ex1_scales_match = bool(ex1_pct50 == ex1_q50)
    ex1_multi_ok = list(ex1_multi) == [1.75, 3.5, 5.25]
except Exception:
    ex1_scales_match = False
    ex1_multi_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: calling np.percentile()/np.quantile() on a Series
# does NOT dispatch to Series.quantile() -- it returns a bare scalar, no
# Index. Series.quantile() on a LIST of q values keeps a real Index instead.
s = pd.Series(arr)


def np_percentile_on_series(series):
    # Return np.percentile(series, 50) -- a bare NumPy scalar, not a Series.
    #   return np.percentile(series, 50)
    ...


def series_quantile_multi(series):
    # Return series.quantile([0.25, 0.5, 0.75]) -- a Series with the q
    # values themselves as the Index.
    #   return series.quantile([0.25, 0.5, 0.75])
    ...


# ex2_np_result = np_percentile_on_series(s)
ex2_np_result = ...
# ex2_multi_series = series_quantile_multi(s)
ex2_multi_series = ...
try:
    ex2_np_is_not_series = not isinstance(ex2_np_result, pd.Series)
    ex2_multi_has_index = list(ex2_multi_series.index) == [0.25, 0.5, 0.75]
except Exception:
    ex2_np_is_not_series = False
    ex2_multi_has_index = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: plain np.percentile() has no skipna concept -- one
# NaN anywhere poisons the whole result to NaN. Series.quantile() drops NaN
# automatically by default and returns a real number.
arr_nan = np.array([1.0, 2.0, np.nan, 4.0])
s_nan = pd.Series(arr_nan)

# ex3_np_nan_result = np.percentile(arr_nan, 50)
ex3_np_nan_result = ...
# ex3_series_nan_result = s_nan.quantile(0.5)
ex3_series_nan_result = ...
try:
    ex3_np_is_nan = bool(np.isnan(ex3_np_nan_result))
    ex3_series_is_real = bool(not pd.isna(ex3_series_nan_result))
except Exception:
    ex3_np_is_nan = False
    ex3_series_is_real = False

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
    check("Exercise 1: np.percentile()/np.quantile() agree on matching scales; multi-q returns an ordered array",
          lambda: ex1_scales_match is True and ex1_multi_ok is True),
    check("Exercise 2: np.percentile() on a Series returns a bare scalar (no Index); Series.quantile() keeps one",
          lambda: ex2_np_is_not_series is True and ex2_multi_has_index is True),
    check("Exercise 3: plain np.percentile() poisons to NaN; Series.quantile() drops NaN and returns a real number",
          lambda: ex3_np_is_nan is True and ex3_series_is_real is True),
]

print("\nAll green — lesson 111 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
