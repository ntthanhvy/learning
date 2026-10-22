# Practice 105 — Series.str.pad(): fixed-width alignment, and the sign trap
#                zfill() doesn't have
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/105_str_pad.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: side="left" (default), side="right", and
# side="both" each pad in the expected position; a string already at or
# past width= passes through unchanged.
s = pd.Series(["7", "42", "123"])

# ex1_left = s.str.pad(width=5)
ex1_left = ...
# ex1_right = s.str.pad(width=5, side="right")
ex1_right = ...
# ex1_unchanged = pd.Series(["123"]).str.pad(width=1)
ex1_unchanged = ...
try:
    ex1_left_ok = bool((ex1_left == ["    7", "   42", "  123"]).all())
    ex1_right_ok = bool((ex1_right == ["7    ", "42   ", "123  "]).all())
    ex1_unchanged_ok = bool(ex1_unchanged.iloc[0] == "123")
except Exception:
    ex1_left_ok = False
    ex1_right_ok = False
    ex1_unchanged_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: zfill() and pad(side="left", fillchar="0") agree
# on a plain positive string but disagree on a string with a leading minus
# sign -- zfill() is sign-aware, str.pad() is not.
signed = pd.Series(["-7", "42"])


def compare_zfill_and_pad(values):
    # Return a tuple (zfill_result, pad_result) where:
    #   zfill_result = values.str.zfill(5)
    #   pad_result   = values.str.pad(width=5, side="left", fillchar="0")
    # return values.str.zfill(5), values.str.pad(width=5, side="left", fillchar="0")
    ...


# ex2_zfill, ex2_pad = compare_zfill_and_pad(signed)
ex2_pair = ...
try:
    ex2_zfill, ex2_pad = ex2_pair
    ex2_zfill_ok = bool(ex2_zfill.iloc[0] == "-0007")
    ex2_pad_ok = bool(ex2_pad.iloc[0] == "000-7")
    ex2_agree_on_positive_ok = bool(ex2_zfill.iloc[1] == ex2_pad.iloc[1] == "00042")
except Exception:
    ex2_zfill_ok = False
    ex2_pad_ok = False
    ex2_agree_on_positive_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: NaN passes through .str.pad() untouched while a
# real string in the same Series gets padded.
mixed = pd.Series(["7", np.nan, "42"])

# ex3_result = mixed.str.pad(width=5, fillchar="0")
ex3_result = ...
try:
    ex3_seven_ok = bool(ex3_result[0] == "00007")
    ex3_nan_ok = bool(pd.isna(ex3_result[1]))
    ex3_fortytwo_ok = bool(ex3_result[2] == "00042")
except Exception:
    ex3_seven_ok = False
    ex3_nan_ok = False
    ex3_fortytwo_ok = False

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
    check("Exercise 1: side='left'/'right' pad the expected position, width= is a minimum",
          lambda: ex1_left_ok is True
          and ex1_right_ok is True
          and ex1_unchanged_ok is True),
    check("Exercise 2: zfill() is sign-aware, pad(fillchar='0') is not -- they disagree on '-7'",
          lambda: ex2_zfill_ok is True
          and ex2_pad_ok is True
          and ex2_agree_on_positive_ok is True),
    check("Exercise 3: NaN passes through .str.pad() untouched, real strings get padded",
          lambda: ex3_seven_ok is True
          and ex3_nan_ok is True
          and ex3_fortytwo_ok is True),
]

print("\nAll green — lesson 105 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
