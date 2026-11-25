# Practice 139 — Series.sem(): the std()-derived ratio, and the
# constant-column contrast with skew()/kurt()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/139_sem.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .sem() equals .std() divided by the square root of
# the count, exactly, on the same Series.
s = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])


def s_sem():
    # Return s.sem().
    #   return s.sem()
    ...


def s_std_over_sqrt_n():
    # Return s.std() divided by np.sqrt(len(s)).
    #   return s.std() / np.sqrt(len(s))
    ...


ex1_sem = s_sem()
ex1_std_over_sqrt_n = s_std_over_sqrt_n()
try:
    ex1_matches = abs(float(ex1_sem) - float(ex1_std_over_sqrt_n)) < 1e-9
except Exception:
    ex1_matches = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2/3/4: a one-element Series's .sem() is NaN (the
# inherited single-row ddof=1 trap, same root cause as Lesson 137's .std()).
# A constant 10-value Series's .sem() is a real 0.0 -- the OPPOSITE of
# Lesson 138's .skew()/.kurt() on the identical kind of input, which both
# return NaN on a constant column.
single = pd.Series([42.0])
constant = pd.Series([5.0] * 10)


def single_sem():
    # Return single.sem().
    #   return single.sem()
    ...


def constant_sem():
    # Return constant.sem().
    #   return constant.sem()
    ...


def constant_skew():
    # Return constant.skew() (for contrast -- expect NaN, not 0.0).
    #   return constant.skew()
    ...


ex2_single_sem = single_sem()
ex2_constant_sem = constant_sem()
ex2_constant_skew = constant_skew()
try:
    ex2_single_is_nan = pd.isna(ex2_single_sem)
    ex2_constant_sem_is_zero = float(ex2_constant_sem) == 0.0
    ex2_constant_skew_is_nan = pd.isna(ex2_constant_skew)
except Exception:
    ex2_single_is_nan = False
    ex2_constant_sem_is_zero = False
    ex2_constant_skew_is_nan = False

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
    check("Exercise 1: sem() equals std() / sqrt(count) exactly",
          lambda: ex1_matches is True),
    check("Exercise 2: single-row sem() is NaN; constant-column sem() is 0.0 while skew() is NaN",
          lambda: ex2_single_is_nan is True and ex2_constant_sem_is_zero is True and ex2_constant_skew_is_nan is True),
]

print("\nAll green — lesson 139 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
