# Practice 76 — str.split(): breaking one text column into several
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/76_str_split.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

orders = pd.DataFrame({
    "customer_full": ["An Nguyen-North", "Binh Tran-South", "Chi Le-East",
                       "Danh Vo-West", np.nan],
    "sku_path": ["ELEC/PHONE/CASE-01", "HOME/KITCHEN/MUG-02", "ELEC/LAPTOP/DOCK-03",
                 "HOME/BEDROOM/LAMP-04", "TOYS/BLOCK-05"],
})

# ---------------------------------------------------------------------------
# Exercise 1 — default str.split(" ") (expand=False) returns a Series of
# PYTHON LISTS, one list per row, native length per row (no padding). Fill
# in the literal int 2 for how many pieces "An Nguyen-North" splits into on
# a single space (not just any placeholder -- checks the literal value
# itself, to avoid a freebie pass).
ex1_expected_len = ...
try:
    ex1_lists = orders["customer_full"].str.split(" ")
    ex1_row0_len = len(ex1_lists.iloc[0])
    ex1_row0_is_list = isinstance(ex1_lists.iloc[0], list)
    ex1_row4_is_missing = ex1_lists.iloc[4] is np.nan or pd.isna(ex1_lists.iloc[4])
except Exception:
    ex1_row0_len = ex1_row0_is_list = ex1_row4_is_missing = None

# ---------------------------------------------------------------------------
# Exercise 2 — expand=True turns the same split into a DataFrame, one column
# per piece. Splitting sku_path on "/" gives 3 columns for a 3-segment path
# -- but row 4 ("TOYS/BLOCK-05") only has 2 segments, so its 3rd column is
# padded with NaN, not an error. Fill in the literal string "/" for the
# delimiter (not just any placeholder -- checks the literal value, to avoid
# a freebie pass).
ex2_delimiter = ...
try:
    ex2_parts = orders["sku_path"].str.split(ex2_delimiter, expand=True)
    ex2_shape = ex2_parts.shape
    ex2_row4_col2_is_na = pd.isna(ex2_parts.loc[4, 2])
except Exception:
    ex2_shape = ex2_row4_col2_is_na = None

# ---------------------------------------------------------------------------
# Exercise 3 — n= caps how many splits happen, so the REST of the string
# stays intact in the final piece. Splitting "customer_full" on "-" with
# n=1 separates "name region" from the trailing "-North"/"-South"/etc in
# exactly one cut. Fill in the literal int 1 for n= (not just any
# placeholder -- checks the literal value, to avoid a freebie pass).
ex3_n = ...
try:
    ex3_parts = orders["customer_full"].str.split("-", n=ex3_n, expand=True)
    ex3_parts.columns = ["name_part", "region_part"]
    ex3_row0_name = ex3_parts.loc[0, "name_part"]
    ex3_row0_region = ex3_parts.loc[0, "region_part"]
except Exception:
    ex3_row0_name = ex3_row0_region = None

# ---------------------------------------------------------------------------
# Exercise 4 — .str[i] indexes into the list form (expand=False) positionally,
# and is SAFE on ragged lists: a row whose list is too short for that
# position returns NaN instead of raising IndexError. Fill in the literal
# int 2 for the position that is out-of-range for row 4's shorter
# "sku_path" list (not just any placeholder -- checks the literal value, to
# avoid a freebie pass).
ex4_position = ...
try:
    ex4_lists = orders["sku_path"].str.split("/")
    ex4_row4_result = ex4_lists.str[ex4_position].iloc[4]
    ex4_row4_is_na = pd.isna(ex4_row4_result)
    ex4_row0_result = ex4_lists.str[ex4_position].iloc[0]
except Exception:
    ex4_row4_is_na = None
    ex4_row0_result = None

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
    check("Exercise 1: default split(expand=False) gives native-length lists per row",
          lambda: ex1_expected_len == 2 and ex1_row0_len == 2
          and ex1_row0_is_list is True and ex1_row4_is_missing is True),
    check("Exercise 2: expand=True pads a shorter row's extra column with NaN",
          lambda: ex2_delimiter == "/" and ex2_shape == (5, 3)
          and ex2_row4_col2_is_na is True),
    check("Exercise 3: n= caps split count, leaving the remainder intact",
          lambda: ex3_n == 1 and ex3_row0_name == "An Nguyen"
          and ex3_row0_region == "North"),
    check("Exercise 4: .str[i] on a ragged list is safe, returns NaN not IndexError",
          lambda: ex4_position == 2 and ex4_row4_is_na is True
          and ex4_row0_result == "CASE-01"),
]

print("\nAll green — lesson 76 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
