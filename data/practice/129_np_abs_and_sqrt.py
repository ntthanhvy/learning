# Practice 129 — np.abs() and np.sqrt(): the two building blocks under every
# error-metric column
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/129_np_abs_and_sqrt.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.abs() preserves an int Series' own dtype; np.sqrt()
# always upcasts to float64; Series.sqrt() does not exist at all.
s_int = pd.Series([-5, 3, -2], index=["a", "b", "c"])


def abs_dtype(s):
    # Return the dtype (as a string) of np.abs(s).
    #   return str(np.abs(s).dtype)
    ...


def sqrt_dtype(s):
    # Return the dtype (as a string) of np.sqrt(s.abs()) (use .abs() first so
    # sqrt never sees a negative number here).
    #   return str(np.sqrt(s.abs()).dtype)
    ...


def series_has_sqrt_method(s):
    # Return True if calling s.sqrt() raises AttributeError, else False.
    #   try:
    #       s.sqrt()
    #       return False
    #   except AttributeError:
    #       return True
    ...


ex1_abs_dtype = abs_dtype(s_int)
ex1_sqrt_dtype = sqrt_dtype(s_int)
ex1_no_sqrt_method = series_has_sqrt_method(s_int)
try:
    ex1_abs_stays_int = ex1_abs_dtype == "int64"
    ex1_sqrt_upcasts = ex1_sqrt_dtype == "float64"
    ex1_no_sqrt_method_correct = ex1_no_sqrt_method is True
except Exception:
    ex1_abs_stays_int = False
    ex1_sqrt_upcasts = False
    ex1_no_sqrt_method_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.sqrt() on a negative returns NaN; np.abs() on
# int64's own most negative possible value silently overflows back to the
# same negative number (no warning, no error).
arrf = np.array([-4.0, 9.0])
minval = np.iinfo(np.int64).min
arr_minint = np.array([minval], dtype=np.int64)


def sqrt_of(a):
    # Return np.sqrt(a).
    #   return np.sqrt(a)
    ...


def abs_of_int64_min(a):
    # Return np.abs(a).
    #   return np.abs(a)
    ...


ex2_sqrt_result = sqrt_of(arrf)
ex2_abs_result = abs_of_int64_min(arr_minint)
try:
    ex2_negative_sqrt_is_nan = bool(pd.isna(ex2_sqrt_result[0]))
    ex2_positive_sqrt_correct = bool(ex2_sqrt_result[1] == 3.0)
    # The overflow: np.abs() on int64's floor returns the SAME negative value.
    ex2_abs_overflow_stays_negative = int(ex2_abs_result[0]) == minval
except Exception:
    ex2_negative_sqrt_is_nan = False
    ex2_positive_sqrt_correct = False
    ex2_abs_overflow_stays_negative = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: an end-to-end mean-absolute-error and RMSE built
# from np.abs() and np.sqrt() together, no loop.
actual = pd.Series([10, 20, 30])
predicted = pd.Series([12, 18, 33])


def mean_absolute_error(a, p):
    # Return the mean of np.abs(a - p).
    #   return np.abs(a - p).mean()
    ...


def rmse(a, p):
    # Return np.sqrt of the mean of the squared error (a - p) ** 2.
    #   err = a - p
    #   return np.sqrt((err ** 2).mean())
    ...


ex3_mae = mean_absolute_error(actual, predicted)
ex3_rmse = rmse(actual, predicted)
try:
    ex3_mae_correct = abs(float(ex3_mae) - 2.3333333333333335) < 1e-9
    ex3_rmse_correct = abs(float(ex3_rmse) - 2.3804761428476167) < 1e-9
except Exception:
    ex3_mae_correct = False
    ex3_rmse_correct = False

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
    check("Exercise 1: np.abs() preserves int64; np.sqrt() always upcasts to float64; Series.sqrt() does not exist",
          lambda: ex1_abs_stays_int is True and ex1_sqrt_upcasts is True
          and ex1_no_sqrt_method_correct is True),
    check("Exercise 2: np.sqrt() of a negative returns NaN; np.abs() on int64's floor silently overflows back to itself",
          lambda: ex2_negative_sqrt_is_nan is True and ex2_positive_sqrt_correct is True
          and ex2_abs_overflow_stays_negative is True),
    check("Exercise 3: mean absolute error and RMSE built from np.abs() and np.sqrt(), no loop",
          lambda: ex3_mae_correct is True and ex3_rmse_correct is True),
]

print("\nAll green — lesson 129 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
