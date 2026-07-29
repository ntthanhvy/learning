# Practice 22 — query(): WHERE, spelled as a string
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/22_query.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

# Same cleaned 4-row slice as Lessons 6-21:
# An 120.0/01-05, Binh 35.5/01-06, Binh 180.0/01-09, An 42.0/01-10
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — filter to rows with amount > 100, using query() instead of a
# boolean mask.
# clean.query("amount > 100")
try:
    over_100 = clean.query(...)
except Exception:
    over_100 = pd.DataFrame(columns=clean.columns)

# ---------------------------------------------------------------------------
# Exercise 2 — filter to An's orders with amount > 50, using "and" plus a
# string-equality condition inside the query string.
# clean.query("amount > 50 and customer == 'An'")
try:
    an_over_50 = clean.query("amount > 50 and customer == ...")
except Exception:
    an_over_50 = pd.DataFrame(columns=clean.columns)

# ---------------------------------------------------------------------------
# Exercise 3 — filter using a Python variable pulled into the expression
# with the @ prefix (not a hardcoded number). Fill in the column name.
# threshold = 100
# clean.query("amount > @threshold")
threshold = 100
try:
    above_threshold = clean.query(... + " > @threshold")
except Exception:
    above_threshold = pd.DataFrame(columns=clean.columns)

# ---------------------------------------------------------------------------
# Exercise 4 — chain a merge() straight into a query(), with no intermediate
# variable holding a boolean mask.
# clean.merge(customers, on="customer", how="left").query("region == 'South'")
try:
    south_orders = (
        clean
        .merge(customers, on="customer", how="left")
        .query(...)
    )
except Exception:
    south_orders = pd.DataFrame(columns=list(clean.columns) + ["region"])

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
    check("Exercise 1: amount > 100 keeps An/120.0 and Binh/180.0, 2 rows",
          lambda: len(over_100) == 2 and set(over_100["customer"]) == {"An", "Binh"}
          and sorted(over_100["amount"]) == [120.0, 180.0]),
    check("Exercise 2: An's orders over 50 — just order_id 1 (120.0)",
          lambda: len(an_over_50) == 1 and an_over_50["order_id"].iloc[0] == 1
          and an_over_50["amount"].iloc[0] == 120.0),
    check("Exercise 3: @threshold pulls the Python variable, same 2 rows as Ex.1",
          lambda: len(above_threshold) == 2
          and sorted(above_threshold["amount"]) == [120.0, 180.0]),
    check("Exercise 4: merge().query() chain keeps Binh's 2 South orders",
          lambda: len(south_orders) == 2 and set(south_orders["customer"]) == {"Binh"}
          and set(south_orders["region"]) == {"South"}),
]
print("\nAll green — lesson 22 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
