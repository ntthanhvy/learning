# Practice 10 — Timed Drills, Round 2: value_counts, .str, nlargest
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/10_value_counts_str_nlargest.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
# Budget yourself: ~5 min per drill, like a timed round.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
# Same clean slice as Lessons 6-9: drop the unparseable amount (order_id 3) and
# the missing order_date (order_id 4, Chi). 4 clean rows: An x2, Binh x2.
clean = orders.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Drill 1 (value_counts) — how many clean orders does each customer have?
# One line, no groupby: value_counts() on the "customer" column of `clean`.
orders_per_customer = ...

# ---------------------------------------------------------------------------
# Drill 2 (.str accessor) — which customers live in a region whose NAME
# contains "th" (case-insensitive)? Filter `customers` with
# customers["region"].str.contains("th", case=False), keep the whole row.
th_region_customers = ...

# ---------------------------------------------------------------------------
# Drill 3 (nlargest) — the two single BIGGEST orders overall (not per
# customer) from `clean`, by "amount". One call: clean.nlargest(2, "amount").
top_two_orders = ...

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
    check("Drill 1: An has 2 clean orders, Binh has 2 clean orders",
          lambda: orders_per_customer.to_dict() == {"An": 2, "Binh": 2}),
    check("Drill 1: Chi has zero clean orders (dropped by dropna)",
          lambda: "Chi" not in orders_per_customer.index),
    check("Drill 2: th_region_customers is exactly An (North) and Binh (South)",
          lambda: set(th_region_customers["customer"]) == {"An", "Binh"}),
    check("Drill 2: Danh (West — no 'th') is excluded",
          lambda: "Danh" not in th_region_customers["customer"].values),
    check("Drill 3: top_two_orders is Binh/180.0 and An/120.0, in that order",
          lambda: list(zip(top_two_orders["customer"], top_two_orders["amount"]))
          == [("Binh", 180.0), ("An", 120.0)]),
]
print("\nAll green — lesson 10 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
