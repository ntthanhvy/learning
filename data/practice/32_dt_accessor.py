# Practice 32 — The .dt accessor: pulling parts out of a datetime column
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/32_dt_accessor.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-31, but order_date is parsed to datetime64
# this time instead of being left as text:
# An 120.0/2026-01-05 (Mon), An 42.0/2026-01-10 (Sat),
# Binh 35.5/2026-01-06 (Tue), Binh 180.0/2026-01-09 (Fri)
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
clean["order_date"] = pd.to_datetime(clean["order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — pull the weekday NAME for every row via the .dt accessor.
# (the .dt attribute you want is "day_name", called as a method)
try:
    weekday_names = getattr(clean["order_date"].dt, ...)()
except Exception:
    weekday_names = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 2 — build a boolean mask that's True for weekend orders
# (Saturday=5, Sunday=6 in dt.dayofweek), then filter `clean` down to them.
try:
    weekend_mask = clean["order_date"].dt.dayofweek.isin(...)
    weekend_orders = clean[weekend_mask]
except Exception:
    weekend_orders = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — group total amount by weekday name (Section 4's pattern):
# groupby a .dt expression directly, no separate column needed.
try:
    by_weekday = clean.groupby(clean["order_date"].dt.day_name())[...].sum()
except Exception:
    by_weekday = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — reproduce Section 6's NaT gotcha: parse the RAW (unfiltered)
# order_date column with errors="coerce" (order_id 4's blank date becomes
# NaT), then confirm .dt.year does NOT raise -- it returns NaN for that row.
try:
    raw_parsed = raw.copy()
    raw_parsed["order_date_parsed"] = pd.to_datetime(
        raw_parsed["order_date"], errors=...
    )
    years = raw_parsed["order_date_parsed"].dt.year
except Exception:
    years = pd.Series(dtype=float)

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
    check("Exercise 1: weekday_names lists Monday, Saturday, Tuesday, Friday in order",
          lambda: list(weekday_names) == ["Monday", "Saturday", "Tuesday", "Friday"]),
    check("Exercise 2: weekend_orders has exactly 1 row (An's Saturday order, 42.0)",
          lambda: len(weekend_orders) == 1
          and abs(float(weekend_orders.iloc[0]["amount"]) - 42.0) < 1e-9),
    check("Exercise 3: by_weekday sums to 377.5 total across 4 weekday groups",
          lambda: len(by_weekday) == 4 and abs(float(by_weekday.sum()) - 377.5) < 1e-9),
    check("Exercise 3: Friday's total is 180.0 (Binh's order)",
          lambda: abs(float(by_weekday["Friday"]) - 180.0) < 1e-9),
    check("Exercise 4: order_id 4's row (blank date) has a NaT-derived NaN year",
          lambda: len(years) == 6 and pd.isna(years.iloc[3])),
    check("Exercise 4: no exception was raised getting there (years has 6 entries)",
          lambda: len(years) == 6),
]
print("\nAll green — lesson 32 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
