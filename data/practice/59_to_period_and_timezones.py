# Practice 59 — .dt.to_period() and timezones: calendar buckets, not fixed grids
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/59_to_period_and_timezones.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv", parse_dates=["order_date"])
clean = orders.dropna(subset=["order_date"])
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()].copy()
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values("order_date").reset_index(drop=True)
#   clean (4 rows): order_id 1 An 01-05, order_id 2 Binh 01-06,
#   order_id 5 Binh 01-09, order_id 6 An 01-10 -- all fall in the same
#   calendar month, 2026-01.

# ---------------------------------------------------------------------------
# Exercise 1 — group by calendar MONTH with to_period("M") and sum "amount".
# Build the period Series with clean["order_date"].dt.to_period("M"), then
# groupby that Series and sum "amount". NOTE: whole-right-hand-side
# placeholder; an unfilled `monthly = ...` leaves bare Ellipsis, and
# `len(Ellipsis)` raises TypeError on its own -- confirmed directly with a
# standalone probe before shipping, so this does NOT slip through as an
# accidental freebie.
try:
    monthly = ...
    monthly_index_str = [str(i) for i in monthly.index]
    monthly_total = float(monthly.iloc[0]) if len(monthly) else None
except Exception:
    monthly_index_str = None
    monthly_total = None

# ---------------------------------------------------------------------------
# Exercise 2 — tz_localize("UTC") called TWICE on the same column should
# raise TypeError the second time ("Already tz-aware, use tz_convert to
# convert"). First localize clean["order_date"] to "UTC", then call
# tz_localize("UTC") AGAIN on that already-localized result. NOTE:
# whole-right-hand-side placeholder; an unfilled `localized = ...` leaves
# bare Ellipsis, and `Ellipsis.dt` raises AttributeError on its own before
# the second tz_localize call is even reached -- confirmed directly, no
# accidental freebie risk.
try:
    localized = ...
    localized.dt.tz_localize("UTC")
    double_localize_raised = False
except TypeError:
    double_localize_raised = True
except Exception:
    double_localize_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — tz_convert("Asia/Ho_Chi_Minh") on an already-localized ("UTC")
# column. Localize clean["order_date"] to "UTC" first, then tz_convert that
# result to "Asia/Ho_Chi_Minh". NOTE: whole-right-hand-side placeholder; an
# unfilled `converted = ...` leaves bare Ellipsis, and `Ellipsis.dt` raises
# AttributeError on its own -- confirmed directly, same defensive shape as
# Exercise 2.
try:
    converted = ...
    converted_hour = int(converted.iloc[0].hour)
except Exception:
    converted_hour = None

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
    check("Exercise 1: to_period('M') groupby -- one 2026-01 bucket, total 377.5",
          lambda: monthly_index_str == ["2026-01"] and monthly_total == 377.5),
    check("Exercise 2: localizing an already tz-aware column raises TypeError",
          lambda: double_localize_raised is True),
    check("Exercise 3: tz_convert('Asia/Ho_Chi_Minh') on UTC -- hour shifts to 7",
          lambda: converted_hour == 7),
]
print("\nAll green — lesson 59 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
