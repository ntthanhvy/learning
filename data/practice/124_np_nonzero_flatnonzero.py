# Practice 124 — np.nonzero() and np.flatnonzero(): finding WHERE, and a
# tuple that is always truthy
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/124_np_nonzero_flatnonzero.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.nonzero(arr) returns a 1-element tuple (for a
# 1-D array) holding the array of matching index positions -- usable
# directly to index straight back into the original array.
arr = np.array([0, 5, 0, -3, 0, 8])


def nonzero_positions(a):
    # Return np.nonzero(a) -- the raw tuple result, unchanged.
    #   return np.nonzero(a)
    ...


def values_at_nonzero(a):
    # Return a[np.nonzero(a)] -- using the tuple result to index back into a.
    #   return a[np.nonzero(a)]
    ...


ex1_tuple_result = nonzero_positions(arr)
ex1_values = values_at_nonzero(arr)
try:
    ex1_is_tuple = isinstance(ex1_tuple_result, tuple)
    ex1_tuple_len_is_one = len(ex1_tuple_result) == 1
    ex1_positions_correct = ex1_tuple_result[0].tolist() == [1, 3, 5]
    ex1_values_correct = ex1_values.tolist() == [5, -3, 8]
except Exception:
    ex1_is_tuple = False
    ex1_tuple_len_is_one = False
    ex1_positions_correct = False
    ex1_values_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2 (the always-truthy-tuple trap): np.nonzero() on a
# 1-D array ALWAYS returns a 1-element tuple, whether or not anything
# matched -- so bool(np.nonzero(all_zero_arr)) is True even with zero real
# matches. np.count_nonzero() is the correct "how many matched" function.
all_zero_arr = np.array([0, 0, 0])


def nonzero_tuple_truthiness(a):
    # Return bool(np.nonzero(a)) -- the (misleading) truth value of the tuple.
    #   return bool(np.nonzero(a))
    ...


def real_match_count(a):
    # Return np.count_nonzero(a) -- the actual count of non-zero elements.
    #   return np.count_nonzero(a)
    ...


ex2_bool_result = nonzero_tuple_truthiness(all_zero_arr)
ex2_count_result = real_match_count(all_zero_arr)
try:
    # The trap: the tuple reads True even though NOTHING matched.
    ex2_tuple_is_truthy_anyway = bool(ex2_bool_result is True)
    # The real count, from the correctly-named function, is 0.
    ex2_count_is_zero = bool(ex2_count_result == 0)
except Exception:
    ex2_tuple_is_truthy_anyway = False
    ex2_count_is_zero = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: np.flatnonzero() returns a plain array, not a
# tuple -- no truthiness trap on a non-empty result. NaN has a non-zero bit
# pattern, so it is counted as "non-zero" by both functions, confirmed on
# both np.nonzero() and np.flatnonzero().
arr_nan = np.array([0.0, np.nan, 1.0, 0.0])


def flat_positions(a):
    # Return np.flatnonzero(a) -- the flat array result (not a tuple).
    #   return np.flatnonzero(a)
    ...


ex3_flat_result = flat_positions(arr)
ex3_flat_nan_result = flat_positions(arr_nan)
try:
    ex3_flat_is_array = isinstance(ex3_flat_result, np.ndarray)
    ex3_flat_not_tuple = not isinstance(ex3_flat_result, tuple)
    ex3_flat_positions_correct = ex3_flat_result.tolist() == [1, 3, 5]
    # NaN sits at position 1 -- it must be INCLUDED in the result (non-zero bit pattern).
    ex3_nan_position_included = bool(1 in ex3_flat_nan_result.tolist())
except Exception:
    ex3_flat_is_array = False
    ex3_flat_not_tuple = False
    ex3_flat_positions_correct = False
    ex3_nan_position_included = False

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
    check("Exercise 1: np.nonzero(arr) returns a 1-element tuple holding correct positions, usable to index back into arr",
          lambda: ex1_is_tuple is True and ex1_tuple_len_is_one is True
          and ex1_positions_correct is True and ex1_values_correct is True),
    check("Exercise 2: bool(np.nonzero(all_zero_arr)) is True despite zero matches; np.count_nonzero() correctly reports 0",
          lambda: ex2_tuple_is_truthy_anyway is True and ex2_count_is_zero is True),
    check("Exercise 3: np.flatnonzero() returns a plain array (not a tuple), and NaN's position is included as non-zero",
          lambda: ex3_flat_is_array is True and ex3_flat_not_tuple is True
          and ex3_flat_positions_correct is True and ex3_nan_position_included is True),
]

print("\nAll green — lesson 124 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
