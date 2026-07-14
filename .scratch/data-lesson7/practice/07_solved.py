# Practice 07 — Rank & Cumulative: Top N Per Group, Running Totals
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/07_rank_cumulative.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
# Same clean slice as Lesson 6: drop the unparseable amount (order_id 3) and
# the missing order_date (order_id 4, Chi). 4 clean rows: An x2, Binh x2.
clean = df.dropna(subset=["amount", "order_date"])

# ---------------------------------------------------------------------------
# Exercise 1 — rank each customer's own orders by amount, biggest first.
# SQL: RANK() OVER (PARTITION BY customer ORDER BY amount DESC). Ties broken
# by row order here (method="first"), the ROW_NUMBER() flavor of ranking.
clean = clean.assign(
    amount_rank=clean.groupby("customer")["amount"].rank(method="first", ascending=False)
)

# ---------------------------------------------------------------------------
# Exercise 2 — running total per customer, in date order. SQL:
# SUM(amount) OVER (PARTITION BY customer ORDER BY order_date). cumsum()
# only accumulates in ROW order, so sort by date within each customer first.
by_date = clean.sort_values("order_date")
by_date = by_date.assign(
    running_total=by_date.groupby("customer")["amount"].cumsum()
)

# ---------------------------------------------------------------------------
# Exercise 3 — top-N-per-group: keep only each customer's single biggest
# order. Reuse Exercise 1's amount_rank — filter to rank == 1.
top_order_per_customer = clean[clean["amount_rank"] == 1]

# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok

an = clean[clean["customer"] == "An"].set_index("order_id")
binh = clean[clean["customer"] == "Binh"].set_index("order_id")

results = [
    check("Exercise 1: An's 120.0 order (order_id 1) ranks 1, 42.0 (order_id 6) ranks 2",
          lambda: an.loc[1, "amount_rank"] == 1 and an.loc[6, "amount_rank"] == 2),
    check("Exercise 1: Binh's 180.0 order (order_id 5) ranks 1, not 35.5 (order_id 2)",
          lambda: binh.loc[5, "amount_rank"] == 1 and binh.loc[2, "amount_rank"] == 2),
    check("Exercise 2: An's running_total ends at 162.0 (120.0 then +42.0)",
          lambda: by_date[by_date["customer"] == "An"]["running_total"].tolist() == [120.0, 162.0]),
    check("Exercise 2: Binh's running_total ends at 215.5 (35.5 then +180.0)",
          lambda: by_date[by_date["customer"] == "Binh"]["running_total"].tolist() == [35.5, 215.5]),
    check("Exercise 3: top order per customer is exactly An/120.0 and Binh/180.0",
          lambda: len(top_order_per_customer) == 2
          and set(zip(top_order_per_customer["customer"], top_order_per_customer["amount"]))
          == {("An", 120.0), ("Binh", 180.0)}),
]
print("\nAll green — lesson 7 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
