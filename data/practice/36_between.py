# Practice 36 — between()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/36_between.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-35:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
amounts = clean["amount"]

# ---------------------------------------------------------------------------
# Exercise 1 — a mask for amounts between 50 and 150 (inclusive both ends).
try:
    mask_50_150 = amounts.between(..., 150)
except Exception:
    mask_50_150 = None

# ---------------------------------------------------------------------------
# Exercise 2 — use that mask to filter `clean` down to just the matching rows.
try:
    filtered = clean[...]
except Exception:
    filtered = None

# ---------------------------------------------------------------------------
# Exercise 3 — a mask for amounts between 42 and 120, EXCLUDING both ends
# (inclusive="neither").
try:
    mask_neither = amounts.between(42, 120, inclusive=...)
except Exception:
    mask_neither = None

# ---------------------------------------------------------------------------
# Exercise 4 — a date-range mask: order_date between 2026-01-06 and
# 2026-01-09 (inclusive both ends, the default).
try:
    dates = pd.to_datetime(clean["order_date"])
    date_mask = dates.between("2026-01-06", ...)
except Exception:
    date_mask = None

# ---------------------------------------------------------------------------
# Exercise 5 — the NaN gotcha: between() on a Series with a missing value;
# the NaN row should come back False, not True and not an error.
try:
    s = pd.Series([10.0, np.nan, ...])
    nan_mask = s.between(0, 200)
except Exception:
    nan_mask = None

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
    check("Exercise 1: between(50, 150) gives [True, False, False, False]",
          lambda: mask_50_150 is not None and mask_50_150.tolist() == [True, False, False, False]),
    check("Exercise 2: filtered keeps only order_id 1 (An, 120.0)",
          lambda: filtered is not None and filtered["order_id"].tolist() == [1]),
    check("Exercise 3: inclusive='neither' gives [False, False, False, False]",
          lambda: mask_neither is not None and mask_neither.tolist() == [False, False, False, False]),
    check("Exercise 4: date-range mask gives [False, False, True, True]",
          lambda: date_mask is not None and date_mask.tolist() == [False, False, True, True]),
    check("Exercise 5: the NaN row comes back False, not True",
          lambda: nan_mask is not None and nan_mask.tolist() == [True, False, True]),
]
print("\nAll green — lesson 36 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
