# Practice 123 — np.nan_to_num(): replacing NaN AND infinity in one call,
# with a default that fillna() doesn't share
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/123_np_nan_to_num.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: Series.fillna() only ever replaces NaN. Infinity is
# not a missing value to pandas at all, so fillna() leaves +inf/-inf
# completely untouched -- confirmed directly (numpy 2.5.4, pandas 3.1.1).
arr = np.array([1.0, np.nan, np.inf, -np.inf, 5.0])
ser = pd.Series(arr)


def fillna_zero(series):
    # Return series.fillna(0) as a NumPy array (use .to_numpy()).
    #   return series.fillna(0).to_numpy()
    ...


ex1_result = fillna_zero(ser)
try:
    ex1_nan_became_zero = bool(ex1_result[1] == 0.0)
    ex1_posinf_untouched = bool(np.isposinf(ex1_result[2]))
    ex1_neginf_untouched = bool(np.isneginf(ex1_result[3]))
except Exception:
    ex1_nan_became_zero = False
    ex1_posinf_untouched = False
    ex1_neginf_untouched = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2 (the default-value trap): np.nan_to_num(arr) sends
# NaN to 0.0, same instinct as fillna(0) -- but +inf goes to the dtype's own
# LARGEST finite value (~1.7977e+308 for float64), not 0, and -inf to the
# most negative one. nan=/posinf=/neginf= override all three independently.
def nan_to_num_default(a):
    # Return np.nan_to_num(a) with all defaults (no extra kwargs).
    #   return np.nan_to_num(a)
    ...


def nan_to_num_custom(a):
    # Return np.nan_to_num(a, nan=-1, posinf=999, neginf=-999).
    #   return np.nan_to_num(a, nan=-1, posinf=999, neginf=-999)
    ...


ex2_default = nan_to_num_default(arr)
ex2_custom = nan_to_num_custom(arr)
try:
    ex2_default_nan_is_zero = bool(ex2_default[1] == 0.0)
    # The default +inf replacement must be a huge finite number, NOT 0 and NOT inf.
    ex2_default_posinf_is_huge = bool(
        np.isfinite(ex2_default[2]) and ex2_default[2] > 1e300
    )
    ex2_default_neginf_is_huge_negative = bool(
        np.isfinite(ex2_default[3]) and ex2_default[3] < -1e300
    )
    ex2_custom_correct = ex2_custom.tolist() == [1.0, -1.0, 999.0, -999.0, 5.0]
except Exception:
    ex2_default_nan_is_zero = False
    ex2_default_posinf_is_huge = False
    ex2_default_neginf_is_huge_negative = False
    ex2_custom_correct = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3 (the object-dtype no-op): on a native float array,
# np.nan_to_num() replaces NaN normally. On an object-dtype array, it is a
# silent no-op -- confirmed directly the NaN passes straight through, with
# no error and no warning at all.
arr_float = np.array([1.0, np.nan])
arr_obj = np.array([1.0, np.nan], dtype=object)


def nan_to_num_any(a):
    # Return np.nan_to_num(a) -- works for either array passed in.
    #   return np.nan_to_num(a)
    ...


ex3_float_result = nan_to_num_any(arr_float)
ex3_obj_result = nan_to_num_any(arr_obj)
try:
    ex3_float_fixed = bool(ex3_float_result[1] == 0.0)
    ex3_obj_still_nan = bool(isinstance(ex3_obj_result[1], float) and np.isnan(ex3_obj_result[1]))
except Exception:
    ex3_float_fixed = False
    ex3_obj_still_nan = False

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
    check("Exercise 1: Series.fillna(0) replaces NaN but leaves +inf and -inf completely untouched",
          lambda: ex1_nan_became_zero is True and ex1_posinf_untouched is True and ex1_neginf_untouched is True),
    check("Exercise 2: np.nan_to_num() defaults +inf/-inf to the dtype's huge max/min finite value, not 0; nan=/posinf=/neginf= override it",
          lambda: ex2_default_nan_is_zero is True and ex2_default_posinf_is_huge is True
          and ex2_default_neginf_is_huge_negative is True and ex2_custom_correct is True),
    check("Exercise 3: np.nan_to_num() fixes NaN on a float array but is a silent no-op on an object-dtype array",
          lambda: ex3_float_fixed is True and ex3_obj_still_nan is True),
]

print("\nAll green — lesson 123 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
