# Practice 38 — resample()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/38_resample.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-37, set_index'd on the parsed order_date:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
clean["order_date"] = pd.to_datetime(clean["order_date"])
indexed = clean.set_index("order_date")

# ---------------------------------------------------------------------------
# Exercise 1 — daily revenue via resample, gaps included (zero-filled by sum).
try:
    daily_sum = indexed["amount"].resample(...).sum()
except Exception:
    daily_sum = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — same daily buckets, but the MEAN instead of the sum -- an
# empty day should come back NaN here, not 0.0.
try:
    daily_mean = indexed["amount"].resample("D").agg(...)
except Exception:
    daily_mean = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — weekly revenue (single-bucket case: this fixture's whole date
# span fits inside one Sunday-ending week).
try:
    weekly_sum = indexed["amount"].resample(...).sum()
except Exception:
    weekly_sum = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — resample with a per-column aggregation dict: sum the amount,
# take the first customer seen per day.
try:
    daily_mixed = indexed.resample("D").agg({"amount": "sum", "customer": ...})
except Exception:
    daily_mixed = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 5 — asfreq() on the same daily grid: no aggregation happened, so
# an empty day is NaN here too (contrast with Exercise 1's 0.0 from sum()).
try:
    daily_asfreq = indexed["amount"].asfreq(...)
except Exception:
    daily_asfreq = pd.Series(dtype=float)

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
    check("Exercise 1: daily_sum has 6 rows (Jan 5 through Jan 10, gaps included)",
          lambda: len(daily_sum) == 6),
    check("Exercise 1: the two gap days (Jan 7, Jan 8) are zero-filled, not NaN",
          lambda: daily_sum.iloc[2] == 0.0 and daily_sum.iloc[3] == 0.0),
    check("Exercise 2: daily_mean's gap days are NaN, not 0.0",
          lambda: pd.isna(daily_mean.iloc[2]) and pd.isna(daily_mean.iloc[3])),
    check("Exercise 3: weekly_sum has exactly 1 bucket totalling 377.5",
          lambda: len(weekly_sum) == 1 and abs(float(weekly_sum.iloc[0]) - 377.5) < 1e-9),
    check("Exercise 4: daily_mixed's amount column matches daily_sum exactly",
          lambda: daily_mixed["amount"].tolist() == daily_sum.tolist()),
    check("Exercise 4: daily_mixed's customer is NaN on the two gap days",
          lambda: pd.isna(daily_mixed["customer"].iloc[2]) and pd.isna(daily_mixed["customer"].iloc[3])),
    check("Exercise 5: daily_asfreq's gap days are NaN (contrast with Exercise 1's 0.0)",
          lambda: pd.isna(daily_asfreq.iloc[2]) and pd.isna(daily_asfreq.iloc[3])),
]
print("\nAll green — lesson 38 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
