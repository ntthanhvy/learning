# Practice 18 — qcut(): binning by rank, not by value
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/18_qcut.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean 4-row slice as Lessons 6-17: An x2, Binh x2, one order per date.
clean = df.dropna(subset=["amount", "order_date"])
# rows: An/120.0, Binh/35.5, Binh/180.0, An/42.0

# ---------------------------------------------------------------------------
# Exercise 1 — rerun Lesson 12's exact fixed-edge cut() for contrast:
# bins=[0, 40, 100, 200], labels=["Low", "Mid", "High"]
try:
    tier_cut = pd.cut(clean["amount"], bins=..., labels=["Low", "Mid", "High"])
    cut_counts = tier_cut.value_counts()
except Exception:
    cut_counts = pd.Series(dtype=int)

# ---------------------------------------------------------------------------
# Exercise 2 — qcut() into 4 equal-COUNT bins (quartiles), not fixed edges:
# pd.qcut(clean["amount"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
try:
    tier_qcut4 = pd.qcut(clean["amount"], q=..., labels=["Q1", "Q2", "Q3", "Q4"])
    qcut4_counts = tier_qcut4.value_counts()
except Exception:
    qcut4_counts = pd.Series(dtype=int)

# ---------------------------------------------------------------------------
# Exercise 3 — qcut() into 2 bins: the median split.
# pd.qcut(clean["amount"], q=2, labels=["Low", "High"])
try:
    tier_qcut2 = pd.qcut(clean["amount"], q=2, labels=...)
except Exception:
    tier_qcut2 = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 4 — labels=False returns the raw bin number (0-indexed) instead of
# a category label; add 1 to match SQL's NTILE(n), which numbers from 1.
# pd.qcut(clean["amount"], q=4, labels=False) + 1
try:
    ntile = pd.qcut(clean["amount"], q=4, labels=False) + ...
except Exception:
    ntile = pd.Series(dtype=float)

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
    check("Exercise 1: cut() with Lesson 12's bins gives an UNEQUAL split — High=2, Low=1, Mid=1",
          lambda: cut_counts["High"] == 2 and cut_counts["Low"] == 1 and cut_counts["Mid"] == 1),
    check("Exercise 2: qcut(q=4) gives an EQUAL split — exactly 1 row in each of Q1-Q4",
          lambda: qcut4_counts["Q1"] == 1 and qcut4_counts["Q2"] == 1
          and qcut4_counts["Q3"] == 1 and qcut4_counts["Q4"] == 1),
    check("Exercise 3: qcut(q=2) median split — 35.5 & 42.0 are Low, 120.0 & 180.0 are High",
          lambda: str(tier_qcut2.loc[clean["amount"] == 35.5].iloc[0]) == "Low"
          and str(tier_qcut2.loc[clean["amount"] == 42.0].iloc[0]) == "Low"
          and str(tier_qcut2.loc[clean["amount"] == 120.0].iloc[0]) == "High"
          and str(tier_qcut2.loc[clean["amount"] == 180.0].iloc[0]) == "High"),
    check("Exercise 4: ntile (labels=False + 1) — 35.5 is quartile 1, 180.0 is quartile 4",
          lambda: int(ntile.loc[clean["amount"] == 35.5].iloc[0]) == 1
          and int(ntile.loc[clean["amount"] == 180.0].iloc[0]) == 4),
]
print("\nAll green — lesson 18 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
