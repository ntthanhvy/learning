# Practice 45 — ffill() and bfill(): carrying a value across a gap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/45_ffill_and_bfill.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lessons 6-44 (orders_raw.csv), loaded/coerced/cleaned the
# same way, sorted by customer then order_date. Binh's FIRST amount (01-06) is
# deliberately blanked out here -- a real, unknown gap right at the boundary
# between An's rows and Binh's rows, so plain ffill() has something real to
# get wrong.
df = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(df["amount"], errors="coerce")
order_date = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
clean.loc[2, "amount"] = None  # Binh's 2026-01-06 amount becomes genuinely unknown

# ---------------------------------------------------------------------------
# Exercise 1 — plain (ungrouped) ffill() on the "amount" column. This is the
# WRONG answer for this data (it will carry An's amount across into Binh's
# row) -- the point of this exercise is to see that happen with your own eyes
# before Exercise 2 fixes it.
try:
    amount_ffill_wrong = clean[...].ffill()
except Exception:
    amount_ffill_wrong = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — the correct version: ffill() chained after groupby("customer"),
# so each customer's gap only ever looks at that same customer's own earlier
# rows.
try:
    amount_ffill_grouped = clean.groupby(...)["amount"].ffill()
except Exception:
    amount_ffill_grouped = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — bfill() on the small standalone Series below (not the orders
# fixture): pulls the NEXT real value backward instead of carrying the
# previous one forward. Fill in the missing second value (30.0's neighbor,
# a real gap -- use None, not a string or anything else) so the Series is
# [10.0, None, 30.0, None], then bfill() pulls 30.0 back into position 1.
# The TRAILING NaN at the end has nothing below it either, so it must stay
# NaN even after bfill().
gapped = pd.Series([10.0, ..., 30.0, None])
try:
    gapped_bfill = gapped.bfill()
except Exception:
    gapped_bfill = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — limit=1 caps how many consecutive gaps one real value can fill.
# Apply ffill with limit=1 to the Series below, which has THREE consecutive
# gaps -- only the first should get filled, the other two must stay NaN.
run = pd.Series([1.0, None, None, None, 5.0])
try:
    run_filled_limited = run.ffill(limit=...)
except Exception:
    run_filled_limited = pd.Series(dtype=float)

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
    check("Exercise 1: ungrouped ffill() WRONGLY carries 42.0 into Binh's row",
          lambda: len(amount_ffill_wrong) == 4 and amount_ffill_wrong.iloc[2] == 42.0),
    check("Exercise 2: grouped ffill() correctly leaves Binh's row as NaN",
          lambda: len(amount_ffill_grouped) == 4 and pd.isna(amount_ffill_grouped.iloc[2])),
    check("Exercise 2: grouped ffill() still fills An's/Binh's real gaps normally",
          lambda: amount_ffill_grouped.iloc[0] == 120.0
          and amount_ffill_grouped.iloc[3] == 180.0),
    check("Exercise 3: bfill() pulls 30.0 backward into index 1",
          lambda: len(gapped_bfill) == 4 and gapped_bfill.iloc[1] == 30.0),
    check("Exercise 3: the trailing NaN (nothing below it) stays NaN too",
          lambda: gapped_bfill.iloc[1] == 30.0 and pd.isna(gapped_bfill.iloc[3])),
    check("Exercise 4: limit=1 fills only the first of three consecutive gaps",
          lambda: len(run_filled_limited) == 5
          and run_filled_limited.iloc[1] == 1.0
          and pd.isna(run_filled_limited.iloc[2])
          and pd.isna(run_filled_limited.iloc[3])
          and run_filled_limited.iloc[4] == 5.0),
]
print("\nAll green — lesson 45 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
