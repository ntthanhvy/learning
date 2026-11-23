# Practice 137 — Series.std()/.var() vs np.std()/np.var(): the ddof=1 vs
# ddof=0 trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/137_std_var_and_ddof.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1/2: pandas' Series.std() defaults to ddof=1 (sample,
# divide by count - 1); np.std() defaults to ddof=0 (population, divide by
# plain count). On the SAME 8 values they disagree by default, but passing
# a matching ddof= on either side makes the two equal.
values = [2, 4, 4, 4, 5, 5, 7, 9]
s = pd.Series(values)
arr = np.array(values, dtype=float)


def pandas_default_std():
    # Return s.std() (pandas' own default -- do not pass ddof= here).
    #   return s.std()
    ...


def numpy_default_std():
    # Return np.std(arr) (numpy's own default -- do not pass ddof= here).
    #   return np.std(arr)
    ...


def numpy_std_matching_pandas():
    # Return np.std(arr, ddof=1) -- matches pandas' default exactly.
    #   return np.std(arr, ddof=1)
    ...


ex1_pandas_default = pandas_default_std()
ex1_numpy_default = numpy_default_std()
ex1_numpy_ddof1 = numpy_std_matching_pandas()
try:
    ex1_defaults_disagree = float(ex1_pandas_default) != float(ex1_numpy_default)
    ex1_matched_after_ddof = abs(float(ex1_pandas_default) - float(ex1_numpy_ddof1)) < 1e-9
except Exception:
    ex1_defaults_disagree = False
    ex1_matched_after_ddof = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: a one-element Series's .std() is silently NaN under
# pandas' own ddof=1 default (dividing by count - 1 = 0), while np.std() on
# that same single value is a real, non-NaN number (ddof=0 divides by 1).
single = pd.Series([5.0])
single_arr = np.array([5.0])


def single_pandas_std():
    # Return single.std() (pandas' own default).
    #   return single.std()
    ...


def single_numpy_std():
    # Return np.std(single_arr) (numpy's own default).
    #   return np.std(single_arr)
    ...


ex2_pandas_std = single_pandas_std()
ex2_numpy_std = single_numpy_std()
try:
    ex2_pandas_is_nan = pd.isna(ex2_pandas_std)
    ex2_numpy_is_real = (not pd.isna(ex2_numpy_std)) and float(ex2_numpy_std) == 0.0
except Exception:
    ex2_pandas_is_nan = False
    ex2_numpy_is_real = False

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
    check("Exercise 1: pandas std() and np.std() disagree by default, match once ddof=1 is passed",
          lambda: ex1_defaults_disagree is True and ex1_matched_after_ddof is True),
    check("Exercise 2: single-value Series .std() is NaN under pandas' default; np.std() is a real 0.0",
          lambda: ex2_pandas_is_nan is True and ex2_numpy_is_real is True),
]

print("\nAll green — lesson 137 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
