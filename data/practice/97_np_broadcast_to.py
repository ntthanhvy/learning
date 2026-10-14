# Practice 97 — np.broadcast_to(): making the implicit "stretch" an explicit,
# inspectable array
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/97_np_broadcast_to.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1/2: broadcast_to() stretches arr to a target shape,
# and the result is a read-only VIEW sharing memory with arr, not a copy.
# ex1_stretched = np.broadcast_to(arr, (4, 3))
arr = np.array([1, 2, 3])
ex1_stretched = ...
try:
    ex1_shape_ok = bool(ex1_stretched.shape == (4, 3))
    ex1_values_ok = bool(np.array_equal(ex1_stretched, [[1, 2, 3]] * 4))
    ex1_shares_memory = bool(np.shares_memory(ex1_stretched, arr))
    ex1_not_writeable = bool(ex1_stretched.flags.writeable is False)
except Exception:
    ex1_shape_ok = False
    ex1_values_ok = False
    ex1_shares_memory = False
    ex1_not_writeable = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 1: an incompatible target shape raises ValueError --
# (3,) cannot stretch into (4, 4), there is no broadcasting rule for that.
# Call np.broadcast_to(arr, (4, 4)) -- it should raise.
ex2_raised = False
try:
    ...
except ValueError:
    ex2_raised = True
except Exception:
    ex2_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2: writing to the read-only view raises ValueError;
# .copy() makes an independent, writeable array and leaves arr untouched.
# Try: ex1_stretched[0, 0] = 99 -- it should raise.
ex3_write_raised = False
try:
    ...
except ValueError:
    ex3_write_raised = True
except Exception:
    ex3_write_raised = False

# ex3_copied = np.broadcast_to(arr, (4, 3)).copy()
ex3_copied = ...
try:
    ex3_copied[0, 0] = 99
    ex3_copy_writeable = bool(ex3_copied[0, 0] == 99)
    ex3_copy_independent = bool(not np.shares_memory(ex3_copied, arr))
    ex3_arr_untouched = bool(np.array_equal(arr, [1, 2, 3]))
except Exception:
    ex3_copy_writeable = False
    ex3_copy_independent = False
    ex3_arr_untouched = False

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
    check("Exercise 1: broadcast_to() stretches arr to shape, a read-only view sharing memory",
          lambda: ex1_shape_ok is True
          and ex1_values_ok is True
          and ex1_shares_memory is True
          and ex1_not_writeable is True),
    check("Exercise 2: an incompatible target shape raises ValueError",
          lambda: ex2_raised is True),
    check("Exercise 3: writing to the view raises; .copy() is writeable, independent, arr untouched",
          lambda: ex3_write_raised is True
          and ex3_copy_writeable is True
          and ex3_copy_independent is True
          and ex3_arr_untouched is True),
]

print("\nAll green — lesson 97 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
