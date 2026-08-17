# Practice 41 — astype()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/41_astype.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Raw, uncleaned fixture (Lesson 2/40):
#   order_id customer   amount  order_date
#  0        1       An    120.0  2026-01-05
#  1        2     Binh     35.5  2026-01-06
#  2        3       An  unknown  2026-01-07
#  3        4      Chi     99.9         NaN
#  4        5     Binh    180.0  2026-01-09
#  5        6       An     42.0  2026-01-10
# amount reads as text (str) because of the one non-numeric "unknown" cell.

# ---------------------------------------------------------------------------
# Exercise 1 — convert order_id to a narrower int32 dtype.
try:
    order_id_int32 = raw["order_id"].astype(...)
except Exception:
    order_id_int32 = pd.Series(dtype="int64")

# ---------------------------------------------------------------------------
# Exercise 2 — astype(float) directly on the messy amount column should
# RAISE (the "unknown" cell can't convert); pd.to_numeric(errors="coerce")
# on the same column should instead succeed, turning "unknown" into NaN.
astype_raised = False
try:
    raw["amount"].astype(float)
except (ValueError, TypeError):
    astype_raised = True
except Exception:
    astype_raised = False

try:
    amount_coerced = pd.to_numeric(raw["amount"], errors=...)
except Exception:
    amount_coerced = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — convert the coerced amount Series (has one real NaN, from
# "unknown") to pandas' nullable "Float64" dtype. Plain float64 already
# handles NaN fine, but a nullable dtype makes the missing-value slot
# explicit (<NA> instead of NaN) -- the same "Int64" idea from the lesson,
# applied to a column that (unlike order_id) genuinely has fractional values.
try:
    amount_nullable = amount_coerced.astype(...)
except Exception:
    amount_nullable = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 4 — dict form: convert order_id to int32 AND customer to
# category, both in one astype() call.
try:
    converted = raw.astype(...)
except Exception:
    converted = pd.DataFrame()

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
    check("Exercise 1: order_id_int32 has dtype int32",
          lambda: str(order_id_int32.dtype) == "int32"),
    check("Exercise 1: order_id_int32 values unchanged (still 1..6)",
          lambda: order_id_int32.tolist() == [1, 2, 3, 4, 5, 6]),
    check("Exercise 2: astype(float) on the messy amount column raised",
          lambda: astype_raised is True),
    check("Exercise 2: amount_coerced has 6 values, exactly 1 NaN (the 'unknown' row)",
          lambda: len(amount_coerced) == 6 and amount_coerced.isna().sum() == 1),
    check("Exercise 3: amount_nullable has dtype Float64 (nullable, capital F)",
          lambda: str(amount_nullable.dtype) == "Float64"),
    check("Exercise 3: amount_nullable's missing row is pandas <NA>, not a crash",
          lambda: amount_nullable.isna().sum() == 1),
    check("Exercise 4: converted's order_id is int32",
          lambda: str(converted["order_id"].dtype) == "int32"),
    check("Exercise 4: converted's customer is category",
          lambda: str(converted["customer"].dtype) == "category"),
]
print("\nAll green — lesson 41 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
