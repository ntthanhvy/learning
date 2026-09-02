# Practice 56 — json_normalize(): flattening nested JSON into a table
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/56_json_normalize.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import json

import pandas as pd

# New fixture for this lesson: same order_id/amount/order_date values as the
# orders_raw.csv clean 4-row slice used since Lesson 6 (An 120.0/42.0, Binh
# 35.5/180.0), but shaped like a typical API response -- each order nests a
# `customer` object and an `items` list, instead of flat CSV columns.
with open("practice/data/orders_nested.json") as f:
    records = json.load(f)
#   4 dicts, each shaped like:
#   {"order_id": 1, "amount": 120.0, "order_date": "2026-01-05",
#    "customer": {"name": "An", "region": "North"},
#    "items": [{"sku": "A1", "qty": 2}, {"sku": "A2", "qty": 1}]}

# ---------------------------------------------------------------------------
# Exercise 1 — flatten the top-level nested `customer` dict into dotted
# columns with pd.json_normalize() (default sep="."). Check the resulting
# column list and one looked-up value directly. NOTE: whole-right-hand-side
# placeholder; an unfilled `flat = ...` leaves bare Ellipsis, and
# `pd.json_normalize(...)` (Ellipsis as the records argument) raises
# NotImplementedError on its own -- confirmed directly with a standalone
# probe before shipping, so this does NOT slip through as an accidental
# freebie.
try:
    flat = pd.json_normalize(...)
    flat_cols = flat.columns.tolist()
    an_first_region = flat.loc[flat["order_id"] == 1, "customer.region"].iloc[0]
except Exception:
    flat_cols = None
    an_first_region = None

# ---------------------------------------------------------------------------
# Exercise 2 — record_path + meta: explode the nested `items` list into one
# row per item, carrying `order_id` and the nested `customer.name` along as
# meta columns. NOTE: whole-right-hand-side placeholder; an unfilled
# `items_flat = ...` leaves bare Ellipsis, and `Ellipsis["qty"]` raises
# TypeError on its own -- confirmed directly before shipping.
try:
    items_flat = ...
    item_row_count = len(items_flat)
    total_qty = int(items_flat["qty"].sum())
    an_item_customers = set(items_flat.loc[items_flat["order_id"] == 1, "customer.name"])
except Exception:
    item_row_count = None
    total_qty = None
    an_item_customers = None

# ---------------------------------------------------------------------------
# Exercise 3 — json_normalize() does NOT accept a raw JSON string; it expects
# already-parsed Python objects (list of dicts / dict). Confirm the raw-string
# call raises NotImplementedError, then do it the working way: json.loads()
# first, json_normalize() second. NOTE: whole-right-hand-side placeholder; an
# unfilled `raw_call_raised = ...` leaves bare Ellipsis, and `bool(Ellipsis)`
# does NOT raise (Ellipsis is truthy) -- so this placeholder does NOT gate
# itself by raising. Guarded instead by checking `raw_call_raised is True`
# (strict identity), so an unfilled Ellipsis (truthy but not `is True`) still
# correctly prints ✗ with no crash, confirmed directly before shipping.
raw_text = json.dumps(records)
try:
    pd.json_normalize(raw_text)
    raw_call_raised = False
except NotImplementedError:
    raw_call_raised = True
except Exception:
    raw_call_raised = False

try:
    parsed_first = ...
    fixed_cols = pd.json_normalize(parsed_first).columns.tolist()
except Exception:
    fixed_cols = None

# ---------------------------------------------------------------------------
# Exercise 4 — sep= controls the joiner used to build flattened column names
# from nested keys (default "."). Confirm passing sep="_" changes
# "customer.name" to "customer_name". NOTE: whole-right-hand-side
# placeholder; an unfilled `flat_us = ...` leaves bare Ellipsis, and
# `Ellipsis.columns` raises AttributeError on its own -- confirmed directly
# before shipping.
try:
    flat_us = ...
    underscore_cols = flat_us.columns.tolist()
except Exception:
    underscore_cols = None

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
    check("Exercise 1: json_normalize() flattens the nested customer dict into dotted columns",
          lambda: flat_cols == ["order_id", "amount", "order_date", "items", "customer.name", "customer.region"]
          and an_first_region == "North"),
    check("Exercise 2: record_path='items' + meta explodes items, carrying order_id/customer.name along",
          lambda: item_row_count == 6 and total_qty == 10 and an_item_customers == {"An"}),
    check("Exercise 3: raw JSON string raises NotImplementedError; json.loads() first fixes it",
          lambda: raw_call_raised is True
          and fixed_cols == ["order_id", "amount", "order_date", "items", "customer.name", "customer.region"]),
    check("Exercise 4: sep='_' changes the flattened column joiner from '.' to '_'",
          lambda: underscore_cols == ["order_id", "amount", "order_date", "items", "customer_name", "customer_region"]),
]
print("\nAll green — lesson 56 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
