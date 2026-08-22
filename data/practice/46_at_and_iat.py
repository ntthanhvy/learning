# Practice 46 — .at[] and .iat[]: fast single-scalar access
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/46_at_and_iat.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as Lessons 6-45 (orders_raw.csv), loaded/coerced/cleaned the
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
# 0        1       An   120.0 2026-01-05
# 1        6       An    42.0 2026-01-10
# 2        2     Binh    35.5 2026-01-06
# 3        5     Binh   180.0 2026-01-09

# ---------------------------------------------------------------------------
# Exercise 1 — read ONE cell by LABEL with .at[]: row label 2, column "amount"
# (Binh's first order, 35.5). Use .at[], not .loc[].
try:
    binh_first_amount = clean.at[2, ...]
except Exception:
    binh_first_amount = None

# ---------------------------------------------------------------------------
# Exercise 2 — read the SAME cell by POSITION with .iat[]: row position 2,
# column position 2 ("amount" is the 3rd column, index 2). Use .iat[], not
# .iloc[]. Should equal Exercise 1's value.
try:
    binh_first_amount_iat = clean.iat[2, ...]
except Exception:
    binh_first_amount_iat = None

# ---------------------------------------------------------------------------
# Exercise 3 — set ONE cell with .at[]: on a COPY of clean (`touched`, already
# made for you below), set row label 0's "amount" to 500.0 using .at[]. The
# original `clean` must stay completely untouched.
touched = clean.copy()
try:
    touched.at[0, ...] = 500.0
except Exception:
    pass

# ---------------------------------------------------------------------------
# Exercise 4 — realistic combo: find the row LABEL holding each customer's
# max amount with groupby().idxmax() (Lesson 20), then pull just An's max
# amount with a single .at[] lookup using that label.
top_idx = clean.groupby("customer")["amount"].idxmax()
try:
    an_top_amount = clean.at[top_idx[...], "amount"]
except Exception:
    an_top_amount = None

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
    check("Exercise 1: .at[] reads Binh's first amount (35.5) by label",
          lambda: binh_first_amount == 35.5),
    check("Exercise 2: .iat[] reads the identical cell by position",
          lambda: binh_first_amount_iat == 35.5
          and binh_first_amount_iat == binh_first_amount),
    check("Exercise 3: .at[] set touched[0, 'amount'] to 500.0",
          lambda: touched.at[0, "amount"] == 500.0),
    check("Exercise 3: the original clean is completely untouched",
          lambda: clean.at[0, "amount"] == 120.0),
    check("Exercise 4: An's top amount via idxmax() + .at[] is 120.0",
          lambda: an_top_amount == 120.0),
]
print("\nAll green — lesson 46 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
