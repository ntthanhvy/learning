# Practice 17 — crosstab(): frequency tables done right
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/17_crosstab.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-16: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])

# Same bins/labels as Lesson 12: Low <=40, Mid <=100, High <=200.
tier = pd.cut(clean["amount"], bins=[0, 40, 100, 200], labels=["Low", "Mid", "High"])

# ---------------------------------------------------------------------------
# Exercise 1 — pd.crosstab(index, columns) counts how often each customer/tier
# combination occurs, no values/aggfunc needed for a plain count:
# pd.crosstab(clean["customer"], tier)
try:
    counts = pd.crosstab(clean["customer"], ...)
except Exception:
    counts = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — normalize="index" turns each row into proportions of that
# row's own total, summing to 1.0 across each customer:
# pd.crosstab(clean["customer"], tier, normalize="index")
try:
    row_pct = pd.crosstab(clean["customer"], tier, normalize=...)
except Exception:
    row_pct = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — add values= and aggfunc= to sum the real amount column per
# cell instead of counting rows — this is what makes crosstab functionally
# identical to pivot_table:
# pd.crosstab(clean["customer"], tier, values=clean["amount"], aggfunc="sum")
try:
    sums = pd.crosstab(clean["customer"], tier, values=clean["amount"], aggfunc=...)
except Exception:
    sums = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 4 — the equivalence: pd.crosstab(a, b) with no values/aggfunc is
# the same table as pivot_table(index=a, columns=b, aggfunc="size",
# fill_value=0). Build the pivot_table version and prove the two match.
# clean.pivot_table(index="customer", columns=tier, aggfunc="size", fill_value=0)
try:
    via_pivot = clean.pivot_table(index="customer", columns=tier, aggfunc=..., fill_value=0)
    same_as_crosstab = (via_pivot.values == counts.values).all()
except Exception:
    same_as_crosstab = False

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
    check("Exercise 1: counts — An has 0 Low/1 Mid/1 High, Binh has 1 Low/0 Mid/1 High",
          lambda: counts.loc["An", "Low"] == 0
          and counts.loc["An", "Mid"] == 1
          and counts.loc["An", "High"] == 1
          and counts.loc["Binh", "Low"] == 1
          and counts.loc["Binh", "High"] == 1),
    check("Exercise 2: row_pct — An's row is 0.0/0.5/0.5 and sums to 1.0",
          lambda: round(row_pct.loc["An", "Mid"], 2) == 0.5
          and round(row_pct.loc["An", "High"], 2) == 0.5
          and abs(row_pct.loc["An"].sum() - 1.0) < 1e-9),
    check("Exercise 3: sums — An's High cell is 120.0, Binh's Low cell is 35.5",
          lambda: round(sums.loc["An", "High"], 2) == 120.0
          and round(sums.loc["Binh", "Low"], 2) == 35.5),
    check("Exercise 4: crosstab(no values/aggfunc) matches pivot_table(aggfunc='size')",
          lambda: same_as_crosstab),
]
print("\nAll green — lesson 17 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
