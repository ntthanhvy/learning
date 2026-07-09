# Practice 01 — Think in tables, not loops
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/01_tables_not_loops.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["An", "Bình", "An", "Chi", "Bình", "An"],
    "amount":   [120.0, 35.5, 250.0, 99.9, 180.0, 42.0],
    "qty":      [2, 1, 5, 3, 4, 1],
})

# ---------------------------------------------------------------------------
# Exercise 1 — SQL: SELECT customer, amount FROM orders;
# Select just the customer and amount columns (a smaller DataFrame).
ex1 = ...

# ---------------------------------------------------------------------------
# Exercise 2 — SQL: SELECT * FROM orders WHERE amount > 100;
# Keep the rows where amount is greater than 100, using a boolean mask.
ex2 = ...

# ---------------------------------------------------------------------------
# Exercise 3 — SQL: SELECT *, amount / qty AS unit_price FROM orders;
# Add a unit_price column in ONE vectorized expression (no loop).
orders["unit_price"] = ...

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
    check("Exercise 1: SELECT two columns",
          lambda: list(ex1.columns) == ["customer", "amount"] and len(ex1) == 6),
    check("Exercise 2: WHERE amount > 100",
          lambda: sorted(ex2["order_id"].tolist()) == [1, 3, 5]),
    check("Exercise 3: vectorized unit_price",
          lambda: orders["unit_price"].round(2).tolist() == [60.0, 35.5, 50.0, 33.3, 45.0, 42.0]),
]
print("\nAll green — lesson 1 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
