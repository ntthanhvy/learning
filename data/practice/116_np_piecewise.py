# Practice 116 — np.piecewise(): the conditional-branching sibling of
#               np.select() -- and the Series footgun hiding inside it
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/116_np_piecewise.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1-2: each function in funclist runs ONLY on the slice
# of x matching its own condition. A function count of len(condlist) + 1 makes
# the extra, final function the "otherwise" default for unmatched elements.
x = np.array([-5.0, -1.0, 0.0, 2.0, 10.0])


def square_negative_pass_rest(arr):
    # Return np.piecewise(arr, [arr < 0, arr >= 0], [lambda v: v**2, lambda v: v])
    # -- squares the negative slice, passes the non-negative slice through.
    #   return np.piecewise(arr, [arr < 0, arr >= 0], [lambda v: v**2, lambda v: v])
    ...


def below_zero_else_ninety_nine(arr):
    # One condition, TWO functions: len(condlist) + 1 means the 2nd function
    # is the "otherwise" default, run wherever the condition was False.
    # Return np.piecewise(arr, [arr < 0], [lambda v: -1, 99])
    #   return np.piecewise(arr, [arr < 0], [lambda v: -1, 99])
    ...


# ex1_branched = square_negative_pass_rest(x)
ex1_branched = ...
# ex1_with_default = below_zero_else_ninety_nine(x)
ex1_with_default = ...
try:
    ex1_branched_ok = list(ex1_branched) == [25.0, 1.0, 0.0, 2.0, 10.0]
    ex1_default_ok = list(ex1_with_default) == [-1.0, -1.0, 99.0, 99.0, 99.0]
except Exception:
    ex1_branched_ok = False
    ex1_default_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: an element matching NO condition and given no extra
# default function comes back as plain 0, not NaN. A wrong function count
# (neither len(condlist) nor len(condlist) + 1) raises ValueError.
def no_match_defaults_to_zero(arr):
    # Return np.piecewise(arr, [arr < -100], [lambda v: -1]) -- nothing in
    # arr is below -100, so every element falls through to the default: 0.
    #   return np.piecewise(arr, [arr < -100], [lambda v: -1])
    ...


# ex2_unmatched = no_match_defaults_to_zero(x)
ex2_unmatched = ...
try:
    ex2_unmatched_is_zero = list(ex2_unmatched) == [0.0, 0.0, 0.0, 0.0, 0.0]
except Exception:
    ex2_unmatched_is_zero = False

try:
    # 1 condition, 3 functions -- neither 1 nor 2 -- must raise ValueError.
    np.piecewise(x, [x < 0], [lambda v: v, lambda v: v, lambda v: v])
    ex2_wrong_count_raises = False
except ValueError:
    ex2_wrong_count_raises = True
except Exception:
    ex2_wrong_count_raises = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: passing condlist as a list of pandas Series (not
# converted to ndarray) raises a confusing IndexError. Converting each
# CONDITION with .to_numpy() fixes it -- x itself may stay a Series.
s = pd.Series([-5.0, -1.0, 0.0, 2.0, 10.0])


def broken_series_conditions(series):
    # Build conditions as plain Series (NOT converted) and call piecewise
    # with them directly -- this is expected to raise IndexError.
    #   conds = [series < 0, series >= 0]
    #   funcs = [lambda v: v ** 2, lambda v: v]
    #   return np.piecewise(series, conds, funcs)
    conds = [series < 0, series >= 0]
    funcs = [lambda v: v ** 2, lambda v: v]
    return np.piecewise(series, conds, funcs)


def fixed_series_conditions(series):
    # Same idea, but each CONDITION is converted via .to_numpy() first.
    # series itself may stay a Series -- only the conditions need converting.
    #   conds = [(series < 0).to_numpy(), (series >= 0).to_numpy()]
    #   funcs = [lambda v: v ** 2, lambda v: v]
    #   return np.piecewise(series, conds, funcs)
    conds = [(series < 0).to_numpy(), (series >= 0).to_numpy()]
    funcs = [lambda v: v ** 2, lambda v: v]
    return ...


try:
    broken_series_conditions(s)
    ex3_broken_raises = False
except IndexError:
    ex3_broken_raises = True
except Exception:
    ex3_broken_raises = False

try:
    ex3_fixed = fixed_series_conditions(s)
    ex3_fixed_ok = list(ex3_fixed) == [25.0, 1.0, 0.0, 2.0, 10.0]
    ex3_fixed_is_ndarray = isinstance(ex3_fixed, np.ndarray)
except Exception:
    ex3_fixed_ok = False
    ex3_fixed_is_ndarray = False

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
    check("Exercise 1: funclist runs per-condition slice; len(condlist)+1 gives an 'otherwise' default",
          lambda: ex1_branched_ok is True and ex1_default_ok is True),
    check("Exercise 2: an unmatched element with no default defaults to 0; wrong function count raises ValueError",
          lambda: ex2_unmatched_is_zero is True and ex2_wrong_count_raises is True),
    check("Exercise 3: a list of un-converted Series conditions raises IndexError; .to_numpy() on each condition fixes it",
          lambda: ex3_broken_raises is True and ex3_fixed_ok is True
          and ex3_fixed_is_ndarray is True),
]

print("\nAll green — lesson 116 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
