# Practice 133 — np.round(): rounding to the nearest even digit, not the
# nearest half
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/133_np_round.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd
from decimal import Decimal

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: banker's rounding (round-half-to-even) on an exact
# .5 tie: 0.5 -> 0, 1.5 -> 2, 2.5 -> 2 (NOT always rounding up). Index kept
# on a Series.
ties = pd.Series([0.5, 1.5, 2.5], index=["a", "b", "c"])


def round_ties(s):
    # Return np.round(s) (no decimals= needed -- default is 0).
    #   return np.round(s)
    ...


ex1_result = round_ties(ties)
try:
    ex1_values_correct = ex1_result.tolist() == [0.0, 2.0, 2.0]
    ex1_index_kept = list(ex1_result.index) == ["a", "b", "c"]
except Exception:
    ex1_values_correct = False
    ex1_index_kept = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: decimals= controls digit count (including
# negative values rounding left of the decimal point); an int64 Series is
# a true no-op.
price = 1234.5678
s_int = pd.Series([10, 20, 30], dtype="int64")


def round_to_hundred(x):
    # Round x to the nearest hundred using decimals=-2.
    #   return np.round(x, decimals=-2)
    ...


def round_int_series(s):
    # Return np.round(s) -- should be a true no-op on an int64 Series.
    #   return np.round(s)
    ...


ex2_hundred = round_to_hundred(price)
ex2_int_result = round_int_series(s_int)
try:
    ex2_hundred_correct = float(ex2_hundred) == 1200.0
    ex2_int_is_noop = (ex2_int_result.tolist() == [10, 20, 30]
                        and str(ex2_int_result.dtype) == "int64")
except Exception:
    ex2_hundred_correct = False
    ex2_int_is_noop = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: 2.675 is not stored exactly in float64 (checked
# against Decimal()'s own exact stored value); np.rint() matches
# np.round(x, 0).
trap_value = 2.675


def stored_value_is_below_tie(x):
    # Using Decimal(x), return True if the exact stored float value is
    # strictly less than 2.675 (i.e. already below the halfway tie).
    #   return Decimal(x) < Decimal("2.675")
    ...


def rint_matches_round0(x):
    # Return True if np.rint(x) equals np.round(x, 0).
    #   return bool(np.rint(x) == np.round(x, 0))
    ...


ex3_below_tie = stored_value_is_below_tie(trap_value)
ex3_rint_matches = rint_matches_round0(trap_value)
try:
    ex3_below_tie_correct = ex3_below_tie is True
    ex3_rint_matches_correct = ex3_rint_matches is True
    ex3_round_result_is_2_68 = bool(np.round(trap_value, 2) == 2.68)
except Exception:
    ex3_below_tie_correct = False
    ex3_rint_matches_correct = False
    ex3_round_result_is_2_68 = False

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
    check("Exercise 1: np.round() uses banker's rounding on .5 ties (0.5->0, 1.5->2, 2.5->2), Index kept",
          lambda: ex1_values_correct is True and ex1_index_kept is True),
    check("Exercise 2: decimals=-2 rounds to the nearest hundred; np.round() is a true no-op on int64",
          lambda: ex2_hundred_correct is True and ex2_int_is_noop is True),
    check("Exercise 3: 2.675 is stored below the halfway tie in float64; np.rint() matches np.round(x, 0)",
          lambda: ex3_below_tie_correct is True and ex3_rint_matches_correct is True
          and ex3_round_result_is_2_68 is True),
]

print("\nAll green — lesson 133 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
