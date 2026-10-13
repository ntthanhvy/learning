# Practice 96 — DataFrame.insert() and .pop(): the two column-management
# methods that mutate in place
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/96_insert_and_pop.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: insert() mutates the frame directly, placing a new
# column at an exact position, and returns None (nothing to reassign).
# df1.insert(1, "new_col", [100, 200, 300])
df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
ex1_insert_return = ...
try:
    ex1_return_is_none = ex1_insert_return is None
    ex1_cols = list(df1.columns)
    ex1_cols_ok = bool(ex1_cols == ["a", "new_col", "b", "c"])
except Exception:
    ex1_return_is_none = False
    ex1_cols_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 1: insert() raises ValueError on a duplicate column
# name by default; allow_duplicates=True overrides that guard on purpose.
# ex2_duplicate_raised = True/False, set inside the except block below
df2 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
ex2_duplicate_raised = ...
try:
    df2.insert(0, "a", [0, 0])
except ValueError:
    ex2_duplicate_raised = True
except Exception:
    ex2_duplicate_raised = False

# df2.insert(0, "a", [0, 0], allow_duplicates=True)
...
try:
    ex2_allowed_cols = list(df2.columns)
    ex2_allowed_ok = bool(ex2_allowed_cols.count("a") == 2)
except Exception:
    ex2_allowed_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2/3: pop() removes a column AND returns it as a
# Series, mutating the frame directly -- unlike drop(columns=), which
# returns a brand-new frame and leaves the original untouched.
# ex3_popped = df3.pop("b")
df3 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
ex3_popped = ...
try:
    ex3_popped_is_series = isinstance(ex3_popped, pd.Series)
    ex3_popped_values_ok = bool(list(ex3_popped) == [4, 5, 6])
    ex3_df3_cols_ok = bool(list(df3.columns) == ["a", "c"])
except Exception:
    ex3_popped_is_series = False
    ex3_popped_values_ok = False
    ex3_df3_cols_ok = False

# df4.drop(columns=["b"]) -- returns a NEW frame, df4 itself stays unchanged
df4 = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
ex3_dropped = ...
try:
    ex3_dropped_cols_ok = bool(list(ex3_dropped.columns) == ["a", "c"])
    ex3_df4_untouched = bool(list(df4.columns) == ["a", "b", "c"])
except Exception:
    ex3_dropped_cols_ok = False
    ex3_df4_untouched = False

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
    check("Exercise 1: insert() mutates in place at the right position, returns None",
          lambda: ex1_return_is_none is True
          and ex1_cols_ok is True),
    check("Exercise 2: insert() guards duplicate names, allow_duplicates=True overrides it",
          lambda: ex2_duplicate_raised is True
          and ex2_allowed_ok is True),
    check("Exercise 3: pop() mutates + returns a Series; drop(columns=) returns a new frame instead",
          lambda: ex3_popped_is_series is True
          and ex3_popped_values_ok is True
          and ex3_df3_cols_ok is True
          and ex3_dropped_cols_ok is True
          and ex3_df4_untouched is True),
]

print("\nAll green — lesson 96 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
