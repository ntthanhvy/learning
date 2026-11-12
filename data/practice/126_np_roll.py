# Practice 126 — np.roll(): shift-with-wraparound, the sibling
# Series.shift() doesn't have
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/126_np_roll.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.roll() wraps dropped-off elements back around
# with NO NaN, where Series.shift() pads with NaN (and upcasts to float).
arr = np.array([10, 20, 30, 40, 50])
ser = pd.Series([10, 20, 30, 40, 50])


def roll_array(a, shift):
    # Return np.roll(a, shift).
    #   return np.roll(a, shift)
    ...


def shift_series(s, periods):
    # Return s.shift(periods).
    #   return s.shift(periods)
    ...


ex1_roll_result = roll_array(arr, 1)
ex1_shift_result = shift_series(ser, 1)
try:
    # roll(1): the last element (50) wraps around to become the new first element.
    ex1_roll_correct = ex1_roll_result.tolist() == [50, 10, 20, 30, 40]
    # shift(1): the first slot is NaN -- pandas upcasts the whole Series to float.
    ex1_shift_first_is_nan = pd.isna(ex1_shift_result.iloc[0])
    ex1_shift_rest_correct = ex1_shift_result.iloc[1:].tolist() == [10.0, 20.0, 30.0, 40.0]
except Exception:
    ex1_roll_correct = False
    ex1_shift_first_is_nan = False
    ex1_shift_rest_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: np.roll() accepts a plain Python list directly
# (like np.take() does), and a shift larger than the array's length just
# keeps wrapping -- equivalent to shift % len(a).
plain_list = [10, 20, 30, 40, 50]


def roll_list(lst, shift):
    # Return np.roll(lst, shift) -- works even though lst is a plain list.
    #   return np.roll(lst, shift)
    ...


def roll_oversized(a, shift):
    # Return np.roll(a, shift) where shift > len(a).
    #   return np.roll(a, shift)
    ...


ex2_list_result = roll_list(plain_list, 2)
ex2_oversized_result = roll_oversized(arr, 7)  # len(arr) == 5, so 7 wraps like shift=2
try:
    ex2_list_is_array = isinstance(ex2_list_result, np.ndarray)
    ex2_list_correct = ex2_list_result.tolist() == [40, 50, 10, 20, 30]
    # 7 % 5 == 2, so shift=7 must match shift=2 exactly.
    ex2_oversized_correct = ex2_oversized_result.tolist() == roll_array(arr, 2).tolist()
except Exception:
    ex2_list_is_array = False
    ex2_list_correct = False
    ex2_oversized_correct = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: axis=0 rolls whole ROWS in a 2-D array. There is
# no Series.roll() method at all -- calling it raises AttributeError.
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def roll_rows(g, shift):
    # Return np.roll(g, shift, axis=0) -- whole rows wrap down/up.
    #   return np.roll(g, shift, axis=0)
    ...


def series_has_roll_method(s):
    # Return True if calling s.roll(1) raises AttributeError, else False.
    #   try:
    #       s.roll(1)
    #       return False
    #   except AttributeError:
    #       return True
    ...


ex3_rows_result = roll_rows(grid, 1)
ex3_no_roll_method = series_has_roll_method(ser)
try:
    ex3_rows_correct = ex3_rows_result.tolist() == [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
    ex3_no_roll_method_correct = ex3_no_roll_method is True
except Exception:
    ex3_rows_correct = False
    ex3_no_roll_method_correct = False

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
    check("Exercise 1: np.roll() wraps the dropped-off element back around with no NaN; Series.shift() pads with NaN and upcasts to float",
          lambda: ex1_roll_correct is True and ex1_shift_first_is_nan is True
          and ex1_shift_rest_correct is True),
    check("Exercise 2: np.roll() works directly on a plain Python list; a shift larger than the array's length wraps exactly as shift % len(a)",
          lambda: ex2_list_is_array is True and ex2_list_correct is True
          and ex2_oversized_correct is True),
    check("Exercise 3: axis=0 rolls whole rows in a 2-D array; calling .roll() on a Series raises AttributeError, since pandas defines no such method",
          lambda: ex3_rows_correct is True and ex3_no_roll_method_correct is True),
]

print("\nAll green — lesson 126 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
