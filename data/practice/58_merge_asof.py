# Practice 58 — pd.merge_asof(): joining on "nearest date," not an exact key
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/58_merge_asof.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.read_csv("practice/data/orders_raw.csv", parse_dates=["order_date"])
clean = orders.dropna(subset=["order_date"])
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()].copy()
clean["amount"] = clean["amount"].astype(float)
orders_sorted = clean.sort_values("order_date").reset_index(drop=True)
#   orders_sorted (4 rows): order_id 1 An 01-05, order_id 2 Binh 01-06,
#   order_id 5 Binh 01-09, order_id 6 An 01-10

# A small inline promo table: when each discount tier started applying.
promo = pd.DataFrame({
    "effective_date": pd.to_datetime(["2026-01-01", "2026-01-07", "2026-01-10"]),
    "tier": ["standard", "silver", "gold"],
}).sort_values("effective_date").reset_index(drop=True)

# ---------------------------------------------------------------------------
# Exercise 1 — a plain asof merge, default direction="backward": attach the
# LATEST tier effective on or before each order's date. Merge orders_sorted
# with promo, left_on="order_date", right_on="effective_date". NOTE:
# whole-right-hand-side placeholder; an unfilled `merged = ...` leaves bare
# Ellipsis, and `len(Ellipsis)` raises TypeError on its own -- confirmed
# directly with a standalone probe before shipping, so this does NOT slip
# through as an accidental freebie.
try:
    merged = ...
    merged_rows = len(merged)
    merged_tiers = merged["tier"].tolist()
except Exception:
    merged_rows = None
    merged_tiers = None

# ---------------------------------------------------------------------------
# Exercise 2 — an UNSORTED left frame should raise ValueError immediately
# ("left keys must be sorted"). Shuffle orders_sorted with
# .sample(frac=1, random_state=0) (NOT sorted by order_date), then call
# merge_asof on the shuffled frame the same way as Exercise 1. NOTE:
# whole-right-hand-side placeholder; an unfilled `shuffled = ...` leaves bare
# Ellipsis, and `Ellipsis.sample` raises AttributeError on its own before the
# merge_asof call is even reached -- confirmed directly, no accidental
# freebie risk.
try:
    shuffled = ...
    pd.merge_asof(shuffled, promo, left_on="order_date", right_on="effective_date")
    unsorted_raised = False
except ValueError:
    unsorted_raised = True
except Exception:
    unsorted_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — direction="forward": attach the NEXT tier effective at or
# after each order's date, instead of the default backward direction. Same
# merge as Exercise 1 but with direction="forward" added. NOTE:
# whole-right-hand-side placeholder; an unfilled `fwd = ...` leaves bare
# Ellipsis, and `len(Ellipsis)` raises TypeError on its own -- confirmed
# directly, same defensive shape as Exercise 1.
try:
    fwd = ...
    fwd_rows = len(fwd)
    fwd_tiers = fwd["tier"].tolist()
except Exception:
    fwd_rows = None
    fwd_tiers = None

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
    check("Exercise 1: backward asof merge -- 4 rows, tiers standard/standard/silver/gold",
          lambda: merged_rows == 4
          and merged_tiers == ["standard", "standard", "silver", "gold"]),
    check("Exercise 2: an unsorted left frame raises ValueError",
          lambda: unsorted_raised is True),
    check("Exercise 3: direction='forward' -- 4 rows, tiers silver/silver/gold/gold",
          lambda: fwd_rows == 4
          and fwd_tiers == ["silver", "silver", "gold", "gold"]),
]
print("\nAll green — lesson 58 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
