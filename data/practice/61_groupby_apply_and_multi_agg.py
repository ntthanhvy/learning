# Practice 61 — groupby().apply() and multi-function .agg()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/61_groupby_apply_and_multi_agg.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same file as Lessons 2-4, coerced the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount_clean = pd.to_numeric(df["amount"], errors="coerce")
df2 = df.assign(amount_clean=amount_clean)

# ---------------------------------------------------------------------------
# Exercise 1 — per customer: sum AND mean of amount_clean, plus a count of
# order_id, all in one .agg() call. Use a dict: {"amount_clean": ["sum", "mean"],
# "order_id": "count"}. Then flatten the resulting MultiIndex columns by joining
# each pair with "_" (e.g. "amount_clean_sum"), same fix used in Lesson 61.
# NOTE: whole-right-hand-side placeholder; an unfilled `multi_agg = ...`
# leaves bare Ellipsis, and `Ellipsis.columns` raises AttributeError on its
# own -- confirmed directly with a standalone probe before shipping, so the
# flatten step below is wrapped too rather than crashing the whole file.
try:
    multi_agg = ...
    multi_agg.columns = ["_".join(c) for c in multi_agg.columns]
except Exception:
    multi_agg = None

# ---------------------------------------------------------------------------
# Exercise 2 — per customer, the range of amount_clean (max minus min), using
# groupby().apply() since .agg() can't read the same column twice in one
# named function. Finish the function body: return
# g["amount_clean"].max() - g["amount_clean"].min(). Then call
# df2.groupby("customer").apply(_range_fn, include_groups=False) below.
# NOTE: whole-right-hand-side placeholder on both lines; an unfilled
# `return ...` gives a bare Ellipsis result, and an unfilled
# `revenue_range = ...` leaves bare Ellipsis, whose `.groupby`/indexing
# raises AttributeError/TypeError on its own -- confirmed directly with a
# standalone probe before shipping, so neither slips through as a freebie.
def _range_fn(g):
    return ...

try:
    revenue_range = ...
except Exception:
    revenue_range = None

# ---------------------------------------------------------------------------
# Exercise 3 — per customer, return BOTH the range (as above) and the order
# count in one groupby().apply() call, by having the function return a
# pd.Series with two named entries: "range" and "n_orders" (use len(g) for
# the count). Finish the function body, then call groupby().apply() with
# include_groups=False, same shape as Exercise 2. NOTE: whole-right-hand-side
# placeholder on both lines, same freebie-proofing as Exercise 2 -- confirmed
# directly, no accidental freebie risk.
def _range_and_count_fn(g):
    return ...

try:
    range_and_count = ...
except Exception:
    range_and_count = None

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
    check("Exercise 1: multi_agg flattened columns, An sum=162.0 mean=81.0 count=3",
          lambda: list(multi_agg.columns) == ["amount_clean_sum", "amount_clean_mean", "order_id_count"]
          and round(multi_agg.loc["An", "amount_clean_sum"], 1) == 162.0
          and round(multi_agg.loc["An", "amount_clean_mean"], 1) == 81.0
          and multi_agg.loc["An", "order_id_count"] == 3),
    check("Exercise 2: revenue_range — An 78.0, Binh 144.5, Chi 0.0",
          lambda: round(revenue_range["An"], 1) == 78.0
          and round(revenue_range["Binh"], 1) == 144.5
          and round(revenue_range["Chi"], 1) == 0.0),
    check("Exercise 3: range_and_count has both columns, Binh range=144.5 n_orders=2",
          lambda: list(range_and_count.columns) == ["range", "n_orders"]
          and round(range_and_count.loc["Binh", "range"], 1) == 144.5
          and range_and_count.loc["Binh", "n_orders"] == 2),
]
print("\nAll green — lesson 61 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
