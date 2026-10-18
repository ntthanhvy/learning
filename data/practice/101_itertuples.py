# Practice 101 — itertuples(): the better row-loop, for the rare case a loop
# is unavoidable
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/101_itertuples.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops
# are needed to fill in the blanks themselves (loops below are the point of
# the lesson, not something to avoid in the exercises).
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: each row from itertuples() is a namedtuple with
# .Index plus one field per column, readable by attribute.
df = pd.DataFrame({"customer": ["An", "Binh", "Chi"], "amount": [120.0, 35.5, 99.9]})

# ex1_customers = [row.customer for row in df.itertuples()]
ex1_customers = ...
# ex1_amounts = [row.amount for row in df.itertuples()]
ex1_amounts = ...
# ex1_indexes = [row.Index for row in df.itertuples()]
ex1_indexes = ...
try:
    ex1_customers_ok = bool(ex1_customers == ["An", "Binh", "Chi"])
    ex1_amounts_ok = bool(ex1_amounts == [120.0, 35.5, 99.9])
    ex1_indexes_ok = bool(ex1_indexes == [0, 1, 2])
    ex1_is_namedtuple_ok = bool(type(next(df.itertuples())).__name__ == "Pandas")
except Exception:
    ex1_customers_ok = False
    ex1_amounts_ok = False
    ex1_indexes_ok = False
    ex1_is_namedtuple_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: a column name that is not a valid Python identifier
# gets silently renamed to a positional field (_2 here) instead of raising.
df2 = df.rename(columns={"amount": "2024 amount"})

# ex2_first_row = next(df2.itertuples())
ex2_first_row = ...
try:
    # The renamed field should be reachable as a positional attribute, not
    # as `.amount` (that original name no longer exists on the row at all).
    ex2_has_positional_field_ok = bool(hasattr(ex2_first_row, "_2"))
    ex2_positional_value_ok = bool(getattr(ex2_first_row, "_2", None) == 120.0)
    ex2_no_amount_attr_ok = bool(not hasattr(ex2_first_row, "amount"))
    ex2_customer_still_ok = bool(ex2_first_row.customer == "An")
except Exception:
    ex2_has_positional_field_ok = False
    ex2_positional_value_ok = False
    ex2_no_amount_attr_ok = False
    ex2_customer_still_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: the namedtuple itertuples() yields is immutable;
# assigning to one of its fields raises AttributeError.


def assigning_raises_attribute_error(row):
    # Try `row.amount = 1`. Return True if it raises AttributeError,
    # False if it succeeds, and let any other exception type propagate.
    # try:
    #     row.amount = 1
    #     return False
    # except AttributeError:
    #     return True
    ...


# ex3_raised = assigning_raises_attribute_error(next(df.itertuples()))
ex3_raised = ...
try:
    ex3_raised_ok = bool(ex3_raised is True)
except Exception:
    ex3_raised_ok = False

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
    check("Exercise 1: itertuples() rows are namedtuples with .Index plus one field per column",
          lambda: ex1_customers_ok is True
          and ex1_amounts_ok is True
          and ex1_indexes_ok is True
          and ex1_is_namedtuple_ok is True),
    check("Exercise 2: an invalid-identifier column name silently becomes a positional field (_2)",
          lambda: ex2_has_positional_field_ok is True
          and ex2_positional_value_ok is True
          and ex2_no_amount_attr_ok is True
          and ex2_customer_still_ok is True),
    check("Exercise 3: assigning to a yielded row's field raises AttributeError (immutable)",
          lambda: ex3_raised_ok is True),
]

print("\nAll green — lesson 101 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
