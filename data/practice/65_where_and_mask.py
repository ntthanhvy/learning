# Practice 65 — Series.where() and .mask(): conditional replace that keeps the shape
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/65_where_and_mask.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# Same real fixture as recent lessons, cleaned the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(df["amount"], errors="coerce")
order_date = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
s = clean["amount"]  # [120.0, 42.0, 35.5, 180.0]

# ---------------------------------------------------------------------------
# Exercise 1 — where(): keep values >= 100, replace everything else with 0.
try:
    ex1 = s.where(s >= 100, other=...)
except Exception:
    ex1 = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — mask(): the exact opposite polarity of Exercise 1 on the SAME
# condition (s >= 100) and the SAME other=0 -- replace where True this time.
try:
    ex2 = s.mask(..., other=0)
except Exception:
    ex2 = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — where() with NO `other` argument at all. Confirm the default
# fill value for a failing cell.
try:
    ex3 = s.where(...)
except Exception:
    ex3 = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — the misaligned-condition gotcha. Pass a condition covering
# only the FIRST TWO rows (s.iloc[:2] >= 100) to where() on the full `s`.
# Confirm it does NOT raise, and see what the unmatched rows become.
try:
    short_cond = s.iloc[:2] >= 100
    ex4 = s.where(...)
    ex4_raised = False
except Exception:
    ex4 = pd.Series(dtype=float)
    ex4_raised = True

# ---------------------------------------------------------------------------
# Exercise 5 — chain two mask() calls into a 3-tier recode: start from
# "Mid", then "High" for amount >= 150, then "Low" for amount < 50 -- and
# confirm it matches an equivalent np.select() call exactly.
try:
    tier = pd.Series("Mid", index=s.index)
    tier = tier.mask(s >= 150, "High").mask(...)
    ex5_tier = tier.tolist()
except Exception:
    ex5_tier = []

ex5_expected = list(np.select([s >= 150, s < 50], ["High", "Low"], default="Mid"))

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
    check("Exercise 1: where(s >= 100, other=0) keeps highs, zeroes the rest",
          lambda: ex1.tolist() == [120.0, 0.0, 0.0, 180.0]),
    check("Exercise 2: mask() is where()'s exact opposite polarity",
          lambda: ex2.tolist() == [0.0, 42.0, 35.5, 0.0]),
    check("Exercise 3: where() with no `other` defaults to NaN",
          lambda: ex3.isna().tolist() == [False, True, True, False]),
    check("Exercise 4: a misaligned/shorter condition does NOT raise",
          lambda: not ex4_raised),
    check("Exercise 4b: unmatched rows silently become NaN, not an error",
          lambda: ex4.isna().tolist() == [False, True, True, True]),
    check("Exercise 5: chained mask() matches an equivalent np.select() exactly",
          lambda: ex5_tier == ex5_expected and ex5_tier == ["Mid", "Low", "Low", "High"]),
]

print("\nAll green — lesson 65 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
