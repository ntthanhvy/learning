# Practice 35 — clip()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/35_clip.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-34:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
amounts = clean["amount"]

# ---------------------------------------------------------------------------
# Exercise 1 — clip amounts to [50, 150] (both bounds at once).
try:
    both_bounds = amounts.clip(lower=..., upper=150)
except Exception:
    both_bounds = None

# ---------------------------------------------------------------------------
# Exercise 2 — clip amounts with a lower bound of 50 only (no upper bound).
try:
    lower_only = amounts.clip(lower=...)
except Exception:
    lower_only = None

# ---------------------------------------------------------------------------
# Exercise 3 — clip amounts with an upper bound of 100 only (no lower bound).
try:
    upper_only = amounts.clip(upper=...)
except Exception:
    upper_only = None

# ---------------------------------------------------------------------------
# Exercise 4 — per-row bound: clip amounts against a per-row Series floor
# [100, 40, 50, 40] (same row order as `amounts`, positionally aligned).
try:
    row_floor = pd.Series([100, 40, 50, ...])
    per_row = amounts.clip(lower=row_floor)
except Exception:
    per_row = None

# ---------------------------------------------------------------------------
# Exercise 5 — the NaN-passthrough gotcha: clip a small Series containing a
# missing value; the NaN should still be NaN afterward, not filled in.
try:
    s = pd.Series([10.0, np.nan, 200.0])
    clipped_with_nan = s.clip(lower=50, upper=...)
except Exception:
    clipped_with_nan = None

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
    check("Exercise 1: clip(lower=50, upper=150) gives [120.0, 50.0, 50.0, 150.0]",
          lambda: both_bounds is not None and both_bounds.tolist() == [120.0, 50.0, 50.0, 150.0]),
    check("Exercise 2: clip(lower=50) gives [120.0, 50.0, 50.0, 180.0]",
          lambda: lower_only is not None and lower_only.tolist() == [120.0, 50.0, 50.0, 180.0]),
    check("Exercise 3: clip(upper=100) gives [100.0, 42.0, 35.5, 100.0]",
          lambda: upper_only is not None and upper_only.tolist() == [100.0, 42.0, 35.5, 100.0]),
    check("Exercise 4: per-row floor clip gives [120.0, 42.0, 50.0, 180.0]",
          lambda: per_row is not None and per_row.tolist() == [120.0, 42.0, 50.0, 180.0]),
    check("Exercise 5: the NaN stays NaN, not filled with a bound",
          lambda: clipped_with_nan is not None
          and clipped_with_nan.iloc[0] == 50.0
          and pd.isna(clipped_with_nan.iloc[1])
          and clipped_with_nan.iloc[2] == 150.0),
]
print("\nAll green — lesson 35 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
