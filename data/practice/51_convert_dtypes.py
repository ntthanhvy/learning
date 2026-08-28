# Practice 51 — convert_dtypes(): the best-guess dtype pass
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/51_convert_dtypes.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture clean 4-row slice as Lessons 6-50.
raw = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(raw["amount"], errors="coerce")
order_date = pd.to_datetime(raw["order_date"], errors="coerce")
clean = (
    raw.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
#   order_id customer  amount order_date
# 0        1       An   120.0 2026-01-05
# 1        6       An    42.0 2026-01-10
# 2        2     Binh    35.5 2026-01-06
# 3        5     Binh   180.0 2026-01-09

# ---------------------------------------------------------------------------
# Exercise 1 — run convert_dtypes() on the already-cleaned `clean` table.
# order_id (whole-number int64) should become "Int64"; amount (float64)
# should become "Float64" (Section 1).
# NOTE: the placeholder sits on the WHOLE right-hand side, not inside a
# call's arguments -- an unfilled `converted = ...` leaves `converted` as
# bare Ellipsis, and `Ellipsis["order_id"]` raises TypeError on its own (no
# extra guarding needed, unlike a kwarg placeholder such as `numeric_only=...`
# which would stay silently truthy instead).
try:
    converted = ...
    order_id_dtype = str(converted["order_id"].dtype)
    amount_dtype = str(converted["amount"].dtype)
except Exception:
    order_id_dtype = None
    amount_dtype = None

# ---------------------------------------------------------------------------
# Exercise 2 — the gotcha: run convert_dtypes() on the RAW, still-uncoerced
# amount column (still has the stray "unknown" from row 3, blocking numeric
# auto-detection). It does NOT become "Float64" -- every value still counts
# as valid text, so it gets promoted to pandas' own "string" dtype instead,
# still unusable for arithmetic (Section 2).
# NOTE: raw[...] as a DataFrame column selector DOES raise on its own
# (KeyError: Ellipsis, confirmed directly with a standalone probe before
# trusting it -- Ellipsis is not a valid column label), so no extra
# truthiness guarding is needed for this placeholder.
try:
    raw_amount_dtype = str(raw[...].convert_dtypes().dtype)
except Exception:
    raw_amount_dtype = None

# ---------------------------------------------------------------------------
# Exercise 3 — a float64 column where every value happens to be a whole
# number gets promoted to Int64, not Float64; a column with one genuinely
# fractional value stays Float64 (Section 3).
# NOTE: a placeholder written as `fractional[...]` would NOT raise on its
# own -- Ellipsis is a valid whole-Series indexer in pandas (same finding as
# Lessons 20/25/45/46/49), so it would silently return `fractional`
# unchanged and this exercise would ship as an accidental freebie ✓.
# Placing the placeholder on the whole right-hand side instead avoids that:
# an unfilled `fractional_dtype = ...` never even calls .convert_dtypes(),
# so it stays bare Ellipsis and fails the string-equality check below for a
# real ✗, confirmed directly before shipping.
whole_valued = pd.Series([1.0, 2.0, 3.0])
fractional = pd.Series([1.5, 2.0, 3.0])
try:
    whole_dtype = str(whole_valued.convert_dtypes().dtype)
    fractional_dtype = ...
except Exception:
    whole_dtype = None
    fractional_dtype = None

# ---------------------------------------------------------------------------
# Exercise 4 — the fix for Exercise 2's gotcha: coerce FIRST with
# pd.to_numeric(errors="coerce"), THEN convert_dtypes() -- now the column
# genuinely reaches Float64, since the values themselves were fixed before
# the dtype upgrade ran (Section 2's closing fix).
# NOTE: errors=... would NOT raise on its own if left as Ellipsis --
# pd.to_numeric silently treats an unrecognized errors= value as invalid
# only at call time, so this is checked explicitly with `is "coerce"`-style
# assertion instead of trusting a bare call to fail loudly on its own.
try:
    coerce_mode = ...
    assert coerce_mode == "coerce"
    fixed_amount = pd.to_numeric(raw["amount"], errors=coerce_mode).convert_dtypes()
    fixed_amount_dtype = str(fixed_amount.dtype)
except Exception:
    fixed_amount_dtype = None

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
    check("Exercise 1: clean order_id becomes Int64 after convert_dtypes()",
          lambda: order_id_dtype == "Int64"),
    check("Exercise 1: clean amount becomes Float64 after convert_dtypes()",
          lambda: amount_dtype == "Float64"),
    check("Exercise 2: raw (uncoerced) amount becomes string, NOT Float64",
          lambda: raw_amount_dtype == "string"),
    check("Exercise 3: an all-whole-number float64 Series becomes Int64",
          lambda: whole_dtype == "Int64"),
    check("Exercise 3: a genuinely fractional Series stays Float64",
          lambda: fractional_dtype == "Float64"),
    check("Exercise 4: coercing first, then convert_dtypes(), reaches Float64",
          lambda: fixed_amount_dtype == "Float64"),
]
print("\nAll green — lesson 51 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
