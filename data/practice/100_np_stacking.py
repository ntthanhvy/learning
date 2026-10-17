# Practice 100 — np.vstack() / np.hstack() / np.column_stack(): the array
# layer under pd.concat()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/100_np_stacking.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: on two 1-D arrays, vstack returns 2-D (one row per
# array), hstack stays 1-D (just concatenated), column_stack returns the
# column-shaped 2-D opposite of vstack.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# ex1_v = np.vstack([a, b])
ex1_v = ...
# ex1_h = np.hstack([a, b])
ex1_h = ...
# ex1_c = np.column_stack([a, b])
ex1_c = ...
try:
    ex1_v_shape_ok = bool(ex1_v.shape == (2, 3))
    ex1_v_values_ok = bool(np.array_equal(ex1_v, np.array([[1, 2, 3], [4, 5, 6]])))
    ex1_h_shape_ok = bool(ex1_h.shape == (6,))
    ex1_h_values_ok = bool(np.array_equal(ex1_h, np.array([1, 2, 3, 4, 5, 6])))
    ex1_c_shape_ok = bool(ex1_c.shape == (3, 2))
    ex1_c_values_ok = bool(np.array_equal(ex1_c, np.array([[1, 4], [2, 5], [3, 6]])))
except Exception:
    ex1_v_shape_ok = False
    ex1_v_values_ok = False
    ex1_h_shape_ok = False
    ex1_h_values_ok = False
    ex1_c_shape_ok = False
    ex1_c_values_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: on 2-D arrays, vstack matches concatenate(axis=0)
# and hstack matches concatenate(axis=1), exactly.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# ex2_vstack = np.vstack([A, B])
ex2_vstack = ...
# ex2_concat_axis0 = np.concatenate([A, B], axis=0)
ex2_concat_axis0 = ...
# ex2_hstack = np.hstack([A, B])
ex2_hstack = ...
# ex2_concat_axis1 = np.concatenate([A, B], axis=1)
ex2_concat_axis1 = ...
try:
    ex2_vstack_matches_ok = bool(np.array_equal(ex2_vstack, ex2_concat_axis0))
    ex2_hstack_matches_ok = bool(np.array_equal(ex2_hstack, ex2_concat_axis1))
    ex2_vstack_shape_ok = bool(ex2_vstack.shape == (4, 2))
    ex2_hstack_shape_ok = bool(ex2_hstack.shape == (2, 4))
except Exception:
    ex2_vstack_matches_ok = False
    ex2_hstack_matches_ok = False
    ex2_vstack_shape_ok = False
    ex2_hstack_shape_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: a shape mismatch raises ValueError (no silent
# NaN-fill the way pd.concat() does); stacking int + float upcasts to float64.
mismatched_short = np.array([1, 2])


def raises_value_error(fn):
    # Call fn() with no arguments; return True if it raises ValueError,
    # False if it returns normally (any other exception should propagate).
    # try:
    #     fn()
    #     return False
    # except ValueError:
    #     return True
    ...


# ex3_raised = raises_value_error(lambda: np.vstack([a, mismatched_short]))
ex3_raised = ...

ints = np.array([1, 2, 3])
floats = np.array([1.5, 2.5, 3.5])
# ex3_mixed = np.vstack([ints, floats])
ex3_mixed = ...
try:
    ex3_raised_ok = bool(ex3_raised is True)
    ex3_dtype_ok = bool(ex3_mixed.dtype == np.float64)
except Exception:
    ex3_raised_ok = False
    ex3_dtype_ok = False

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
    check("Exercise 1: vstack is 2-D (rows), hstack stays 1-D, column_stack is 2-D (columns)",
          lambda: ex1_v_shape_ok is True
          and ex1_v_values_ok is True
          and ex1_h_shape_ok is True
          and ex1_h_values_ok is True
          and ex1_c_shape_ok is True
          and ex1_c_values_ok is True),
    check("Exercise 2: vstack(2-D) matches concatenate(axis=0), hstack(2-D) matches concatenate(axis=1)",
          lambda: ex2_vstack_matches_ok is True
          and ex2_hstack_matches_ok is True
          and ex2_vstack_shape_ok is True
          and ex2_hstack_shape_ok is True),
    check("Exercise 3: shape mismatch raises ValueError; int+float stacking upcasts to float64",
          lambda: ex3_raised_ok is True
          and ex3_dtype_ok is True),
]

print("\nAll green — lesson 100 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
