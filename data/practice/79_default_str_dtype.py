# Practice 79 — pandas 3.0's default str dtype, and the select_dtypes gotcha
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/79_default_str_dtype.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
big = pd.concat([df] * 500, ignore_index=True)

# ---------------------------------------------------------------------------
# Exercise 1 — what dtype does a plain text column get from read_csv() on
# current pandas, by default (no dtype= passed at all)? Fill in the literal
# string "str" (not just any placeholder -- checks the literal value itself,
# to avoid a freebie pass).
ex1_expected_dtype_name = ...
try:
    ex1_actual = str(df["customer"].dtype)
    ex1_is_stringdtype_instance = isinstance(df["customer"].dtype, pd.StringDtype)
except Exception:
    ex1_actual = ex1_is_stringdtype_instance = None

# ---------------------------------------------------------------------------
# Exercise 2 — does converting the default "str" column to legacy "object"
# change memory usage on the repeated (big) table? Fill in the literal string
# "object" as the target dtype name to cast to (not just any placeholder --
# checks the literal value, to avoid a freebie pass).
ex2_legacy_dtype_name = ...
try:
    ex2_object_mem = big["customer"].astype(ex2_legacy_dtype_name).memory_usage(deep=True)
    ex2_default_mem = big["customer"].memory_usage(deep=True)
    ex2_same_memory = ex2_object_mem == ex2_default_mem
except Exception:
    ex2_same_memory = None

# ---------------------------------------------------------------------------
# Exercise 3 — the default "str" dtype and the NULLABLE "string" dtype (from
# convert_dtypes(), Lesson 51) are the same StringDtype CLASS but use a
# different missing-value marker. Fill in the literal string "storage" as the
# StringDtype attribute name that both objects share and can be compared
# (not just any placeholder -- checks the literal value, to avoid a freebie
# pass). Hint: dtype objects also expose `.na_value`.
ex3_attr_name = ...
try:
    ex3_default_dtype = df["customer"].dtype
    ex3_nullable_dtype = df["customer"].convert_dtypes().dtype
    ex3_same_storage = getattr(ex3_default_dtype, ex3_attr_name) == getattr(ex3_nullable_dtype, ex3_attr_name)
    ex3_default_na = ex3_default_dtype.na_value
    ex3_nullable_na = ex3_nullable_dtype.na_value
    # default's na_value is plain float NaN; nullable's is pd.NA -- they must differ
    ex3_na_values_differ = ex3_default_na is not ex3_nullable_na
except Exception:
    ex3_same_storage = ex3_na_values_differ = None

# ---------------------------------------------------------------------------
# Exercise 4 — select_dtypes(include="object") still catches the new default
# "str" columns today, but only via a deprecated backward-compat shim that
# raises a warning and will stop working in a future pandas version. Fill in
# the literal string "str" as the forward-compatible include= value that
# catches the same columns with NO warning (not just any placeholder --
# checks the literal value, to avoid a freebie pass).
ex4_forward_compatible_include = ...
try:
    import warnings
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        ex4_legacy_cols = df.select_dtypes(include="object").columns.tolist()
        ex4_legacy_warned = len(caught) > 0
    with warnings.catch_warnings(record=True) as caught2:
        warnings.simplefilter("always")
        ex4_modern_cols = df.select_dtypes(include=ex4_forward_compatible_include).columns.tolist()
        ex4_modern_warned = len(caught2) > 0
    ex4_same_columns = ex4_legacy_cols == ex4_modern_cols
except Exception:
    ex4_legacy_warned = ex4_modern_warned = ex4_same_columns = None

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
    check("Exercise 1: read_csv() gives text columns the new default str dtype",
          lambda: ex1_expected_dtype_name == "str" and ex1_actual == "str"
          and ex1_is_stringdtype_instance is True),
    check("Exercise 2: default str and legacy object cost the identical memory",
          lambda: ex2_legacy_dtype_name == "object" and ex2_same_memory is True),
    check("Exercise 3: same StringDtype class, but different missing-value marker",
          lambda: ex3_attr_name == "storage" and ex3_same_storage is True
          and ex3_na_values_differ is True),
    check("Exercise 4: include=\"str\" matches include=\"object\", with no deprecation warning",
          lambda: ex4_forward_compatible_include == "str" and ex4_same_columns is True
          and ex4_legacy_warned is True and ex4_modern_warned is False),
]

print("\nAll green — lesson 79 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
