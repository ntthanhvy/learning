# Practice 72 — .ewm(): the moving average that never forgets, just discounts
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/72_ewm.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as recent lessons, cleaned the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount_col = pd.to_numeric(df["amount"], errors="coerce")
order_date_col = pd.to_datetime(df["order_date"], errors="coerce")
clean = (
    df.assign(amount=amount_col, order_date=order_date_col)
    .dropna(subset=["amount", "order_date"])
    .sort_values(["customer", "order_date"])
    .reset_index(drop=True)
)
an = clean[clean["customer"] == "An"].reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — span=2, adjust=False on An's two amounts (120.0, 42.0). Row 1
# comes out 68.0 -- NOT the plain average 81.0 that rolling(2).mean() would
# give, since 42.0 (the more recent value) counts more than 120.0 here.
# Fill in the literal integer 2 for span=, and the literal boolean False for
# adjust= (not just any falsy placeholder -- a bare "..." left unfilled is
# ALSO falsy to pandas' own truthiness in some spots, so this checks the
# literal value itself, to avoid a freebie pass).
ex1_span_value = ...
ex1_adjust_value = ...
try:
    ex1_ewm = an["amount"].ewm(span=ex1_span_value, adjust=ex1_adjust_value).mean()
except Exception:
    ex1_ewm = None

# ---------------------------------------------------------------------------
# Exercise 2 — the SAME span=2, but adjust=True (the default) instead. Row 1
# comes out 61.5 -- a DIFFERENT number from Exercise 1's 68.0, proving
# adjust= is not cosmetic. Fill in the literal boolean True.
ex2_adjust_value = ...
try:
    ex2_ewm = an["amount"].ewm(span=2, adjust=ex2_adjust_value).mean()
except Exception:
    ex2_ewm = None

# ---------------------------------------------------------------------------
# Exercise 3 — passing both span= and alpha= together raises ValueError;
# pandas will not guess which decay parameterization you meant. Fill in the
# literal float 0.5 for alpha= (not just any placeholder -- this checks the
# value actually assigned, not merely that *some* exception fires).
ex3_alpha_value = ...
try:
    an["amount"].ewm(span=2, alpha=ex3_alpha_value)
    ex3_raised = False
except ValueError:
    ex3_raised = True
except Exception:
    ex3_raised = False

# ---------------------------------------------------------------------------
# Exercise 4 — .ewm() chained after groupby("customer") keeps each
# customer's smoothing independent: Binh's smoothed series must NOT be
# affected by An's rows. Fill in the literal string "customer" for the
# groupby key.
ex4_group_key = ...
try:
    ex4_grouped = clean.groupby(ex4_group_key)["amount"].apply(
        lambda s: s.ewm(span=2, adjust=False).mean()
    )
except Exception:
    ex4_grouped = None

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
    check("Exercise 1: span=2, adjust=False gives row 1 = 68.0, not the plain average 81.0",
          lambda: ex1_span_value == 2 and ex1_adjust_value is False and ex1_ewm is not None
          and len(ex1_ewm) == 2
          and round(ex1_ewm.iloc[0], 1) == 120.0
          and round(ex1_ewm.iloc[1], 1) == 68.0),
    check("Exercise 2: same span=2, adjust=True gives a DIFFERENT row 1 = 61.5",
          lambda: ex2_adjust_value is True and ex2_ewm is not None
          and len(ex2_ewm) == 2
          and round(ex2_ewm.iloc[1], 1) == 61.5
          and ex1_ewm is not None
          and round(ex2_ewm.iloc[1], 1) != round(ex1_ewm.iloc[1], 1)),
    check("Exercise 3: span= and alpha= together raises ValueError",
          lambda: ex3_alpha_value == 0.5 and ex3_raised is True),
    check("Exercise 4: groupby('customer') keeps Binh's smoothing independent of An's",
          lambda: ex4_group_key == "customer" and ex4_grouped is not None
          and round(ex4_grouped.loc[("Binh", 2)], 1) == 35.5
          and round(ex4_grouped.loc[("Binh", 3)], 3) == 131.833),
]

print("\nAll green — lesson 72 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
