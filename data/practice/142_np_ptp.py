# Practice 142 — np.ptp(): max minus min in one call, and the
# narrow-dtype overflow trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/142_np_ptp.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# Same small DataFrame shape this lesson used throughout.
df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [10, 20, 5],
})

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1/2: np.ptp() on a 1-D array matches .max() - .min()
# exactly, and np.ptp(df, axis=0) matches each column's own range.
def ptp_1d():
    # Return np.ptp(df["b"].to_numpy()).
    #   return np.ptp(df["b"].to_numpy())
    ...


def ptp_axis0():
    # Return np.ptp(df, axis=0) -- the per-column range as a Series.
    #   return np.ptp(df, axis=0)
    ...


ex1_1d = ptp_1d()
ex1_axis0 = ptp_axis0()
try:
    ex1_1d_matches = bool(abs(float(ex1_1d) - float(df["b"].max() - df["b"].min())) < 1e-9)
    ex1_axis0_matches_a = bool(abs(float(ex1_axis0["a"]) - float(df["a"].max() - df["a"].min())) < 1e-9)
    ex1_axis0_matches_b = bool(abs(float(ex1_axis0["b"]) - float(df["b"].max() - df["b"].min())) < 1e-9)
except Exception:
    ex1_1d_matches = False
    ex1_axis0_matches_a = False
    ex1_axis0_matches_b = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: casting the same two values to int8 makes
# np.ptp() silently return a wrong negative number, while the identical
# values at a wider dtype return the correct range.
narrow = np.array([-128, 127], dtype=np.int8)
wide = np.array([-128, 127], dtype=np.int64)


def ptp_narrow():
    # Return np.ptp(narrow) -- the int8 version, expected to be WRONG.
    #   return np.ptp(narrow)
    ...


def ptp_wide():
    # Return np.ptp(wide) -- the int64 version, expected to be correct (255).
    #   return np.ptp(wide)
    ...


ex2_narrow = ptp_narrow()
ex2_wide = ptp_wide()
try:
    ex2_narrow_is_wrong = bool(int(ex2_narrow) != 255)
    ex2_wide_is_correct = bool(int(ex2_wide) == 255)
except Exception:
    ex2_narrow_is_wrong = False
    ex2_wide_is_correct = False

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
    check("Exercise 1: np.ptp() on a 1-D array and np.ptp(df, axis=0) match .max() - .min()",
          lambda: ex1_1d_matches is True and ex1_axis0_matches_a is True
          and ex1_axis0_matches_b is True),
    check("Exercise 2: np.ptp() on int8 silently overflows (wrong); on int64 it is correct (255)",
          lambda: ex2_narrow_is_wrong is True and ex2_wide_is_correct is True),
]

print("\nAll green — lesson 142 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
