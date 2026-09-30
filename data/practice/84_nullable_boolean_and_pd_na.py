# Practice 84 — Nullable boolean (BooleanDtype) and pd.NA: a third truth value
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/84_nullable_boolean_and_pd_na.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — building a Series from [True, False, None] with NO dtype
# declared does not produce bool at all -- it silently falls back to object,
# since plain NumPy bool has no missing-value slot (Section 1).
# Fill in the dtype string you'd expect this to actually become.
# ex1_expected_dtype = "object"
ex1_expected_dtype = ...
try:
    ex1_series = pd.Series([True, False, None])
    ex1_actual_dtype = str(ex1_series.dtype)
except Exception:
    ex1_actual_dtype = None

# ---------------------------------------------------------------------------
# Exercise 2 — the same values built WITH dtype="boolean" keep a real third
# state for the missing entry: pd.NA (Section 1-2). Fill in the dtype string
# to pass, and confirm the third entry really is pd.NA.
# ex2_dtype_name = "boolean"
ex2_dtype_name = ...
try:
    ex2_series = pd.Series([True, False, None], dtype=ex2_dtype_name)
    ex2_dtype_str = str(ex2_series.dtype)
    ex2_third_is_na = ex2_series[2] is pd.NA
except Exception:
    ex2_dtype_str = None
    ex2_third_is_na = None

# ---------------------------------------------------------------------------
# Exercise 3 — Kleene logic on a boolean Series [True, False, pd.NA]:
# False & NA short-circuits to False (False wins regardless), but
# True & NA cannot short-circuit, so the NA passes through (Section 3).
# Fill in the two missing operands below.
# ex3_and_false_operand = False
# ex3_and_true_operand = True
ex3_and_false_operand = ...
ex3_and_true_operand = ...
try:
    ex3_base = pd.Series([True, False, pd.NA], dtype="boolean")
    ex3_and_false = (ex3_base & ex3_and_false_operand).tolist()
    ex3_and_true = (ex3_base & ex3_and_true_operand).tolist()
    ex3_false_wins = ex3_and_false == [False, False, False]
    ex3_na_passes_through = ex3_and_true[2] is pd.NA
except Exception:
    ex3_false_wins = None
    ex3_na_passes_through = None

# ---------------------------------------------------------------------------
# Exercise 4 — astype(bool) on an object column holding a real None
# silently turns it into False (data corruption, no warning); astype to the
# nullable dtype name preserves it as a real pd.NA instead (Section 4).
# Fill in the nullable dtype name to astype() to.
# ex4_nullable_dtype_name = "boolean"
ex4_nullable_dtype_name = ...
try:
    ex4_source = pd.Series([True, False, None], dtype=object)
    ex4_plain_bool = ex4_source.astype(bool)
    ex4_nullable = ex4_source.astype(ex4_nullable_dtype_name)
    ex4_plain_corrupts_to_false = ex4_plain_bool.tolist() == [True, False, False]
    ex4_nullable_preserves_na = ex4_nullable.iloc[2] is pd.NA
except Exception:
    ex4_plain_corrupts_to_false = None
    ex4_nullable_preserves_na = None

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
    check("Exercise 1: [True, False, None] with no dtype silently becomes object, not bool",
          lambda: ex1_actual_dtype == ex1_expected_dtype == "object"),
    check("Exercise 2: dtype='boolean' keeps a real pd.NA as the third entry",
          lambda: ex2_dtype_str == "boolean" and ex2_third_is_na is True),
    check("Exercise 3: False & NA short-circuits to False, but True & NA passes NA through",
          lambda: ex3_false_wins is True and ex3_na_passes_through is True),
    check("Exercise 4: astype(bool) corrupts None to False; astype('boolean') preserves pd.NA",
          lambda: ex4_plain_corrupts_to_false is True and ex4_nullable_preserves_na is True),
]

print("\nAll green — lesson 84 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
