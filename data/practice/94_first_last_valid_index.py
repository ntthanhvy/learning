# Practice 94 — first_valid_index() / last_valid_index(): trimming the NaN
# padding off a time series
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/94_first_last_valid_index.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: first_valid_index()/last_valid_index() return the
# real row LABEL (not a position). Slicing between them trims leading/
# trailing NaN padding while leaving a real gap in the MIDDLE untouched.
# ex1_first = temp.first_valid_index()
# ex1_last = temp.last_valid_index()
# ex1_trimmed = temp.loc[ex1_first:ex1_last]
temp = pd.Series(
    [np.nan, np.nan, 20.1, 21.4, np.nan, 19.8, np.nan, np.nan],
    index=pd.date_range("2026-01-01", periods=8, freq="D"),
)
ex1_first = ...
ex1_last = ...
try:
    ex1_first_is_jan3 = bool(ex1_first == pd.Timestamp("2026-01-03"))
    ex1_last_is_jan6 = bool(ex1_last == pd.Timestamp("2026-01-06"))
    ex1_trimmed = temp.loc[ex1_first:ex1_last]
    ex1_trimmed_len_is_4 = bool(len(ex1_trimmed) == 4)
    # the real middle gap (2026-01-05) must survive the trim, still NaN
    ex1_middle_gap_kept = bool(pd.isna(ex1_trimmed.loc["2026-01-05"]))
except Exception:
    ex1_first_is_jan3 = False
    ex1_last_is_jan6 = False
    ex1_trimmed_len_is_4 = False
    ex1_middle_gap_kept = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: on a DataFrame there is no per-column version --
# first_valid_index() looks across the WHOLE row and returns one label for
# the first row where ANY column has a real value.
# ex2_first = ex2_df.first_valid_index()
# ex2_last = ex2_df.last_valid_index()
ex2_df = pd.DataFrame(
    {
        "a": [np.nan, np.nan, 1, 2],
        "b": [np.nan, 3, np.nan, np.nan],
    },
    index=["w", "x", "y", "z"],
)
ex2_first = ...
ex2_last = ...
try:
    # row "w" is all-NaN; row "x" has b=3, so it wins even though a is still NaN there
    ex2_first_is_x = bool(ex2_first == "x")
    ex2_last_is_z = bool(ex2_last == "z")
except Exception:
    ex2_first_is_x = False
    ex2_last_is_z = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2's sharper trap: an all-NaN Series and an empty
# Series both return None quietly -- no exception -- unlike idxmax() on an
# all-NaN input, which raises ValueError (Lessons 20/91/93).
# ex3_allnan_result = allnan.first_valid_index()
# ex3_empty_result = empty.first_valid_index()
allnan = pd.Series([np.nan, np.nan])
empty = pd.Series([], dtype=float)
ex3_allnan_result = ...
ex3_empty_result = ...
try:
    ex3_allnan_is_none = ex3_allnan_result is None
    ex3_empty_is_none = ex3_empty_result is None
    # confirm idxmax() on the same all-NaN data raises, as the contrast
    ex3_idxmax_raises = False
    try:
        allnan.idxmax()
    except ValueError:
        ex3_idxmax_raises = True
except Exception:
    ex3_allnan_is_none = False
    ex3_empty_is_none = False
    ex3_idxmax_raises = False

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
    check("Exercise 1: first/last_valid_index return real labels; slicing trims edges, keeps the middle gap",
          lambda: ex1_first_is_jan3 is True
          and ex1_last_is_jan6 is True
          and ex1_trimmed_len_is_4 is True
          and ex1_middle_gap_kept is True),
    check("Exercise 2: on a DataFrame, one label for the whole row, not per column",
          lambda: ex2_first_is_x is True
          and ex2_last_is_z is True),
    check("Exercise 3: all-NaN/empty return None quietly; idxmax() raises on the same data",
          lambda: ex3_allnan_is_none is True
          and ex3_empty_is_none is True
          and ex3_idxmax_raises is True),
]

print("\nAll green — lesson 94 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
