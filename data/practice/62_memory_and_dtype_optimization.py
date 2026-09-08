# Practice 62 — memory/dtype optimization: memory_usage(deep=True) and downcasting
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/62_memory_and_dtype_optimization.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same file as Lessons 2-4, coerced the same way, then repeated 500x so the memory
# differences are large enough to see clearly (a 6-row table can't show a
# meaningful byte-count gap).
df = pd.read_csv("practice/data/orders_raw.csv")
amount_clean = pd.to_numeric(df["amount"], errors="coerce")
df2 = df.assign(amount_clean=amount_clean).dropna(subset=["amount_clean"])
big = pd.concat([df2] * 500, ignore_index=True)

# ---------------------------------------------------------------------------
# Exercise 1 — confirm the shallow-vs-deep gap on memory_usage(). Compute
# shallow_total (deep=False, the default) and deep_total (deep=True) as the
# SUM across every column of `big`. deep_total should come out noticeably
# bigger than shallow_total, since customer/order_date/amount are text.
try:
    shallow_total = ...
    deep_total = ...
except Exception:
    shallow_total = None
    deep_total = None

# ---------------------------------------------------------------------------
# Exercise 2 — convert big["customer"] to the category dtype (Lesson 25) and
# check that its memory_usage(deep=True) dropped versus the original str
# column's memory_usage(deep=True). Store the two byte counts as
# customer_str_bytes and customer_cat_bytes.
try:
    customer_str_bytes = ...
    customer_cat_bytes = ...
except Exception:
    customer_str_bytes = None
    customer_cat_bytes = None

# ---------------------------------------------------------------------------
# Exercise 3 — downcast big["order_id"] (values only ever 1-6) safely with
# pd.to_numeric(..., downcast="integer"). Store the result's dtype (as a
# string, e.g. str(result.dtype)) in order_id_downcast_dtype.
try:
    order_id_downcast_dtype = ...
except Exception:
    order_id_downcast_dtype = None

# ---------------------------------------------------------------------------
# Exercise 4 — reproduce the silent-wraparound gotcha: build
# pd.Series([100, 200, 300], dtype="int64"), cast it directly with
# .astype("int8") (NOT to_numeric downcast), and store the resulting list of
# values in wrapped_values. int8's range is -128..127, so 200 and 300 will
# NOT raise -- they'll silently wrap to different, wrong-looking numbers.
try:
    wrapped_values = ...
except Exception:
    wrapped_values = None

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
    check("Exercise 1: deep_total noticeably bigger than shallow_total",
          lambda: shallow_total is not None and deep_total is not None
          and deep_total > shallow_total * 2),
    check("Exercise 2: customer as category uses far less memory than as str",
          lambda: customer_str_bytes is not None and customer_cat_bytes is not None
          and customer_cat_bytes < customer_str_bytes / 10),
    check("Exercise 3: order_id safely downcast to a narrow int dtype",
          lambda: order_id_downcast_dtype in ("int8", "int16", "int32")),
    check("Exercise 4: astype('int8') silently wraps 200 and 300 to wrong values",
          lambda: wrapped_values is not None
          and wrapped_values[0] == 100
          and wrapped_values[1] != 200
          and wrapped_values[2] != 300),
]
print("\nAll green — lesson 62 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
