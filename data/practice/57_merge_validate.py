# Practice 57 — merge(validate=): catching row-multiplication before it ships
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/57_merge_validate.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Reuses Lesson 5's fixtures -- no new fixture needed for this lesson.
orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")
#   orders: 6 rows -- An has 3, Binh has 2, Chi has 1 (Chi has no customer row)
#   customers: 3 rows, one per customer -- An, Binh, Danh (Danh never ordered)

# ---------------------------------------------------------------------------
# Exercise 1 — a passing validate= check. customers (left) is unique per
# customer; orders (right) may repeat a customer freely. Merge customers ->
# orders, on="customer", how="inner", validate="one_to_many". NOTE:
# whole-right-hand-side placeholder; an unfilled `merged = ...` leaves bare
# Ellipsis, and `len(Ellipsis)` raises TypeError on its own -- confirmed
# directly with a standalone probe before shipping, so this does NOT slip
# through as an accidental freebie.
try:
    merged = ...
    merged_rows = len(merged)
    merged_cols = merged.columns.tolist()
except Exception:
    merged_rows = None
    merged_cols = None

# ---------------------------------------------------------------------------
# Exercise 2 — mislabeling the SAME merge as validate="one_to_one" should
# raise pandas.errors.MergeError, since orders (right) genuinely repeats the
# customer key. Fill in `mislabel_validate` with the (wrong, but plausible)
# label a rushed engineer might have assumed. NOTE: whole-value placeholder;
# an unfilled `mislabel_validate = ...` passed straight into validate=...
# raises ValueError ("Ellipsis" is not a valid argument) on its own, caught
# by the generic `except Exception` below rather than the specific
# `except pd.errors.MergeError` -- so `mislabel_raised` stays False and
# correctly prints ✗ unsolved, confirmed directly before shipping.
mislabel_validate = ...
try:
    customers.merge(orders, on="customer", how="inner", validate=mislabel_validate)
    mislabel_raised = False
except pd.errors.MergeError:
    mislabel_raised = True
except Exception:
    mislabel_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — the reversed direction: orders (left) may repeat the key,
# customers (right) must be unique. Merge orders -> customers, on="customer",
# how="inner", validate="many_to_one". NOTE: whole-right-hand-side
# placeholder; an unfilled `reversed_merge = ...` leaves bare Ellipsis, and
# `len(Ellipsis)` raises TypeError on its own -- confirmed directly before
# shipping, same defensive shape as Exercise 1.
try:
    reversed_merge = ...
    reversed_rows = len(reversed_merge)
    reversed_cols = reversed_merge.columns.tolist()
except Exception:
    reversed_rows = None
    reversed_cols = None

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
    check("Exercise 1: validate='one_to_many' passes, same 5 rows as a plain merge",
          lambda: merged_rows == 5
          and merged_cols == ["customer", "region", "order_id", "amount", "order_date"]),
    check("Exercise 2: mislabeling as validate='one_to_one' raises MergeError",
          lambda: mislabel_raised is True and mislabel_validate == "one_to_one"),
    check("Exercise 3: reversed direction, validate='many_to_one' passes, same 5 rows",
          lambda: reversed_rows == 5
          and reversed_cols == ["order_id", "customer", "amount", "order_date", "region"]),
]
print("\nAll green — lesson 57 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
