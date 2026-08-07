# Practice 30 — Broadcasting: why pandas arithmetic "just works"
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/30_broadcasting.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-29:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — broadcast a scalar: bump every amount up by 10% (multiply the
# whole "amount" column by 1.1), no loop.
try:
    bumped = clean[...] * 1.1
except Exception:
    bumped = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — deviation from the column's own mean: subtract amount's mean
# from every row (Section 2's Series-minus-scalar broadcast, the same shape
# Lesson 16's transform("mean") automates per group).
try:
    deviation = clean[...] - clean["amount"].mean()
except Exception:
    deviation = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — raw NumPy shape broadcasting (Section 4): a (2, 3) array plus
# a (3,) row should broadcast the row across both rows of the array.
# arr = [[1, 2, 3], [4, 5, 6]], row = [10, 20, 30]
try:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    row = np.array([...])
    broadcast_result = arr + row
except Exception:
    broadcast_result = np.zeros((1, 1))

# ---------------------------------------------------------------------------
# Exercise 4 — reproduce Section 5's index-mismatch gotcha on purpose: two
# Series with different index labels ("a","b","c" vs "a","b") added together
# should NOT raise -- it silently produces NaN for the unmatched label "c".
try:
    s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    s2 = pd.Series([10, 20], index=[...])
    gotcha_result = s1 + s2
    n_gotcha_nan = int(gotcha_result.isna().sum())
except Exception:
    gotcha_result = pd.Series(dtype=float)
    n_gotcha_nan = -1

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
    check("Exercise 1: bumped is amount * 1.1 (An's 120.0 -> 132.0)",
          lambda: len(bumped) == 4
          and abs(float(bumped.iloc[0]) - 132.0) < 1e-9),
    check("Exercise 1: bumped's Binh 180.0 row -> 198.0",
          lambda: abs(float(bumped.iloc[3]) - 198.0) < 1e-9),
    check("Exercise 2: deviation has 4 rows summing to (numerically) 0",
          lambda: len(deviation) == 4 and abs(float(deviation.sum())) < 1e-9),
    check("Exercise 2: An's first deviation is 25.625 (120.0 - 94.375)",
          lambda: abs(float(deviation.iloc[0]) - 25.625) < 1e-9),
    check("Exercise 3: broadcast_result has shape (2, 3)",
          lambda: broadcast_result.shape == (2, 3)),
    check("Exercise 3: broadcast_result is [[11,22,33],[14,25,36]]",
          lambda: broadcast_result.tolist() == [[11, 22, 33], [14, 25, 36]]),
    check("Exercise 4: gotcha_result does not raise, has label 'c' as NaN",
          lambda: "c" in gotcha_result.index and pd.isna(gotcha_result["c"])),
    check("Exercise 4: n_gotcha_nan is exactly 1",
          lambda: n_gotcha_nan == 1),
]
print("\nAll green — lesson 30 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
