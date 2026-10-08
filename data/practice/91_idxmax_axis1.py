# Practice 91 — idxmax(axis=1) / idxmin(axis=1): which COLUMN, not which row
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/91_idxmax_axis1.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: idxmax(axis=1) returns, for each ROW, the COLUMN
# NAME holding that row's max value -- the row-wise mirror of Lesson 20's
# default axis=0 case (which returns a row label instead).
# ex1_best_subjects = scores.idxmax(axis=1)
scores = pd.DataFrame({
    "math": [90, 70, 60],
    "sci": [80, 95, 60],
    "art": [70, 60, 60],
}, index=["An", "Binh", "Chi"])
ex1_best_subjects = ...
try:
    ex1_is_series = isinstance(ex1_best_subjects, pd.Series)
    ex1_index_matches_rows = list(ex1_best_subjects.index) == ["An", "Binh", "Chi"]
    ex1_an_is_math = bool(ex1_best_subjects["An"] == "math")
    ex1_binh_is_sci = bool(ex1_best_subjects["Binh"] == "sci")
except Exception:
    ex1_is_series = False
    ex1_index_matches_rows = False
    ex1_an_is_math = False
    ex1_binh_is_sci = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2's tie rule: Chi's row is math=60, sci=60, art=60, a
# flat 3-way tie. idxmax(axis=1) resolves it to the FIRST column by
# POSITION (left to right), not alphabetically. Fill in which column name
# wins Chi's tie.
# ex2_chi_winner = "math"
ex2_chi_winner = ...
try:
    ex2_flipped_order_df = scores[["art", "sci", "math"]]  # same values, columns reordered
    ex2_winner_matches = bool(scores.idxmax(axis=1)["Chi"] == ex2_chi_winner)
    ex2_reorder_changes_winner = bool(
        ex2_flipped_order_df.idxmax(axis=1)["Chi"] == "art"
    )
except Exception:
    ex2_winner_matches = False
    ex2_reorder_changes_winner = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3's NaN split: a row with SOME NaN values silently
# skips them under the default skipna=True; a row that is ENTIRELY NaN has
# nothing left to compare and raises ValueError instead. Fill in whether
# the partial-NaN case raises (True/False).
# ex3_partial_nan_raises = False
scores2 = scores.astype(float)
scores2.loc["Chi", "math"] = np.nan  # Chi: math=NaN, sci=60, art=60 -- partial
scores3 = scores.astype(float)
scores3.loc["Chi"] = np.nan  # Chi: entirely NaN
ex3_partial_nan_raises = ...
try:
    try:
        partial_result = scores2.idxmax(axis=1)
        ex3_partial_actually_raised = False
    except ValueError:
        partial_result = None
        ex3_partial_actually_raised = True
    ex3_partial_check_matches = bool(ex3_partial_actually_raised == ex3_partial_nan_raises)
    ex3_partial_chi_is_sci = (
        partial_result is not None and bool(partial_result["Chi"] == "sci")
    )

    try:
        scores3.idxmax(axis=1)
        ex3_all_nan_raised = False
    except ValueError:
        ex3_all_nan_raised = True
except Exception:
    ex3_partial_check_matches = False
    ex3_partial_chi_is_sci = False
    ex3_all_nan_raised = False

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
    check("Exercise 1: idxmax(axis=1) returns the column name holding each row's max",
          lambda: ex1_is_series is True
          and ex1_index_matches_rows is True
          and ex1_an_is_math is True
          and ex1_binh_is_sci is True),
    check("Exercise 2: an all-tied row resolves to the first column by position, not alphabetically",
          lambda: ex2_winner_matches is True
          and ex2_reorder_changes_winner is True),
    check("Exercise 3: partial-NaN row silently skips it (skipna=True); all-NaN row raises ValueError",
          lambda: ex3_partial_check_matches is True
          and ex3_partial_chi_is_sci is True
          and ex3_all_nan_raised is True),
]

print("\nAll green — lesson 91 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
