# Practice 44 — pivot_table() vs .pivot(), and margins=True
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/44_pivot_table_and_margins.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Small inline orders fixture (same customer/order domain as Lessons 6-43).
# An placed TWO orders on 2026-01-05 (order_id 1 and 3) -- a deliberate
# duplicate customer/order_date pair, so .pivot() has something real to
# fail on and pivot_table() has something real to aggregate.
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer": ["An", "Binh", "An", "Binh", "An"],
    "order_date": ["2026-01-05", "2026-01-06", "2026-01-05", "2026-01-06", "2026-01-10"],
    "amount": [120.0, 35.5, 60.0, 180.0, 42.0],
})

# ---------------------------------------------------------------------------
# Exercise 1 — plain .pivot() raises ValueError on the duplicate An/2026-01-05
# pair. Call orders.pivot(index="customer", columns="order_date",
# values="amount") inside the try, and confirm it's a ValueError specifically
# (not some other error from a still-unsolved placeholder below).
pivot_error_type = None
try:
    orders.pivot(index="customer", columns="order_date", values=...)
except Exception as e:
    pivot_error_type = type(e)

# ---------------------------------------------------------------------------
# Exercise 2 — pivot_table() with aggfunc="sum" does NOT raise on the same
# duplicate data; it aggregates instead. fill_value=0 for the empty cells.
try:
    wide_sum = orders.pivot_table(
        index="customer", columns="order_date", values="amount",
        aggfunc=..., fill_value=0,
    )
except Exception:
    wide_sum = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — pivot_table()'s default aggfunc (no aggfunc= passed at all)
# is "mean", not "sum" -- a DIFFERENT value for An's 2026-01-05 cell than
# Exercise 2's explicit sum. Call pivot_table with no aggfunc argument.
try:
    wide_mean = orders.pivot_table(
        index="customer", columns="order_date", values=...,
        fill_value=0,
    )
except Exception:
    wide_mean = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 4 — margins=True adds a grand-total row and column, each using
# the same aggfunc ("sum" here). The bottom-right corner is the grand total
# of every order's amount, however you sum your way there. Name that extra
# row/column "All" via margins_name.
try:
    wide_margins = orders.pivot_table(
        index="customer", columns="order_date", values="amount",
        aggfunc="sum", fill_value=0, margins=True, margins_name=...,
    )
except Exception:
    wide_margins = pd.DataFrame()

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
    check("Exercise 1: .pivot() raised ValueError on the duplicate pair",
          lambda: pivot_error_type is ValueError),
    check("Exercise 2: pivot_table(aggfunc='sum') did not raise, An/01-05 is 180.0",
          lambda: wide_sum.loc["An", "2026-01-05"] == 180.0),
    check("Exercise 2: Binh/01-06 sum is 215.5, Binh/01-10 fill_value is 0",
          lambda: wide_sum.loc["Binh", "2026-01-06"] == 215.5
          and wide_sum.loc["Binh", "2026-01-10"] == 0),
    check("Exercise 3: default aggfunc is 'mean', An/01-05 is 90.0 (not 180.0)",
          lambda: wide_mean.loc["An", "2026-01-05"] == 90.0),
    check("Exercise 4: margins=True adds an 'All' row and column",
          lambda: "All" in wide_margins.index and "All" in wide_margins.columns),
    check("Exercise 4: grand-total corner (437.5) matches orders['amount'].sum()",
          lambda: wide_margins.loc["All", "All"] == orders["amount"].sum() == 437.5),
]
print("\nAll green — lesson 44 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
