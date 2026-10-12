# Practice 95 — np.repeat() and np.tile(): two different ways to multiply an
# array, and why broadcasting usually beats both
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/95_np_repeat_and_tile.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.repeat() repeats each element IN PLACE, grouped
# together -- either a flat scalar count, or a per-element counts array.
# ex1_scalar = np.repeat(arr, 3)
# ex1_counts = np.repeat(arr, [1, 2, 3])
arr = np.array([10, 20, 30])
ex1_scalar = ...
ex1_counts = ...
try:
    ex1_scalar_ok = bool(np.array_equal(ex1_scalar, [10, 10, 10, 20, 20, 20, 30, 30, 30]))
    ex1_counts_ok = bool(np.array_equal(ex1_counts, [10, 20, 20, 30, 30, 30]))
except Exception:
    ex1_scalar_ok = False
    ex1_counts_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.tile() repeats the WHOLE array as one block,
# a visibly different order from repeat() on the identical input.
# ex2_tiled = np.tile(arr, 3)
ex2_tiled = ...
try:
    ex2_tiled_ok = bool(np.array_equal(ex2_tiled, [10, 20, 30, 10, 20, 30, 10, 20, 30]))
    # repeat and tile must disagree on this input -- different granularity
    ex2_differs_from_repeat = not bool(np.array_equal(ex2_tiled, ex1_scalar))
except Exception:
    ex2_tiled_ok = False
    ex2_differs_from_repeat = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: pair repeat() with tile() to build a cartesian
# customer x date grid, then confirm plain broadcasting reaches the same
# numbers as a tile()-materialized version, without building the extra copy.
# ex3_customer_col = np.repeat(customers, len(dates))
# ex3_date_col = np.tile(dates, len(customers))
# ex3_broadcast_result = arr * 1.1
customers = np.array(["An", "Binh"])
dates = pd.date_range("2026-01-01", periods=3, freq="D")
ex3_customer_col = ...
ex3_date_col = ...
ex3_broadcast_result = ...
try:
    ex3_grid = pd.DataFrame({"customer": ex3_customer_col, "date": ex3_date_col})
    ex3_grid_len_is_6 = bool(len(ex3_grid) == 6)
    ex3_first_is_an = bool(ex3_grid.iloc[0]["customer"] == "An")
    ex3_last_is_binh = bool(ex3_grid.iloc[-1]["customer"] == "Binh")
    # the tile()-materialized version of the same scale-up, for comparison
    ex3_tiled_scale = np.tile([1.1], len(arr))
    ex3_matches_broadcast = bool(np.allclose(ex3_broadcast_result, arr * ex3_tiled_scale))
except Exception:
    ex3_grid_len_is_6 = False
    ex3_first_is_an = False
    ex3_last_is_binh = False
    ex3_matches_broadcast = False

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
    check("Exercise 1: np.repeat() repeats each element in place, scalar and per-element counts",
          lambda: ex1_scalar_ok is True
          and ex1_counts_ok is True),
    check("Exercise 2: np.tile() repeats the whole array as one block, differs from repeat()",
          lambda: ex2_tiled_ok is True
          and ex2_differs_from_repeat is True),
    check("Exercise 3: repeat()+tile() build a cartesian grid; broadcasting matches a tiled scale-up",
          lambda: ex3_grid_len_is_6 is True
          and ex3_first_is_an is True
          and ex3_last_is_binh is True
          and ex3_matches_broadcast is True),
]

print("\nAll green — lesson 95 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
