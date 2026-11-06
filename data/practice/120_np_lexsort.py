# Practice 120 — np.lexsort(): multi-key sort positions, keys passed in a backwards-looking order
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/120_np_lexsort.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 2: the LAST key in the tuple passed to np.lexsort() is
# the PRIMARY sort key, ties broken by the second-to-last key, and so on --
# backwards from the intuitive left-to-right reading. Confirmed to match
# sort_values(by=["last_name", "first_name"]) exactly once the tuple order
# is reversed (primary key last).
last_name = np.array(["Tran", "Tran", "Le", "Le"])
first_name = np.array(["Binh", "An", "Chi", "An"])
df = pd.DataFrame({"last_name": last_name, "first_name": first_name})


def lexsort_by_last_then_first(last, first):
    # Return np.lexsort((first, last)) -- last_name PRIMARY, first_name tiebreak.
    #   return np.lexsort((first, last))
    ...


def sort_values_by_last_then_first(frame):
    # Return frame.sort_values(by=["last_name", "first_name"]).index.to_numpy().
    #   return frame.sort_values(by=["last_name", "first_name"]).index.to_numpy()
    ...


# ex1_lexsort = lexsort_by_last_then_first(last_name, first_name)
ex1_lexsort = ...
# ex1_sort_values = sort_values_by_last_then_first(df)
ex1_sort_values = ...
try:
    ex1_matches = list(ex1_lexsort) == list(ex1_sort_values)
    ex1_correct_order = list(ex1_lexsort) == [3, 2, 1, 0]
except Exception:
    ex1_matches = False
    ex1_correct_order = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: a single key wrapped in a one-element tuple,
# np.lexsort((x,)), is byte-identical to plain np.argsort(x) -- lexsort() is
# a strict generalization of argsort() to multiple keys, not a different
# algorithm.
x = np.array([30.0, 10.0, 20.0])


def lexsort_single_key(arr):
    # Return np.lexsort((arr,)) -- note the trailing comma, a 1-element tuple.
    #   return np.lexsort((arr,))
    ...


def argsort_same_key(arr):
    # Return np.argsort(arr).
    #   return np.argsort(arr)
    ...


# ex2_lexsort = lexsort_single_key(x)
ex2_lexsort = ...
# ex2_argsort = argsort_same_key(x)
ex2_argsort = ...
try:
    ex2_matches = list(ex2_lexsort) == list(ex2_argsort)
    ex2_correct_order = list(ex2_lexsort) == [1, 2, 0]
except Exception:
    ex2_matches = False
    ex2_correct_order = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 5: a NaN in any key sorts to the end of that key's
# order, confirmed identical to sort_values()'s own default NaN placement --
# not an undocumented trap the way digitize()/histogram() turned out to be.
primary = np.array([1.0, np.nan, 1.0, np.nan, 2.0])
secondary = np.array([5, 1, 3, 9, 0])
nan_df = pd.DataFrame({"primary": primary, "secondary": secondary})


def lexsort_with_nan(p, s):
    # Return np.lexsort((s, p)) -- primary PRIMARY key, secondary tiebreak.
    #   return np.lexsort((s, p))
    ...


def sort_values_with_nan(frame):
    # Return frame.sort_values(by=["primary", "secondary"]).index.to_numpy().
    #   return frame.sort_values(by=["primary", "secondary"]).index.to_numpy()
    ...


# ex3_lexsort = lexsort_with_nan(primary, secondary)
ex3_lexsort = ...
# ex3_sort_values = sort_values_with_nan(nan_df)
ex3_sort_values = ...
try:
    ex3_matches = list(ex3_lexsort) == list(ex3_sort_values)
    ex3_nan_last = list(ex3_lexsort)[-2:] == [1, 3] or list(ex3_lexsort)[-2:] == [3, 1]
except Exception:
    ex3_matches = False
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
    check("Exercise 1: np.lexsort((first, last)) sorts by the LAST tuple item first -- matches sort_values(by=[last, first]) exactly",
          lambda: ex1_matches is True and ex1_correct_order is True),
    check("Exercise 2: np.lexsort((x,)) on a single key is identical to np.argsort(x)",
          lambda: ex2_matches is True and ex2_correct_order is True),
    check("Exercise 3: np.lexsort() sorts NaN to the end, matching sort_values()'s own NaN placement exactly",
          lambda: ex3_matches is True and ex3_nan_last is True),
]

print("\nAll green — lesson 120 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
