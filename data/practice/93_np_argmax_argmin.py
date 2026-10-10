# Practice 93 — np.argmax() / np.argmin(): positions, flattening, and a NaN trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/93_np_argmax_argmin.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.argmax() with no axis= flattens the array first,
# returning one flat position. np.unravel_index() translates it back to the
# real (row, col) position.
# ex1_flat_pos = np.argmax(arr)
# ex1_row_col = np.unravel_index(ex1_flat_pos, arr.shape)
arr = np.array([
    [3, 7, 2],
    [5, 5, 1],
    [0, 0, 0],
])
ex1_flat_pos = ...
try:
    ex1_row_col = np.unravel_index(ex1_flat_pos, arr.shape)
    ex1_flat_is_1 = bool(ex1_flat_pos == 1)
    ex1_points_at_true_max = bool(arr[ex1_row_col] == arr.max())
    ex1_per_row = np.argmax(arr, axis=1)
    ex1_per_row_matches = bool(list(ex1_per_row) == [1, 0, 0])
except Exception:
    ex1_flat_is_1 = False
    ex1_points_at_true_max = False
    ex1_per_row_matches = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: a flat tie resolves to the first occurrence, by
# position -- the same rule idxmax()/idxmin() already use.
# ex2_tie_winner = np.argmax(tie)
tie = np.array([4, 9, 9, 2])
ex2_tie_winner = ...
try:
    ex2_is_first_nine = bool(ex2_tie_winner == 1)
    ex2_not_second_nine = bool(ex2_tie_winner != 2)
except Exception:
    ex2_is_first_nine = False
    ex2_not_second_nine = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: plain np.argmax() has no skipna option, so a NaN
# in the array can silently win -- it lands on the NaN's own position, not
# the real max. np.nanargmax() is the NaN-safe fix.
# ex3_plain_argmax = np.argmax(nan_arr)       # lands on the NaN itself
# ex3_nanargmax = np.nanargmax(nan_arr)       # skips the NaN, finds real max
nan_arr = np.array([1.0, np.nan, 3.0])
ex3_plain_argmax = ...
ex3_nanargmax = ...
try:
    ex3_plain_hits_nan_position = bool(ex3_plain_argmax == 1)
    ex3_nanargmax_finds_real_max = bool(ex3_nanargmax == 2)
    ex3_they_differ = bool(ex3_plain_argmax != ex3_nanargmax)
except Exception:
    ex3_plain_hits_nan_position = False
    ex3_nanargmax_finds_real_max = False
    ex3_they_differ = False

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
    check("Exercise 1: no axis= flattens first; unravel_index finds the true max",
          lambda: ex1_flat_is_1 is True
          and ex1_points_at_true_max is True
          and ex1_per_row_matches is True),
    check("Exercise 2: a flat tie resolves to the first occurrence by position",
          lambda: ex2_is_first_nine is True
          and ex2_not_second_nine is True),
    check("Exercise 3: plain argmax hits the NaN; nanargmax finds the real max",
          lambda: ex3_plain_hits_nan_position is True
          and ex3_nanargmax_finds_real_max is True
          and ex3_they_differ is True),
]

print("\nAll green — lesson 93 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
