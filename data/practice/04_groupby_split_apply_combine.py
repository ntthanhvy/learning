# Practice 04 — GroupBy: split, apply, combine
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/04_groupby_split_apply_combine.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# Same file as Lessons 2–3, coerced the same way.
df = pd.read_csv("practice/data/orders_raw.csv")
amount_clean = pd.to_numeric(df["amount"], errors="coerce")
df2 = df.assign(amount_clean=amount_clean)

# ---------------------------------------------------------------------------
# Exercise 1 — total amount per customer: SELECT customer, SUM(amount_clean)
# FROM df2 GROUP BY customer. .sum() ignores NaN on its own (skipna=True).
totals = ...

# ---------------------------------------------------------------------------
# Exercise 2 — order count per customer, counting EVERY row including the one
# with a missing amount: SELECT customer, COUNT(*) FROM df2 GROUP BY customer.
# .size() counts rows per group regardless of NaN; .count() would skip them —
# that difference is the point of this exercise.
order_counts = ...

# ---------------------------------------------------------------------------
# Exercise 3 — the SQL HAVING step: keep only customers with more than one
# order, sorted by total descending. Filter totals using order_counts > 1,
# then .sort_values(ascending=False). One line, using the two Series above.
repeat_customers = ...

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
    check("Exercise 1: totals per customer — An 162.0, Binh 215.5, Chi 99.9",
          lambda: round(totals["An"], 1) == 162.0 and round(totals["Binh"], 1) == 215.5
          and round(totals["Chi"], 1) == 99.9),
    check("Exercise 2: order_counts counts ALL rows — An 3, Binh 2, Chi 1",
          lambda: order_counts["An"] == 3 and order_counts["Binh"] == 2 and order_counts["Chi"] == 1),
    check("Exercise 3: repeat_customers is Binh then An, Chi excluded",
          lambda: list(repeat_customers.index) == ["Binh", "An"] and len(repeat_customers) == 2),
]
print("\nAll green — lesson 4 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
