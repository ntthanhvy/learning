# Practice 39 — stack()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/39_stack.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-38:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
clean["order_date"] = pd.to_datetime(clean["order_date"])

by_customer_date = clean.groupby(["customer", "order_date"])["amount"].sum()

# ---------------------------------------------------------------------------
# Exercise 1 — rebuild Lesson 15's wide_by_date: unstack the order_date level,
# zero-filling combinations that never happened.
try:
    wide_by_date = by_customer_date.unstack(...,  fill_value=0)
except Exception:
    wide_by_date = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — stack wide_by_date back and check the round trip: the restacked
# Series should match by_customer_date's own values exactly (stack/unstack
# are true inverses).
try:
    restacked = wide_by_date.stack()
except Exception:
    restacked = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — unstack WITHOUT fill_value (real NaN gaps this time), then
# stack it back. On this course's pandas version, stack() keeps every row,
# NaN included — it does not silently drop the newly-created all-NaN rows.
try:
    wide_nan = by_customer_date.unstack("order_date")
    restacked_nan = wide_nan.stack(...)
except Exception:
    restacked_nan = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — two-aggfunc pivot_table (MultiIndex columns), then
# stack(level=0) to pull the aggfunc level down natively, no flatten step.
try:
    pv = clean.pivot_table(
        index="customer", columns="order_date", values="amount",
        aggfunc=["sum", "count"], fill_value=0,
    )
    stacked_level0 = pv.stack(level=...)
except Exception:
    stacked_level0 = pd.DataFrame()

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
    check("Exercise 1: wide_by_date has 2 rows (An, Binh) and 4 date columns",
          lambda: wide_by_date.shape == (2, 4)),
    check("Exercise 1: An's zero-filled 01-06 cell is 0.0, not NaN",
          lambda: wide_by_date.loc["An", pd.Timestamp("2026-01-06")] == 0.0),
    check("Exercise 2: restacked has 8 rows (2 customers x 4 dates)",
          lambda: len(restacked) == 8),
    check("Exercise 2: restacked matches by_customer_date at every real combo",
          lambda: restacked.loc[("An", "2026-01-05")] == 120.0
          and restacked.loc[("Binh", "2026-01-09")] == 180.0),
    check("Exercise 3: restacked_nan keeps all 8 rows (no auto-drop of NaN combos)",
          lambda: len(restacked_nan) == 8),
    check("Exercise 3: restacked_nan's never-ordered combo is genuinely NaN",
          lambda: pd.isna(restacked_nan.loc[("An", "2026-01-06")])),
    check("Exercise 4: stacked_level0 has a 2-level row MultiIndex (customer, sum/count)",
          lambda: stacked_level0.index.nlevels == 2
          and set(stacked_level0.index.get_level_values(1)) == {"sum", "count"}),
    check("Exercise 4: An's sum row totals 162.0 (120.0 + 0.0 + 0.0 + 42.0)",
          lambda: stacked_level0.loc[("An", "sum")].sum() == 162.0),
    check("Exercise 4: An's count row has exactly 2 real orders (01-05 and 01-10)",
          lambda: stacked_level0.loc[("An", "count")].sum() == 2.0),
]
print("\nAll green — lesson 39 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
