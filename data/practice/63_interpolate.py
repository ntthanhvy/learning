# Practice 63 — interpolate(): filling a gap by estimating between real neighbors
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/63_interpolate.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lesson 45 (orders_raw.csv), loaded/coerced/cleaned the
# same way, sorted by customer then order_date. Binh's FIRST amount (01-06) is
# deliberately blanked out here -- a real, unknown gap right at the boundary
# between An's rows and Binh's rows, so plain (ungrouped) interpolate() has
# something real to get wrong.
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
# Exercise 1 — plain (ungrouped) interpolate() on the "amount" column. This is
# the WRONG answer for this data (it draws a straight line from An's last
# value into Binh's row) -- the point of this exercise is to see that happen
# with your own eyes before Exercise 2 fixes it.
try:
    amount_interp_wrong = clean[...].interpolate()
except Exception:
    amount_interp_wrong = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — the correct version. There is no groupby-native interpolate()
# (unlike ffill()/bfill()) -- use groupby("customer")["amount"].transform(...)
# with a lambda calling .interpolate() on each group's own Series.
try:
    amount_interp_grouped = clean.groupby("customer")["amount"].transform(
        lambda s: ...
    )
except Exception:
    amount_interp_grouped = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — default interpolate() on the standalone Series below leaves a
# LEADING gap (nothing above it to draw a line from) as NaN. Run plain
# .interpolate() (no arguments) on `gapped` and store the result.
gapped = pd.Series([None, 10.0, None, 30.0])
try:
    gapped_interp_default = ...
except Exception:
    gapped_interp_default = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 4 — limit_direction="both" fills that same leading edge (by
# extending the nearest real neighbor flat, since there's no second point to
# draw a true line from). Run it on the same `gapped` Series with the right
# keyword argument.
try:
    gapped_interp_both = gapped.interpolate(limit_direction=...)
except Exception:
    gapped_interp_both = pd.Series(dtype=float)

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
    check("Exercise 1: ungrouped interpolate() WRONGLY draws a line into Binh's row",
          lambda: len(amount_interp_wrong) == 4
          and amount_interp_wrong.iloc[2] not in (None,)
          and not pd.isna(amount_interp_wrong.iloc[2])
          and amount_interp_wrong.iloc[2] != 180.0),
    check("Exercise 2: grouped interpolate() correctly leaves Binh's row as NaN",
          lambda: len(amount_interp_grouped) == 4 and pd.isna(amount_interp_grouped.iloc[2])),
    check("Exercise 2: grouped interpolate() leaves An's/Binh's real values untouched",
          lambda: amount_interp_grouped.iloc[0] == 120.0
          and amount_interp_grouped.iloc[1] == 42.0
          and amount_interp_grouped.iloc[3] == 180.0),
    check("Exercise 3: default interpolate() leaves the leading gap as NaN",
          lambda: len(gapped_interp_default) == 4
          and pd.isna(gapped_interp_default.iloc[0])
          and gapped_interp_default.iloc[2] == 20.0),
    check("Exercise 4: limit_direction='both' fills the leading gap too",
          lambda: len(gapped_interp_both) == 4
          and gapped_interp_both.iloc[0] == 10.0
          and not pd.isna(gapped_interp_both.iloc[0])),
]
print("\nAll green — lesson 63 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
