# Practice 19 — nunique() and explode(): counting distinct, and un-nesting lists
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/19_nunique_and_explode.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-18: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])
# rows: An/120.0/01-05, Binh/35.5/01-06, Binh/180.0/01-09, An/42.0/01-10

# ---------------------------------------------------------------------------
# Exercise 1 — nunique() on the RAW (6-row) file: how many DISTINCT customers
# placed orders, not how many rows/orders exist.
# df["customer"].nunique()
try:
    distinct_customers = df[...].nunique()
except Exception:
    distinct_customers = None

# ---------------------------------------------------------------------------
# Exercise 2 — contrast nunique() against plain count(): nunique() counts
# DISTINCT values, count() counts non-null ROWS. Compare them on the raw
# "customer" column (6 rows, 3 distinct names, no missing customers).
# df["customer"].count()
try:
    row_count = df[...].count()
except Exception:
    row_count = None

# ---------------------------------------------------------------------------
# Exercise 3 — nunique() per group: how many distinct order dates does each
# customer have, on the clean 4-row slice.
# clean.groupby("customer")["order_date"].nunique()
try:
    dates_per_customer = clean.groupby("customer")[...].nunique()
except Exception:
    dates_per_customer = pd.Series(dtype=int)

# ---------------------------------------------------------------------------
# Exercise 4 — explode(): a small inline DataFrame of orders that each carry
# a list of tags. explode() should produce one row per tag, duplicating the
# other columns (order_id) alongside each exploded value.
tagged = pd.DataFrame({
    "order_id": [1, 2],
    "tags": [["urgent", "gift"], ["bulk"]],
})
# tagged.explode("tags")
try:
    exploded = tagged.explode(...)
except Exception:
    exploded = pd.DataFrame(columns=["order_id", "tags"])

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
    check("Exercise 1: nunique() on raw customer column is 3 (An, Binh, Chi) — not 6 rows",
          lambda: distinct_customers == 3),
    check("Exercise 2: count() on raw customer column is 6 (non-null rows) — different question than nunique()",
          lambda: row_count == 6),
    check("Exercise 3: An has 2 distinct order dates, Binh has 2 distinct order dates",
          lambda: dates_per_customer["An"] == 2 and dates_per_customer["Binh"] == 2),
    check("Exercise 4: exploded has 3 rows (2 tags for order 1, 1 tag for order 2), order_id duplicated for order 1",
          lambda: len(exploded) == 3
          and list(exploded.loc[exploded["order_id"] == 1, "tags"]) == ["urgent", "gift"]
          and list(exploded.loc[exploded["order_id"] == 2, "tags"]) == ["bulk"]),
]
print("\nAll green — lesson 19 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
