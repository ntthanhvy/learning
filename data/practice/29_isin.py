# Practice 29 — isin(): filtering against a list of values
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/29_isin.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")

# Same cleaned rows as Lessons 6-28:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — filter `clean` to rows whose customer is "An" or "Chi", using
# isin() (not chained == / | comparisons).
try:
    an_or_chi = clean[clean["customer"].isin([...])]
except Exception:
    an_or_chi = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — the opposite: rows whose customer is NOT "An" (negate isin()
# with ~).
try:
    not_an = clean[~clean["customer"].isin([...])]
except Exception:
    not_an = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — rebuild Lesson 5's "customer with no orders" anti-join using
# isin() instead of merge(indicator=True): rows of `customers` whose
# "customer" value does NOT appear in clean["customer"].
try:
    never_ordered = customers[~customers["customer"].isin(clean[...])]
except Exception:
    never_ordered = pd.DataFrame()

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
    check("Exercise 1: an_or_chi has exactly An's 2 rows (Chi has no clean rows)",
          lambda: len(an_or_chi) == 2 and set(an_or_chi["customer"]) == {"An"}),
    check("Exercise 1: an_or_chi's amounts are 120.0 and 42.0",
          lambda: sorted(an_or_chi["amount"].tolist()) == [42.0, 120.0]),
    check("Exercise 2: not_an has exactly Binh's 2 rows",
          lambda: len(not_an) == 2 and set(not_an["customer"]) == {"Binh"}),
    check("Exercise 3: never_ordered is exactly Danh (West)",
          lambda: list(never_ordered["customer"]) == ["Danh"]
          and list(never_ordered["region"]) == ["West"]),
]
print("\nAll green — lesson 29 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
