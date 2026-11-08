# Practice 122 — np.isin(): the array primitive under Series.isin(), and two traps it doesn't share
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/122_np_isin.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: np.isin(arr, candidates) returns a True/False mask,
# element-for-element identical to Series.isin(candidates) on the same data --
# confirmed directly (numpy 2.5.4) on this course's customer column.
customer = np.array(["An", "Chi", "Binh", "An"])
candidates = ["An", "Chi"]
ser = pd.Series(customer)


def isin_mask(arr, cands):
    # Return np.isin(arr, cands).
    #   return np.isin(arr, cands)
    ...


ex1_np_mask = isin_mask(customer, candidates)
try:
    ex1_matches_series = np.array_equal(ex1_np_mask, ser.isin(candidates).to_numpy())
    ex1_correct = ex1_np_mask.tolist() == [True, True, False, True]
except Exception:
    ex1_matches_series = False
    ex1_correct = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 2 (the bare-scalar trap): Series.isin("An") raises
# TypeError on current pandas (Lesson 29's confirmed guard). np.isin(arr, "An")
# does NOT raise -- confirmed directly it treats "An" as one scalar candidate
# and matches it exactly, with no character-by-character iteration either.
small = np.array(["An", "Chi"])


def isin_bare_string(arr, scalar):
    # Return np.isin(arr, scalar) -- a bare string, not wrapped in a list.
    #   return np.isin(arr, scalar)
    ...


def series_isin_raises(ser_, scalar):
    # Call ser_.isin(scalar) inside try/except TypeError; return True if it
    # raised TypeError, False otherwise.
    #   try:
    #       ser_.isin(scalar)
    #       return False
    #   except TypeError:
    #       return True
    ...


ex2_np_result = isin_bare_string(small, "An")
ex2_series_raised = series_isin_raises(pd.Series(small), "An")
try:
    ex2_np_no_raise_correct = ex2_np_result.tolist() == [True, False]
    ex2_series_raised_correct = ex2_series_raised is True
except Exception:
    ex2_np_no_raise_correct = False
    ex2_series_raised_correct = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3 (the NaN trap): Series.isin([np.nan]) matches NaN
# rows to each other (pandas treats missing values as matching for membership
# purposes). np.isin(arr, [np.nan]) does NOT -- confirmed directly it uses
# plain float equality, and NaN != NaN under IEEE rules, so no row matches at
# all. Confirmed absent from the official numpy.isin() docs.
xn = np.array([1.0, np.nan, 3.0, np.nan])
nan_candidates = [np.nan, 3.0]


def np_isin_nan(arr, cands):
    # Return np.isin(arr, cands).
    #   return np.isin(arr, cands)
    ...


def series_isin_nan(arr, cands):
    # Return pd.Series(arr).isin(cands).to_numpy().
    #   return pd.Series(arr).isin(cands).to_numpy()
    ...


ex3_np_result = np_isin_nan(xn, nan_candidates)
ex3_series_result = series_isin_nan(xn, nan_candidates)
try:
    ex3_np_correct = ex3_np_result.tolist() == [False, False, True, False]
    ex3_series_correct = ex3_series_result.tolist() == [False, True, True, True]
    ex3_they_disagree = ex3_np_result.tolist() != ex3_series_result.tolist()
except Exception:
    ex3_np_correct = False
    ex3_series_correct = False
    ex3_they_disagree = False

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
    check("Exercise 1: np.isin(arr, candidates) matches Series.isin(candidates) element-for-element",
          lambda: ex1_matches_series is True and ex1_correct is True),
    check("Exercise 2: np.isin() accepts a bare string as one scalar candidate; Series.isin() raises TypeError on the same input",
          lambda: ex2_np_no_raise_correct is True and ex2_series_raised_correct is True),
    check("Exercise 3: Series.isin() matches NaN-to-NaN, but np.isin() does not -- plain float equality, NaN != NaN",
          lambda: ex3_np_correct is True and ex3_series_correct is True and ex3_they_disagree is True),
]

print("\nAll green — lesson 122 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
