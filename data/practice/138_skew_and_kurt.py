# Practice 138 — Series.skew() and .kurt(): shape statistics, and the
# min-count NaN trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/138_skew_and_kurt.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .skew()'s sign names the direction the long tail
# stretches. A right-tailed Series (one huge HIGH outlier) scores positive;
# a left-tailed Series (one huge LOW outlier, otherwise clustered high) scores
# negative.
right_tail = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 100])
left_tail = pd.Series([1, 97, 98, 98, 98, 99, 99, 99, 100])


def right_tail_skew():
    # Return right_tail.skew().
    #   return right_tail.skew()
    ...


def left_tail_skew():
    # Return left_tail.skew().
    #   return left_tail.skew()
    ...


ex1_right_skew = right_tail_skew()
ex1_left_skew = left_tail_skew()
try:
    ex1_right_is_positive = float(ex1_right_skew) > 0
    ex1_left_is_negative = float(ex1_left_skew) < 0
except Exception:
    ex1_right_is_positive = False
    ex1_left_is_negative = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2 + the callout: pandas' .kurt() reports EXCESS
# kurtosis, so a large random-normal sample scores close to 0 (not the raw
# textbook value of 3). Separately, a 2-element Series is below both
# .skew()'s minimum of 3 and .kurt()'s minimum of 4 non-null values, so both
# return a silent NaN rather than raising.
rng = np.random.default_rng(42)
normal_sample = pd.Series(rng.normal(size=100_000))
tiny = pd.Series([5.0, 6.0])


def normal_sample_kurt():
    # Return normal_sample.kurt().
    #   return normal_sample.kurt()
    ...


def tiny_skew():
    # Return tiny.skew() (only 2 values -- below skew()'s min of 3).
    #   return tiny.skew()
    ...


def tiny_kurt():
    # Return tiny.kurt() (only 2 values -- below kurt()'s min of 4).
    #   return tiny.kurt()
    ...


ex2_normal_kurt = normal_sample_kurt()
ex2_tiny_skew = tiny_skew()
ex2_tiny_kurt = tiny_kurt()
try:
    ex2_kurt_near_zero = abs(float(ex2_normal_kurt)) < 0.1
    ex2_tiny_skew_is_nan = pd.isna(ex2_tiny_skew)
    ex2_tiny_kurt_is_nan = pd.isna(ex2_tiny_kurt)
except Exception:
    ex2_kurt_near_zero = False
    ex2_tiny_skew_is_nan = False
    ex2_tiny_kurt_is_nan = False

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
    check("Exercise 1: right-tailed Series scores positive skew, left-tailed scores negative",
          lambda: ex1_right_is_positive is True and ex1_left_is_negative is True),
    check("Exercise 2: large normal sample's kurt() is near 0 (excess, not raw 3); tiny Series skew()/kurt() are NaN",
          lambda: ex2_kurt_near_zero is True and ex2_tiny_skew_is_nan is True and ex2_tiny_kurt_is_nan is True),
]

print("\nAll green — lesson 138 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
