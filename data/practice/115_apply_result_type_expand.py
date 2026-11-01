# Practice 115 — apply(result_type="expand"): turning one row-function's
#               tuple into real columns
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/115_apply_result_type_expand.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: with no result_type at all, a tuple-returning
# apply(fn, axis=1) stays as ONE object-dtype Series, not split into columns.
orders = pd.DataFrame({
    "customer": ["An", "Binh", "Chi"],
    "price": [100.0, 50.0, 200.0],
    "qty": [2, 3, 1],
})


def row_stats(row):
    return (row["price"] * row["qty"], row["price"] / row["qty"])


# ex1_default = orders.apply(row_stats, axis=1)
ex1_default = ...
try:
    ex1_is_series = isinstance(ex1_default, pd.Series)
    ex1_dtype_is_object = ex1_default.dtype == object
    ex1_first_is_tuple = isinstance(ex1_default.iloc[0], tuple)
except Exception:
    ex1_is_series = False
    ex1_dtype_is_object = False
    ex1_first_is_tuple = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: result_type="expand" spreads a dict return into
# real, named columns -- and the expanded result can be assigned straight
# back onto the original frame as new columns.
def row_stats_dict(row):
    return {"total": row["price"] * row["qty"], "unit": row["price"] / row["qty"]}


def expand_to_dataframe(df):
    # Return df.apply(row_stats_dict, axis=1, result_type="expand") -- a
    # DataFrame with two real columns, "total" and "unit".
    #   return df.apply(row_stats_dict, axis=1, result_type="expand")
    ...


def assign_expanded_columns(df):
    # Build out = df.copy(), then assign
    # out[["total", "unit"]] = expand_to_dataframe(df), then return out.
    #   out = df.copy()
    #   out[["total", "unit"]] = expand_to_dataframe(df)
    #   return out
    ...


# ex2_expanded = expand_to_dataframe(orders)
ex2_expanded = ...
# ex2_assigned = assign_expanded_columns(orders)
ex2_assigned = ...
try:
    ex2_is_dataframe = isinstance(ex2_expanded, pd.DataFrame)
    ex2_columns_ok = list(ex2_expanded.columns) == ["total", "unit"]
    ex2_an_total_ok = round(float(ex2_expanded.loc[0, "total"]), 4) == 200.0
    ex2_assigned_has_cols = {"total", "unit"}.issubset(set(ex2_assigned.columns))
except Exception:
    ex2_is_dataframe = False
    ex2_columns_ok = False
    ex2_an_total_ok = False
    ex2_assigned_has_cols = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3's callout: result_type="expand" is a no-op (falls
# back to a plain Series, no error) in two cases: axis=0 (the default), and
# when the function's return value is not list-like (e.g. a bare scalar).
def scalar_fn(row):
    return row["price"] * row["qty"]


# ex3_axis0_expand = orders[["price", "qty"]].apply(lambda col: col.sum(), result_type="expand")
ex3_axis0_expand = ...
# ex3_scalar_expand = orders.apply(scalar_fn, axis=1, result_type="expand")
ex3_scalar_expand = ...
try:
    # axis=0 (default) ignores result_type entirely -- one total per column.
    ex3_axis0_is_series = isinstance(ex3_axis0_expand, pd.Series)
    # a scalar-returning row function also stays a plain Series even with
    # result_type="expand" -- "expand" only acts on list-like returns.
    ex3_scalar_is_series = isinstance(ex3_scalar_expand, pd.Series)
except Exception:
    ex3_axis0_is_series = False
    ex3_scalar_is_series = False

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
    check("Exercise 1: no result_type leaves a tuple-returning apply() as one object-dtype Series",
          lambda: ex1_is_series is True and ex1_dtype_is_object is True
          and ex1_first_is_tuple is True),
    check("Exercise 2: result_type=\"expand\" spreads a dict return into named columns; assigns back cleanly",
          lambda: ex2_is_dataframe is True and ex2_columns_ok is True
          and ex2_an_total_ok is True and ex2_assigned_has_cols is True),
    check("Exercise 3: result_type=\"expand\" is a no-op on axis=0 and on a scalar-returning function",
          lambda: ex3_axis0_is_series is True and ex3_scalar_is_series is True),
]

print("\nAll green — lesson 115 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
