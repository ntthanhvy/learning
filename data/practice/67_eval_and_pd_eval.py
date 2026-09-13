# Practice 67 — df.eval() and pd.eval(): SELECT expressions, spelled as a string
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/67_eval_and_pd_eval.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture as recent lessons, cleaned the same way. NOTE: these
# intermediate Series are named *_col on purpose, NOT "amount"/"order_date"
# -- Exercise 4 needs pd.eval("amount > threshold") to have no bare local
# variable named "amount" it could accidentally resolve against, so the
# only "amount" it could possibly mean is the DataFrame column, which
# pd.eval() (unlike df.eval()) has no way to see without spelling out
# clean.amount. Confirmed directly with a standalone probe before shipping:
# leaving a bare module-level `amount = ...` in scope makes pd.eval("amount
# > threshold") silently succeed against THAT variable instead of raising,
# which would have made Exercise 4 test nothing at all.
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
# Exercise 1 — df.eval() computing a new "half" column (amount / 2). Confirm
# it matches an equivalent assign() call exactly.
try:
    ex1 = clean.eval(...)
except Exception:
    ex1 = None

# ---------------------------------------------------------------------------
# Exercise 2 — inplace=True mutates clean2 directly and returns None.
clean2 = clean.copy()
try:
    ex2_return = clean2.eval("half = amount / 2", inplace=...)
except Exception:
    ex2_return = "not None"

# ---------------------------------------------------------------------------
# Exercise 3 — df.eval() needs @ to reach an outside Python variable. Fill in
# the expression string so it filters amount > threshold using @threshold.
threshold = 100
try:
    ex3 = clean.eval(...).tolist()
except Exception:
    ex3 = None

# Same expression WITHOUT @ should raise -- confirmed directly with a
# standalone probe before shipping: pandas looks for a column literally
# named "threshold", finds none, and raises UndefinedVariableError.
ex3_no_at_raised = False
try:
    clean.eval("amount > threshold")
except Exception:
    ex3_no_at_raised = True

# ---------------------------------------------------------------------------
# Exercise 4 — pd.eval() (the bare top-level function, NOT a DataFrame
# method) has NO column awareness at all. Confirm the bare column name
# "amount" raises there too, even though clean.eval("amount > @threshold")
# above worked fine with the identical bare name.
ex4_bare_raised = False
try:
    pd.eval("amount > threshold")
except Exception:
    ex4_bare_raised = True

# Fill in the correct top-level form: spell the DataFrame out explicitly
# (clean.amount) so pd.eval() has something to resolve "amount" against.
try:
    ex4_explicit = pd.eval(...).tolist()
except Exception:
    ex4_explicit = None

# ---------------------------------------------------------------------------
# Exercise 5 — a multi-line eval() computing TWO columns in one call: half
# (amount / 2) and doubled (amount * 2).
try:
    ex5 = clean.eval(
        """
half = amount / 2
doubled = ...
"""
    )
except Exception:
    ex5 = None

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
    check("Exercise 1: df.eval() computed column matches assign() exactly",
          lambda: ex1 is not None
          and ex1.equals(clean.assign(half=clean["amount"] / 2))),
    check("Exercise 2: inplace=True returns None and mutates clean2 directly",
          lambda: ex2_return is None and "half" in clean2.columns
          and clean2["half"].tolist() == [60.0, 21.0, 17.75, 90.0]),
    check("Exercise 3: @threshold works, bare threshold (no @) raises",
          lambda: ex3 == [True, False, False, True] and ex3_no_at_raised),
    check("Exercise 4: pd.eval() bare column raises, clean.amount form works",
          lambda: ex4_bare_raised
          and ex4_explicit == [True, False, False, True]),
    check("Exercise 5: multi-line eval() adds both half and doubled columns",
          lambda: ex5 is not None
          and ex5["doubled"].tolist() == [240.0, 84.0, 71.0, 360.0]
          and ex5["half"].tolist() == [60.0, 21.0, 17.75, 90.0]),
]

print("\nAll green — lesson 67 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
