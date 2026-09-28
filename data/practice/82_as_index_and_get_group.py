# Practice 82 — groupby(as_index=False) and .get_group(): two groupby leftovers
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/82_as_index_and_get_group.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
df["amount_clean"] = pd.to_numeric(df["amount"], errors="coerce")

# ---------------------------------------------------------------------------
# Exercise 1 — pass as_index=False to groupby() itself and confirm the result
# matches the default groupby's .sum() chained with .reset_index() exactly
# (Section 2).
# ex1_flat = df.groupby("customer", as_index=False)["amount_clean"].sum()
try:
    ex1_flat = df.groupby("customer", as_index=...)["amount_clean"].sum()
    ex1_baseline = df.groupby("customer")["amount_clean"].sum().reset_index()
    ex1_matches = ex1_flat.equals(ex1_baseline)
except Exception:
    ex1_matches = None

# ---------------------------------------------------------------------------
# Exercise 2 — the exact same single-column .sum() call returns a Series by
# default, but a DataFrame once as_index=False is passed. Confirm both types
# (Section 2).
try:
    ex2_default_result = df.groupby("customer")["amount_clean"].sum()
    ex2_flat_result = df.groupby("customer", as_index=...)["amount_clean"].sum()
    ex2_default_is_series = isinstance(ex2_default_result, pd.Series)
    ex2_flat_is_dataframe = isinstance(ex2_flat_result, pd.DataFrame)
except Exception:
    ex2_default_is_series = ex2_flat_is_dataframe = None

# ---------------------------------------------------------------------------
# Exercise 3 — .get_group() on a GroupBy object returns the original,
# un-aggregated rows for exactly one named group. Fetch An's own rows and
# confirm it matches a plain boolean-mask filter row for row (Section 3).
# grouped = df.groupby("customer")
# ex3_an_rows = grouped.get_group("An")
grouped = df.groupby("customer")
try:
    ex3_an_rows = grouped.get_group(...)
    ex3_expected = df[df["customer"] == "An"]
    ex3_matches = ex3_an_rows.equals(ex3_expected)
    ex3_row_count = len(ex3_an_rows)
except Exception:
    ex3_matches = None
    ex3_row_count = None

# ---------------------------------------------------------------------------
# Exercise 4 — calling .get_group() with a name that was never a value in the
# grouping column raises KeyError immediately, rather than returning an empty
# DataFrame silently. Fill in the exception type expected (Section 3).
# ex4_error_type = KeyError
ex4_error_type = ...
try:
    grouped.get_group("Zzz")
    ex4_raised_correct_error = False
except BaseException as e:
    ex4_raised_correct_error = isinstance(ex4_error_type, type) and isinstance(e, ex4_error_type)

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
    check("Exercise 1: as_index=False matches default groupby().sum().reset_index() exactly",
          lambda: ex1_matches is True),
    check("Exercise 2: default single-column sum() is a Series, as_index=False version is a DataFrame",
          lambda: ex2_default_is_series is True and ex2_flat_is_dataframe is True),
    check("Exercise 3: get_group('An') returns An's 3 original rows, matching a boolean-mask filter",
          lambda: ex3_matches is True and ex3_row_count == 3),
    check("Exercise 4: get_group() on a missing group name raises KeyError",
          lambda: ex4_raised_correct_error is True),
]

print("\nAll green — lesson 82 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
