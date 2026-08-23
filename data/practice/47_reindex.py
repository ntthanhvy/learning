# Practice 47 — reindex(): forcing a Series/DataFrame onto a chosen label set
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/47_reindex.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lessons 6-46 (orders_raw.csv), loaded/coerced/cleaned the
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
# Exercise 1 — Lesson 32's own dangling gotcha, finally fixed: revenue by
# weekday, reindexed onto the full Monday-through-Sunday order (currently
# only 4 of 7 weekdays have any revenue at all).
by_day = clean.groupby(clean["order_date"].dt.day_name())["amount"].sum()
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
try:
    by_day_full_week = by_day.reindex(weekday_order, fill_value=...)
except Exception:
    by_day_full_week = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 2 — reindex a per-customer revenue total onto every KNOWN customer
# name (including "Danh", who placed no order in this fixture at all), with
# NO fill_value this time -- a customer with no matching row should come back
# as a genuine NaN, not zero (zero would wrongly claim "known to have spent
# nothing" instead of "no data").
totals_by_cust = clean.groupby("customer")["amount"].sum()
all_customers = ["An", "Binh", "Danh"]
try:
    totals_all_customers = totals_by_cust.reindex(...)
except Exception:
    totals_all_customers = pd.Series(dtype=float)

# ---------------------------------------------------------------------------
# Exercise 3 — the gotcha: reindex() requires UNIQUE labels on that axis, or
# it raises ValueError rather than guessing. `clean` set_index'd on "customer"
# directly has two "An" rows and two "Binh" rows -- a real duplicate-label
# axis. Confirm reindex() raises on it (catch the exception and record its
# type), the reason Exercise 2 had to group-and-sum FIRST to get a
# unique-per-customer index before reindexing.
by_cust_raw = clean.set_index("customer")
try:
    by_cust_raw.reindex(all_customers)
    raw_reindex_error_type = None
except Exception as e:
    raw_reindex_error_type = type(e)

# ---------------------------------------------------------------------------
# Exercise 4 — reindex a column LIST onto a DataFrame: add a "region" column
# that doesn't exist in `clean` at all. reindex(columns=[...]) doesn't raise
# for a genuinely missing column -- it silently adds it, all-NaN, same
# "no crash, quietly wrong" family as Lesson 43's zero-match rows.
try:
    with_region_col = clean.reindex(columns=["order_id", "customer", "amount", "region"])
except Exception:
    with_region_col = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 5 — contrast with .loc[]: asking .loc[] for a label that isn't
# there raises KeyError immediately, where reindex() on that same list would
# have quietly returned NaN for it instead. Confirm .loc[] raises here.
try:
    by_day.loc[weekday_order]
    loc_error_type = None
except Exception as e:
    loc_error_type = type(e)

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
    check("Exercise 1: all 7 weekdays present, in Mon-Sun order",
          lambda: by_day_full_week.index.tolist() == weekday_order),
    check("Exercise 1: real revenue days keep their true totals",
          lambda: by_day_full_week["Monday"] == 120.0
          and by_day_full_week["Friday"] == 180.0),
    check("Exercise 1: no-revenue days are filled with 0.0, not NaN",
          lambda: by_day_full_week["Wednesday"] == 0.0
          and by_day_full_week["Sunday"] == 0.0),
    check("Exercise 2: An's and Binh's real totals survive reindexing",
          lambda: totals_all_customers["An"] == 162.0
          and totals_all_customers["Binh"] == 215.5),
    check("Exercise 2: Danh (no orders at all) is NaN, not 0.0",
          lambda: pd.isna(totals_all_customers["Danh"])),
    check("Exercise 3: reindexing a duplicate-label axis raises ValueError",
          lambda: raw_reindex_error_type is ValueError),
    check("Exercise 4: the new 'region' column exists and is entirely NaN",
          lambda: "region" in with_region_col.columns
          and with_region_col["region"].isna().all()),
    check("Exercise 4: the real columns are untouched",
          lambda: with_region_col.loc[0, "amount"] == 120.0),
    check("Exercise 5: .loc[] on the same missing labels raises KeyError",
          lambda: loc_error_type is KeyError),
]
print("\nAll green — lesson 47 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
