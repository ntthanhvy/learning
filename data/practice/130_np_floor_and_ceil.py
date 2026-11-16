# Practice 130 — np.floor() and np.ceil(): rounding toward infinity, not toward
# zero
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/130_np_floor_and_ceil.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.floor()/np.ceil() are a true no-op on an int64
# Series (dtype AND values unchanged) -- unlike np.sqrt(), which always
# upcasts to float64. Series.floor() does not exist at all.
s_int = pd.Series([1, -1, 3, 7])


def floor_dtype(s):
    # Return the dtype (as a string) of np.floor(s).
    #   return str(np.floor(s).dtype)
    ...


def floor_values_unchanged(s):
    # Return True if np.floor(s) equals s everywhere (a true no-op).
    #   return bool((np.floor(s) == s).all())
    ...


def series_has_floor_method(s):
    # Return True if calling s.floor() raises AttributeError, else False.
    #   try:
    #       s.floor()
    #       return False
    #   except AttributeError:
    #       return True
    ...


ex1_floor_dtype = floor_dtype(s_int)
ex1_floor_unchanged = floor_values_unchanged(s_int)
ex1_no_floor_method = series_has_floor_method(s_int)
try:
    ex1_dtype_is_int64 = ex1_floor_dtype == "int64"
    ex1_truly_unchanged = ex1_floor_unchanged is True
    ex1_no_floor_method_correct = ex1_no_floor_method is True
except Exception:
    ex1_dtype_is_int64 = False
    ex1_truly_unchanged = False
    ex1_no_floor_method_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: on a negative input, np.floor() rounds toward
# negative infinity (away from zero), while np.trunc() rounds toward zero
# instead; Series.round() rounds to nearest (banker's rounding), a third,
# different behavior.
neg = pd.Series([-1.2, -2.5])


def floor_of(s):
    # Return np.floor(s).
    #   return np.floor(s)
    ...


def trunc_of(s):
    # Return np.trunc(s).
    #   return np.trunc(s)
    ...


def rounded_of(s):
    # Return s.round() (pandas' own nearest-rounding method).
    #   return s.round()
    ...


ex2_floor_result = floor_of(neg)
ex2_trunc_result = trunc_of(neg)
ex2_round_result = rounded_of(neg)
try:
    # floor(-1.2) == -2.0: rounds AWAY from zero (toward -infinity)
    ex2_floor_away_from_zero = float(ex2_floor_result.iloc[0]) == -2.0
    # trunc(-1.2) == -1.0: rounds TOWARD zero instead
    ex2_trunc_toward_zero = float(ex2_trunc_result.iloc[0]) == -1.0
    # round(-2.5) == -2.0 under banker's rounding (round half to even)
    ex2_round_is_nearest = float(ex2_round_result.iloc[1]) == -2.0
except Exception:
    ex2_floor_away_from_zero = False
    ex2_trunc_toward_zero = False
    ex2_round_is_nearest = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: rounding a price column DOWN to whole dollars with
# np.floor(), end to end, no loop.
prices = pd.Series([19.99, 20.01, 5.00, 100.0])


def floor_prices(p):
    # Return np.floor(p) -- each price rounded down to the nearest whole dollar.
    #   return np.floor(p)
    ...


ex3_floored = floor_prices(prices)
try:
    ex3_floored_correct = ex3_floored.tolist() == [19.0, 20.0, 5.0, 100.0]
except Exception:
    ex3_floored_correct = False

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
    check("Exercise 1: np.floor() is a true no-op on int64 (dtype + values unchanged); Series.floor() does not exist",
          lambda: ex1_dtype_is_int64 is True and ex1_truly_unchanged is True
          and ex1_no_floor_method_correct is True),
    check("Exercise 2: np.floor() rounds toward -infinity on negatives; np.trunc() rounds toward zero; Series.round() rounds to nearest",
          lambda: ex2_floor_away_from_zero is True and ex2_trunc_toward_zero is True
          and ex2_round_is_nearest is True),
    check("Exercise 3: rounding a price column down to whole dollars with np.floor(), no loop",
          lambda: ex3_floored_correct is True),
]

print("\nAll green — lesson 130 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
