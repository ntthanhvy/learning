# Practice 05 — Merge & join
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/05_merge_and_join.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

# ---------------------------------------------------------------------------
# Exercise 1 — inner join: SELECT * FROM orders JOIN customers ON
# orders.customer = customers.customer. Chi has an order but no customer
# record, so her row should NOT appear in the result.
inner = ...

# ---------------------------------------------------------------------------
# Exercise 2 — customers who never ordered: left join customers -> orders,
# indicator=True, filter _merge == "left_only", then pull the "customer"
# column as a list (.tolist()). Section 2's exact pattern.
never_ordered = ...

# ---------------------------------------------------------------------------
# Exercise 3 — orders with no matching customer record (a data-quality
# check): left join orders -> customers, indicator=True, filter
# _merge == "left_only", then pull "order_id" as a list.
orphan_order_ids = ...

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
    check("Exercise 1: inner join keeps 5 rows, Chi's order excluded",
          lambda: len(inner) == 5 and "Chi" not in inner["customer"].values),
    check("Exercise 2: never_ordered is exactly ['Danh']",
          lambda: never_ordered == ["Danh"]),
    check("Exercise 3: orphan_order_ids is exactly [4] (Chi's order)",
          lambda: orphan_order_ids == [4]),
]
print("\nAll green — lesson 5 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
