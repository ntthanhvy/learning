import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")

clean = (
    df
    .assign(amount=lambda d: pd.to_numeric(d["amount"], errors="coerce"))
    .dropna(subset=["amount", "order_date"])
)

def add_amount_rank(d):
    return d.assign(
        amount_rank=d.groupby("customer")["amount"].rank(method="first", ascending=False)
    )

top_per_customer = (
    clean
    .pipe(add_amount_rank)
    .query("amount_rank == 1")
)

def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok

results = [
    check("Exercise 1: clean has 4 rows (order_id 3 and 4 dropped)",
          lambda: len(clean) == 4),
    check("Exercise 1: clean's amount column is numeric (float64)",
          lambda: str(clean["amount"].dtype) == "float64"),
    check("Exercise 2: add_amount_rank ranks An's 120.0 order (order_id 1) as 1",
          lambda: add_amount_rank(clean).set_index("order_id").loc[1, "amount_rank"] == 1),
    check("Exercise 2: add_amount_rank ranks Binh's 35.5 order (order_id 2) as 2",
          lambda: add_amount_rank(clean).set_index("order_id").loc[2, "amount_rank"] == 2),
    check("Exercise 3: top_per_customer is exactly An/120.0 and Binh/180.0",
          lambda: len(top_per_customer) == 2
          and set(zip(top_per_customer["customer"], top_per_customer["amount"]))
          == {("An", 120.0), ("Binh", 180.0)}),
]
print("\nAll green — lesson 8 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run.")
