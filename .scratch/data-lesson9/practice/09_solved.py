import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
clean = orders.dropna(subset=["amount", "order_date"])

clean = clean.assign(
    amount_rank=clean.groupby("customer")["amount"].rank(method="first", ascending=False)
)
second_highest = clean[clean["amount_rank"] == 2]

merged = pd.merge(clean, customers, on="customer", how="inner")
revenue_by_region = merged.groupby("region", as_index=False)["amount"].sum()

never_ordered = (
    pd.merge(customers, clean, on="customer", how="left", indicator=True)
    .query("_merge == 'left_only'")["customer"]
    .tolist()
)

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
      else "\nSome ✗ left — fix and re-run.")
