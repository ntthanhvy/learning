# Practice 60 — str.contains(): substring filtering, and the NaN trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/60_str_contains.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv")
customers = pd.read_csv("practice/data/customers.csv")
merged = orders.merge(customers, on="customer", how="left")
#   merged (6 rows): order_id 1/3/6 An (region North), order_id 2/5 Binh
#   (region South), order_id 4 Chi -- Chi has no customers.csv row, so
#   "region" is genuinely NaN for that one row.

# ---------------------------------------------------------------------------
# Exercise 1 — filter to rows whose "region" contains "south", case-insensitive.
# Use merged["region"].str.contains("south", case=False, na=False) as the mask,
# then index merged with it. NOTE: whole-right-hand-side placeholder; an
# unfilled `south_mask = ...` leaves bare Ellipsis, and `Ellipsis.str` raises
# AttributeError on its own -- confirmed directly with a standalone probe
# before shipping, so this does NOT slip through as an accidental freebie.
try:
    south_mask = ...
    south_rows = merged[south_mask]
    south_order_ids = sorted(south_rows["order_id"].tolist())
except Exception:
    south_order_ids = None

# ---------------------------------------------------------------------------
# Exercise 2 — rows whose "region" does NOT contain "north" (case-insensitive),
# treating a missing region as "doesn't contain north" (na=False) BEFORE
# negating with ~. This should include Chi's NaN-region row too. NOTE:
# whole-right-hand-side placeholder; an unfilled `not_north_mask = ...` leaves
# bare Ellipsis, and `~Ellipsis` raises TypeError on its own -- confirmed
# directly, no accidental freebie risk.
try:
    not_north_mask = ...
    not_north_rows = merged[not_north_mask]
    not_north_order_ids = sorted(not_north_rows["order_id"].tolist())
except Exception:
    not_north_order_ids = None

# ---------------------------------------------------------------------------
# Exercise 3 — literal (non-regex) substring match. Given `skus` below, find
# which values contain a LITERAL "A." (the dot itself, not "any character")
# using regex=False. NOTE: whole-right-hand-side placeholder; an unfilled
# `literal_mask = ...` leaves bare Ellipsis, and `Ellipsis.str` raises
# AttributeError on its own -- confirmed directly, same defensive shape as
# Exercises 1 and 2.
skus = pd.Series(["A.1", "A21", "B.5"])
try:
    literal_mask = ...
    literal_matches = sorted(skus[literal_mask].tolist())
except Exception:
    literal_matches = None

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
    check("Exercise 1: region contains 'south' (case-insensitive) -- order_ids [2, 5]",
          lambda: south_order_ids == [2, 5]),
    check("Exercise 2: NOT contains 'north', na=False before negating -- order_ids [2, 4, 5]",
          lambda: not_north_order_ids == [2, 4, 5]),
    check("Exercise 3: literal 'A.' match, regex=False -- only ['A.1']",
          lambda: literal_matches == ["A.1"]),
]
print("\nAll green — lesson 60 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
