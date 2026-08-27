# Practice 50 — corr(): does this actually move with that?
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/50_corr.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Small inline reps table (not a shared CSV fixture, same precedent as Lesson
# 19's tagged-orders table and Lesson 11's inline "double-submitted export"
# table): calls_made and deals_closed are genuinely related; office_size_sqm
# is an unrelated decoy column (Section 2's gotcha).
demo = pd.DataFrame({
    "rep":             ["Mai", "Long", "Chi", "Huy", "Trang"],
    "calls_made":      [10, 25, 15, 40, 30],
    "deals_closed":    [2, 6, 3, 9, 7],
    "office_size_sqm": [12, 30, 15, 8, 45],
})

# Same real fixture clean 4-row slice as Lessons 6-49.
raw = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(raw["amount"], errors="coerce")
order_date = pd.to_datetime(raw["order_date"], errors="coerce")
clean = (
    raw.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
#   order_id customer  amount order_date
# 0        1       An   120.0 2026-01-05
# 1        6       An    42.0 2026-01-10
# 2        2     Binh    35.5 2026-01-06
# 3        5     Binh   180.0 2026-01-09

# ---------------------------------------------------------------------------
# Exercise 1 — calls_made and deals_closed genuinely move together. Get their
# corr() value (Section 1).
try:
    calls_deals_corr = demo["calls_made"].corr(demo[...])
except Exception:
    calls_deals_corr = None

# ---------------------------------------------------------------------------
# Exercise 2 — office_size_sqm has no real reason to track calls_made. Get
# their corr() value too, and see how much weaker it is (Section 2).
try:
    calls_office_corr = demo["calls_made"].corr(demo[...])
except Exception:
    calls_office_corr = None

# ---------------------------------------------------------------------------
# Exercise 3 — whole-DataFrame corr() on `clean` raises ValueError, since it
# still carries the text customer column and the datetime order_date column.
# Pass the keyword that narrows the computation to numeric columns only
# (Section 3), then pull the order_id/amount corr value out of the matrix.
# NOTE: numeric_only=... would NOT raise on its own (bool(...) is truthy in
# Python, so pandas would silently treat it as numeric_only=True) -- the
# `is True` check below forces a real, explicit boolean instead of relying
# on that accidental truthiness.
try:
    use_numeric_only = ...
    assert use_numeric_only is True
    numeric_corr = clean.corr(numeric_only=use_numeric_only)
    order_amount_corr = float(numeric_corr.loc["order_id", "amount"])
except Exception:
    order_amount_corr = None

# ---------------------------------------------------------------------------
# Exercise 4 — corr()'s default NaN handling is pairwise deletion: only the
# row where EITHER compared column is missing gets dropped, not the whole
# table. Set row 2's deals_closed to NaN, then confirm corr() on the
# remaining 4 complete rows matches a manual dropna + corr() by hand
# (Section 4).
demo_gap = demo.copy()
demo_gap.loc[2, "deals_closed"] = None
try:
    pairwise_corr = demo_gap["calls_made"].corr(demo_gap[...])
    manual = demo_gap.dropna(subset=["deals_closed"])
    manual_corr = manual["calls_made"].corr(manual["deals_closed"])
except Exception:
    pairwise_corr = None
    manual_corr = None

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
    check("Exercise 1: calls_made vs deals_closed corr() is ~0.9959 (strongly related)",
          lambda: abs(calls_deals_corr - 0.9958962509386671) < 1e-9),
    check("Exercise 2: calls_made vs office_size_sqm corr() is ~0.1710 (weak, unrelated)",
          lambda: abs(calls_office_corr - 0.17095081120783429) < 1e-9),
    check("Exercise 3: numeric_only=True fixes the crash; order_id vs amount corr() is ~0.0443",
          lambda: abs(order_amount_corr - 0.04427167913261477) < 1e-9),
    check("Exercise 4: pairwise corr() with the NaN row matches a manual dropna corr()",
          lambda: pairwise_corr is not None and manual_corr is not None
          and abs(pairwise_corr - manual_corr) < 1e-9),
    check("Exercise 4: that pairwise/manual value is ~0.9964, not the full-table 0.9959",
          lambda: abs(pairwise_corr - 0.9964037900472442) < 1e-9),
]
print("\nAll green — lesson 50 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
