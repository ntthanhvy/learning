# Practice 54 — .equals() and .compare(): checking whether two DataFrames match
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/54_equals_and_compare.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same real fixture clean 4-row slice as Lessons 6-53.
raw = pd.read_csv("practice/data/orders_raw.csv")
amount = pd.to_numeric(raw["amount"], errors="coerce")
order_date = pd.to_datetime(raw["order_date"], errors="coerce")
clean = (
    raw.assign(amount=amount, order_date=order_date)
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
# Exercise 1 — equals(): a genuine copy should compare equal to the original
# (Section 1). NOTE: `df.equals(...)` does NOT raise on its own -- Ellipsis
# is not a DataFrame, so pandas' own comparison logic returns plain `False`
# for an unfilled call, joining this course's running Ellipsis-is-truthy/
# doesn't-raise family (confirmed directly with a standalone probe before
# shipping: `df.equals(...)` returns `False`, never raises). Checking with
# `is True` (strict identity) rather than plain truthiness catches this: an
# unfilled exercise leaves `same` as `False`, and `False is True` is False,
# giving a correct ✗ either way the bug could otherwise slip through.
try:
    same = clean.equals(...)
except Exception:
    same = None

# ---------------------------------------------------------------------------
# Exercise 2 — equals() is dtype-strict: identical VALUES in a float32 copy
# of "amount" still compare unequal to the float64 original (Section 1). The
# whole right-hand side is the placeholder; an unfilled `narrowed = ...`
# leaves `narrowed` as bare Ellipsis, and `Ellipsis.astype` raises
# AttributeError on its own, confirmed directly before shipping.
try:
    narrowed = ...
    narrowed["amount"] = narrowed["amount"].astype("float32")
    dtype_equal = clean.equals(narrowed)
except Exception:
    dtype_equal = None

# ---------------------------------------------------------------------------
# Exercise 3 — compare(): change one cell (Binh's second amount, row 3) and
# confirm compare() reports exactly that one differing value under "amount"
# (Section 2). NOTE: same whole-right-hand-side style; an unfilled
# `changed = ...` leaves bare Ellipsis, and `Ellipsis.copy` raises
# AttributeError on its own, confirmed directly before shipping.
try:
    changed = ...
    changed.loc[3, "amount"] = 999.0
    diff = clean.compare(changed)
    diff_rows = len(diff)
    diff_value = diff[("amount", "other")].iloc[0]
except Exception:
    diff_rows = None
    diff_value = None

# ---------------------------------------------------------------------------
# Exercise 4 — why not just `==`: NaN never equals NaN under `==`, so two
# otherwise-identical frames that both carry a real NaN report as "not
# equal" through `(a == b).all().all()`, while `.equals()` correctly treats
# matching NaN positions as equal (Section 3). NOTE: whole-right-hand-side
# placeholder; an unfilled `elementwise_equal = ...` leaves bare Ellipsis,
# and `(...).all` raises AttributeError on its own (Ellipsis has no `.all`
# attribute), confirmed directly before shipping.
a = pd.DataFrame({"x": [1.0, float("nan")]})
b = pd.DataFrame({"x": [1.0, float("nan")]})
try:
    elementwise_equal = ...
    double_equal_result = elementwise_equal.all().all()
except Exception:
    double_equal_result = None

try:
    equals_result = a.equals(b)
except Exception:
    equals_result = None

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
    check("Exercise 1: clean.equals(a real copy) is True",
          lambda: same is True),
    check("Exercise 2: equals() is dtype-strict -- float32 copy of amount compares unequal",
          lambda: dtype_equal is False),
    check("Exercise 3: compare() reports exactly 1 differing row, other=999.0",
          lambda: diff_rows == 1 and abs(diff_value - 999.0) < 1e-9),
    check("Exercise 4: (a == b).all().all() is False because NaN != NaN under ==",
          lambda: double_equal_result == False and double_equal_result is not None),
    check("Exercise 4: a.equals(b) is True -- equals() treats matching NaN as equal",
          lambda: equals_result is True),
]
print("\nAll green — lesson 54 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
