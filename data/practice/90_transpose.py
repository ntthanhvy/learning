# Practice 90 — .T / transpose(): flipping rows and columns, and the dtype trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/90_transpose.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: transposing a DataFrame whose columns already share
# one dtype (both int64) keeps that dtype -- no upcast needed. Fill in the
# attribute that flips rows and columns.
# ex1_flipped = ex1_df.T
ex1_df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
ex1_flipped = ...
try:
    ex1_is_dataframe = isinstance(ex1_flipped, pd.DataFrame)
    ex1_shape_flipped = ex1_flipped.shape == (2, 2) and list(ex1_flipped.index) == ["a", "b"]
    ex1_dtype_stayed_int = bool((ex1_flipped.dtypes == "int64").all())
except Exception:
    ex1_is_dataframe = False
    ex1_shape_flipped = False
    ex1_dtype_stayed_int = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 1's real trap: a mix of int64 and float64 columns
# silently upcasts EVERY cell to float64 after transpose, with no warning.
# Fill in the dtype name that the whole transposed frame ends up holding.
# ex2_expected_dtype = "float64"
ex2_df = pd.DataFrame({"count": [10, 20], "ratio": [0.5, 0.75]})
ex2_expected_dtype = ...
try:
    ex2_flipped = ex2_df.T
    ex2_all_upcast = bool((ex2_flipped.dtypes == ex2_expected_dtype).all())
    ex2_original_had_two_dtypes = bool(ex2_df["count"].dtype != ex2_df["ratio"].dtype)
except Exception:
    ex2_all_upcast = False
    ex2_original_had_two_dtypes = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2's sharper trap: mixing strings and numbers upcasts
# the whole transposed frame to object, and a row-wise sum(axis=1) then
# silently does the WRONG operation per row -- string-concatenating the text
# row instead of raising -- rather than giving a clean numeric answer.
# ex3_name_row_result = "AnBinh"
ex3_df = pd.DataFrame({"name": ["An", "Binh"], "score": [90, 85]})
ex3_name_row_result = ...
try:
    ex3_flipped = ex3_df.T
    ex3_is_object_dtype = bool((ex3_flipped.dtypes == "object").all())
    ex3_summed = ex3_flipped.sum(axis=1)
    ex3_no_error_raised = True
    ex3_name_row_matches = bool(ex3_summed["name"] == ex3_name_row_result)
    ex3_score_row_is_numeric_sum = bool(ex3_summed["score"] == 175)
except Exception:
    ex3_is_object_dtype = False
    ex3_no_error_raised = False
    ex3_name_row_matches = False
    ex3_score_row_is_numeric_sum = False

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
    check("Exercise 1: .T flips rows/columns, same dtype stays when columns already agree",
          lambda: ex1_is_dataframe is True
          and ex1_shape_flipped is True
          and ex1_dtype_stayed_int is True),
    check("Exercise 2: int64 + float64 columns silently upcast the whole transposed frame to float64",
          lambda: ex2_original_had_two_dtypes is True
          and ex2_all_upcast is True),
    check("Exercise 3: strings + numbers upcast to object, and sum(axis=1) silently string-concats the text row",
          lambda: ex3_is_object_dtype is True
          and ex3_no_error_raised is True
          and ex3_name_row_matches is True
          and ex3_score_row_is_numeric_sum is True),
]

print("\nAll green — lesson 90 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
