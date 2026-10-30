# Practice 113 — Series.to_frame() and DataFrame.squeeze(): crossing back and
#                forth over the Series/DataFrame line
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/113_to_frame_and_squeeze.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: groupby(...).sum() returns a Series with the key in
# the Index. to_frame() wraps it as a one-column DataFrame, keeping the key
# in the Index (not promoting it to a column) and naming the one column
# after name= (or the Series's own .name if name= is omitted).
df = pd.read_csv("practice/data/orders_raw.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

totals = df.groupby("customer")["amount"].sum()  # a Series: An 162.0, Binh 215.5, Chi 99.9

# ex1_frame = totals.to_frame(name="total_amount")
ex1_frame = ...
try:
    ex1_is_dataframe = isinstance(ex1_frame, pd.DataFrame)
    ex1_one_column = ex1_frame.columns.tolist() == ["total_amount"]
    ex1_key_still_in_index = ex1_frame.index.tolist() == ["An", "Binh", "Chi"]
    ex1_values_ok = ex1_frame["total_amount"].tolist() == [162.0, 215.5, 99.9]
except Exception:
    ex1_is_dataframe = False
    ex1_one_column = False
    ex1_key_still_in_index = False
    ex1_values_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: reset_index() is the DIFFERENT move -- it promotes
# the Index into a real column instead, giving two columns, not one.


def to_frame_version(series):
    # Return series.to_frame(name="total_amount") -- ONE column, key stays
    # in the Index.
    #   return series.to_frame(name="total_amount")
    ...


def reset_index_version(series):
    # Return series.reset_index(name="total_amount") -- TWO columns, key
    # promoted out of the Index.
    #   return series.reset_index(name="total_amount")
    ...


# ex2_to_frame = to_frame_version(totals)
ex2_to_frame = ...
# ex2_reset = reset_index_version(totals)
ex2_reset = ...
try:
    ex2_to_frame_one_col = len(ex2_to_frame.columns) == 1
    ex2_reset_two_cols = ex2_reset.columns.tolist() == ["customer", "total_amount"]
    ex2_reset_has_rangeindex = ex2_reset.index.tolist() == [0, 1, 2]
except Exception:
    ex2_to_frame_one_col = False
    ex2_reset_two_cols = False
    ex2_reset_has_rangeindex = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: squeeze() is the inverse of to_frame(). A
# one-column DataFrame squeezes back to a Series; a one-row-one-column
# DataFrame squeezes all the way to a bare scalar; a many-row/many-column
# DataFrame is a no-op (returns the same DataFrame, unchanged).
wrapped = totals.to_frame(name="total_amount")  # 3 rows, 1 column


def squeeze_one_column(frame):
    # Return frame.squeeze() on the 3-row, 1-column `wrapped` DataFrame --
    # should come back as a Series.
    #   return frame.squeeze()
    ...


def squeeze_one_row_one_column(frame):
    # frame.iloc[[0]] is 1 row, 1 column -- squeeze() on THAT should return
    # a bare scalar, not a Series.
    #   return frame.iloc[[0]].squeeze()
    ...


# ex3_series_back = squeeze_one_column(wrapped)
ex3_series_back = ...
# ex3_scalar_back = squeeze_one_row_one_column(wrapped)
ex3_scalar_back = ...
# ex3_no_op = df[["order_id", "amount"]].squeeze()  -- many rows, many cols: unchanged
ex3_no_op = ...
try:
    ex3_is_series = isinstance(ex3_series_back, pd.Series)
    ex3_is_scalar = not isinstance(ex3_scalar_back, (pd.Series, pd.DataFrame))
    ex3_scalar_value_ok = float(ex3_scalar_back) == 162.0
    ex3_no_op_is_dataframe = isinstance(ex3_no_op, pd.DataFrame)
    ex3_no_op_shape_ok = ex3_no_op.shape == df[["order_id", "amount"]].shape
except Exception:
    ex3_is_series = False
    ex3_is_scalar = False
    ex3_scalar_value_ok = False
    ex3_no_op_is_dataframe = False
    ex3_no_op_shape_ok = False

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
    check("Exercise 1: to_frame(name=...) wraps the Series as a one-column DataFrame, key stays in the Index",
          lambda: ex1_is_dataframe is True and ex1_one_column is True
          and ex1_key_still_in_index is True and ex1_values_ok is True),
    check("Exercise 2: to_frame() keeps one column (key in Index); reset_index() promotes the key to a second column",
          lambda: ex2_to_frame_one_col is True and ex2_reset_two_cols is True
          and ex2_reset_has_rangeindex is True),
    check("Exercise 3: squeeze() reverses to_frame() -- one column back to a Series, one-row-one-col to a scalar, no-op otherwise",
          lambda: ex3_is_series is True and ex3_is_scalar is True
          and ex3_scalar_value_ok is True and ex3_no_op_is_dataframe is True
          and ex3_no_op_shape_ok is True),
]

print("\nAll green — lesson 113 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
