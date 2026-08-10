# Practice 34 — pd.get_dummies()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/34_get_dummies.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

# Same cleaned rows as Lessons 6-33, merged with customers.csv for region:
# An 120.0/01-05/North, An 42.0/01-10/North, Binh 35.5/01-06/South, Binh 180.0/01-09/South
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
merged = clean.merge(customers, on="customer", how="left")

# ---------------------------------------------------------------------------
# Exercise 1 — one-hot encode the "customer" column. The result should have
# NO "customer" column left, but two new True/False columns instead.
try:
    dummies = pd.get_dummies(merged, columns=[...])
except Exception:
    dummies = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — the row-sum-to-1 property: every row has exactly one True
# across the new customer dummy columns.
try:
    dummy_cols = [c for c in dummies.columns if c.startswith("customer_")]
    row_sums = dummies[dummy_cols].sum(axis=...)
except Exception:
    row_sums = None

# ---------------------------------------------------------------------------
# Exercise 3 — prefix=: one-hot encode merged["customer"] directly (a Series,
# not a DataFrame this time) with prefix "cust" instead of the default name.
try:
    prefixed = pd.get_dummies(merged["customer"], prefix=...)
except Exception:
    prefixed = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 4 — drop_first=True: one-hot encode merged["customer"] again, but
# drop the first category's column this time (only one column should remain).
try:
    dropped = pd.get_dummies(merged[...], drop_first=True)
    dropped_cols = list(dropped.columns)
except Exception:
    dropped_cols = []

# ---------------------------------------------------------------------------
# Exercise 5 — the silent-NaN gotcha: a small Series with a missing value,
# one-hot encoded with dummy_na=True so the missing row gets its own visible
# column instead of blending into "False everywhere".
try:
    s = pd.Series(["a", "b", ..., "a"])
    with_na_col = pd.get_dummies(s, dummy_na=True)
except Exception:
    with_na_col = pd.DataFrame()

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
    check("Exercise 1: customer column is gone, two new True/False columns exist",
          lambda: "customer" not in dummies.columns
          and "customer_An" in dummies.columns
          and "customer_Binh" in dummies.columns
          and len(dummies) == 4),
    check("Exercise 2: every row sums to exactly 1 across the dummy columns",
          lambda: row_sums is not None and row_sums.tolist() == [1, 1, 1, 1]),
    check("Exercise 3: prefix='cust' renames the columns cust_An / cust_Binh",
          lambda: "cust_An" in prefixed.columns and "cust_Binh" in prefixed.columns),
    check("Exercise 4: drop_first=True leaves exactly one column, 'Binh'",
          lambda: dropped_cols == ["Binh"]),
    check("Exercise 5: dummy_na=True adds a visible NaN column, True on row 2",
          lambda: len(with_na_col.columns) == 3
          and with_na_col.iloc[:, -1].tolist() == [False, False, True, False]),
]
print("\nAll green — lesson 34 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
