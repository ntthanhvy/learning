# Practice 15 — Unstack: pulling a row-index level back into columns
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/15_unstack.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-14: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — groupby on TWO columns at once produces a Series with a
# 2-level MultiIndex row index (customer, order_date), same idea as Lesson
# 14's MultiIndex COLUMNS but on the row side instead:
# clean.groupby(["customer", "order_date"])["amount"].sum()
by_customer_date = ...

# ---------------------------------------------------------------------------
# Exercise 2 — unstack("order_date") pulls the order_date level out of the
# row index and spreads it across columns, turning the long Series back into
# a wide DataFrame (customer x date) — the same shape Lesson 6's pivot_table
# built directly. Pass fill_value=0 so a (customer, date) combo that never
# happened becomes 0 instead of NaN:
# by_customer_date.unstack("order_date", fill_value=0)
try:
    wide_by_date = by_customer_date.unstack(..., fill_value=0)
except Exception:
    wide_by_date = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — unstack takes a level name OR position; unstacking the OTHER
# level ("customer" this time) from the SAME Series spreads customers across
# columns instead, with order_date left in the row index:
# by_customer_date.unstack("customer", fill_value=0)
try:
    wide_by_customer = by_customer_date.unstack(..., fill_value=0)
except Exception:
    wide_by_customer = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 4 — fill_value=0 only fills the gaps; it never changes any real
# total. Prove it: the grand total of wide_by_date (all cells summed, zeros
# included) must equal the grand total of the original long amounts.
# wide_by_date.values.sum()  /  clean["amount"].sum()
try:
    totals_match = wide_by_date.values.sum() == clean["amount"].sum()
except Exception:
    totals_match = False

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
    check("Exercise 1: by_customer_date has a 2-level MultiIndex, An/01-05 is 120.0",
          lambda: by_customer_date.index.nlevels == 2
          and by_customer_date.loc[("An", "2026-01-05")] == 120.0
          and by_customer_date.loc[("Binh", "2026-01-09")] == 180.0),
    check("Exercise 2: wide_by_date is customer x date, An's 01-06 (never happened) is 0",
          lambda: wide_by_date.loc["An", "2026-01-05"] == 120.0
          and wide_by_date.loc["An", "2026-01-06"] == 0
          and wide_by_date.loc["Binh", "2026-01-06"] == 35.5),
    check("Exercise 3: wide_by_customer is date x customer, the OTHER level unstacked",
          lambda: wide_by_customer.loc["2026-01-05", "An"] == 120.0
          and wide_by_customer.loc["2026-01-05", "Binh"] == 0
          and wide_by_customer.loc["2026-01-09", "Binh"] == 180.0),
    check("Exercise 4: fill_value=0 doesn't change the grand total (377.5)",
          lambda: totals_match and wide_by_date.values.sum() == 377.5),
]
print("\nAll green — lesson 15 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
