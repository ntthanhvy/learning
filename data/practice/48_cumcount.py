# Practice 48 — cumcount(): a running position within each group
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/48_cumcount.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lessons 6-47 (orders_raw.csv), loaded/coerced/cleaned the
# same way, sorted by customer then order_date.
df = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(df["amount"], errors="coerce")
order_date = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
#   order_id customer  amount order_date
# 0        1       An   120.0 2026-01-05  (Monday)
# 1        6       An    42.0 2026-01-10  (Saturday)
# 2        2     Binh    35.5 2026-01-06  (Tuesday)
# 3        5     Binh   180.0 2026-01-09  (Friday)

# ---------------------------------------------------------------------------
# Exercise 1 — Lesson 28's own dangling gotcha, finally explained: number each
# customer's visits in row order, 1-indexed (cumcount() itself is 0-indexed).
try:
    clean["visit_num"] = clean.groupby("customer").cumcount() + ...
except Exception:
    clean["visit_num"] = pd.Series(dtype="Int64")

# ---------------------------------------------------------------------------
# Exercise 2 — contrast with rank() (Lesson 7): cumcount() numbers by ROW
# POSITION, rank() numbers by VALUE. On this fixture An's chronologically
# FIRST order (visit_num 1) is actually the LARGER amount (120.0 > 42.0), so
# rank(method="first") on amount ascending gives it rank 2, not 1 -- the two
# numberings genuinely disagree here. Compute amount_rank the same way
# Lesson 7 did.
try:
    clean["amount_rank"] = clean.groupby("customer")["amount"].rank(method=...)
except Exception:
    clean["amount_rank"] = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — contrast with nunique() (Lesson 19): a small inline table (same
# pattern as Lesson 19's tagged-orders example) where one customer has a
# REPEATED amount. cumcount() must still reach 3 (three real rows); nunique()
# must report only 2 (the repeated 50.0 only counts once).
demo = pd.DataFrame({
    "customer": ["An", "An", "An", "Binh"],
    "amount": [50.0, 50.0, 75.0, 30.0],
})
try:
    demo["visit_num"] = demo.groupby("customer").cumcount() + 1
    demo_nunique = demo.groupby("customer")["amount"].nunique()
except Exception:
    demo["visit_num"] = pd.Series(dtype="Int64")
    demo_nunique = pd.Series(dtype="Int64")

# ---------------------------------------------------------------------------
# Exercise 4 — ascending=False: flag each group's LAST row (by current row
# order) with a boolean column. cumcount(ascending=False) counts DOWN to 0 on
# the last row of every group, so "is the last row" is "count remaining < 1"
# (fill in the threshold -- an int).
try:
    clean["is_last_visit"] = clean.groupby("customer").cumcount(ascending=False) < ...
except Exception:
    clean["is_last_visit"] = [False] * len(clean)

# ---------------------------------------------------------------------------
# Exercise 5 — cumcount() only exists on a GroupBy object. Confirm calling it
# on a plain (ungrouped) Series raises AttributeError.
try:
    clean["amount"].cumcount()
    plain_series_error_type = None
except Exception as e:
    plain_series_error_type = type(e)

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
    check("Exercise 1: visit_num is 1-indexed (starts at 1, not 0)",
          lambda: clean.loc[0, "visit_num"] == 1 and clean.loc[1, "visit_num"] == 2),
    check("Exercise 1: both customers restart their count at 1",
          lambda: clean.loc[2, "visit_num"] == 1 and clean.loc[3, "visit_num"] == 2),
    check("Exercise 2: amount_rank disagrees with visit_num on An's rows",
          lambda: clean.loc[0, "amount_rank"] == 2.0 and clean.loc[1, "amount_rank"] == 1.0),
    check("Exercise 2: rank still restarts per customer (Binh's 35.5 is rank 1)",
          lambda: clean.loc[2, "amount_rank"] == 1.0 and clean.loc[3, "amount_rank"] == 2.0),
    check("Exercise 3: cumcount() reaches 3 for An's three real rows",
          lambda: demo.loc[2, "visit_num"] == 3),
    check("Exercise 3: nunique() reports only 2 distinct amounts for An",
          lambda: demo_nunique["An"] == 2 and demo_nunique["Binh"] == 1),
    check("Exercise 4: the last row of each customer's group is flagged True",
          lambda: bool(clean.loc[1, "is_last_visit"]) and bool(clean.loc[3, "is_last_visit"])),
    check("Exercise 4: non-last rows are flagged False",
          lambda: not bool(clean.loc[0, "is_last_visit"]) and not bool(clean.loc[2, "is_last_visit"])),
    check("Exercise 5: cumcount() on a plain ungrouped Series raises AttributeError",
          lambda: plain_series_error_type is AttributeError),
]
print("\nAll green — lesson 48 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
