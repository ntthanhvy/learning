# Practice 40 — groupby().filter()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/40_groupby_filter.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Raw, uncleaned fixture (Lesson 2):
#   order_id customer   amount  order_date
#  0        1       An    120.0  2026-01-05
#  1        2     Binh     35.5  2026-01-06
#  2        3       An  unknown  2026-01-07
#  3        4      Chi     99.9         NaN
#  4        5     Binh    180.0  2026-01-09
#  5        6       An     42.0  2026-01-10
# An x3, Binh x2, Chi x1. amount has one non-numeric "unknown" (An's order_id 3).
raw["amount_num"] = pd.to_numeric(raw["amount"], errors="coerce")

# ---------------------------------------------------------------------------
# Exercise 1 — keep only rows belonging to customers with 2+ orders total.
# Chi (1 order) should be dropped entirely; every An/Binh row survives.
try:
    by_count = raw.groupby("customer").filter(lambda g: len(g) >= ...)
except Exception:
    by_count = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — keep only rows belonging to customers whose numeric amount
# total exceeds 150 (Chi=99.9 drops, An=162.0 and Binh=215.5 survive).
try:
    by_sum = raw.groupby("customer").filter(lambda g: g["amount_num"].sum(skipna=True) > ...)
except Exception:
    by_sum = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — contrast shapes: agg() collapses to one row per group,
# filter() keeps every original column at full row-level detail.
try:
    agg_result = raw.groupby("customer")[...].sum()
except Exception:
    agg_result = pd.Series(dtype=float)

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
    check("Exercise 1: by_count has 5 rows (Chi's single order dropped)",
          lambda: len(by_count) == 5),
    check("Exercise 1: Chi is not present at all in by_count",
          lambda: "Chi" not in set(by_count["customer"])),
    check("Exercise 1: by_count keeps original columns intact (order_id present)",
          lambda: "order_id" in by_count.columns and set(by_count["order_id"]) == {1, 2, 3, 5, 6}),
    check("Exercise 2: by_sum has the same 5 rows as by_count",
          lambda: sorted(by_sum["order_id"]) == [1, 2, 3, 5, 6]),
    check("Exercise 2: Chi is not present at all in by_sum",
          lambda: "Chi" not in set(by_sum["customer"])),
    check("Exercise 3: agg_result has exactly 3 rows (one per customer, incl. Chi)",
          lambda: len(agg_result) == 3),
    check("Exercise 3: agg_result's An total is 162.0, unlike filter()'s row-level output",
          lambda: agg_result.loc["An"] == 162.0),
]
print("\nAll green — lesson 40 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
