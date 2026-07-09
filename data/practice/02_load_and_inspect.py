# Practice 02 — Load & inspect real files
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/02_load_and_inspect.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — load the raw file exactly as it sits on disk. No parsing hints
# yet: read it plain, so you can see what pandas infers on its own.
# File: practice/data/orders_raw.csv (relative to where you run this script).
df = ...

# ---------------------------------------------------------------------------
# Exercise 2 — "amount" is read as text (one row has the string "unknown" in
# it, so the WHOLE column loses its numeric dtype). Fix it: convert to a
# proper numeric column, turning anything unparseable into NaN instead of
# crashing.
amount_clean = ...

# ---------------------------------------------------------------------------
# Exercise 3 — "order_date" is read as text too (dates are just strings to
# read_csv unless told otherwise). Parse it into real datetimes, turning the
# blank field into NaT (pandas' "missing timestamp") instead of crashing.
order_date_clean = ...

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
    check("Exercise 1: read_csv loads all 6 rows, 4 columns",
          lambda: df.shape == (6, 4) and list(df.columns) == ["order_id", "customer", "amount", "order_date"]),
    check("Exercise 2: amount_clean is numeric with one NaN",
          lambda: amount_clean.notna().sum() == 5 and round(amount_clean.dropna().sum(), 1) == 477.4),
    check("Exercise 3: order_date_clean is datetime with one NaT",
          lambda: str(order_date_clean.dtype).startswith("datetime64") and order_date_clean.isna().sum() == 1),
]
print("\nAll green — lesson 2 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
