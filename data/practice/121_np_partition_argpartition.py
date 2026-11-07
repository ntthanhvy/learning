# Practice 121 — np.partition() / np.argpartition(): the fast "top N" primitive under nlargest()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/121_np_partition_argpartition.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 2: np.partition(x, k) only guarantees the value at
# index k equals the true kth-smallest (matches np.sort(x)[k] exactly), with
# everything left <= it and everything right >= it -- but confirmed directly
# that neither side ends up internally sorted on a big-enough array.
rng = np.random.default_rng(42)
big = rng.integers(0, 100_000, size=2000)
k = 500


def partition_at_k(arr, kth):
    # Return np.partition(arr, kth).
    #   return np.partition(arr, kth)
    ...


ex1_part = partition_at_k(big, k)
ex1_sorted = np.sort(big)
try:
    ex1_pivot_matches = bool(ex1_part[k] == ex1_sorted[k])
    ex1_left_ok = bool(np.all(ex1_part[:k] <= ex1_part[k]))
    ex1_right_ok = bool(np.all(ex1_part[k + 1:] >= ex1_part[k]))
    ex1_left_unsorted = list(ex1_part[:k]) != sorted(ex1_part[:k].tolist())
except Exception:
    ex1_pivot_matches = False
    ex1_left_ok = False
    ex1_right_ok = False
    ex1_left_unsorted = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: np.argpartition(arr, -N)[-N:] gives the indices of
# the N largest values (unordered among themselves) without a full sort.
# Confirmed to match the same SET of values as pandas' Series.nlargest(N).
vals = rng.integers(0, 1000, size=30)
ser = pd.Series(vals)
N = 5


def top_n_indices(arr, n):
    # Return np.argpartition(arr, -n)[-n:] -- indices of the n largest values.
    #   return np.argpartition(arr, -n)[-n:]
    ...


ex2_idx = top_n_indices(vals, N)
try:
    ex2_values = set(vals[ex2_idx].tolist())
    ex2_expected = set(ser.nlargest(N).tolist())
    ex2_matches_nlargest = ex2_values == ex2_expected
    ex2_right_count = len(ex2_idx) == N
except Exception:
    ex2_matches_nlargest = False
    ex2_right_count = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 4: a NaN in the input sorts to the very end of
# np.partition()'s output, byte-identical to where plain np.sort() places
# it -- not a separate undocumented trap this time, both already agree.
xn = np.array([5.0, np.nan, 1.0, 3.0, np.nan, 2.0])


def partition_with_nan(arr, kth):
    # Return np.partition(arr, kth).
    #   return np.partition(arr, kth)
    ...


ex3_part = partition_with_nan(xn, 2)
ex3_sorted = np.sort(xn)
try:
    ex3_non_nan_matches = np.array_equal(ex3_part[:4], ex3_sorted[:4])
    ex3_nan_last = bool(np.isnan(ex3_part[-1])) and bool(np.isnan(ex3_part[-2]))
except Exception:
    ex3_non_nan_matches = False
    ex3_nan_last = False

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
    check("Exercise 1: np.partition() gets the pivot exact at index k, but leaves both sides internally unsorted",
          lambda: ex1_pivot_matches is True and ex1_left_ok is True and ex1_right_ok is True and ex1_left_unsorted is True),
    check("Exercise 2: np.argpartition(arr, -N)[-N:] finds the same SET of top-N values as Series.nlargest(N)",
          lambda: ex2_matches_nlargest is True and ex2_right_count is True),
    check("Exercise 3: np.partition() sorts NaN to the very end, matching np.sort()'s own NaN placement exactly",
          lambda: ex3_non_nan_matches is True and ex3_nan_last is True),
]

print("\nAll green — lesson 121 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
