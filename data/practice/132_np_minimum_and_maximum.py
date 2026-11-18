# Practice 132 — np.minimum() and np.maximum(): elementwise pairwise
# comparison, and clip()'s hidden engine
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/132_np_minimum_and_maximum.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.minimum()/np.maximum() compare two Series
# elementwise (not a reduction to one scalar), keep the Index, and are
# int-preserving when both inputs are already int64.
a = pd.Series([1, 5, 3], index=["x", "y", "z"])
b = pd.Series([4, 2, 3], index=["x", "y", "z"])


def elementwise_min(s1, s2):
    # Return np.minimum(s1, s2).
    #   return np.minimum(s1, s2)
    ...


def elementwise_max(s1, s2):
    # Return np.maximum(s1, s2).
    #   return np.maximum(s1, s2)
    ...


ex1_min_result = elementwise_min(a, b)
ex1_max_result = elementwise_max(a, b)
try:
    ex1_min_values = ex1_min_result.tolist() == [1, 2, 3]
    ex1_max_values = ex1_max_result.tolist() == [4, 5, 3]
    ex1_min_dtype_int = str(ex1_min_result.dtype) == "int64"
    ex1_index_kept = list(ex1_min_result.index) == ["x", "y", "z"]
except Exception:
    ex1_min_values = False
    ex1_max_values = False
    ex1_min_dtype_int = False
    ex1_index_kept = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: Series.clip(lower=, upper=) is confirmed identical
# to np.minimum(np.maximum(x, lower), upper).
x = pd.Series([1, 10, 5, -3])
lower = pd.Series([0, 0, 0, 0])
upper = pd.Series([8, 8, 8, 8])


def clip_via_minimum_maximum(s, lo, hi):
    # Reproduce s.clip(lower=lo, upper=hi) using only np.minimum()/np.maximum().
    #   return np.minimum(np.maximum(s, lo), hi)
    ...


ex2_builtin_clip = x.clip(lower=lower, upper=upper)
ex2_manual_clip = clip_via_minimum_maximum(x, lower, upper)
try:
    ex2_clip_matches = ex2_builtin_clip.tolist() == ex2_manual_clip.tolist()
    ex2_clip_expected = ex2_builtin_clip.tolist() == [1, 8, 5, 0]
except Exception:
    ex2_clip_matches = False
    ex2_clip_expected = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: np.minimum()/np.maximum() propagate NaN silently
# if either side is NaN; np.fmin()/np.fmax() skip NaN and return the real
# value instead.
c = pd.Series([1.0, np.nan, 3.0])
d = pd.Series([2.0, 5.0, np.nan])


def nan_propagating_min(s1, s2):
    # Return np.minimum(s1, s2).
    #   return np.minimum(s1, s2)
    ...


def nan_skipping_min(s1, s2):
    # Return np.fmin(s1, s2).
    #   return np.fmin(s1, s2)
    ...


ex3_minimum_result = nan_propagating_min(c, d)
ex3_fmin_result = nan_skipping_min(c, d)
try:
    ex3_minimum_has_nan = bool(pd.isna(ex3_minimum_result.iloc[1])) and bool(pd.isna(ex3_minimum_result.iloc[2]))
    ex3_fmin_skips_nan = ex3_fmin_result.tolist() == [1.0, 5.0, 3.0]
except Exception:
    ex3_minimum_has_nan = False
    ex3_fmin_skips_nan = False

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
    check("Exercise 1: np.minimum()/np.maximum() compare elementwise, keep the Index, stay int64",
          lambda: ex1_min_values is True and ex1_max_values is True
          and ex1_min_dtype_int is True and ex1_index_kept is True),
    check("Exercise 2: clip(lower=, upper=) equals minimum(maximum(x, lower), upper)",
          lambda: ex2_clip_matches is True and ex2_clip_expected is True),
    check("Exercise 3: np.minimum() propagates NaN; np.fmin() skips it and returns the real value",
          lambda: ex3_minimum_has_nan is True and ex3_fmin_skips_nan is True),
]

print("\nAll green — lesson 132 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
