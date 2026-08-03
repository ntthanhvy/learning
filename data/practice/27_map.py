# Practice 27 — .map(): recoding a Series value-by-value
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/27_map.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-26:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — recode `customer` to `region` with a plain dict, no merge().
# region_map = clean["customer"].map({"An": "North", "Binh": "South"})
try:
    region_map = clean[...].map({"An": "North", "Binh": "South"})
except Exception:
    region_map = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 2 — recode `amount` to a High/Low label with a function.
# amount_label = clean["amount"].map(lambda x: "High" if x >= 100 else "Low")
try:
    amount_label = clean[...].map(lambda x: "High" if x >= 100 else "Low")
except Exception:
    amount_label = pd.Series(dtype=object)

# ---------------------------------------------------------------------------
# Exercise 3 — reproduce the unmatched-key gotcha on purpose: map `customer`
# through a dict that's missing "Binh", then count how many NaNs result.
# partial = clean["customer"].map({"An": "North"})
# n_missing = partial.isna().sum()
try:
    partial = clean[...].map({"An": "North"})
    n_missing = partial.isna().sum()
except Exception:
    partial = pd.Series(dtype=object)
    n_missing = -1

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
    check("Exercise 1: region_map recodes customer -> region correctly",
          lambda: region_map.tolist() == ["North", "North", "South", "South"]),
    check("Exercise 2: amount_label buckets High/Low correctly",
          lambda: amount_label.tolist() == ["High", "Low", "Low", "High"]),
    check("Exercise 3: partial has An mapped, Binh rows are NaN",
          lambda: partial.tolist()[:2] == ["North", "North"] and partial.isna().tolist()[2:] == [True, True]),
    check("Exercise 3: n_missing counts exactly the 2 unmatched Binh rows",
          lambda: n_missing == 2),
]
print("\nAll green — lesson 27 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
