# Practice 85 — Sparse dtype: compressing a column that's mostly one repeated value
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/85_sparse_dtype.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1 — casting a mostly-zero Series to Sparse[int64] with an
# EXPLICIT fill_value=0 (Section 1). Fill in the fill_value to pass.
# ex1_fill_value = 0
ex1_fill_value = ...
try:
    ex1_dense = pd.Series([0, 0, 0, 5, 0, 0, 3, 0])
    ex1_sparse = ex1_dense.astype(pd.SparseDtype("int64", fill_value=ex1_fill_value))
    ex1_dtype_str = str(ex1_sparse.dtype)
    ex1_density = ex1_sparse.sparse.density
except Exception:
    ex1_dtype_str = None
    ex1_density = None

# ---------------------------------------------------------------------------
# Exercise 2 — the fill_value trap (Section 2): casting a real all-zero
# column to Sparse[float64] with NO fill_value declared should NOT shrink
# memory the way the explicit fill_value=0.0 version does, because the
# default fill is NaN, not 0. Fill in the correct fill_value to use for
# the "fixed" version so it actually compresses.
# ex2_correct_fill_value = 0.0
ex2_correct_fill_value = ...
try:
    n = 2000
    ex2_dense = pd.Series(np.zeros(n))
    ex2_dense.iloc[:40] = 7.5  # 2% filled, rest real 0.0

    ex2_no_fill = ex2_dense.astype("Sparse[float64]")  # no fill_value -- defaults to NaN
    ex2_with_fill = ex2_dense.astype(pd.SparseDtype("float64", fill_value=ex2_correct_fill_value))

    ex2_dense_mem = ex2_dense.memory_usage(deep=True)
    ex2_no_fill_mem = ex2_no_fill.memory_usage(deep=True)
    ex2_with_fill_mem = ex2_with_fill.memory_usage(deep=True)

    # the no-fill_value version should NOT be smaller than dense (the trap)
    ex2_no_fill_is_not_smaller = ex2_no_fill_mem >= ex2_dense_mem
    # the explicit fill_value version SHOULD be meaningfully smaller than dense
    ex2_with_fill_is_smaller = ex2_with_fill_mem < (ex2_dense_mem / 2)
except Exception:
    ex2_no_fill_is_not_smaller = None
    ex2_with_fill_is_smaller = None

# ---------------------------------------------------------------------------
# Exercise 3 — get_dummies(sparse=True) defaults fill_value=False on its
# own, and reading values back matches the dense version exactly (Section 3).
# Fill in the keyword value to request the sparse version.
# ex3_sparse_flag = True
ex3_sparse_flag = ...
try:
    ex3_flag_is_real_true = ex3_sparse_flag is True
    ex3_cats = pd.Series(["a", "b", "a", "c", "b"])
    ex3_dense_dum = pd.get_dummies(ex3_cats)
    ex3_sparse_dum = pd.get_dummies(ex3_cats, sparse=ex3_sparse_flag)
    ex3_fill_value = ex3_sparse_dum["a"].dtype.fill_value
    ex3_values_match = ex3_dense_dum["a"].tolist() == ex3_sparse_dum["a"].tolist()
except Exception:
    ex3_flag_is_real_true = None
    ex3_fill_value = None
    ex3_values_match = None

# ---------------------------------------------------------------------------
# Exercise 4 — groupby().sum() on a sparse column returns correct values,
# no special handling needed (Section 4). Fill in the grouping column name.
# ex4_group_col = "g"
ex4_group_col = ...
try:
    ex4_df = pd.DataFrame({
        "g": ["x", "x", "y", "y"],
        "v": pd.array([0, 0, 5, 0], dtype=pd.SparseDtype("int64", fill_value=0)),
    })
    ex4_result = ex4_df.groupby(ex4_group_col)["v"].sum()
    ex4_x_total = int(ex4_result.loc["x"])
    ex4_y_total = int(ex4_result.loc["y"])
except Exception:
    ex4_x_total = None
    ex4_y_total = None

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
    check("Exercise 1: explicit fill_value=0 gives Sparse[int64, 0] with density 0.25",
          lambda: ex1_dtype_str == "Sparse[int64, 0]" and ex1_density == 0.25),
    check("Exercise 2: no fill_value= defaults to NaN (no shrink); fill_value=0.0 shrinks a lot",
          lambda: ex2_no_fill_is_not_smaller is True and ex2_with_fill_is_smaller is True),
    check("Exercise 3: get_dummies(sparse=True) defaults fill_value=False; values match dense",
          lambda: ex3_flag_is_real_true is True and ex3_fill_value is False and ex3_values_match is True),
    check("Exercise 4: groupby().sum() on a sparse column returns correct totals",
          lambda: ex4_x_total == 0 and ex4_y_total == 5),
]

print("\nAll green — lesson 85 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
