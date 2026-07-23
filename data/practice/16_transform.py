# Practice 16 — transform(): broadcasting a group value back to every row
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/16_transform.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-15: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — transform("mean") computes each customer's average amount, but
# unlike agg()/sum() it returns a result the SAME LENGTH as clean, one value
# per original row (each customer's rows all get that customer's mean):
# clean.groupby("customer")["amount"].transform("mean")
try:
    group_mean = clean.groupby("customer")["amount"].transform(...)
except Exception:
    group_mean = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — because group_mean is already aligned row-for-row with clean,
# subtracting it needs no merge/join back — just plain Series subtraction:
# clean["amount"] - group_mean
try:
    dev_from_group_mean = clean["amount"] - group_mean
except Exception:
    dev_from_group_mean = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — transform() accepts any aggregation name, not just "mean".
# Use "sum" this time to get each row's share of its customer's total:
# clean["amount"] / clean.groupby("customer")["amount"].transform("sum")
try:
    group_total = clean.groupby("customer")["amount"].transform(...)
    pct_of_group_total = clean["amount"] / group_total
except Exception:
    pct_of_group_total = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — the defining property of transform(): its output is always the
# same length as the input it was called on, row for row, group size no
# matter. Prove it for group_mean.
# len(group_mean) == len(clean)
same_length = len(group_mean) == len(clean)

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
    check("Exercise 1: group_mean aligns per row — An's rows are both 81.0, Binh's both 107.75",
          lambda: round(group_mean.iloc[0], 2) == 81.0
          and round(group_mean.iloc[1], 2) == 107.75
          and round(group_mean.iloc[2], 2) == 107.75
          and round(group_mean.iloc[3], 2) == 81.0),
    check("Exercise 2: dev_from_group_mean — first row (An, 120.0) is +39.0 above its group mean",
          lambda: round(dev_from_group_mean.iloc[0], 2) == 39.0
          and round(dev_from_group_mean.iloc[1], 2) == -72.25
          and round(dev_from_group_mean.iloc[2], 2) == 72.25),
    check("Exercise 3: pct_of_group_total — An's two rows sum to 1.0 (100% of An's total)",
          lambda: abs(pct_of_group_total.iloc[0] + pct_of_group_total.iloc[3] - 1.0) < 1e-9
          and round(pct_of_group_total.iloc[0], 4) == 0.7407),
    check("Exercise 4: transform() output is exactly as long as its input, no collapsing",
          lambda: same_length and len(group_mean) == 4),
]
print("\nAll green — lesson 16 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
