# Practice 78 — .assign(): adding columns without ever risking SettingWithCopy
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/78_assign.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.DataFrame({
    "customer": ["An", "Binh", "Chi"],
    "amount": [120.0, 215.5, 99.9],
    "qty": [3, 2, 1],
})

# ---------------------------------------------------------------------------
# Exercise 1 — basic single-column assign: add "unit_price" = amount / qty.
# .assign() returns a NEW DataFrame -- df itself must stay untouched (no
# "unit_price" column on df afterward). Fill in the literal string
# "unit_price" as the keyword name to check for (not just any placeholder --
# checks the literal value itself, to avoid a freebie pass).
ex1_new_col_name = ...
try:
    ex1_out = df.assign(**{ex1_new_col_name: df["amount"] / df["qty"]})
    ex1_row0 = ex1_out[ex1_new_col_name].iloc[0]
    ex1_df_untouched = ex1_new_col_name not in df.columns
except Exception:
    ex1_row0 = ex1_df_untouched = None

# ---------------------------------------------------------------------------
# Exercise 2 — two keywords in one call: "unit_price" then "unit_price_rounded",
# where the second one's lambda reads the first one's new column off `d`.
# A plain (non-lambda) expression there would raise KeyError, since it would
# evaluate against the ORIGINAL df, which never has "unit_price". Fill in the
# literal int 1 for the round() precision (not just any placeholder -- checks
# the literal value, to avoid a freebie pass).
ex2_round_ndigits = ...
try:
    ex2_out = df.assign(
        unit_price=lambda d: d["amount"] / d["qty"],
        unit_price_rounded=lambda d: d["unit_price"].round(ex2_round_ndigits),
    )
    ex2_row1 = ex2_out["unit_price_rounded"].iloc[1]  # Binh: 215.5 / 2 = 107.75 -> 107.8
except Exception:
    ex2_row1 = None

# ---------------------------------------------------------------------------
# Exercise 3 — overwrite an EXISTING column ("amount") via assign(), doubling
# it in the result, while df's own "amount" column stays fully unchanged.
# Fill in the literal int 2 as the multiplier (not just any placeholder --
# checks the literal value, to avoid a freebie pass).
ex3_multiplier = ...
try:
    ex3_out = df.assign(amount=lambda d: d["amount"] * ex3_multiplier)
    ex3_out_amounts = ex3_out["amount"].tolist()
    ex3_df_amounts = df["amount"].tolist()
except Exception:
    ex3_out_amounts = ex3_df_amounts = None

# ---------------------------------------------------------------------------
# Exercise 4 — .assign() on a FILTERED SLICE needs no .copy() first and
# raises nothing (Lesson 26's SettingWithCopy concern never applies, since
# assign() never writes into the slice's own memory). Filter df to rows
# where amount > 100, then assign a "flag" column set to True.
# Fill in the literal int 100 as the threshold (not just any placeholder --
# checks the literal value, to avoid a freebie pass).
ex4_threshold = ...
try:
    ex4_sub = df[df["amount"] > ex4_threshold]
    ex4_flagged = ex4_sub.assign(flag=True)
    ex4_all_flagged = bool(ex4_flagged["flag"].all())
    ex4_row_count = len(ex4_flagged)
except Exception:
    ex4_all_flagged = None
    ex4_row_count = None

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
    check("Exercise 1: unit_price added in the result, df itself stays untouched",
          lambda: ex1_new_col_name == "unit_price" and ex1_row0 == 40.0
          and ex1_df_untouched is True),
    check("Exercise 2: second keyword's lambda reads the first keyword's new column",
          lambda: ex2_round_ndigits == 1 and ex2_row1 == 107.8),
    check("Exercise 3: overwritten amount doubled in the result, df's own amount unchanged",
          lambda: ex3_multiplier == 2 and ex3_out_amounts == [240.0, 431.0, 199.8]
          and ex3_df_amounts == [120.0, 215.5, 99.9]),
    check("Exercise 4: assign() on a filtered slice works with no .copy(), all flagged True",
          lambda: ex4_threshold == 100 and ex4_row_count == 2 and ex4_all_flagged is True),
]

print("\nAll green — lesson 78 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
