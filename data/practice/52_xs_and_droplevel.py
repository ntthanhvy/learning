# Practice 52 — .xs() and droplevel(): slicing and simplifying a MultiIndex
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/52_xs_and_droplevel.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture clean 4-row slice as Lessons 6-51.
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

# Lesson 15's grouped Series -- a two-level row MultiIndex (customer, order_date).
by_customer_date = clean.groupby(["customer", "order_date"])["amount"].sum()

# ---------------------------------------------------------------------------
# Exercise 1 — .xs() on the outer level (An's 2 rows, order_date left as the
# only remaining index level) and on the INNER level via level="order_date"
# (every customer's value for 2026-01-05 -- only An ordered that day, so only
# An's row survives) (Sections 1-2).
# NOTE: the placeholder sits on the WHOLE right-hand side of each assignment,
# not inside .xs()'s own arguments -- an unfilled `an_slice = ...` leaves
# `an_slice` as bare Ellipsis, and `Ellipsis.sum()` raises AttributeError on
# its own (no extra guarding needed), confirmed directly before shipping.
try:
    an_slice = ...
    an_slice_sum = an_slice.sum()
    an_slice_len = len(an_slice)
except Exception:
    an_slice_sum = None
    an_slice_len = None

try:
    jan5_slice = ...
    jan5_an = float(jan5_slice.loc["An"])
    jan5_len = len(jan5_slice)
except Exception:
    jan5_an = None
    jan5_len = None

# ---------------------------------------------------------------------------
# Exercise 2 — the two-aggfunc pivot_table (Lesson 39's fixture) has a
# MultiIndex on the COLUMNS. .xs("sum", axis=1, level=0) pulls just the "sum"
# half back out to a plain single-level-column table (Section 2).
# NOTE: placeholder on the whole right-hand side, same reasoning as Exercise 1
# -- `sum_only = ...` stays bare Ellipsis, and `Ellipsis.loc[...]` raises
# AttributeError on its own, confirmed directly before shipping.
pv = clean.pivot_table(
    index="customer", columns="order_date", values="amount",
    aggfunc=["sum", "count"], fill_value=0,
)
try:
    sum_only = ...
    an_sum_total = float(sum_only.loc["An"].sum())
    sum_only_ncols = sum_only.shape[1]
except Exception:
    an_sum_total = None
    sum_only_ncols = None

# ---------------------------------------------------------------------------
# Exercise 3 — drop_level=False keeps the matched level instead of removing
# it: an_slice_kept should still have "customer" as one of its index names,
# unlike Exercise 1's an_slice, which drops it (Section 3).
# NOTE: same whole-right-hand-side placeholder style; `Ellipsis.index` raises
# AttributeError on its own, confirmed directly before shipping.
try:
    an_slice_kept = ...
    kept_names = list(an_slice_kept.index.names)
except Exception:
    kept_names = None

# ---------------------------------------------------------------------------
# Exercise 4 — droplevel() on the stacked pivot: stack(level=0) first builds
# a genuine two-level row MultiIndex (customer outer, aggfunc inner), then
# droplevel(0) removes the OUTER level (leaving just "sum"/"count" repeated,
# 4 rows, no customer info) and droplevel(1) removes the INNER level (leaving
# "An"/"Binh" each repeated twice, 4 rows, no aggfunc info) -- neither call
# filters any row out, unlike every .xs() call above (Sections 4-5). The
# gotcha: after droplevel(1), the resulting index has duplicate "An"/"Binh"
# labels -- check .index.is_unique to confirm it's False.
# NOTE: same whole-right-hand-side placeholder style throughout.
stacked = pv.stack(level=0)
try:
    dropped_outer = ...
    dropped_outer_len = len(dropped_outer)
except Exception:
    dropped_outer_len = None

try:
    dropped_inner = ...
    dropped_inner_len = len(dropped_inner)
    dropped_inner_unique = dropped_inner.index.is_unique
except Exception:
    dropped_inner_len = None
    dropped_inner_unique = None

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
    check("Exercise 1: xs('An') keeps both of An's rows (sum=162.0)",
          lambda: an_slice_len == 2 and abs(an_slice_sum - 162.0) < 1e-9),
    check("Exercise 1: xs(..., level='order_date') on 2026-01-05 gives only An (120.0)",
          lambda: jan5_len == 1 and abs(jan5_an - 120.0) < 1e-9),
    check("Exercise 2: xs('sum', axis=1, level=0) narrows to 4 date columns, An sums to 162.0",
          lambda: sum_only_ncols == 4 and abs(an_sum_total - 162.0) < 1e-9),
    check("Exercise 3: drop_level=False keeps 'customer' in the index names",
          lambda: kept_names == ["customer", "order_date"]),
    check("Exercise 4: droplevel(0) leaves all 4 rows, no filtering",
          lambda: dropped_outer_len == 4),
    check("Exercise 4: droplevel(1) leaves all 4 rows but a NON-unique index",
          lambda: dropped_inner_len == 4 and dropped_inner_unique is False),
]
print("\nAll green — lesson 52 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
