# Practice 37 — combine_first()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/37_combine_first.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# Two small inline Series mirroring the lesson's exact example: a "verified"
# primary amount (some gaps) and an "estimated" fallback amount (also has
# values where primary is missing).
primary = pd.Series([120.0, np.nan, 35.5, np.nan])
fallback = pd.Series([999.0, 42.0, 999.0, 180.0])

# ---------------------------------------------------------------------------
# Exercise 1 — fill primary's gaps from fallback.
try:
    filled = primary.combine_first(...)
except Exception:
    filled = None

# ---------------------------------------------------------------------------
# Exercise 2 — confirm primary's OWN value always wins over a conflicting
# fallback value (row 0: primary has 120.0, fallback has 999.0).
try:
    row0_value = filled.iloc[...]
except Exception:
    row0_value = None

# ---------------------------------------------------------------------------
# Exercise 3 — fallback2 has no index labels 2 or 3 at all. Combine it with
# primary and confirm the resulting gap at label 3 stays NaN (no fallback to
# use, no error).
fallback2 = pd.Series([999.0, 42.0], index=[0, 1])
try:
    gap_result = primary.combine_first(...)
except Exception:
    gap_result = None

# ---------------------------------------------------------------------------
# Exercise 4 — DataFrame version: fill df1's gaps cell-by-cell from df2.
try:
    df1 = pd.DataFrame({"amount": [120.0, np.nan], "region": [np.nan, "South"]})
    df2 = pd.DataFrame({"amount": [999.0, 35.5], "region": ["North", "South"]})
    df_filled = df1.combine_first(...)
except Exception:
    df_filled = None

# ---------------------------------------------------------------------------
# Exercise 5 — contrast with update(): unlike combine_first(), update()
# mutates in place and lets the OTHER Series overwrite existing values.
try:
    updated = primary.copy()
    updated.update(...)
except Exception:
    updated = None

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
    check("Exercise 1: combine_first fills gaps -> [120.0, 42.0, 35.5, 180.0]",
          lambda: filled is not None and filled.tolist() == [120.0, 42.0, 35.5, 180.0]),
    check("Exercise 2: row 0 keeps primary's own 120.0, not fallback's 999.0",
          lambda: row0_value is not None and row0_value == 120.0),
    check("Exercise 3: no-match gap at label 3 stays NaN -> [120.0, 42.0, 35.5, NaN]",
          lambda: gap_result is not None
          and gap_result.iloc[:3].tolist() == [120.0, 42.0, 35.5]
          and pd.isna(gap_result.iloc[3])),
    check("Exercise 4: DataFrame combine_first fills each cell independently",
          lambda: df_filled is not None
          and df_filled["amount"].tolist() == [120.0, 35.5]
          and df_filled["region"].tolist() == ["North", "South"]),
    check("Exercise 5: update() overwrites with fallback's values -> [999.0, 42.0, 999.0, 180.0]",
          lambda: updated is not None and updated.tolist() == [999.0, 42.0, 999.0, 180.0]),
]
print("\nAll green — lesson 37 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
