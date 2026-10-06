# Practice 89 — pd.testing.assert_frame_equal(): comparing tables for a real test
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/89_assert_frame_equal.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd
import pandas.testing as pdt

# ---------------------------------------------------------------------------
# Exercise 1 — a genuine copy passes silently (Section 1). assert_frame_equal
# returns None and raises nothing when the two DataFrames truly match. Fill in
# the method call that makes an identical copy of ex1_df.
# ex1_copy = ex1_df.copy()
ex1_df = pd.DataFrame({"customer": ["An", "Binh"], "amount": [120.0, 35.5]})
ex1_copy = ...
try:
    ex1_copy_is_dataframe = isinstance(ex1_copy, pd.DataFrame)
    ex1_result = pdt.assert_frame_equal(ex1_df, ex1_copy)  # raises on mismatch
    ex1_result_is_none = ex1_result is None
    ex1_passed_without_raising = True
except Exception:
    ex1_copy_is_dataframe = False
    ex1_result_is_none = False
    ex1_passed_without_raising = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2's tolerance behavior: a tiny 1e-9 float drift passes
# assert_frame_equal() by default (small tolerance), but fails once
# check_exact=True is passed (bit-for-bit). Fill in the keyword value that
# forces the bit-for-bit comparison.
# ex2_check_exact_value = True
ex2_check_exact_value = ...
try:
    ex2_value_is_real_true = ex2_check_exact_value is True
    ex2_base = pd.DataFrame({"amount": [120.0, 35.5]})
    ex2_drifted = ex2_base.copy()
    ex2_drifted["amount"] = ex2_drifted["amount"] + 1e-9

    ex2_default_raised = False
    try:
        pdt.assert_frame_equal(ex2_base, ex2_drifted)
    except AssertionError:
        ex2_default_raised = True

    ex2_exact_raised = False
    try:
        pdt.assert_frame_equal(ex2_base, ex2_drifted, check_exact=ex2_check_exact_value)
    except AssertionError:
        ex2_exact_raised = True
except Exception:
    ex2_value_is_real_true = False
    ex2_default_raised = None
    ex2_exact_raised = None

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3's check_dtype=False escape hatch: a float32 column
# that is value-identical to a float64 column fails assert_frame_equal() by
# default (dtype-strict, same as .equals()), but passes once check_dtype is
# turned off. Fill in the keyword value that relaxes the dtype check.
# ex3_check_dtype_value = False
ex3_check_dtype_value = ...
try:
    ex3_value_is_real_false = ex3_check_dtype_value is False
    ex3_wide = pd.DataFrame({"amount": [120.0, 35.5]})
    ex3_narrow = ex3_wide.copy()
    ex3_narrow["amount"] = ex3_narrow["amount"].astype("float32")

    ex3_default_raised = False
    try:
        pdt.assert_frame_equal(ex3_wide, ex3_narrow)
    except AssertionError:
        ex3_default_raised = True

    ex3_relaxed_raised = False
    try:
        pdt.assert_frame_equal(ex3_wide, ex3_narrow, check_dtype=ex3_check_dtype_value)
    except AssertionError:
        ex3_relaxed_raised = True

    ex3_equals_check = ex3_wide.equals(ex3_narrow)  # Lesson 54's .equals(): always dtype-strict
except Exception:
    ex3_value_is_real_false = False
    ex3_default_raised = None
    ex3_relaxed_raised = None
    ex3_equals_check = None

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
    check("Exercise 1: assert_frame_equal() on a genuine copy passes silently (returns None)",
          lambda: ex1_copy_is_dataframe is True
          and ex1_passed_without_raising is True
          and ex1_result_is_none is True),
    check("Exercise 2: 1e-9 drift passes by default but fails once check_exact=True",
          lambda: ex2_value_is_real_true is True
          and ex2_default_raised is False
          and ex2_exact_raised is True),
    check("Exercise 3: check_dtype=False lets float32 match float64, unlike .equals()",
          lambda: ex3_value_is_real_false is True
          and ex3_default_raised is True
          and ex3_relaxed_raised is False
          and ex3_equals_check is False),
]

print("\nAll green — lesson 89 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
