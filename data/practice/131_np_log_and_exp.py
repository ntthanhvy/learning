# Practice 131 — np.log() and np.exp(): the skew-fix transform, and its undo
# button
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/131_np_log_and_exp.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.log()/np.exp() always upcast an int Series to
# float64 (same rule as np.sqrt(), not the int-preserving rule np.floor()/
# np.ceil()/np.abs() follow). Series.log()/Series.exp() do not exist at all.
s_int = pd.Series([1, 10, 100], index=["a", "b", "c"])


def log_dtype(s):
    # Return the dtype (as a string) of np.log(s).
    #   return str(np.log(s).dtype)
    ...


def exp_dtype(s):
    # Return the dtype (as a string) of np.exp(s).
    #   return str(np.exp(s).dtype)
    ...


def series_has_log_method(s):
    # Return True if calling s.log() raises AttributeError, else False.
    #   try:
    #       s.log()
    #       return False
    #   except AttributeError:
    #       return True
    ...


ex1_log_dtype = log_dtype(s_int)
ex1_exp_dtype = exp_dtype(s_int)
ex1_no_log_method = series_has_log_method(s_int)
try:
    ex1_log_is_float64 = ex1_log_dtype == "float64"
    ex1_exp_is_float64 = ex1_exp_dtype == "float64"
    ex1_no_log_method_correct = ex1_no_log_method is True
except Exception:
    ex1_log_is_float64 = False
    ex1_exp_is_float64 = False
    ex1_no_log_method_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.log(0) is -inf (with a warning, not an
# exception); np.log() of a negative is NaN instead; np.log1p(0) is a clean
# 0.0 with neither problem.
vals = pd.Series([0.0, -5.0, 10.0])


def log_of(s):
    # Return np.log(s).
    #   return np.log(s)
    ...


def log1p_of_zero():
    # Return np.log1p(0.0).
    #   return np.log1p(0.0)
    ...


ex2_log_result = log_of(vals)
ex2_log1p_zero = log1p_of_zero()
try:
    ex2_log_zero_is_neginf = bool(ex2_log_result.iloc[0] == float("-inf"))
    ex2_log_negative_is_nan = bool(pd.isna(ex2_log_result.iloc[1]))
    ex2_log1p_zero_is_clean = bool(float(ex2_log1p_zero) == 0.0)
except Exception:
    ex2_log_zero_is_neginf = False
    ex2_log_negative_is_nan = False
    ex2_log1p_zero_is_clean = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: an end-to-end log-transform-then-reverse round
# trip, checked with np.isclose() rather than == (float round-trip noise).
prices = pd.Series([10.0, 1000.0, 50000.0])


def round_trip(p):
    # Transform with np.log(), then reverse with np.exp(). Return the result.
    #   return np.exp(np.log(p))
    ...


ex3_back = round_trip(prices)
try:
    # == would fail here from float round-trip noise -- np.isclose() is the
    # correct check, same rule Lesson 117's np.isclose()/np.allclose() taught.
    ex3_round_trip_close = bool(np.isclose(ex3_back, prices).all())
    ex3_round_trip_not_exact = not bool((ex3_back == prices).all())
except Exception:
    ex3_round_trip_close = False
    ex3_round_trip_not_exact = False

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
    check("Exercise 1: np.log()/np.exp() always upcast int64 to float64; Series.log() does not exist",
          lambda: ex1_log_is_float64 is True and ex1_exp_is_float64 is True
          and ex1_no_log_method_correct is True),
    check("Exercise 2: np.log(0) is -inf, np.log(negative) is NaN, np.log1p(0) is a clean 0.0",
          lambda: ex2_log_zero_is_neginf is True and ex2_log_negative_is_nan is True
          and ex2_log1p_zero_is_clean is True),
    check("Exercise 3: exp(log(x)) round-trips closely (np.isclose()) but not exactly (==)",
          lambda: ex3_round_trip_close is True and ex3_round_trip_not_exact is True),
]

print("\nAll green — lesson 131 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
