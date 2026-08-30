# Practice 53 — to_dict() and to_records(): handing a table back to plain Python
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/53_to_dict_and_to_records.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import json

import pandas as pd

# Same real fixture clean 4-row slice as Lessons 6-52.
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
# Exercise 1 — to_dict(orient="records"): a list of one dict per row. 4 rows
# in, 4 dicts out, same order; the first row's "amount" is 120.0 (Section 1).
# NOTE: the placeholder sits on the WHOLE right-hand side, not inside
# to_dict()'s own arguments -- an unfilled `records = ...` leaves `records`
# as bare Ellipsis, and `len(Ellipsis)` raises TypeError on its own (no extra
# guarding needed), confirmed directly with a standalone probe before
# shipping.
try:
    records = ...
    records_len = len(records)
    first_amount = records[0]["amount"]
except Exception:
    records_len = None
    first_amount = None

# ---------------------------------------------------------------------------
# Exercise 2 — Series.to_dict(): the grouped per-customer totals become a
# plain {label: value} dict, no Index object left at all (Section 2).
# NOTE: same whole-right-hand-side placeholder style; `Ellipsis["An"]` raises
# TypeError on its own, confirmed directly before shipping.
try:
    totals_dict = ...
    an_total = totals_dict["An"]
    binh_total = totals_dict["Binh"]
except Exception:
    an_total = None
    binh_total = None

# ---------------------------------------------------------------------------
# Exercise 3 — to_records(index=False): a NumPy structured array. Its field
# names should be exactly the 4 column names, in order, with no leftover
# "index" field since index=False was passed (Section 3).
# NOTE: `to_records(index=...)` does NOT raise on its own if the Ellipsis
# sits in the index= kwarg -- Ellipsis is truthy, so pandas would silently
# treat it as index=True, joining this course's running Ellipsis-is-truthy
# family (confirmed directly with a standalone probe before shipping).
# Placing the placeholder on the whole right-hand side instead avoids that:
# an unfilled `rec = ...` never even calls .to_records(), so it stays bare
# Ellipsis and `Ellipsis.dtype` raises AttributeError for a real ✗.
try:
    rec = ...
    rec_fields = list(rec.dtype.names)
except Exception:
    rec_fields = None

# ---------------------------------------------------------------------------
# Exercise 4 — the gotcha: json.dumps() on a plain to_dict(orient="records")
# result raises TypeError, since Timestamp isn't JSON-serializable. Fixing
# it first with .dt.strftime("%Y-%m-%d") on the order_date column makes it
# serialize cleanly (Section 4).
# NOTE: same whole-right-hand-side placeholder style; `json.dumps(Ellipsis)`
# raises TypeError on its own, confirmed directly before shipping.
try:
    json.dumps(clean.to_dict(orient="records"))
    raw_json_ok = True
except TypeError:
    raw_json_ok = False

try:
    fixed = clean.assign(order_date=clean["order_date"].dt.strftime("%Y-%m-%d"))
    fixed_json = ...
    parsed_back = json.loads(fixed_json)
    fixed_json_len = len(parsed_back)
except Exception:
    fixed_json_len = None

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
    check("Exercise 1: to_dict(orient='records') gives 4 row-dicts, first amount 120.0",
          lambda: records_len == 4 and abs(first_amount - 120.0) < 1e-9),
    check("Exercise 2: grouped Series.to_dict() gives An 162.0 / Binh 215.5",
          lambda: abs(an_total - 162.0) < 1e-9 and abs(binh_total - 215.5) < 1e-9),
    check("Exercise 3: to_records(index=False) fields match the 4 columns exactly",
          lambda: rec_fields == ["order_id", "customer", "amount", "order_date"]),
    check("Exercise 4: json.dumps() on the raw to_dict() result raises TypeError",
          lambda: raw_json_ok is False),
    check("Exercise 4: json.dumps() after .dt.strftime() succeeds, 4 rows round-trip",
          lambda: fixed_json_len == 4),
]
print("\nAll green — lesson 53 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
