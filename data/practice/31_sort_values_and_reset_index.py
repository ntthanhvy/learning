# Practice 31 — sort_values() and reset_index() edge cases
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/31_sort_values_and_reset_index.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-30:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)
# clean's index is now a plain 0..3, matching row order -- re-scramble it on purpose
# below so this practice file can reproduce Section 2's .loc/.iloc mismatch.

# ---------------------------------------------------------------------------
# Exercise 1 — sort `clean` by "amount" (ascending) WITHOUT resetting the
# index, then read both the true first row (position) and whatever row is
# still labeled 0 (label) — reproduce Section 2's mismatch.
try:
    sorted_by_amount = clean.sort_values(...)
    first_by_position = float(sorted_by_amount.iloc[0]["amount"])
    row_still_labeled_0 = float(sorted_by_amount.loc[0]["amount"])
except Exception:
    sorted_by_amount = pd.DataFrame()
    first_by_position = None
    row_still_labeled_0 = None

# ---------------------------------------------------------------------------
# Exercise 2 — same sort as Exercise 1, but this time reset the index in the
# SAME call via ignore_index=True, so .loc[0] and .iloc[0] agree.
try:
    sorted_reset = clean.sort_values(..., ignore_index=True)
except Exception:
    sorted_reset = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 3 — groupby("customer")["amount"].sum(), then turn the grouped
# Series back into a DataFrame with reset_index(), renaming the value column
# to "total_amount" in the same call (Section 8's name= keyword).
try:
    grouped = clean.groupby("customer")["amount"].sum()
    grouped_df = grouped.reset_index(name=...)
except Exception:
    grouped_df = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 4 — sort the RAW (uncleaned) amounts, coerced to numeric, with
# na_position="first" so the unparseable "unknown" row's NaN sorts to the
# front instead of pandas' default (last).
try:
    raw_num = raw.copy()
    raw_num["amount_num"] = pd.to_numeric(raw_num["amount"], errors="coerce")
    sorted_na_first = raw_num.sort_values("amount_num", na_position=...)
except Exception:
    sorted_na_first = pd.DataFrame()

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
    check("Exercise 1: sorted_by_amount's true first row (iloc[0]) is 35.5",
          lambda: first_by_position is not None and abs(first_by_position - 35.5) < 1e-9),
    check("Exercise 1: the row still labeled 0 (loc[0]) is a DIFFERENT value, 120.0",
          lambda: row_still_labeled_0 is not None and abs(row_still_labeled_0 - 120.0) < 1e-9),
    check("Exercise 2: sorted_reset's index is a plain 0..3, matching row order",
          lambda: len(sorted_reset) == 4
          and list(sorted_reset.index) == [0, 1, 2, 3]
          and abs(float(sorted_reset.iloc[0]["amount"]) - 35.5) < 1e-9),
    check("Exercise 3: grouped_df is a DataFrame with a 'total_amount' column",
          lambda: isinstance(grouped_df, pd.DataFrame)
          and "total_amount" in grouped_df.columns
          and "customer" in grouped_df.columns),
    check("Exercise 3: An's total_amount is 162.0, Binh's is 215.5",
          lambda: dict(zip(grouped_df["customer"], grouped_df["total_amount"]))
          == {"An": 162.0, "Binh": 215.5}),
    check("Exercise 4: the unparseable row's NaN now sorts FIRST",
          lambda: len(sorted_na_first) == 6 and pd.isna(sorted_na_first["amount_num"].iloc[0])),
]
print("\nAll green — lesson 31 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
