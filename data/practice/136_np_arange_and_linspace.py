# Practice 136 — np.arange() vs np.linspace(): the float-step trap,
# plus np.zeros()/np.ones()/np.full()/np.empty()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/136_np_arange_and_linspace.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1/2: np.arange()'s stop is EXCLUSIVE (same convention
# as Python's range()); np.linspace()'s stop is INCLUSIVE by default. On the
# same (0, 10) span, arange(0, 10, 2) has 5 elements and never reaches 10;
# linspace(0, 10, 5) also has 5 elements, but its last one IS exactly 10.0.
start = 0
stop = 10


def arange_result():
    # Return np.arange(start, stop, 2).
    #   return np.arange(start, stop, 2)
    ...


def linspace_result():
    # Return np.linspace(start, stop, 5).
    #   return np.linspace(start, stop, 5)
    ...


ex1_arange = arange_result()
ex1_linspace = linspace_result()
try:
    ex1_arange_len = len(ex1_arange)
    ex1_arange_excludes_stop = stop not in [float(v) for v in ex1_arange]
    ex1_linspace_len = len(ex1_linspace)
    ex1_linspace_includes_stop = float(ex1_linspace[-1]) == float(stop)
except Exception:
    ex1_arange_len = -1
    ex1_arange_excludes_stop = False
    ex1_linspace_len = -1
    ex1_linspace_includes_stop = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: np.zeros()/np.ones() default to float64 regardless
# of shape; np.full() infers its dtype FROM the fill value instead (int fill
# -> int64 array); np.empty() does NOT reliably contain zeros -- its values
# are uninitialized leftover memory, unlike np.zeros().
shape = 3
fill_value = 7


def zeros_result():
    # Return np.zeros(shape).
    #   return np.zeros(shape)
    ...


def full_result():
    # Return np.full(shape, fill_value).
    #   return np.full(shape, fill_value)
    ...


def empty_result():
    # Return np.empty(shape).
    #   return np.empty(shape)
    ...


ex2_zeros = zeros_result()
ex2_full = full_result()
ex2_empty = empty_result()
try:
    ex2_zeros_is_float64 = np.asarray(ex2_zeros).dtype == np.float64
    ex2_full_is_int64 = np.asarray(ex2_full).dtype == np.int64
    # np.empty() doesn't promise zeros -- just confirm it ran and produced
    # an array of the right shape/dtype-kind, without asserting its values.
    ex2_empty_right_shape = np.asarray(ex2_empty).shape == (shape,)
except Exception:
    ex2_zeros_is_float64 = False
    ex2_full_is_int64 = False
    ex2_empty_right_shape = False

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
    check("Exercise 1: arange(0,10,2) excludes 10 (5 elems); linspace(0,10,5) includes 10",
          lambda: ex1_arange_len == 5 and ex1_arange_excludes_stop is True
          and ex1_linspace_len == 5 and ex1_linspace_includes_stop is True),
    check("Exercise 2: zeros() is float64, full(7) infers int64, empty() has right shape",
          lambda: ex2_zeros_is_float64 is True and ex2_full_is_int64 is True
          and ex2_empty_right_shape is True),
]

print("\nAll green — lesson 136 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
