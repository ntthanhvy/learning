# Practice 49 — describe(): the fast summary-stats sanity check
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/49_describe.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lessons 2-48 (orders_raw.csv). Load it RAW first --
# describe() on an uncoerced load is today's opening gotcha (Section 1).
raw = pd.read_csv("practice/data/orders_raw.csv")
#   order_id customer  amount order_date
# 0        1       An     120.0 2026-01-05
# 1        2     Binh      35.5 2026-01-06
# 2        3       An unknown  2026-01-07
# 3        4      Chi      99.9        NaN
# 4        5     Binh     180.0 2026-01-09
# 5        6       An      42.0 2026-01-10

# Then the same clean 4-row slice Lessons 6-48 have used.
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
# Exercise 1 — on the RAW (uncoerced) load, raw["amount"] is still a str
# column (the literal "unknown" value blocked automatic numeric parsing) --
# describe() on a str Series does NOT compute mean/std, it reports
# count/unique/top/freq instead, same as any other categorical column. Count
# how many of raw["amount"]'s 6 rows are covered by describe()'s own "count".
try:
    raw_amount_described = raw["amount"].describe()
    raw_amount_count = int(raw_amount_described[...])
except Exception:
    raw_amount_count = -1

# ---------------------------------------------------------------------------
# Exercise 2 — describe() on the CLEAN, properly-coerced numeric amount
# column: get the mean and the median (the "50%" row) from one call.
try:
    amount_described = clean["amount"].describe()
    amount_mean = amount_described["mean"]
    amount_median = float(amount_described[...])
except Exception:
    amount_mean = None
    amount_median = None

# ---------------------------------------------------------------------------
# Exercise 3 — plain DataFrame describe() only summarizes NUMERIC columns by
# default -- customer (a str column) is silently dropped, not an error.
# Pass the keyword that widens it to summarize every column, numeric or not.
try:
    full_described = clean.describe(include=...)
    customer_in_result = "customer" in full_described.columns
except Exception:
    customer_in_result = False

# ---------------------------------------------------------------------------
# Exercise 4 — describe() chains after groupby() exactly like agg() does:
# one full describe() block per group instead of one for the whole column.
# Get Binh's mean amount out of the grouped-describe result.
try:
    grouped_described = clean.groupby("customer")["amount"].describe()
    binh_mean = float(grouped_described.loc[..., "mean"])
except Exception:
    binh_mean = None

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
    check("Exercise 1: raw_amount_count is the str column's non-null row count (6)",
          lambda: raw_amount_count == 6),
    check("Exercise 2: amount_mean is 94.375 (120.0+42.0+35.5+180.0)/4",
          lambda: abs(amount_mean - 94.375) < 1e-9),
    check("Exercise 2: amount_median is 81.0 (the middle of 35.5/42.0/120.0/180.0)",
          lambda: abs(amount_median - 81.0) < 1e-9),
    check("Exercise 3: include=... widens describe() to cover the customer column too",
          lambda: customer_in_result is True),
    check("Exercise 4: grouped describe() gives Binh's mean as 107.75 ((35.5+180.0)/2)",
          lambda: abs(binh_mean - 107.75) < 1e-9),
]
print("\nAll green — lesson 49 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
