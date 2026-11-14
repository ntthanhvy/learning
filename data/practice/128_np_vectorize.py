# Practice 128 — np.vectorize(): a name that promises vectorization and
# does not deliver it
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/128_np_vectorize.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.vectorize() gives the identical result to a
# plain Python loop over the same function, since it IS one under the hood.
def classify(x):
    if x > 100:
        return "high"
    elif x > 50:
        return "mid"
    else:
        return "low"


values = [10, 60, 150, 30, 99]


def classify_via_loop(vals):
    # Return a plain Python list, calling classify() once per value via a
    # list comprehension (not a `for` statement, but still a per-element
    # Python loop under the hood).
    #   return [classify(v) for v in vals]
    ...


def classify_via_vectorize(vals):
    # Wrap classify() with np.vectorize() and call it on vals.
    #   return np.vectorize(classify)(vals)
    ...


ex1_loop_result = classify_via_loop(values)
ex1_vec_result = classify_via_vectorize(values)
try:
    ex1_matches_loop = list(ex1_vec_result) == list(ex1_loop_result)
except Exception:
    ex1_matches_loop = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.vectorize() broadcasts two differently-shaped
# array arguments together; calling it on a Series returns a bare ndarray,
# not a Series.
def addxy(x, y):
    return x + y


col = np.array([[1], [2], [3]])
row = np.array([10, 20, 30])


def broadcast_add(a, b):
    # Wrap addxy() with np.vectorize() and call it on a and b.
    #   return np.vectorize(addxy)(a, b)
    ...


ser = pd.Series([1, 2, 3])


def vectorized_on_series(s):
    # Wrap classify() with np.vectorize() and call it directly on a Series.
    #   return np.vectorize(classify)(s)
    ...


ex2_broadcast_result = broadcast_add(col, row)
ex2_series_result = vectorized_on_series(ser)
try:
    ex2_broadcast_shape_correct = ex2_broadcast_result.shape == (3, 3)
    ex2_broadcast_values_correct = list(ex2_broadcast_result[0]) == [11, 21, 31]
    # The result on a Series must be a bare ndarray, NOT a Series.
    ex2_result_is_ndarray = isinstance(ex2_series_result, np.ndarray)
    ex2_result_is_not_series = not isinstance(ex2_series_result, pd.Series)
except Exception:
    ex2_broadcast_shape_correct = False
    ex2_broadcast_values_correct = False
    ex2_result_is_ndarray = False
    ex2_result_is_not_series = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: cache=True does not stop repeated identical values
# from being recomputed -- it only skips the one dtype-calibration call.
calls_log = []


def counting(x):
    calls_log.append(x)
    return x * 2


def run_with_cache(arr):
    # Wrap counting() with np.vectorize(..., cache=True) and call it on arr.
    #   return np.vectorize(counting, cache=True)(arr)
    ...


ex3_input = np.array([5, 5, 5, 7])
ex3_result = run_with_cache(ex3_input)
try:
    # Every element must still trigger its own call to counting(), including
    # the three repeated 5s -- cache=True does not memoize by value.
    ex3_all_values_called = len(calls_log) == len(ex3_input)
    ex3_result_correct = list(ex3_result) == [10, 10, 10, 14]
except Exception:
    ex3_all_values_called = False
    ex3_result_correct = False

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
    check("Exercise 1: np.vectorize() matches a plain per-element Python loop exactly",
          lambda: ex1_matches_loop is True),
    check("Exercise 2: np.vectorize() broadcasts differently-shaped array args; on a Series it returns a bare ndarray, not a Series",
          lambda: ex2_broadcast_shape_correct is True and ex2_broadcast_values_correct is True
          and ex2_result_is_ndarray is True and ex2_result_is_not_series is True),
    check("Exercise 3: cache=True does not memoize by value -- repeated identical inputs are still recomputed every time",
          lambda: ex3_all_values_called is True and ex3_result_correct is True),
]

print("\nAll green — lesson 128 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
