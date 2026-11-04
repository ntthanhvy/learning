# Practice 118 — np.digitize(): the raw-array layer under cut() and qcut()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/118_np_digitize.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1-2: np.digitize(x, bins) returns one bin index per
# value, no labels attached. np.digitize(x, bins) - 1 matches
# pd.cut(x, bins=bins, labels=False) exactly, on every in-range value.
amounts = np.array([120.0, 35.5, 180.0, 42.0])
bins = [0, 40, 100, 200]


def raw_bin_indices(x):
    # Return np.digitize(x, bins) -- one bin index per value.
    #   return np.digitize(x, bins)
    ...


def matches_cut_labels(x):
    # Return np.digitize(x, bins) - 1 -- should equal pd.cut(..., labels=False).
    #   return np.digitize(x, bins) - 1
    ...


# ex1_digitize = raw_bin_indices(amounts)
ex1_digitize = ...
# ex1_minus_one = matches_cut_labels(amounts)
ex1_minus_one = ...
try:
    ex1_digitize_ok = list(ex1_digitize) == [3, 1, 3, 2]
    cut_labels = pd.cut(pd.Series(amounts), bins=bins, labels=False)
    ex1_matches_cut = list(ex1_minus_one) == list(cut_labels)
except Exception:
    ex1_digitize_ok = False
    ex1_matches_cut = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: right=False (default) treats each bin as
# bins[i-1] <= x < bins[i] -- an exact edge value joins the bin STARTING
# there. right=True flips to bins[i-1] < x <= bins[i] -- the edge value
# joins the bin ENDING there instead.
edge_value = np.array([40.0])


def edge_default_right_false(x):
    # Return np.digitize(x, bins) -- default right=False.
    #   return np.digitize(x, bins)
    ...


def edge_with_right_true(x):
    # Return np.digitize(x, bins, right=True) -- flips which side is inclusive.
    #   return np.digitize(x, bins, right=True)
    ...


# ex2_default = edge_default_right_false(edge_value)
ex2_default = ...
# ex2_right_true = edge_with_right_true(edge_value)
ex2_right_true = ...
try:
    ex2_default_ok = list(ex2_default) == [2]
    ex2_right_true_ok = list(ex2_right_true) == [1]
except Exception:
    ex2_default_ok = False
    ex2_right_true_ok = False

try:
    # Non-monotonic bins must raise ValueError immediately.
    np.digitize(amounts, [100, 0, 200, 40])
    ex2_nonmonotonic_raises = False
except ValueError:
    ex2_nonmonotonic_raises = True
except Exception:
    ex2_nonmonotonic_raises = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 4: a NaN value fails every comparison against every
# bin edge, so np.digitize() silently drops it into the final catch-all
# bucket (index len(bins)) -- the same code a genuinely huge value gets, no
# warning at all. pd.cut(), built on top, correctly keeps it as NaN instead.
vals_with_nan = np.array([np.nan, 50.0])


def digitize_with_nan(x):
    # Return np.digitize(x, bins) -- NaN silently lands in bin len(bins).
    #   return np.digitize(x, bins)
    ...


def cut_with_nan(x):
    # Return pd.cut(pd.Series(x), bins=bins, labels=False) -- NaN stays NaN.
    #   return pd.cut(pd.Series(x), bins=bins, labels=False)
    ...


# ex3_digitize_nan = digitize_with_nan(vals_with_nan)
ex3_digitize_nan = ...
# ex3_cut_nan = cut_with_nan(vals_with_nan)
ex3_cut_nan = ...
try:
    ex3_digitize_fake_bin = list(ex3_digitize_nan) == [len(bins), 2]
    ex3_cut_real_nan = bool(pd.isna(ex3_cut_nan.iloc[0])) and bool(ex3_cut_nan.iloc[1] == 1)
except Exception:
    ex3_digitize_fake_bin = False
    ex3_cut_real_nan = False

# np.digitize() accepts a Series directly and always returns a plain ndarray.
s = pd.Series(amounts, index=["An", "Binh", "Binh2", "An2"])
try:
    ex3_series_result = np.digitize(s, bins)
    ex3_series_is_ndarray = isinstance(ex3_series_result, np.ndarray)
except Exception:
    ex3_series_is_ndarray = False

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
    check("Exercise 1: np.digitize() gives raw bin indices; minus 1 matches pd.cut(labels=False)",
          lambda: ex1_digitize_ok is True and ex1_matches_cut is True),
    check("Exercise 2: right=False/True flip which side of an exact edge is inclusive; bad bins raise ValueError",
          lambda: ex2_default_ok is True and ex2_right_true_ok is True
          and ex2_nonmonotonic_raises is True),
    check("Exercise 3: NaN silently lands in the last bin for digitize(); pd.cut() correctly keeps it as NaN",
          lambda: ex3_digitize_fake_bin is True and ex3_cut_real_nan is True
          and ex3_series_is_ndarray is True),
]

print("\nAll green — lesson 118 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
