# Practice 117 — np.isclose() and np.allclose(): comparing floats without
#                ever using ==
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/117_np_isclose_allclose.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1-2: plain == fails on floats that are "the same"
# number due to binary rounding. np.isclose() is element-wise ("close
# enough" per position); np.allclose() is isclose() followed by .all(),
# one single bool for the whole comparison.
a = np.array([1.0, 2.0, 3.0])
b = np.array([1.0 + 1e-9, 2.0, 3.00001])


def classic_float_trap():
    # Return 0.1 + 0.2 == 0.3 -- the textbook floating-point rounding trap.
    #   return 0.1 + 0.2 == 0.3
    ...


def classic_float_fixed():
    # Return np.isclose(0.1 + 0.2, 0.3) -- the same comparison, "close
    # enough" instead of bit-for-bit.
    #   return np.isclose(0.1 + 0.2, 0.3)
    ...


# ex1_raw_eq = classic_float_trap()
ex1_raw_eq = ...
# ex1_isclose_fix = classic_float_fixed()
ex1_isclose_fix = ...
# ex1_elementwise = np.isclose(a, b)
ex1_elementwise = ...
# ex1_collapsed = np.allclose(a, b)
ex1_collapsed = ...
try:
    ex1_raw_eq_is_false = ex1_raw_eq is False
    ex1_isclose_fix_is_true = bool(ex1_isclose_fix) is True
    ex1_elementwise_ok = list(ex1_elementwise) == [True, True, True]
    ex1_collapsed_is_bool = isinstance(ex1_collapsed, bool) and ex1_collapsed is True
except Exception:
    ex1_raw_eq_is_false = False
    ex1_isclose_fix_is_true = False
    ex1_elementwise_ok = False
    ex1_collapsed_is_bool = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: the atol=/rtol= formula is
# abs(a - b) <= atol + rtol * abs(b). Widening atol= on purpose lets a
# real rounding-sized difference pass that the default would reject.
e = np.array([1.0, 2.0])
f = np.array([1.01, 2.0])


def default_tolerance_check(x, y):
    # Return np.isclose(x, y) -- using the default atol=1e-08, rtol=1e-05.
    #   return np.isclose(x, y)
    ...


def widened_tolerance_check(x, y):
    # Return np.isclose(x, y, atol=0.02) -- widened on purpose so a 0.01
    # difference now passes.
    #   return np.isclose(x, y, atol=0.02)
    ...


# ex2_default = default_tolerance_check(e, f)
ex2_default = ...
# ex2_widened = widened_tolerance_check(e, f)
ex2_widened = ...
try:
    ex2_default_rejects = list(ex2_default) == [False, True]
    ex2_widened_accepts = list(ex2_widened) == [True, True]
except Exception:
    ex2_default_rejects = False
    ex2_widened_accepts = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 4: NaN never counts as matching NaN by default (same
# rule as ==), even though both arrays carry it in the identical spot.
# equal_nan=True flips that one rule without touching anything else.
c = np.array([np.nan, 1.0])
d = np.array([np.nan, 1.0])


def nan_mismatch_default(x, y):
    # Return np.allclose(x, y) -- the NaN position counts as a mismatch
    # by default, so this should come back False even though the 1.0s match.
    #   return np.allclose(x, y)
    ...


def nan_mismatch_fixed(x, y):
    # Return np.allclose(x, y, equal_nan=True) -- now a shared NaN
    # position counts as matching.
    #   return np.allclose(x, y, equal_nan=True)
    ...


# ex3_default = nan_mismatch_default(c, d)
ex3_default = ...
# ex3_fixed = nan_mismatch_fixed(c, d)
ex3_fixed = ...
try:
    ex3_default_is_false = ex3_default is False
    ex3_fixed_is_true = ex3_fixed is True
except Exception:
    ex3_default_is_false = False
    ex3_fixed_is_true = False

# A scalar target broadcasts against a whole Series cleanly -- no special
# handling needed beyond ordinary broadcasting (Section 5).
s = pd.Series([2.9999999999, 3.0, 3.0000001])
try:
    ex3_series_broadcast_ok = bool(np.allclose(s, 3.0)) is True
except Exception:
    ex3_series_broadcast_ok = False

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
    check("Exercise 1: == fails on 0.1+0.2 vs 0.3; isclose()/allclose() correctly call it close",
          lambda: ex1_raw_eq_is_false is True and ex1_isclose_fix_is_true is True
          and ex1_elementwise_ok is True and ex1_collapsed_is_bool is True),
    check("Exercise 2: default atol rejects a 0.01 gap; widening atol= on purpose lets it pass",
          lambda: ex2_default_rejects is True and ex2_widened_accepts is True),
    check("Exercise 3: NaN-vs-NaN mismatches by default; equal_nan=True fixes it; Series broadcast is clean",
          lambda: ex3_default_is_false is True and ex3_fixed_is_true is True
          and ex3_series_broadcast_ok is True),
]

print("\nAll green — lesson 117 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
