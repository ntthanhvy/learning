# Practice 125 — np.take(): fancy indexing that also works on plain lists,
# with a mode= safety valve
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/125_np_take.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.take() matches fancy indexing on an ndarray, but
# ALSO works directly on a plain Python list, where list[[...]] raises
# TypeError.
arr = np.array([10, 20, 30, 40, 50])
plain_list = [10, 20, 30, 40, 50]


def take_from_array(a, positions):
    # Return np.take(a, positions).
    #   return np.take(a, positions)
    ...


def take_from_list(lst, positions):
    # Return np.take(lst, positions) -- works even though lst is a plain list.
    #   return np.take(lst, positions)
    ...


ex1_array_result = take_from_array(arr, [0, 2, 4])
ex1_list_result = take_from_list(plain_list, [0, 2])
try:
    ex1_array_correct = ex1_array_result.tolist() == [10, 30, 50]
    ex1_list_is_array = isinstance(ex1_list_result, np.ndarray)
    ex1_list_correct = ex1_list_result.tolist() == [10, 30]
    # Confirm the gap: plain fancy indexing on the list itself raises TypeError.
    try:
        plain_list[[0, 2]]
        ex1_fancy_index_raises = False
    except TypeError:
        ex1_fancy_index_raises = True
except Exception:
    ex1_array_correct = False
    ex1_list_is_array = False
    ex1_list_correct = False
    ex1_fancy_index_raises = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2 (the mode= trap): the default mode="raise" crashes
# on an out-of-bounds index just like fancy indexing. mode="clip" pins an
# out-of-range index to the nearest valid position instead -- and clips a
# NEGATIVE out-of-range index to position 0 (the first element), not the
# last one the way ordinary negative indexing treats -1.
small_arr = np.array([10, 20, 30, 40, 50])


def take_default_raises(a, positions):
    # Call np.take(a, positions) with the default mode and return whether it
    # raised an IndexError (True) or not (False).
    #   try:
    #       np.take(a, positions)
    #       return False
    #   except IndexError:
    #       return True
    ...


def take_clip(a, positions):
    # Return np.take(a, positions, mode="clip").
    #   return np.take(a, positions, mode="clip")
    ...


ex2_raised = take_default_raises(small_arr, [10])
ex2_clip_result = take_clip(small_arr, [10, -10])
try:
    ex2_default_raises_correct = ex2_raised is True
    # index 10 clips to the last element (50); index -10 clips to the FIRST
    # element (10), not the last one -- clip mode disables negative wraparound.
    ex2_clip_correct = ex2_clip_result.tolist() == [50, 10]
except Exception:
    ex2_default_raises_correct = False
    ex2_clip_correct = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: axis=0 selects rows from a 2-D array (not a
# flattened lookup). Series.take() is position-based and keeps the
# ORIGINAL index labels on whichever rows got selected -- it never
# renumbers to a fresh RangeIndex.
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ser = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])


def take_rows(g, positions):
    # Return np.take(g, positions, axis=0) -- whole rows at the given positions.
    #   return np.take(g, positions, axis=0)
    ...


def take_series_rows(s, positions):
    # Return s.take(positions) -- pandas' own position-based take().
    #   return s.take(positions)
    ...


ex3_rows_result = take_rows(grid, [0, 2])
ex3_series_result = take_series_rows(ser, [0, 2, 4])
try:
    ex3_rows_correct = ex3_rows_result.tolist() == [[1, 2, 3], [7, 8, 9]]
    ex3_series_values_correct = ex3_series_result.tolist() == [10, 30, 50]
    # The original labels a, c, e must survive -- NOT renumbered to 0, 1, 2.
    ex3_series_labels_preserved = ex3_series_result.index.tolist() == ["a", "c", "e"]
except Exception:
    ex3_rows_correct = False
    ex3_series_values_correct = False
    ex3_series_labels_preserved = False

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
    check("Exercise 1: np.take() matches fancy indexing on an array, and also works directly on a plain Python list where list[[...]] raises TypeError",
          lambda: ex1_array_correct is True and ex1_list_is_array is True
          and ex1_list_correct is True and ex1_fancy_index_raises is True),
    check("Exercise 2: default mode='raise' raises IndexError on an out-of-bounds index; mode='clip' pins +10 to the last element and -10 to the FIRST element",
          lambda: ex2_default_raises_correct is True and ex2_clip_correct is True),
    check("Exercise 3: axis=0 selects whole rows from a 2-D array; Series.take() keeps the original index labels on the selected rows, never renumbering them",
          lambda: ex3_rows_correct is True and ex3_series_values_correct is True
          and ex3_series_labels_preserved is True),
]

print("\nAll green — lesson 125 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
