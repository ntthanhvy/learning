# Practice 28 — pd.wide_to_long(): melting several metrics at once
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/28_wide_to_long.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-27:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# Number each customer's visits 1, 2, ... in date order (Lesson 4's groupby).
clean["visit"] = clean.groupby("customer").cumcount() + 1

# ---------------------------------------------------------------------------
# Exercise 1 — build a wide table with TWO metrics per visit: pivot_table with
# index="customer", columns="visit", values=["amount", "order_date"],
# aggfunc="first", then flatten the MultiIndex columns to "amount_1" style
# strings (Lesson 14's move): [f"{a}_{b}" for a, b in wide.columns]
try:
    wide = clean.pivot_table(index="customer", columns="visit",
                              values=["amount", "order_date"], aggfunc="first")
    wide.columns = [...]
    wide = wide.reset_index()
except Exception:
    wide = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — reshape `wide` back to long with pd.wide_to_long(): the two
# stubnames are "amount" and "order_date", i="customer" (already unique per
# row), j="visit" (the new suffix column), sep="_", suffix=r"\d+".
try:
    long = pd.wide_to_long(wide, stubnames=[...], i="customer", j="visit",
                            sep="_", suffix=r"\d+").reset_index()
except Exception:
    long = pd.DataFrame(columns=["customer", "visit", "amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 3 — reproduce the missing-stubname gotcha on purpose: call
# wide_to_long with a stubnames list that includes "amount" (real) AND
# "nonexistent" (not a real column prefix at all). It should NOT raise --
# it silently adds a "nonexistent" column filled entirely with NaN.
try:
    gotcha = pd.wide_to_long(wide, stubnames=["amount", ...], i="customer",
                              j="visit", sep="_", suffix=r"\d+").reset_index()
    n_gotcha_nan = gotcha["nonexistent"].isna().sum()
except Exception:
    gotcha = pd.DataFrame()
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
    check("Exercise 1: wide has flat columns amount_1/amount_2/order_date_1/order_date_2",
          lambda: set(wide.columns) == {"customer", "amount_1", "amount_2",
                                         "order_date_1", "order_date_2"}
          and float(wide.loc[wide["customer"] == "An", "amount_1"].iloc[0]) == 120.0),
    check("Exercise 2: long has 4 rows, An visit 2 amount is 42.0",
          lambda: len(long) == 4
          and set(long.columns) == {"customer", "visit", "amount", "order_date"}
          and float(long[(long["customer"] == "An") & (long["visit"] == 2)]["amount"].iloc[0]) == 42.0),
    check("Exercise 2: Binh visit 1 order_date is 2026-01-06",
          lambda: long[(long["customer"] == "Binh") & (long["visit"] == 1)]["order_date"].iloc[0] == "2026-01-06"),
    check("Exercise 3: gotcha does not raise; has a 'nonexistent' column",
          lambda: "nonexistent" in gotcha.columns and len(gotcha) == 4),
    check("Exercise 3: n_gotcha_nan is exactly 4 (every row, all NaN)",
          lambda: n_gotcha_nan == 4),
]
print("\nAll green — lesson 28 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
