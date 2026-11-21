# Practice 135 — np.mod()/np.remainder() vs np.fmod(): the sign trap,
# plus np.power()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/135_np_mod_and_power.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import warnings

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1/2: np.mod()/np.remainder() use floored division
# (sign of the divisor); np.fmod() uses C-style truncated division (sign of
# the dividend). On (-7, 3) they disagree: mod gives 2, fmod gives -1.
# np.mod and np.remainder are literally the same function object.
dividend = -7
divisor = 3


def mod_result(a, b):
    # Return np.mod(a, b).
    #   return np.mod(a, b)
    ...


def fmod_result(a, b):
    # Return np.fmod(a, b).
    #   return np.fmod(a, b)
    ...


def mod_is_remainder():
    # Return True if np.mod is the identical object as np.remainder.
    #   return np.mod is np.remainder
    ...


ex1_mod = mod_result(dividend, divisor)
ex1_fmod = fmod_result(dividend, divisor)
ex1_identity = mod_is_remainder()
try:
    ex1_mod_correct = int(ex1_mod) == 2
    ex1_fmod_correct = int(ex1_fmod) == -1
    ex1_identity_correct = ex1_identity is True
except Exception:
    ex1_mod_correct = False
    ex1_fmod_correct = False
    ex1_identity_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: np.divmod() returns (floor_divide, mod) as a
# tuple; np.power() with a negative base and a fractional float exponent
# returns NaN, not the real root, with a RuntimeWarning (suppress it here --
# it's the expected trap, not a bug).
neg_base = -8.0
third = 1 / 3


def divmod_result(a, b):
    # Return np.divmod(a, b) as a tuple.
    #   return np.divmod(a, b)
    ...


def power_neg_fractional(base, exp):
    # Return np.power(base, exp), suppressing the expected RuntimeWarning.
    #   with warnings.catch_warnings():
    #       warnings.simplefilter("ignore", RuntimeWarning)
    #       return np.power(base, exp)
    ...


ex2_divmod = divmod_result(dividend, divisor)
ex2_power = power_neg_fractional(neg_base, third)
try:
    q, r = (float(v) for v in ex2_divmod)
    ex2_divmod_correct = (q, r) == (-3.0, 2.0)
    ex2_power_is_nan = bool(np.isnan(float(ex2_power)))
except Exception:
    ex2_divmod_correct = False
    ex2_power_is_nan = False

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
    check("Exercise 1: np.mod(-7,3)=2, np.fmod(-7,3)=-1, np.mod is np.remainder",
          lambda: ex1_mod_correct is True and ex1_fmod_correct is True
          and ex1_identity_correct is True),
    check("Exercise 2: np.divmod(-7,3)=(-3,2); np.power(-8.0, 1/3) is NaN",
          lambda: ex2_divmod_correct is True and ex2_power_is_nan is True),
]

print("\nAll green — lesson 135 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
