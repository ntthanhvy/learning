# Practice 20 — idxmax() and idxmin(): WHICH row, not just the value
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/20_idxmax_and_idxmin.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-19: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])
# rows (index label : customer/amount/date): 0 An/120.0/01-05, 1 Binh/35.5/01-06,
#                                             4 Binh/180.0/01-09, 5 An/42.0/01-10

# ---------------------------------------------------------------------------
# Exercise 1 — contrast .max() (a VALUE) against .idxmax() (an INDEX LABEL)
# on the whole "amount" column.
# clean["amount"].max()    -> 180.0
# clean["amount"].idxmax() -> 4  (the label of the row holding 180.0)
try:
    max_value = clean[...].max()
except Exception:
    max_value = None
try:
    max_idx = clean[...].idxmax()
except Exception:
    max_idx = None

# ---------------------------------------------------------------------------
# Exercise 2 — use that label with .loc[] to pull back the FULL winning row,
# not just the amount column.
# clean.loc[max_idx]
try:
    max_row = clean.loc[max_idx]
except Exception:
    max_row = None

# ---------------------------------------------------------------------------
# Exercise 3 — groupby(...)["amount"].idxmax(): each customer's top order's
# INDEX LABEL (not the amount itself).
# clean.groupby("customer")["amount"].idxmax()
try:
    top_idx_per_customer = clean.groupby("customer")[...].idxmax()
except Exception:
    top_idx_per_customer = pd.Series(dtype="int64")

# ---------------------------------------------------------------------------
# Exercise 4 — feed the grouped label Series into .loc[] to get each
# customer's FULL top-order row in one step (order_id, customer, amount,
# order_date — not just the amount).
# clean.loc[top_idx_per_customer]
try:
    top_row_per_customer = clean.loc[top_idx_per_customer]
except Exception:
    top_row_per_customer = pd.DataFrame(columns=["order_id", "customer", "amount", "order_date"])

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
    check("Exercise 1: max() is 180.0 (a value), idxmax() is 4 (the row's index label)",
          lambda: max_value == 180.0 and max_idx == 4),
    check("Exercise 2: .loc[max_idx] pulls the full row — Binh's 180.0 order on 2026-01-09",
          lambda: max_row is not None
          and max_row["customer"] == "Binh"
          and max_row["amount"] == 180.0
          and max_row["order_date"] == "2026-01-09"),
    check("Exercise 3: An's top-order label is 0, Binh's top-order label is 4",
          lambda: top_idx_per_customer["An"] == 0 and top_idx_per_customer["Binh"] == 4),
    check("Exercise 4: full top-order rows — An/120.0/01-05 and Binh/180.0/01-09",
          lambda: len(top_row_per_customer) == 2
          and float(top_row_per_customer.loc[0, "amount"]) == 120.0
          and float(top_row_per_customer.loc[4, "amount"]) == 180.0),
]
print("\nAll green — lesson 20 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
