# Practice 75 — searchsorted(): binary search on data you already sorted
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/75_searchsorted.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

df = pd.read_csv("practice/data/orders_raw.csv")
amt = pd.to_numeric(df["amount"], errors="coerce").dropna()
sorted_vals = np.unique(amt.to_numpy())  # Lesson 74's guarantee: sorted, deduped

# ---------------------------------------------------------------------------
# Exercise 1 — basic insertion position on the sorted, deduplicated amounts
# ([35.5, 42.0, 99.9, 120.0, 180.0]). Fill in the literal int 100 for the
# query value (not just any placeholder -- checks the literal value itself,
# to avoid a freebie pass).
ex1_query = ...
try:
    ex1_position = int(np.searchsorted(sorted_vals, ex1_query))
except Exception:
    ex1_position = None

# ---------------------------------------------------------------------------
# Exercise 2 — side="left" vs side="right" on an EXACT match (99.9, at index
# 2), and confirming side="right" equals a plain <= boolean-mask count. Fill
# in the literal strings "left" and "right" (not just any placeholder --
# checks the literal values, to avoid a freebie pass).
ex2_side_left = ...
ex2_side_right = ...
try:
    ex2_left_pos = int(np.searchsorted(sorted_vals, 99.9, side=ex2_side_left))
    ex2_right_pos = int(np.searchsorted(sorted_vals, 99.9, side=ex2_side_right))
    ex2_mask_count = int((sorted_vals <= 99.9).sum())
except Exception:
    ex2_left_pos = ex2_right_pos = ex2_mask_count = None

# ---------------------------------------------------------------------------
# Exercise 3 — today's central finding: searchsorted() on the RAW unsorted
# amount column gives a WRONG position, silently, no error -- confirmed to
# differ from the correct sorted-array answer for query value 40. Fill in
# the literal boolean True (not just any truthy placeholder -- a bare
# unfilled "..." is ALSO truthy in Python, so this checks the literal value
# itself, to avoid a freebie pass).
ex3_expect_divergence = ...
try:
    unsorted_vals = amt.to_numpy()  # raw appearance order, NOT sorted
    ex3_unsorted_pos = int(np.searchsorted(unsorted_vals, 40))
    ex3_sorted_pos = int(np.searchsorted(sorted_vals, 40))
    ex3_actually_diverges = ex3_unsorted_pos != ex3_sorted_pos
except Exception:
    ex3_actually_diverges = None

# ---------------------------------------------------------------------------
# Exercise 4 — manual bucketing with bin edges [0, 50, 100, 150, 200], cross-
# checked against pd.cut()'s own bucket codes on the same values. Fill in
# the literal string "right" for the side= keyword used in the bucketing
# formula (not just any placeholder -- checks the literal value, to avoid a
# freebie pass).
bin_edges = np.array([0, 50, 100, 150, 200])
bucket_values = np.array([35.5, 42.0, 99.9, 120.0, 180.0, 50.0])
ex4_side = ...
try:
    ex4_bucket_idx = (np.searchsorted(bin_edges, bucket_values, side=ex4_side) - 1).tolist()
    ex4_cut_codes = pd.cut(bucket_values, bins=bin_edges, right=False, include_lowest=True).codes.tolist()
except Exception:
    ex4_bucket_idx = ex4_cut_codes = None

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
    check("Exercise 1: basic insertion position on sorted, deduplicated amounts",
          lambda: ex1_query == 100 and ex1_position == 3),
    check("Exercise 2: side='left'/'right' split on an exact match, right == <= mask count",
          lambda: ex2_side_left == "left" and ex2_side_right == "right"
          and ex2_left_pos == 2 and ex2_right_pos == 3 and ex2_mask_count == 3),
    check("Exercise 3: unsorted input gives a silently wrong, diverging position",
          lambda: ex3_expect_divergence is True and ex3_actually_diverges is True
          and ex3_unsorted_pos == 2 and ex3_sorted_pos == 1),
    check("Exercise 4: manual bucketing matches pd.cut()'s own bucket codes exactly",
          lambda: ex4_side == "right" and ex4_bucket_idx == ex4_cut_codes == [0, 0, 1, 2, 3, 1]),
]

print("\nAll green — lesson 75 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
