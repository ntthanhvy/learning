# Practice 13 — Timed Drills, Round 5: rolling() & expanding() windows
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/13_rolling_and_expanding.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
# Budget yourself: ~5-7 min per drill, like a timed round.
import pandas as pd

# ---------------------------------------------------------------------------
# Both drills use the real orders_raw.csv fixture, same clean 4-row slice
# used since Lesson 6: An 120.0 (2026-01-05) then 42.0 (2026-01-10);
# Binh 35.5 (2026-01-06) then 180.0 (2026-01-09).
orders = pd.read_csv("practice/data/orders_raw.csv")
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
clean = orders.dropna(subset=["amount", "order_date"])
ordered = clean.sort_values(["customer", "order_date"])

# ---------------------------------------------------------------------------
# Drill 1 (rolling) — 2-order moving average of amount, per customer.
# Steps: ordered.groupby("customer")["amount"].rolling(window=2).mean(),
# then .values to assign it back as a plain column (avoids the groupby
# index getting in the way of a straight column assignment).
try:
    ordered["amount_roll2_mean"] = ...
except Exception:
    ordered["amount_roll2_mean"] = None

# ---------------------------------------------------------------------------
# Drill 2 (expanding) — running average of amount so far, per customer.
# Same shape as Drill 1, swap rolling(window=2) for expanding().
try:
    ordered["amount_expand_mean"] = ...
except Exception:
    ordered["amount_expand_mean"] = None

# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def roll_vals(customer):
    return list(ordered.loc[ordered["customer"] == customer, "amount_roll2_mean"])


def expand_vals(customer):
    return list(ordered.loc[ordered["customer"] == customer, "amount_expand_mean"])


results = [
    check("Drill 1: An's rolling(2) mean is NaN then 81.0 (120.0, 42.0 -> avg 81.0)",
          lambda: (
              pd.isna(roll_vals("An")[0])
              and round(roll_vals("An")[1], 2) == 81.0
          )),
    check("Drill 1: Binh's rolling(2) mean is NaN then 107.75 (35.5, 180.0 -> avg 107.75)",
          lambda: (
              pd.isna(roll_vals("Binh")[0])
              and round(roll_vals("Binh")[1], 2) == 107.75
          )),
    check("Drill 2: An's expanding mean is 120.0 then 81.0 (no leading NaN)",
          lambda: (
              round(expand_vals("An")[0], 2) == 120.0
              and round(expand_vals("An")[1], 2) == 81.0
          )),
    check("Drill 2: Binh's expanding mean is 35.5 then 107.75 (no leading NaN)",
          lambda: (
              round(expand_vals("Binh")[0], 2) == 35.5
              and round(expand_vals("Binh")[1], 2) == 107.75
          )),
]
print("\nAll green — lesson 13 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
