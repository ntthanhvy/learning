# Practice 127 — np.sign(): the three-way bucket code underneath a
# positive/negative/zero flag column
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/127_np_sign.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.sign() matches a nested np.where() chain exactly,
# and keeps a Series' original index when called on a Series (returns a
# Series, not a bare ndarray).
delta = pd.Series([-5, 0, 3, -2, 7], index=["a", "b", "c", "d", "e"])


def sign_via_where(s):
    # Return the same three-way bucket as np.sign(), but built from a
    # nested np.where() chain: 1 if s > 0, else -1 if s < 0, else 0.
    #   return np.where(s > 0, 1, np.where(s < 0, -1, 0))
    ...


def sign_direct(s):
    # Return np.sign(s).
    #   return np.sign(s)
    ...


ex1_where_result = sign_via_where(delta)
ex1_sign_result = sign_direct(delta)
try:
    ex1_matches_where = list(ex1_sign_result) == list(ex1_where_result)
    # Called on a Series, np.sign() must return a Series with the same index.
    ex1_is_series = isinstance(ex1_sign_result, pd.Series)
    ex1_index_kept = list(ex1_sign_result.index) == list(delta.index)
except Exception:
    ex1_matches_where = False
    ex1_is_series = False
    ex1_index_kept = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: a NaN input passes straight through as NaN, never
# bucketed into -1/0/1; a signed zero (-0.0) returns plain 0.0, not -1.
arrf = np.array([-5.0, 0.0, 3.0, np.nan, -0.0])


def sign_float(a):
    # Return np.sign(a).
    #   return np.sign(a)
    ...


ex2_result = sign_float(arrf)
try:
    # Index 3 is NaN in the input; np.sign() must leave it as NaN, not 0/-1/1.
    ex2_nan_stays_nan = bool(pd.isna(ex2_result[3]))
    # Index 4 is -0.0; np.sign() must return plain 0.0 there, not -1.
    ex2_neg_zero_is_zero = bool(ex2_result[4] == 0.0)
    # The three real values must still bucket correctly.
    ex2_real_values_correct = list(ex2_result[:3]) == [-1.0, 0.0, 1.0]
except Exception:
    ex2_nan_stays_nan = False
    ex2_neg_zero_is_zero = False
    ex2_real_values_correct = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: pandas defines no Series.sign()/DataFrame.sign() at
# all -- calling it raises AttributeError.
ser = pd.Series([-1, 0, 1])


def series_has_sign_method(s):
    # Return True if calling s.sign() raises AttributeError, else False.
    #   try:
    #       s.sign()
    #       return False
    #   except AttributeError:
    #       return True
    ...


ex3_no_sign_method = series_has_sign_method(ser)
try:
    ex3_no_sign_method_correct = ex3_no_sign_method is True
except Exception:
    ex3_no_sign_method_correct = False

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
    check("Exercise 1: np.sign() matches a nested np.where() chain exactly, and keeps a Series' own index (returns a Series, not a bare ndarray)",
          lambda: ex1_matches_where is True and ex1_is_series is True
          and ex1_index_kept is True),
    check("Exercise 2: a NaN input passes straight through as NaN (never bucketed); a signed zero (-0.0) returns plain 0.0, not -1",
          lambda: ex2_nan_stays_nan is True and ex2_neg_zero_is_zero is True
          and ex2_real_values_correct is True),
    check("Exercise 3: pandas defines no Series.sign()/DataFrame.sign() method at all; calling it raises AttributeError",
          lambda: ex3_no_sign_method_correct is True),
]

print("\nAll green — lesson 127 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
