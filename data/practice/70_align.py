# Practice 70 — align(): making two mismatched frames line up on purpose
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/70_align.py
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

# Two overlapping-but-not-identical slices keyed by order_id, with
# different rows present AND different columns -- same setup as the lesson.
by_id = clean.set_index("order_id")
left = by_id[["customer", "amount"]].loc[[1, 2, 5]]
right = by_id[["amount", "order_date"]].loc[[2, 5, 6]]

# ---------------------------------------------------------------------------
# Exercise 1 — default align(): both returned frames share the UNION of
# index labels [1, 2, 5, 6] and the UNION of columns. Fill in the other
# frame to align against (the literal name `right`).
ex1_other = ...
try:
    ex1_a, ex1_b = left.align(ex1_other)
except Exception:
    ex1_a, ex1_b = None, None

# ---------------------------------------------------------------------------
# Exercise 2 — join="inner" keeps only labels present on BOTH sides for
# both index and columns -- no NaN anywhere in the result. Fill in the
# literal string "inner" (not just any placeholder -- this checks the
# value actually passed, not merely that align() ran).
ex2_join_value = ...
try:
    ex2_a, ex2_b = left.align(right, join=ex2_join_value)
except Exception:
    ex2_a, ex2_b = None, None

# ---------------------------------------------------------------------------
# Exercise 3 — axis=0 aligns only the row index; each side keeps its OWN
# columns untouched. Fill in the literal integer 0.
ex3_axis_value = ...
try:
    ex3_a, ex3_b = left.align(right, axis=ex3_axis_value)
except Exception:
    ex3_a, ex3_b = None, None

# ---------------------------------------------------------------------------
# Exercise 4 — fill_value=0 works cleanly on a numeric-only subset (just
# the "amount" column from each side), but raises TypeError on the
# original mixed-dtype frames because the union of columns includes the
# string "customer" column. Fill in the literal integer 0.
ex4_fill_value = ...
left_num, right_num = left[["amount"]], right[["amount"]]
try:
    ex4_a, ex4_b = left_num.align(right_num, fill_value=ex4_fill_value)
except Exception:
    ex4_a, ex4_b = None, None
try:
    left.align(right, fill_value=ex4_fill_value)
    ex4_raised = False
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
    check("Exercise 1: default align() returns both frames on the union index/columns",
          lambda: ex1_other is right and ex1_a is not None and ex1_b is not None
          and ex1_a.index.tolist() == [1, 2, 5, 6]
          and ex1_b.index.tolist() == [1, 2, 5, 6]
          and sorted(ex1_a.columns.tolist()) == ["amount", "customer", "order_date"]
          and sorted(ex1_b.columns.tolist()) == ["amount", "customer", "order_date"]),
    check("Exercise 2: join=\"inner\" keeps only shared labels, no NaN anywhere",
          lambda: ex2_join_value == "inner" and ex2_a is not None and ex2_b is not None
          and ex2_a.index.tolist() == [2, 5]
          and ex2_a.columns.tolist() == ["amount"]
          and not ex2_a.isna().any().any() and not ex2_b.isna().any().any()),
    check("Exercise 3: axis=0 aligns rows only, each side keeps its own columns",
          lambda: ex3_axis_value == 0 and ex3_a is not None and ex3_b is not None
          and ex3_a.index.tolist() == [1, 2, 5, 6]
          and ex3_b.index.tolist() == [1, 2, 5, 6]
          and ex3_a.columns.tolist() == ["customer", "amount"]
          and ex3_b.columns.tolist() == ["amount", "order_date"]),
    check("Exercise 4: fill_value=0 works on numeric-only subset, raises TypeError on mixed dtypes",
          lambda: ex4_fill_value == 0 and ex4_a is not None
          and ex4_a.loc[6, "amount"] == 0.0 and ex4_raised is True),
]

print("\nAll green — lesson 70 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
