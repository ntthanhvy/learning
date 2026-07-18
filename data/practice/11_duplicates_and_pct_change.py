# Practice 11 — Timed Drills, Round 3: duplicated, drop_duplicates, pct_change
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/11_duplicates_and_pct_change.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
# Budget yourself: ~5 min per drill, like a timed round.
import pandas as pd

# ---------------------------------------------------------------------------
# Drills 1-2 use a small inline "double-submitted export" DataFrame — a
# realistic scenario (a retry resent the same rows), not a new CSV fixture.
raw_export = pd.DataFrame({
    "customer": ["An", "Binh", "An", "Chi", "An"],
    "amount":   [120.0, 35.5, 120.0, 99.9, 120.0],
})
# rows: 0=An/120 1=Binh/35.5 2=An/120(repeat of 0) 3=Chi/99.9 4=An/120(repeat of 0)

# ---------------------------------------------------------------------------
# Drill 1 (duplicated) — which rows are exact repeats of an earlier row?
# One call, default keep="first": raw_export.duplicated()
is_dupe = ...

# ---------------------------------------------------------------------------
# Drill 2 (drop_duplicates) — the export with repeats removed, keeping each
# row's first occurrence. One call: raw_export.drop_duplicates()
deduped = ...

# ---------------------------------------------------------------------------
# Drill 3 (pct_change) — order-over-order % change in amount, per customer,
# on the real orders_raw.csv fixture (same clean slice as Lessons 6-10).
# Steps: sort_values(["customer", "order_date"]), then
# groupby("customer")["amount"].pct_change() as a new column "amount_pct_change".
orders = pd.read_csv("practice/data/orders_raw.csv")
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
clean = orders.dropna(subset=["amount", "order_date"])

try:
    ordered = ...  # clean, sorted by ["customer", "order_date"]
    ordered["amount_pct_change"] = ...
except Exception:
    ordered = pd.DataFrame({"customer": [], "amount_pct_change": []})

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
    check("Drill 1: is_dupe is False,False,True,False,True (rows 2 & 4 repeat row 0)",
          lambda: list(is_dupe) == [False, False, True, False, True]),
    check("Drill 1: exactly 2 rows flagged duplicated",
          lambda: int(is_dupe.sum()) == 2),
    check("Drill 2: deduped has 3 rows (An, Binh, Chi — one each)",
          lambda: len(deduped) == 3),
    check("Drill 2: deduped keeps the FIRST An row (order preserved)",
          lambda: deduped.iloc[0]["customer"] == "An" and deduped.iloc[0]["amount"] == 120.0),
    check("Drill 3: An's pct_change is NaN then -0.65 (120.0 -> 42.0)",
          lambda: (
              pd.isna(ordered.loc[ordered["customer"] == "An", "amount_pct_change"].iloc[0])
              and round(ordered.loc[ordered["customer"] == "An", "amount_pct_change"].iloc[1], 2) == -0.65
          )),
    check("Drill 3: Binh's pct_change is NaN then ~4.07 (35.5 -> 180.0)",
          lambda: (
              pd.isna(ordered.loc[ordered["customer"] == "Binh", "amount_pct_change"].iloc[0])
              and round(ordered.loc[ordered["customer"] == "Binh", "amount_pct_change"].iloc[1], 2) == 4.07
          )),
]
print("\nAll green — lesson 11 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
