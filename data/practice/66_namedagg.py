# Practice 66 — pd.NamedAgg: naming multi-column aggregations without the MultiIndex dance
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/66_namedagg.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as recent lessons, cleaned the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(df["amount"], errors="coerce")
order_date = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount, order_date=order_date)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)

# ---------------------------------------------------------------------------
# Exercise 1 — pd.NamedAgg across three DIFFERENT source columns in one call:
# total = sum of amount, orders = count of order_id, first_order = min of
# order_date. Remember the real keyword is aggfunc=, not func=.
# NOTE: whole-right-hand-side placeholder; an unfilled `named = ...` leaves
# bare Ellipsis, and `Ellipsis.columns` raises AttributeError on its own --
# confirmed directly with a standalone probe before shipping.
try:
    named = clean.groupby("customer").agg(
        total=pd.NamedAgg(column="amount", aggfunc="sum"),
        orders=pd.NamedAgg(column="order_id", aggfunc="count"),
        first_order=pd.NamedAgg(column="order_date", aggfunc=...),
    )
except Exception:
    named = None

# ---------------------------------------------------------------------------
# Exercise 2 — the plain-tuple shorthand: ("amount", "sum") / ("order_id",
# "count") should produce a result IDENTICAL to Exercise 1's total/orders
# columns (ignore first_order here; just the first two).
try:
    tupled = clean.groupby("customer").agg(
        total=("amount", "sum"),
        orders=...,
    )
except Exception:
    tupled = None

# ---------------------------------------------------------------------------
# Exercise 3 — a custom lambda as aggfunc=, computing the same per-customer
# range (max minus min of amount) Lesson 61 needed groupby().apply() for.
# Finish the lambda: s.max() - s.min().
try:
    ranged = clean.groupby("customer").agg(
        spread=pd.NamedAgg(column="amount", aggfunc=...),
    )
except Exception:
    ranged = None

# ---------------------------------------------------------------------------
# Exercise 4 — the whole-groupby-only gotcha. The call below is already
# complete and correct on its own -- an ALREADY column-selected groupby,
# clean.groupby("customer")["amount"], given a pd.NamedAgg the same way
# Exercise 1 used it. Predict what happens, then fill in `ex4_prediction`
# with either "raises" or "works" to match what you observe when you run
# this file with the `try` fully intact (don't touch the try/except below).
# NOTE: whole-value placeholder; an unfilled `ex4_prediction = ...` compares
# unequal to both "raises" and "works" below -- confirmed directly with a
# standalone probe before shipping, so a blank guess cannot pass by luck.
ex4_prediction = ...

ex4_raised = False
try:
    clean.groupby("customer")["amount"].agg(
        total=pd.NamedAgg(column="amount", aggfunc="sum")
    )
except TypeError:
    ex4_raised = True
except Exception:
    ex4_raised = False

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
    check("Exercise 1: named columns flat (no MultiIndex), An total=162.0 orders=2",
          lambda: named is not None
          and list(named.columns) == ["total", "orders", "first_order"]
          and not isinstance(named.columns, pd.MultiIndex)
          and round(named.loc["An", "total"], 1) == 162.0
          and named.loc["An", "orders"] == 2),
    check("Exercise 1b: first_order is the earliest date per customer",
          lambda: named is not None
          and str(named.loc["An", "first_order"].date()) == "2026-01-05"
          and str(named.loc["Binh", "first_order"].date()) == "2026-01-06"),
    check("Exercise 2: tuple shorthand identical to Exercise 1's NamedAgg result",
          lambda: tupled is not None
          and tupled.equals(named[["total", "orders"]])),
    check("Exercise 3: custom lambda aggfunc gives An spread=78.0, Binh spread=144.5",
          lambda: ranged is not None
          and round(ranged.loc["An", "spread"], 1) == 78.0
          and round(ranged.loc["Binh", "spread"], 1) == 144.5),
    check("Exercise 4: NamedAgg on an already column-selected groupby raises TypeError",
          lambda: ex4_raised is True
          and ex4_prediction == "raises"),
]

print("\nAll green — lesson 66 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
