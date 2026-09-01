# Practice 55 — add_prefix() and add_suffix(): renaming a whole axis at once
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/55_add_prefix_and_add_suffix.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture clean 4-row slice as Lessons 6-54.
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
# Exercise 1 — add_prefix(): stamp "raw_" onto every column of `clean` (Section
# 1). Check the resulting column list directly. NOTE: `clean.add_prefix(...)`
# does NOT raise on its own -- Ellipsis is a valid (if useless) argument to
# add_prefix(), since it gets str()-coerced into the prefix rather than
# type-checked, confirmed directly with a standalone probe before shipping
# (`clean.add_prefix(...)` runs fine and just produces oddly-named columns
# like "Ellipsisorder_id"). The check below compares the FULL expected column
# list, so an unfilled placeholder produces the wrong list and still ✗
# correctly -- it just doesn't crash getting there.
try:
    prefixed = clean.add_prefix(...)
    prefixed_cols = prefixed.columns.tolist()
except Exception:
    prefixed_cols = None

# ---------------------------------------------------------------------------
# Exercise 2 — the real payoff: groupby().agg() with multiple functions on one
# column produces plain-named columns ("sum", "mean", "count"); add_prefix()
# disambiguates them with the source column's name (Section 2). NOTE: whole-
# right-hand-side placeholder; an unfilled `by_customer = ...` leaves bare
# Ellipsis, and `Ellipsis.add_prefix` raises AttributeError on its own,
# confirmed directly before shipping.
try:
    by_customer = ...
    named = by_customer.add_prefix("amount_")
    named_cols = named.columns.tolist()
    an_sum = named.loc["An", "amount_sum"]
except Exception:
    named_cols = None
    an_sum = None

# ---------------------------------------------------------------------------
# Exercise 3 — the MultiIndex-every-level gotcha: aggregating two source
# columns with different functions produces genuine MultiIndex columns;
# add_prefix() stamps the prefix onto EVERY level, not just the outer one
# (Section 3). Flattening to plain strings first, then prefixing, is the
# working fix. NOTE: whole-right-hand-side placeholder; an unfilled
# `multi = ...` leaves bare Ellipsis, and `Ellipsis.columns` raises
# AttributeError on its own, confirmed directly before shipping.
try:
    multi = ...
    multi_prefixed_cols = multi.add_prefix("x_").columns.tolist()
    flat_cols = ["_".join(col).strip("_") for col in multi.columns]
    multi.columns = flat_cols
    flat_prefixed_cols = multi.add_prefix("agg_").columns.tolist()
except Exception:
    multi_prefixed_cols = None
    flat_prefixed_cols = None

# ---------------------------------------------------------------------------
# Exercise 4 — axis=0 (or axis="index") retargets add_prefix()/add_suffix()
# onto the row index instead of the columns (Section 4). NOTE: whole-right-
# hand-side placeholder; an unfilled `row_prefixed = ...` leaves bare
# Ellipsis, and `Ellipsis.index` raises AttributeError on its own, confirmed
# directly before shipping.
try:
    row_prefixed = ...
    row_index = row_prefixed.index.tolist()
except Exception:
    row_index = None

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
    check("Exercise 1: add_prefix('raw_') renames every column of clean",
          lambda: prefixed_cols == ["raw_order_id", "raw_customer", "raw_amount", "raw_order_date"]),
    check("Exercise 2: groupby().agg([...]) + add_prefix('amount_') names every column",
          lambda: named_cols == ["amount_sum", "amount_mean", "amount_count"]
          and abs(an_sum - 162.0) < 1e-9),
    check("Exercise 3: add_prefix() on MultiIndex columns prefixes every level",
          lambda: multi_prefixed_cols == [("x_amount", "x_sum"), ("x_amount", "x_mean"), ("x_order_id", "x_count")]),
    check("Exercise 3: flatten-then-prefix gives clean flat names",
          lambda: flat_prefixed_cols == ["agg_amount_sum", "agg_amount_mean", "agg_order_id_count"]),
    check("Exercise 4: add_prefix('row_', axis=0) renames the row index, not columns",
          lambda: row_index == ["row_0", "row_1", "row_2", "row_3"]),
]
print("\nAll green — lesson 55 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
