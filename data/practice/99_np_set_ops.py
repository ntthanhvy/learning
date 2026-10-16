# Practice 99 — np.intersect1d() / np.union1d() / np.setdiff1d(): SQL's
# INTERSECT/UNION/EXCEPT, as arrays
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/99_np_set_ops.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: basic intersect1d/union1d/setdiff1d, and confirming
# setdiff1d is NOT symmetric (order of the two arrays changes the result).
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
# ex1_intersect = np.intersect1d(a, b)
ex1_intersect = ...
# ex1_union = np.union1d(a, b)
ex1_union = ...
# ex1_diff_ab = np.setdiff1d(a, b)   -- in a, not in b
ex1_diff_ab = ...
# ex1_diff_ba = np.setdiff1d(b, a)   -- in b, not in a
ex1_diff_ba = ...
try:
    ex1_intersect_ok = bool(np.array_equal(ex1_intersect, np.array([3, 4, 5])))
    ex1_union_ok = bool(np.array_equal(ex1_union, np.array([1, 2, 3, 4, 5, 6, 7])))
    ex1_diff_ab_ok = bool(np.array_equal(ex1_diff_ab, np.array([1, 2])))
    ex1_diff_ba_ok = bool(np.array_equal(ex1_diff_ba, np.array([6, 7])))
    ex1_asymmetric_ok = bool(not np.array_equal(ex1_diff_ab, ex1_diff_ba))
except Exception:
    ex1_intersect_ok = False
    ex1_union_ok = False
    ex1_diff_ab_ok = False
    ex1_diff_ba_ok = False
    ex1_asymmetric_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2: assume_unique=True on non-unique input silently
# returns a WRONG (still-has-duplicates) result; the default stays correct.
dup = np.array([1, 1, 2])
other = np.array([1, 2])
# ex2_correct = np.intersect1d(dup, other)                      -- default, correct
ex2_correct = ...
# ex2_wrong = np.intersect1d(dup, other, assume_unique=True)     -- lies about uniqueness
ex2_wrong = ...
try:
    ex2_correct_ok = bool(np.array_equal(ex2_correct, np.array([1, 2])))
    ex2_wrong_has_dup_ok = bool(len(ex2_wrong) == 3 and list(ex2_wrong).count(1) == 2)
except Exception:
    ex2_correct_ok = False
    ex2_wrong_has_dup_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2: the NaN trap. intersect1d requires NaN == NaN to
# count as shared, and NaN never equals NaN, so two NaN-only arrays never
# intersect. union1d has no such equality-matching requirement and keeps
# a NaN that appears in its input.
nan_a = np.array([np.nan])
nan_b = np.array([np.nan])
# ex3_nan_intersect = np.intersect1d(nan_a, nan_b)   -- empty! NaN != NaN
ex3_nan_intersect = ...
nan_c = np.array([1.0, np.nan, 3.0])
nan_d = np.array([np.nan, 3.0, 4.0])
# ex3_nan_union = np.union1d(nan_c, nan_d)   -- keeps one NaN
ex3_nan_union = ...
try:
    ex3_intersect_empty_ok = bool(len(ex3_nan_intersect) == 0)
    ex3_union_has_nan_ok = bool(np.isnan(ex3_nan_union).sum() == 1)
    ex3_union_len_ok = bool(len(ex3_nan_union) == 4)
except Exception:
    ex3_intersect_empty_ok = False
    ex3_union_has_nan_ok = False
    ex3_union_len_ok = False

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
    check("Exercise 1: intersect1d/union1d/setdiff1d match, and setdiff1d is asymmetric",
          lambda: ex1_intersect_ok is True
          and ex1_union_ok is True
          and ex1_diff_ab_ok is True
          and ex1_diff_ba_ok is True
          and ex1_asymmetric_ok is True),
    check("Exercise 2: assume_unique=True on non-unique input silently keeps duplicates",
          lambda: ex2_correct_ok is True
          and ex2_wrong_has_dup_ok is True),
    check("Exercise 3: intersect1d(NaN, NaN) is empty; union1d keeps exactly one NaN",
          lambda: ex3_intersect_empty_ok is True
          and ex3_union_has_nan_ok is True
          and ex3_union_len_ok is True),
]

print("\nAll green — lesson 99 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
