# Practice 92 — pd.merge(how="cross"): every row paired with every row
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/92_merge_cross.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: how="cross" produces the cartesian product of both
# frames' rows -- every left row paired with every right row, no key needed.
# ex1_crossed = pd.merge(sizes, colors, how="cross")
sizes = pd.DataFrame({"size": ["S", "M", "L"]})
colors = pd.DataFrame({"color": ["red", "blue"]})
ex1_crossed = ...
try:
    ex1_row_count = len(ex1_crossed)
    ex1_has_both_cols = set(ex1_crossed.columns) == {"size", "color"}
    ex1_first_row_is_S_red = bool(
        ex1_crossed.iloc[0]["size"] == "S" and ex1_crossed.iloc[0]["color"] == "red"
    )
except Exception:
    ex1_row_count = -1
    ex1_has_both_cols = False
    ex1_first_row_is_S_red = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: passing on= together with how="cross" raises
# MergeError, since a cross join has no key at all. Fill in whether it
# raises (True/False).
# ex2_on_with_cross_raises = True
ex2_on_with_cross_raises = ...
try:
    try:
        pd.merge(sizes, colors.assign(size=["red", "blue"]), how="cross", on="size")
        ex2_actually_raised = False
    except Exception:
        ex2_actually_raised = True
    ex2_check_matches = bool(ex2_actually_raised == ex2_on_with_cross_raises)
except Exception:
    ex2_check_matches = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: row count multiplies, it doesn't add. Crossing a
# 4-row frame with a 5-row frame produces 20 rows, not 9.
# ex3_expected_row_count = 20
left4 = pd.DataFrame({"p": range(4)})
right5 = pd.DataFrame({"q": range(5)})
ex3_expected_row_count = ...
try:
    ex3_actual_row_count = len(pd.merge(left4, right5, how="cross"))
    ex3_count_matches = bool(ex3_actual_row_count == ex3_expected_row_count)
    ex3_not_additive = bool(ex3_expected_row_count != len(left4) + len(right5))
except Exception:
    ex3_count_matches = False
    ex3_not_additive = False

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
    check("Exercise 1: how=\"cross\" pairs every left row with every right row",
          lambda: ex1_row_count == 6
          and ex1_has_both_cols is True
          and ex1_first_row_is_S_red is True),
    check("Exercise 2: on= together with how=\"cross\" raises an error",
          lambda: ex2_check_matches is True
          and ex2_on_with_cross_raises is True),
    check("Exercise 3: row count multiplies (4x5=20), it doesn't add (4+5=9)",
          lambda: ex3_count_matches is True
          and ex3_not_additive is True
          and ex3_expected_row_count == 20),
]

print("\nAll green — lesson 92 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
