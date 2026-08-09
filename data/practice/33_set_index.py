# Practice 33 — set_index()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/33_set_index.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-32:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — set_index() on "order_id" (unique in this fixture), reassigned
# to a new variable rather than inplace=True (this course's default).
try:
    by_id = clean.set_index(...)
except Exception:
    by_id = pd.DataFrame()

# ---------------------------------------------------------------------------
# Exercise 2 — .loc[] lookup by the new index: order_id 5 is Binh's 180.0
# order on 2026-01-09.
try:
    row_5 = by_id.loc[...]
    amount_5 = float(row_5["amount"])
except Exception:
    amount_5 = None

# ---------------------------------------------------------------------------
# Exercise 3 — reset_index() round trip: set_index() then reset_index()
# should reproduce `clean` exactly.
try:
    round_trip = by_id.reset_index()
    is_round_trip = round_trip.equals(...)
except Exception:
    is_round_trip = False

# ---------------------------------------------------------------------------
# Exercise 4 — multi-column set_index() builds a MultiIndex; look up
# ("Binh", "2026-01-09") as a tuple.
try:
    multi = clean.set_index(...)
    binh_row = multi.loc[("Binh", "2026-01-09")]
    multi_amount = float(binh_row["amount"])
except Exception:
    multi_amount = None

# ---------------------------------------------------------------------------
# Exercise 5 — the non-unique-index gotcha: set_index() on "customer" (An and
# Binh each appear twice) does NOT raise, and .loc["An"] does NOT raise
# either -- it silently returns a multi-row DataFrame instead of one Series
# row. Set index_is_unique and an_result yourself to reproduce this.
try:
    by_customer = clean.set_index(...)
    index_is_unique = by_customer.index.is_unique
    an_result = by_customer.loc["An"]
except Exception:
    index_is_unique = None
    an_result = None

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
    check("Exercise 1: by_id's index is order_id, columns no longer include it",
          lambda: by_id.index.name == "order_id"
          and "order_id" not in by_id.columns
          and len(by_id) == 4),
    check("Exercise 2: .loc[5] finds Binh's 180.0 order",
          lambda: amount_5 is not None and abs(amount_5 - 180.0) < 1e-9),
    check("Exercise 3: set_index() then reset_index() reproduces clean exactly",
          lambda: is_round_trip is True),
    check("Exercise 4: multi is a MultiIndex, .loc[('Binh','2026-01-09')] is 180.0",
          lambda: isinstance(multi.index, pd.MultiIndex)
          and multi_amount is not None
          and abs(multi_amount - 180.0) < 1e-9),
    check("Exercise 5: index_is_unique is False (customer has duplicates)",
          lambda: index_is_unique is False),
    check("Exercise 5: .loc['An'] returns BOTH An rows as a DataFrame, not one",
          lambda: isinstance(an_result, pd.DataFrame) and len(an_result) == 2),
]
print("\nAll green — lesson 33 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
