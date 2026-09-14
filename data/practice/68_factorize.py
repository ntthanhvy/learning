# Practice 68 — factorize(): the integer codes hiding under category dtype
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/68_factorize.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
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

# ---------------------------------------------------------------------------
# Exercise 1 — pd.factorize() on the "customer" column. Confirm the
# appearance-order codes/uniques pair: An appears first (code 0), then Binh
# (code 1).
try:
    ex1_codes, ex1_uniques = pd.factorize(...)
except Exception:
    ex1_codes, ex1_uniques = None, None

# ---------------------------------------------------------------------------
# Exercise 2 — reconstruction: uniques[codes] should exactly recover the
# original column when there is no missing data.
try:
    ex2_reconstructed = ex1_uniques[...]
except Exception:
    ex2_reconstructed = None

# ---------------------------------------------------------------------------
# Exercise 3 — sort=True makes factorize() match category dtype's codes and
# categories exactly. Use a Series where appearance order and alphabetical
# order genuinely differ (Chi appears first, but sorts last). Fill in the
# boolean literal True (not just any truthy value -- a bare "..." left
# unfilled is ALSO truthy to Python, so this checks the literal value
# itself, not merely the resulting behavior, to avoid a freebie pass).
s_unsorted = pd.Series(["Chi", "An", "Chi", "Binh", "An"])
ex3_sort_value = ...
try:
    ex3_codes, ex3_uniques = pd.factorize(s_unsorted, sort=ex3_sort_value)
except Exception:
    ex3_codes, ex3_uniques = None, None
ex3_cat = s_unsorted.astype("category")

# ---------------------------------------------------------------------------
# Exercise 4 — the -1 sentinel gotcha. A Series with a missing value: An,
# None, Binh, An, NaN. Confirm the missing rows get code -1, and that naive
# uniques[codes] reconstruction silently returns the WRONG value (not a
# crash) for those rows, because -1 indexes the LAST uniques entry.
s_with_nan = pd.Series(["An", None, "Binh", "An", np.nan])
try:
    ex4_codes, ex4_uniques = pd.factorize(...)
except Exception:
    ex4_codes, ex4_uniques = None, None
try:
    ex4_reconstructed = ex4_uniques[ex4_codes]
except Exception:
    ex4_reconstructed = None

# ---------------------------------------------------------------------------
# Exercise 5 — use_na_sentinel=False gives the missing value its own real
# code and slot in uniques, instead of -1. Confirm uniques now has 3 entries
# (An, Binh, and NaN itself), not 2.
try:
    ex5_codes, ex5_uniques = pd.factorize(s_with_nan, use_na_sentinel=...)
except Exception:
    ex5_codes, ex5_uniques = None, None

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
    check("Exercise 1: factorize() gives appearance-order codes/uniques",
          lambda: ex1_codes is not None and ex1_codes.tolist() == [0, 0, 1, 1]
          and ex1_uniques.tolist() == ["An", "Binh"]),
    check("Exercise 2: uniques[codes] exactly reconstructs the column",
          lambda: ex2_reconstructed is not None
          and ex2_reconstructed.tolist() == clean["customer"].tolist()),
    check("Exercise 3: sort=True matches category dtype's codes/categories",
          lambda: ex3_sort_value is True and ex3_codes is not None
          and ex3_codes.tolist() == ex3_cat.cat.codes.tolist()
          and ex3_uniques.tolist() == ex3_cat.cat.categories.tolist()),
    check("Exercise 4: -1 sentinel present, naive reconstruction is silently wrong",
          lambda: ex4_codes is not None and ex4_codes.tolist() == [0, -1, 1, 0, -1]
          and ex4_reconstructed is not None
          and ex4_reconstructed.tolist() != ["An", None, "Binh", "An", None]),
    check("Exercise 5: use_na_sentinel=False gives NaN its own real code",
          lambda: ex5_uniques is not None and len(ex5_uniques) == 3
          and (-1 not in ex5_codes.tolist())),
]

print("\nAll green — lesson 68 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
