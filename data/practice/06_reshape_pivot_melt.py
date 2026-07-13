# Practice 06 — Reshape: pivot_table & melt
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/06_reshape_pivot_melt.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Lesson 3 already covered cleaning — today builds on a clean table: drop the
# row with an unparseable amount (order_id 3) and the row with no order_date
# (order_id 4, Chi). 4 clean rows remain: An x2, Binh x2.
clean = df.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — wide report: SQL's SUM(CASE WHEN order_date = ... THEN amount
# END) GROUP BY customer, one column per date. pivot_table(index="customer",
# columns="order_date", values="amount", aggfunc="sum", fill_value=0).
wide = ...

# ---------------------------------------------------------------------------
# Exercise 2 — melt wide back to long: reset_index() first (customer is
# currently the INDEX, melt needs it as an ordinary column), then
# .melt(id_vars="customer", var_name="order_date", value_name="amount").
long = ...

# ---------------------------------------------------------------------------
# Exercise 3 — the round-trip gotcha: fill_value=0 padded customer/date
# combinations that never existed in `clean`, so long has more rows than
# clean. Filter long to amount != 0 — the row count should match len(clean).
real_rows = ...

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
    check("Exercise 1: wide is 2 customers x 4 dates, An/01-05 is 120.0",
          lambda: wide.shape == (2, 4) and wide.loc["An", "2026-01-05"] == 120.0
          and wide.loc["An", "2026-01-06"] == 0),
    check("Exercise 2: long has 8 rows (2 customers x 4 dates), right columns",
          lambda: len(long) == 8 and list(long.columns) == ["customer", "order_date", "amount"]),
    check("Exercise 3: real_rows count matches the original 4 clean rows",
          lambda: len(real_rows) == len(clean) == 4),
]
print("\nAll green — lesson 6 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
