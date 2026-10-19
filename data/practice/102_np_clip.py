# Practice 102 — np.clip(): the array-level clamp underneath Series.clip()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/102_np_clip.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.clip() on a plain NumPy array clamps every
# value inside [lower, upper]; values already inside pass through untouched.
arr = np.array([120.0, 5.0, 999.0, 50.0])

# ex1_clipped = np.clip(arr, 50, 150)
ex1_clipped = ...
try:
    ex1_clipped_ok = bool(np.array_equal(ex1_clipped, np.array([120.0, 50.0, 150.0, 50.0])))
except Exception:
    ex1_clipped_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 1: np.clip() on a pandas Series returns a Series
# back, byte-identical to calling Series.clip() directly.
s = pd.Series([120.0, 5.0, 999.0, 50.0])

# ex2_np_result = np.clip(s, 50, 150)
ex2_np_result = ...
# ex2_series_result = s.clip(lower=50, upper=150)
ex2_series_result = ...
try:
    ex2_is_series_ok = bool(isinstance(ex2_np_result, pd.Series))
    ex2_matches_ok = bool(np.array_equal(ex2_np_result.to_numpy(), ex2_series_result.to_numpy()))
except Exception:
    ex2_is_series_ok = False
    ex2_matches_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2: lower > upper does not raise -- every value
# silently becomes the upper bound instead.

arr2 = np.array([1.0, 2.0, 3.0, 4.0])


def clip_with_swapped_bounds(a):
    # Call np.clip(a, 150, 50) -- lower=150 is bigger than upper=50.
    # Just return the result; np.clip() itself will not raise here.
    # return np.clip(a, 150, 50)
    ...


# ex3_result = clip_with_swapped_bounds(arr2)
ex3_result = ...
try:
    ex3_all_fifty_ok = bool(np.array_equal(ex3_result, np.array([50.0, 50.0, 50.0, 50.0])))
except Exception:
    ex3_all_fifty_ok = False

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
    check("Exercise 1: np.clip() clamps a plain array into [lower, upper]",
          lambda: ex1_clipped_ok is True),
    check("Exercise 2: np.clip() on a Series returns a Series, identical to Series.clip()",
          lambda: ex2_is_series_ok is True
          and ex2_matches_ok is True),
    check("Exercise 3: lower > upper silently collapses every value to upper, no error",
          lambda: ex3_all_fifty_ok is True),
]

print("\nAll green — lesson 102 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
