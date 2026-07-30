# Practice 23 — shift(): pulling the previous (or next) row's value alongside
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/23_shift.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-22, but sorted by customer then date so each
# customer's orders sit next to each other in time order (shift() trusts row
# order, same as pct_change()/cumsum()/rolling() before it):
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
ordered = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — pull each customer's PREVIOUS order amount alongside the
# current row, using shift(1) after groupby(). The first order of each
# customer should come back NaN (nothing before it).
# ordered.groupby("customer")["amount"].shift(1)
try:
    ordered["prev_amount"] = ordered.groupby("customer")["amount"].shift(...)
except Exception:
    ordered["prev_amount"] = pd.Series([None] * len(ordered))

# ---------------------------------------------------------------------------
# Exercise 2 — pull each customer's NEXT order amount instead, using a
# negative shift. The LAST order of each customer should come back NaN.
# ordered.groupby("customer")["amount"].shift(-1)
try:
    ordered["next_amount"] = ordered.groupby("customer")["amount"].shift(...)
except Exception:
    ordered["next_amount"] = pd.Series([None] * len(ordered))

# ---------------------------------------------------------------------------
# Exercise 3 — the classic pitfall: shift() with NO groupby bleeds values
# across customers, since it only looks at physical row position. Build
# "wrong_prev" the naive way (no groupby) so the checks below can prove it
# differs from Exercise 1's correctly-grouped prev_amount.
# ordered["amount"].shift(1)
try:
    ordered["wrong_prev"] = ordered[...].shift(1)
except Exception:
    ordered["wrong_prev"] = pd.Series([None] * len(ordered))

# ---------------------------------------------------------------------------
# Exercise 4 — reconstruct diff() by hand from shift(), to show diff() is
# just "current minus shift(1)" under the hood. Compare it against the real
# groupby(...).diff() on the same column.
# ordered.groupby("customer")["amount"].diff()
try:
    ordered["amount_diff_manual"] = ordered["amount"] - ordered["prev_amount"]
    ordered["amount_diff_builtin"] = ordered.groupby("customer")["amount"].diff(...)
except Exception:
    ordered["amount_diff_manual"] = pd.Series([None] * len(ordered))
    ordered["amount_diff_builtin"] = pd.Series([None] * len(ordered))

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
    check("Exercise 1: shift(1) per customer — An's prev_amount is NaN then 120.0",
          lambda: ordered.loc[ordered["customer"] == "An", "prev_amount"].isna().tolist() == [True, False]
          and ordered.loc[(ordered["customer"] == "An") & (ordered["order_date"] == "2026-01-10"), "prev_amount"].iloc[0] == 120.0),
    check("Exercise 1: Binh's prev_amount is NaN then 35.5",
          lambda: ordered.loc[ordered["customer"] == "Binh", "prev_amount"].isna().tolist() == [True, False]
          and ordered.loc[(ordered["customer"] == "Binh") & (ordered["order_date"] == "2026-01-09"), "prev_amount"].iloc[0] == 35.5),
    check("Exercise 2: shift(-1) per customer — An's next_amount is 42.0 then NaN",
          lambda: ordered.loc[ordered["customer"] == "An", "next_amount"].isna().tolist() == [False, True]
          and ordered.loc[(ordered["customer"] == "An") & (ordered["order_date"] == "2026-01-05"), "next_amount"].iloc[0] == 42.0),
    check("Exercise 3: ungrouped shift() bleeds across customers — Binh's first row wrongly gets An's 42.0",
          lambda: ordered.loc[(ordered["customer"] == "Binh") & (ordered["order_date"] == "2026-01-06"), "wrong_prev"].iloc[0] == 42.0
          and ordered.loc[(ordered["customer"] == "Binh") & (ordered["order_date"] == "2026-01-06"), "prev_amount"].isna().iloc[0]),
    check("Exercise 4: hand-built (amount - shift(1)) matches the real groupby diff() exactly",
          lambda: ordered["amount_diff_manual"].fillna(-999).round(6).tolist()
          == ordered["amount_diff_builtin"].fillna(-999).round(6).tolist()
          and ordered.loc[(ordered["customer"] == "An") & (ordered["order_date"] == "2026-01-10"), "amount_diff_builtin"].iloc[0] == -78.0),
]
print("\nAll green — lesson 23 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
