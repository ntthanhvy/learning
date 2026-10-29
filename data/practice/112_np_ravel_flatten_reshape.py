# Practice 112 — np.ravel() vs .flatten(): the view-or-copy trap hiding
#               behind two functions that look interchangeable
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/112_np_ravel_flatten_reshape.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: .flatten() and .ravel() produce the identical
# flattened values and order on a plain 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# ex1_flat = arr.flatten()
ex1_flat = ...
# ex1_rav = arr.ravel()
ex1_rav = ...
try:
    ex1_same_values = ex1_flat.tolist() == ex1_rav.tolist() == [1, 2, 3, 4, 5, 6]
except Exception:
    ex1_same_values = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: the aliasing trap. Mutating a .flatten() result
# never changes the original array; mutating a .ravel() result DOES, because
# ravel() returned a view here (the array is plain and contiguous).


def mutate_flatten_result(a):
    # Flatten `a` with .flatten(), set index 0 of the result to 999, and
    # return the ORIGINAL array `a` afterward (to check it stayed unchanged).
    #   f = a.flatten()
    #   f[0] = 999
    #   return a
    ...


def mutate_ravel_result(a):
    # Flatten `a` with .ravel(), set index 0 of the result to 999, and
    # return the ORIGINAL array `a` afterward (to check it changed too).
    #   r = a.ravel()
    #   r[0] = 999
    #   return a
    ...


# ex2_after_flatten = mutate_flatten_result(np.array([[1, 2, 3], [4, 5, 6]]))
ex2_after_flatten = ...
# ex2_after_ravel = mutate_ravel_result(np.array([[1, 2, 3], [4, 5, 6]]))
ex2_after_ravel = ...
try:
    ex2_flatten_unaffected = ex2_after_flatten.tolist() == [[1, 2, 3], [4, 5, 6]]
    ex2_ravel_affected = ex2_after_ravel.tolist() == [[999, 2, 3], [4, 5, 6]]
except Exception:
    ex2_flatten_unaffected = False
    ex2_ravel_affected = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 4: .reshape(-1) matches .ravel()'s flattened output,
# and an incompatible target shape raises ValueError rather than guessing.
arr2 = np.array([[1, 2, 3], [4, 5, 6]])


def reshape_flat(a):
    # Return a.reshape(-1) -- -1 tells NumPy to infer the single dimension.
    #   return a.reshape(-1)
    ...


def reshape_bad_shape(a):
    # Try a.reshape(4, 2) (6 elements don't fit 4x2) inside a try/except,
    # returning True if ValueError was raised, False otherwise.
    #   try:
    #       a.reshape(4, 2)
    #       return False
    #   except ValueError:
    #       return True
    ...


# ex3_reshaped = reshape_flat(arr2)
ex3_reshaped = ...
# ex3_bad_shape_raised = reshape_bad_shape(arr2)
ex3_bad_shape_raised = ...
try:
    ex3_matches_ravel = ex3_reshaped.tolist() == arr2.ravel().tolist()
    ex3_raised_value_error = ex3_bad_shape_raised is True
except Exception:
    ex3_matches_ravel = False
    ex3_raised_value_error = False

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
    check("Exercise 1: .flatten() and .ravel() agree on the same flattened values and order",
          lambda: ex1_same_values is True),
    check("Exercise 2: mutating .flatten()'s result leaves the original untouched; mutating .ravel()'s result changes it",
          lambda: ex2_flatten_unaffected is True and ex2_ravel_affected is True),
    check("Exercise 3: .reshape(-1) matches .ravel(); an incompatible shape raises ValueError",
          lambda: ex3_matches_ravel is True and ex3_raised_value_error is True),
]

print("\nAll green — lesson 112 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
