# Practice 134 — np.trunc(): the fourth rounding direction, and np.fix()'s
# retirement
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/134_np_trunc_and_fix.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import warnings

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.trunc() rounds toward zero (chops the
# fraction), not toward a neighbor. On -1.7, floor/ceil/trunc/round land on
# four values with exactly two of them equal (ceil and trunc both -1.0).
pos_val = 1.7
neg_val = -1.7


def trunc_toward_zero(x):
    # Return np.trunc(x).
    #   return np.trunc(x)
    ...


ex1_pos = trunc_toward_zero(pos_val)
ex1_neg = trunc_toward_zero(neg_val)


def four_way_on_neg(x):
    # Return a tuple (floor, ceil, trunc, round) of np.floor(x), np.ceil(x),
    # np.trunc(x), np.round(x) on x.
    #   return (np.floor(x), np.ceil(x), np.trunc(x), np.round(x))
    ...


ex1_four_way = four_way_on_neg(neg_val)
try:
    ex1_pos_correct = float(ex1_pos) == 1.0
    ex1_neg_correct = float(ex1_neg) == -1.0
    four = tuple(float(v) for v in ex1_four_way)
    ex1_four_way_correct = four == (-2.0, -1.0, -1.0, -2.0)
except Exception:
    ex1_pos_correct = False
    ex1_neg_correct = False
    ex1_four_way_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.fix() matches np.trunc() value-for-value
# (just deprecated, not numerically different); an int64 Series is a true
# no-op under np.trunc().
mixed = np.array([1.9, -1.9, 2.5, -2.5])
s_int = pd.Series([1, -2, 3], dtype="int64")


def fix_matches_trunc(a):
    # Return True if np.fix(a) equals np.trunc(a) elementwise, for every
    # element. Suppress the DeprecationWarning while calling np.fix --
    # that warning is expected, not a bug.
    #   with warnings.catch_warnings():
    #       warnings.simplefilter("ignore", DeprecationWarning)
    #       return bool(np.array_equal(np.fix(a), np.trunc(a)))
    ...


def trunc_int_series(s):
    # Return np.trunc(s) -- should be a true no-op on an int64 Series.
    #   return np.trunc(s)
    ...


ex2_fix_matches = fix_matches_trunc(mixed)
ex2_int_result = trunc_int_series(s_int)
try:
    ex2_fix_matches_correct = ex2_fix_matches is True
    ex2_int_is_noop = (ex2_int_result.tolist() == [1, -2, 3]
                        and str(ex2_int_result.dtype) == "int64")
except Exception:
    ex2_fix_matches_correct = False
    ex2_int_is_noop = False

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
    check("Exercise 1: np.trunc() rounds toward zero; floor/ceil/trunc/round on -1.7 give (-2,-1,-1,-2)",
          lambda: ex1_pos_correct is True and ex1_neg_correct is True
          and ex1_four_way_correct is True),
    check("Exercise 2: np.fix() matches np.trunc() value-for-value; np.trunc() is a true no-op on int64",
          lambda: ex2_fix_matches_correct is True and ex2_int_is_noop is True),
]

print("\nAll green — lesson 134 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
