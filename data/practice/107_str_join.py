# Practice 107 — Series.str.join(): collapsing a list column back to
#                text, and the silent NaN it leaves behind
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/107_str_join.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .str.split(sep) followed by .str.join(sep) with the
# SAME separator round-trips exactly back to the original Series.
original = pd.Series(["a,b,c", "x,y"])

# split_result = original.str.split(",")
split_result = ...
# ex1_joined_back = split_result.str.join(",")
ex1_joined_back = ...
try:
    ex1_ok = bool((ex1_joined_back == original).all())
except Exception:
    ex1_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: a row whose list has a non-string item joins to
# NaN silently (no exception at all), while a sibling row whose list is all
# strings joins normally in the SAME call.
mixed = pd.Series([["a", 1, "b"], ["c", "d"]])


def join_rows(values, sep):
    # Return values.str.join(sep) -- one line, no loop.
    #   return values.str.join(sep)
    ...


# ex2_result = join_rows(mixed, "-")
ex2_result = ...
try:
    ex2_row0_is_nan = bool(pd.isna(ex2_result.iloc[0]))
    ex2_row1_ok = bool(ex2_result.iloc[1] == "c-d")
except Exception:
    ex2_row0_is_nan = False
    ex2_row1_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: a genuine whole-row NaN (not a list at all) passes
# through .str.join() untouched, same pass-through shape as every other
# .str method this course has covered.
with_nan = pd.Series([["a", "b"], np.nan, ["c", "d"]])

# ex3_result = with_nan.str.join("-")
ex3_result = ...
try:
    ex3_row0_ok = bool(ex3_result.iloc[0] == "a-b")
    ex3_row1_is_nan = bool(pd.isna(ex3_result.iloc[1]))
    ex3_row2_ok = bool(ex3_result.iloc[2] == "c-d")
except Exception:
    ex3_row0_ok = False
    ex3_row1_is_nan = False
    ex3_row2_ok = False

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
    check("Exercise 1: .str.split() then .str.join() with the same sep round-trips exactly",
          lambda: ex1_ok is True),
    check("Exercise 2: a non-string list item makes just that row NaN; the sibling row joins fine",
          lambda: ex2_row0_is_nan is True and ex2_row1_ok is True),
    check("Exercise 3: a genuine whole-row NaN passes through .str.join() untouched",
          lambda: ex3_row0_ok is True
          and ex3_row1_is_nan is True
          and ex3_row2_ok is True),
]

print("\nAll green — lesson 107 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
