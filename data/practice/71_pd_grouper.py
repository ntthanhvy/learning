# Practice 71 — pd.Grouper(): grouping by a date frequency, not just a column's values
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/71_pd_grouper.py
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

# ---------------------------------------------------------------------------
# Exercise 1 — a SOLO pd.Grouper(key="order_date", freq="D") as the only
# groupby key fills empty calendar days with 0.0, exactly like resample().
# Fill in the literal string "order_date" for key=, and "D" for freq=.
ex1_key_value = ...
ex1_freq_value = ...
try:
    ex1_daily = clean.groupby(pd.Grouper(key=ex1_key_value, freq=ex1_freq_value))["amount"].sum()
except Exception:
    ex1_daily = None

# ---------------------------------------------------------------------------
# Exercise 2 — COMBINED with another groupby key ("customer"), that
# gap-filling disappears: the result has exactly one row per (customer, day)
# combination that actually occurred, no zero-filled rows in between.
# Fill in the two-element list ["customer", pd.Grouper(key="order_date", freq="D")].
ex2_keys = ...
try:
    ex2_combo = clean.groupby(ex2_keys)["amount"].sum()
except Exception:
    ex2_combo = None

# ---------------------------------------------------------------------------
# Exercise 3 — freq="M" is dead on this pandas version (raises ValueError);
# freq="ME" (month end) is the current spelling. Fill in the literal
# string "ME".
ex3_freq_value = ...
try:
    clean.groupby(pd.Grouper(key="order_date", freq="M"))["amount"].sum()
    ex3_old_raised = False
except ValueError:
    ex3_old_raised = True
except Exception:
    ex3_old_raised = False
try:
    ex3_monthly = clean.groupby(pd.Grouper(key="order_date", freq=ex3_freq_value))["amount"].sum()
except Exception:
    ex3_monthly = None

# ---------------------------------------------------------------------------
# Exercise 4 — on a frame already indexed by order_date, use level= instead
# of key= (passing key= there raises KeyError). Fill in the literal string
# "order_date" for level=.
ex4_level_value = ...
indexed = clean.set_index("order_date")
try:
    ex4_daily = indexed.groupby(pd.Grouper(level=ex4_level_value, freq="D"))["amount"].sum()
except Exception:
    ex4_daily = None

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
    check("Exercise 1: solo Grouper fills empty 01-07/01-08 days with 0.0",
          lambda: ex1_key_value == "order_date" and ex1_freq_value == "D" and ex1_daily is not None
          and len(ex1_daily) == 6
          and ex1_daily.loc["2026-01-07"] == 0.0
          and ex1_daily.loc["2026-01-08"] == 0.0),
    check("Exercise 2: combined with customer, only 4 real rows -- no gap-fill",
          lambda: ex2_combo is not None and len(ex2_combo) == 4
          and round(ex2_combo.loc[("An", "2026-01-05")], 1) == 120.0
          and round(ex2_combo.loc[("Binh", "2026-01-09")], 1) == 180.0),
    check("Exercise 3: freq=\"M\" raises ValueError; freq=\"ME\" works",
          lambda: ex3_freq_value == "ME" and ex3_old_raised is True and ex3_monthly is not None
          and len(ex3_monthly) == 1
          and round(ex3_monthly.iloc[0], 1) == 377.5),
    check("Exercise 4: level= on an indexed frame matches Exercise 1's totals",
          lambda: ex4_level_value == "order_date" and ex4_daily is not None
          and ex1_daily is not None and ex4_daily.equals(ex1_daily)),
]

print("\nAll green — lesson 71 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
