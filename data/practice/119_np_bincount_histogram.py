# Practice 119 — np.bincount() / np.histogram(): the counting siblings of digitize()
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/119_np_bincount_histogram.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Sections 1-2: np.bincount(codes) tallies each integer code,
# matching value_counts() once reindexed to the same code order. weights=
# switches it from counting occurrences to summing weights per code -- the
# same shape as a groupby().sum(), without pandas.
s = pd.Series(["An", "Binh", "Binh", "Chi", "An", "An"])
codes, uniques = pd.factorize(s)
weights = np.array([10.0, 20.0, 5.0, 1.0, 2.0, 3.0])


def code_tally(c):
    # Return np.bincount(c) -- one count per distinct code value.
    #   return np.bincount(c)
    ...


def weighted_tally(c, w):
    # Return np.bincount(c, weights=w) -- sum of weights per code, not a count.
    #   return np.bincount(c, weights=w)
    ...


# ex1_tally = code_tally(codes)
ex1_tally = ...
# ex1_weighted = weighted_tally(codes, weights)
ex1_weighted = ...
try:
    ex1_tally_ok = list(ex1_tally) == [3, 2, 1]
    vc_reindexed = s.value_counts().reindex(uniques).to_numpy()
    ex1_matches_value_counts = list(ex1_tally) == list(vc_reindexed)
    ex1_weighted_ok = list(ex1_weighted) == [15.0, 25.0, 1.0]
except Exception:
    ex1_tally_ok = False
    ex1_matches_value_counts = False
    ex1_weighted_ok = False

try:
    # bincount() rejects float input loudly -- never a silent coercion.
    np.bincount(np.array([1.5, 2.0]))
    ex1_float_raises = False
except TypeError:
    ex1_float_raises = True
except Exception:
    ex1_float_raises = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: np.histogram(x, bins=bins) returns per-bin COUNTS
# directly. Confirmed: bincount(digitize(x, bins) - 1, minlength=len(bins)-1)
# reproduces those same counts exactly -- histogram() chains yesterday's two
# functions together, skipping the manual per-value index step.
amounts = np.array([120.0, 35.5, 180.0, 42.0, 40.0])
bins = [0, 40, 100, 200]


def histogram_counts(x):
    # Return only the counts array from np.histogram(x, bins=bins) (ignore edges).
    #   counts, _ = np.histogram(x, bins=bins)
    #   return counts
    ...


def chained_equivalent(x):
    # Return np.bincount(np.digitize(x, bins) - 1, minlength=len(bins) - 1).
    #   return np.bincount(np.digitize(x, bins) - 1, minlength=len(bins) - 1)
    ...


# ex2_histogram = histogram_counts(amounts)
ex2_histogram = ...
# ex2_chained = chained_equivalent(amounts)
ex2_chained = ...
try:
    ex2_histogram_ok = list(ex2_histogram) == [1, 2, 2]
    ex2_matches_chain = list(ex2_histogram) == list(ex2_chained)
except Exception:
    ex2_histogram_ok = False
    ex2_matches_chain = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 4: any out-of-range value (NaN included, since every
# comparison against it is False) is silently dropped from every bin count --
# no exception, no warning, and the counts sum to less than len(x). pd.cut()
# correctly surfaces the missing count as its own NaN row instead.
vals_with_nan = np.array([np.nan, 50.0, 120.0])


def histogram_with_nan(x):
    # Return only the counts array from np.histogram(x, bins=bins) (ignore edges).
    #   counts, _ = np.histogram(x, bins=bins)
    #   return counts
    ...


def cut_value_counts_with_nan(x):
    # Return pd.cut(pd.Series(x), bins=bins).value_counts(dropna=False) -- NaN gets its own row.
    #   return pd.cut(pd.Series(x), bins=bins).value_counts(dropna=False)
    ...


# ex3_hist_nan = histogram_with_nan(vals_with_nan)
ex3_hist_nan = ...
# ex3_cut_vc = cut_value_counts_with_nan(vals_with_nan)
ex3_cut_vc = ...
try:
    ex3_hist_short = int(ex3_hist_nan.sum()) == 2 and len(vals_with_nan) == 3
    ex3_cut_has_nan_row = bool(ex3_cut_vc.get(np.nan, 0) == 1)
except Exception:
    ex3_hist_short = False
    ex3_cut_has_nan_row = False

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
    check("Exercise 1: bincount() tallies codes like value_counts(); weights= sums like groupby().sum(); float input raises TypeError",
          lambda: ex1_tally_ok is True and ex1_matches_value_counts is True
          and ex1_weighted_ok is True and ex1_float_raises is True),
    check("Exercise 2: histogram()'s counts equal bincount(digitize(x, bins) - 1, minlength=len(bins) - 1)",
          lambda: ex2_histogram_ok is True and ex2_matches_chain is True),
    check("Exercise 3: histogram() silently drops NaN (count falls short); pd.cut().value_counts(dropna=False) keeps it as its own row",
          lambda: ex3_hist_short is True and ex3_cut_has_nan_row is True),
]

print("\nAll green — lesson 119 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
