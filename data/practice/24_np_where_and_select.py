# Practice 24 — np.where() and np.select(): vectorized if/else
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/24_np_where_and_select.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-23:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — two-way split with np.where(): "High" if amount >= 100,
# else "Low". CASE WHEN amount >= 100 THEN 'High' ELSE 'Low' END.
# np.where(clean["amount"] >= 100, "High", "Low")
try:
    clean["tier"] = np.where(clean["amount"] >= ..., "High", "Low")
except Exception:
    clean["tier"] = pd.Series([None] * len(clean))

# ---------------------------------------------------------------------------
# Exercise 2 — three-way split with np.select(): "High" if amount >= 150,
# "Mid" if amount >= 50, else "Low". Order matters: put the >= 150 condition
# FIRST so it isn't shadowed by the >= 50 condition matching first.
# conditions = [clean["amount"] >= 150, clean["amount"] >= 50]
# choices = ["High", "Mid"]
# np.select(conditions, choices, default="Low")
try:
    conditions = [clean["amount"] >= 150, clean["amount"] >= 50]
    choices = ["High", "Mid"]
    clean["tier3"] = np.select(conditions, ..., default="Low")
except Exception:
    clean["tier3"] = pd.Series([None] * len(clean))

# Exercise 3 — prove order matters: build the SAME two conditions but in the
# WRONG order (>= 50 checked before >= 150). Binh's 180.0 row qualifies for
# BOTH conditions -- correctly ordered it lands on "High" (Exercise 2), but
# with >= 50 checked first it wrongly lands on "Mid" instead, since
# np.select() always uses the FIRST matching condition.
# np.select([clean["amount"] >= 50, clean["amount"] >= 150], ["Mid", "High"], default="Low")
try:
    wrong_conditions = [clean["amount"] >= 50, clean["amount"] >= 150]
    wrong_choices = ["Mid", "High"]
    clean["tier3_wrong_order"] = np.select(..., wrong_choices, default="Low")
except Exception:
    clean["tier3_wrong_order"] = pd.Series([None] * len(clean))

# ---------------------------------------------------------------------------
# Exercise 4 — left-merge with customers.csv, then use np.where() to fill a
# missing (NaN) region with "Unknown" instead of leaving it blank. An and
# Binh both have a real customers.csv match (North/South) so this checks
# np.where() leaves real values untouched -- Lesson 5's orphan case (Chi,
# order_id 4, no customers.csv row) is exactly when this branch would kick
# in for real, but Chi was already dropped by the amount-cleaning step above.
# np.where(merged["region"].isna(), "Unknown", merged["region"])
try:
    customers = pd.read_csv("practice/data/customers.csv")
    merged = clean.merge(customers, on="customer", how="left")
    merged["region_label"] = np.where(merged["region"].isna(), "Unknown", merged[...])
except Exception:
    merged = clean.copy()
    merged["region_label"] = pd.Series([None] * len(merged))

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
    check("Exercise 1: np.where() tier — An 120.0->High, 42.0->Low; Binh 35.5->Low, 180.0->High",
          lambda: clean["tier"].tolist() == ["High", "Low", "Low", "High"]),
    check("Exercise 2: np.select() tier3 — An 120.0->Mid, 42.0->Low; Binh 35.5->Low, 180.0->High",
          lambda: clean["tier3"].tolist() == ["Mid", "Low", "Low", "High"]),
    check("Exercise 3: swapping condition order changes Binh's 180.0 row from High to Mid (order matters, first match wins)",
          lambda: clean["tier3_wrong_order"].tolist() == ["Mid", "Low", "Low", "Mid"]
          and clean.loc[clean["amount"] == 180.0, "tier3"].iloc[0] == "High"
          and clean.loc[clean["amount"] == 180.0, "tier3_wrong_order"].iloc[0] == "Mid"),
    check("Exercise 4: merged region_label matches the real region for An (North) and Binh (South), no NaN leaks through",
          lambda: merged.loc[merged["customer"] == "An", "region_label"].tolist() == ["North", "North"]
          and merged.loc[merged["customer"] == "Binh", "region_label"].tolist() == ["South", "South"]
          and merged["region_label"].isna().sum() == 0),
]
print("\nAll green — lesson 24 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
