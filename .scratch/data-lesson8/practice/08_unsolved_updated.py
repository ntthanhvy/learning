# Practice 08 — Method Chaining & Pipeline Shape
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/08_method_chaining_pipeline.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")

# ---------------------------------------------------------------------------
# Exercise 1 — write Lessons 3+7's cleaning as ONE chain, starting from `df`:
# coerce amount to numeric, then drop rows missing amount or order_date.
# Wrap the expression in parentheses; use .assign(amount=lambda d: ...) for
# the coerce step.
clean = ...

# ---------------------------------------------------------------------------
# Exercise 2 — a standalone function usable with .pipe(). It should return
# its input DataFrame with a new "amount_rank" column: each customer's
# orders ranked by amount, biggest first, ties broken by row order.
def add_amount_rank(d):
    return d.assign(
        amount_rank=...
    )

# ---------------------------------------------------------------------------
# Exercise 3 — one chain, starting from `clean`, that uses .pipe(add_amount_rank)
# then keeps only each customer's single biggest order (amount_rank == 1).
# Use .query() for the filter step.
top_per_customer = ...

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
    check("Exercise 1: clean has 4 rows (order_id 3 and 4 dropped)",
          lambda: len(clean) == 4),
    check("Exercise 1: clean's amount column is numeric (float64)",
          lambda: str(clean["amount"].dtype) == "float64"),
    check("Exercise 2: add_amount_rank ranks An's 120.0 order (order_id 1) as 1",
          lambda: add_amount_rank(clean).set_index("order_id").loc[1, "amount_rank"] == 1),
    check("Exercise 2: add_amount_rank ranks Binh's 35.5 order (order_id 2) as 2",
          lambda: add_amount_rank(clean).set_index("order_id").loc[2, "amount_rank"] == 2),
    check("Exercise 3: top_per_customer is exactly An/120.0 and Binh/180.0",
          lambda: len(top_per_customer) == 2
          and set(zip(top_per_customer["customer"], top_per_customer["amount"]))
          == {("An", 120.0), ("Binh", 180.0)}),
]
print("\nAll green — lesson 8 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
