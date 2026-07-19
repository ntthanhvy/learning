# Practice 12 — apply() and pd.cut(): row-wise logic and vectorized binning
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/12_apply_and_cut.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
clean = orders.dropna(subset=["amount", "order_date"])
merged = clean.merge(customers, on="customer", how="left")
# rows: An/120.0/North, Binh/35.5/South, Binh/180.0/South, An/42.0/North

# ---------------------------------------------------------------------------
# Drill 1 (apply, axis=1) — build a one-line label per order combining THREE
# columns (customer, region, amount) into a formatted string. No vectorized
# string-format shortcut for this shape — an honest use of apply().
def make_label(row):
    # TODO: return f"{row['customer']} ({row['region']}): ${row['amount']:.2f}"
    ...


merged["label"] = merged.apply(make_label, axis=1)

# ---------------------------------------------------------------------------
# Drill 2 (pd.cut) — bin "amount" into tiers, WITHOUT apply() or a loop.
# bins=[0, 40, 100, 200], labels=["Low", "Mid", "High"]
try:
    merged["tier"] = pd.cut(merged["amount"], bins=..., labels=...)
except Exception:
    merged["tier"] = pd.NA

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
    check("Drill 1: An/120.0 row's label reads 'An (North): $120.00'",
          lambda: merged.loc[(merged["customer"] == "An") & (merged["amount"] == 120.0), "label"].iloc[0] == "An (North): $120.00"),
    check("Drill 1: Binh/35.5 row's label reads 'Binh (South): $35.50'",
          lambda: merged.loc[(merged["customer"] == "Binh") & (merged["amount"] == 35.5), "label"].iloc[0] == "Binh (South): $35.50"),
    check("Drill 2: amount 35.5 -> tier 'Low'",
          lambda: str(merged.loc[merged["amount"] == 35.5, "tier"].iloc[0]) == "Low"),
    check("Drill 2: amount 42.0 -> tier 'Mid'",
          lambda: str(merged.loc[merged["amount"] == 42.0, "tier"].iloc[0]) == "Mid"),
    check("Drill 2: 120.0 and 180.0 both land in tier 'High'",
          lambda: (str(merged.loc[merged["amount"] == 120.0, "tier"].iloc[0]) == "High"
                   and str(merged.loc[merged["amount"] == 180.0, "tier"].iloc[0]) == "High")),
]
print("\nAll green — lesson 12 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
