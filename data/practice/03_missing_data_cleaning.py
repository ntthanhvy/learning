# Practice 03 — Missing data & cleaning
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/03_missing_data_cleaning.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same file as Lesson 2, loaded and coerced the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount_clean = pd.to_numeric(df["amount"], errors="coerce")
order_date_clean = pd.to_datetime(df["order_date"], errors="coerce")

# ---------------------------------------------------------------------------
# Exercise 1 — fill the missing amount with the column's median (not 0 — see
# the lesson for why). pandas' .median() already ignores NaN on its own.
amount_filled = ...

# ---------------------------------------------------------------------------
# Exercise 2 — BEFORE the fill above conceptually happened, capture which rows
# were actually missing, so the fill in exercise 1 doesn't silently erase that
# information. One boolean Series, no loop: `amount_clean.isna()`.
amount_was_missing = ...

# ---------------------------------------------------------------------------
# Exercise 3 — order_date has no honest fill value for a "when did this
# happen" analysis, so drop those rows instead. Build a new frame with a
# "order_date_clean" column, then drop rows where it's missing.
df_with_date = df.assign(order_date_clean=order_date_clean)
df_dropped = ...

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
    check("Exercise 1: amount_filled has no NaN, missing row -> median 99.9",
          lambda: amount_filled.isna().sum() == 0 and round(amount_filled.iloc[2], 1) == 99.9),
    check("Exercise 2: amount_was_missing flags exactly the one fabricated row",
          lambda: amount_was_missing.sum() == 1 and bool(amount_was_missing.iloc[2])),
    check("Exercise 3: dropping missing order_date leaves 5 rows, order_id 4 gone",
          lambda: len(df_dropped) == 5 and 4 not in df_dropped["order_id"].tolist()),
]
print("\nAll green — lesson 3 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
