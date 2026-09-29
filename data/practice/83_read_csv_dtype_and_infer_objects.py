# Practice 83 — read_csv(dtype=) and infer_objects(): declaring vs. best-guessing
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/83_read_csv_dtype_and_infer_objects.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — load orders_raw.csv passing dtype= directly to read_csv(),
# declaring order_id as int32 and customer as category up front (Section 2).
# ex1_df = pd.read_csv("practice/data/orders_raw.csv",
#                       dtype={"order_id": "int32", "customer": "category"})
try:
    ex1_df = pd.read_csv(
        "practice/data/orders_raw.csv",
        dtype={"order_id": ..., "customer": ...},
    )
    ex1_order_id_dtype = str(ex1_df["order_id"].dtype)
    ex1_customer_dtype = str(ex1_df["customer"].dtype)
except Exception:
    ex1_order_id_dtype = None
    ex1_customer_dtype = None

# ---------------------------------------------------------------------------
# Exercise 2 — forcing dtype={"amount": "float64"} on the same file raises
# ValueError, because the real "unknown" string in that column can't be
# parsed as a float at load time (Section 2's gotcha). Fill in the exception
# type expected.
# ex2_error_type = ValueError
ex2_error_type = ...
try:
    pd.read_csv("practice/data/orders_raw.csv", dtype={"amount": "float64"})
    ex2_raised_correct_error = False
except BaseException as e:
    ex2_raised_correct_error = isinstance(ex2_error_type, type) and isinstance(e, ex2_error_type)

# ---------------------------------------------------------------------------
# Exercise 3 — an object-dtype Series holding real Python floats relabels to
# float64 under infer_objects() -- no parsing, just a relabel (Section 3).
# Fill in the method name (as a string) below.
# ex3_method_name = "infer_objects"
ex3_method_name = ...
try:
    ex3_before = pd.Series([1.0, 2.0, 3.0], dtype=object)
    ex3_after = getattr(ex3_before, ex3_method_name)()
    ex3_before_dtype = str(ex3_before.dtype)
    ex3_after_dtype = str(ex3_after.dtype)
except Exception:
    ex3_before_dtype = None
    ex3_after_dtype = None

# ---------------------------------------------------------------------------
# Exercise 4 — a genuinely mixed object-dtype Series (real int and real
# string together) comes back from infer_objects() completely unchanged,
# still object dtype AND with the exact same values, string included
# (Section 3). Fill in the missing real string value.
# ex4_fill_value = "two"
ex4_fill_value = ...
try:
    ex4_mixed = pd.Series([1, ex4_fill_value, 3], dtype=object)
    ex4_after = ex4_mixed.infer_objects()
    ex4_after_dtype = str(ex4_after.dtype)
    ex4_values_unchanged = list(ex4_after) == [1, "two", 3]
except Exception:
    ex4_after_dtype = None
    ex4_values_unchanged = None

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
    check("Exercise 1: dtype= at read_csv() time yields int32 order_id and category customer",
          lambda: ex1_order_id_dtype == "int32" and ex1_customer_dtype == "category"),
    check("Exercise 2: dtype={'amount': 'float64'} raises ValueError on the real 'unknown' value",
          lambda: ex2_raised_correct_error is True),
    check("Exercise 3: infer_objects() relabels an object-dtype float Series to float64",
          lambda: ex3_before_dtype == "object" and ex3_after_dtype == "float64"),
    check("Exercise 4: infer_objects() leaves a genuinely mixed object Series unchanged",
          lambda: ex4_after_dtype == "object" and ex4_values_unchanged is True),
]

print("\nAll green — lesson 83 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
