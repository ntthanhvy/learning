# Practice 09 — Timed Drills: Nth Highest, Anti-Join, One Review Chain
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/09_timed_drills.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
# Budget yourself: ~5 min per drill, like a timed round.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
# Same clean slice as Lessons 6-8: drop the unparseable amount (order_id 3) and
# the missing order_date (order_id 4, Chi). 4 clean rows: An x2, Binh x2.
clean = orders.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Drill 1 (LeetCode "Nth Highest" pattern) — each customer's SECOND highest
# order amount. Rank each customer's orders by amount (biggest first), then
# keep rank == 2. A customer with fewer than 2 orders has no row here.
second_highest = ...

# ---------------------------------------------------------------------------
# Drill 2 (StrataScratch "revenue by segment" pattern) — total revenue per
# region, counting only customers who appear in BOTH files (an inner merge
# of clean orders with customers on "customer"), then groupby("region").
# Name the summed column "amount" (the default from a plain .sum()).
revenue_by_region = ...

# ---------------------------------------------------------------------------
# Drill 3 (anti-join, tying Lesson 5's pattern into Lesson 8's chaining) —
# ONE chain, starting from `customers`, that finds customers with NO matching
# row in `clean` at all. Use pd.merge(..., how="left", indicator=True) then
# .query() to keep only "left_only" rows, then select just the "customer"
# column as a list via .tolist() (chain a subscript then .tolist()).
never_ordered = ...

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
    check("Drill 1: second_highest has exactly An/42.0 and Binh/35.5",
          lambda: len(second_highest) == 2
          and set(zip(second_highest["customer"], second_highest["amount"]))
          == {("An", 42.0), ("Binh", 35.5)}),
    check("Drill 1: Chi (only 1 order) is not in second_highest",
          lambda: "Chi" not in second_highest["customer"].values),
    check("Drill 2: North (An) totals 162.0, South (Binh) totals 215.5",
          lambda: set(zip(revenue_by_region["region"], revenue_by_region["amount"]))
          == {("North", 162.0), ("South", 215.5)}),
    check("Drill 2: West (Danh, no orders) is excluded by the inner merge",
          lambda: "West" not in revenue_by_region["region"].values),
    check("Drill 3: never_ordered is exactly ['Danh']",
          lambda: never_ordered == ["Danh"]),
]
print("\nAll green — lesson 9 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
