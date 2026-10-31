# Practice 114 — np.average(): the weighted mean pandas' own .mean() can't
#                compute
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/114_np_average.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 2: np.average() with no weights= matches np.mean()
# exactly. weights= changes the formula to sum(value*weight)/sum(weight).
arr = np.array([100.0, 120.0, 50.0, 55.0, 60.0])
weights = np.array([1, 3, 2, 2, 4])

# ex1_plain = np.average(arr)
ex1_plain = ...
# ex1_mean = np.mean(arr)
ex1_mean = ...
# ex1_weighted = np.average(arr, weights=weights)
ex1_weighted = ...
try:
    ex1_plain_matches_mean = bool(ex1_plain == ex1_mean)
    ex1_weighted_ok = round(float(ex1_weighted), 4) == round(
        float((arr * weights).sum() / weights.sum()), 4
    )
    ex1_weighted_differs = bool(ex1_weighted != ex1_plain)
except Exception:
    ex1_plain_matches_mean = False
    ex1_weighted_ok = False
    ex1_weighted_differs = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: groupby().mean() has no weights= parameter at all
# (raises TypeError). The real per-group weighted average path is
# groupby().apply() calling np.average() one group at a time.
orders = pd.DataFrame({
    "customer": ["An", "An", "Binh", "Binh", "Binh"],
    "price": [100.0, 120.0, 50.0, 55.0, 60.0],
    "qty": [1, 3, 2, 2, 4],
})


def groupby_mean_rejects_weights(df):
    # Try df.groupby("customer")["price"].mean(weights=df["qty"]) inside a
    # try/except, and return True if it raised TypeError, False otherwise.
    #   try:
    #       df.groupby("customer")["price"].mean(weights=df["qty"])
    #       return False
    #   except TypeError:
    #       return True
    ...


def groupby_apply_weighted_average(df):
    # Return df.groupby("customer").apply(
    #     lambda g: np.average(g["price"], weights=g["qty"]),
    #     include_groups=False,
    # ) -- a Series with one weighted average per customer.
    #   return df.groupby("customer").apply(
    #       lambda g: np.average(g["price"], weights=g["qty"]),
    #       include_groups=False,
    #   )
    ...


# ex2_rejects_weights = groupby_mean_rejects_weights(orders)
ex2_rejects_weights = ...
# ex2_weighted_series = groupby_apply_weighted_average(orders)
ex2_weighted_series = ...
try:
    ex2_rejects_ok = ex2_rejects_weights is True
    ex2_an_ok = round(float(ex2_weighted_series.loc["An"]), 4) == 115.0
    ex2_binh_ok = round(float(ex2_weighted_series.loc["Binh"]), 4) == 56.25
except Exception:
    ex2_rejects_ok = False
    ex2_an_ok = False
    ex2_binh_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3's callout: np.average() has no skipna concept. One
# NaN in EITHER the values or the weights poisons the whole result to NaN.
vals_with_nan = np.array([10.0, np.nan, 30.0])
clean_vals = np.array([10.0, 20.0, 30.0])
weights_with_nan = np.array([1.0, np.nan, 1.0])
clean_weights = np.array([1.0, 1.0, 1.0])

# ex3_nan_in_values = np.average(vals_with_nan, weights=clean_weights)
ex3_nan_in_values = ...
# ex3_nan_in_weights = np.average(clean_vals, weights=weights_with_nan)
ex3_nan_in_weights = ...
# ex3_all_clean = np.average(clean_vals, weights=clean_weights)
ex3_all_clean = ...
try:
    ex3_values_nan_poisons = bool(np.isnan(ex3_nan_in_values))
    ex3_weights_nan_poisons = bool(np.isnan(ex3_nan_in_weights))
    ex3_clean_is_real = bool(not np.isnan(ex3_all_clean))
except Exception:
    ex3_values_nan_poisons = False
    ex3_weights_nan_poisons = False
    ex3_clean_is_real = False

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
    check("Exercise 1: np.average() with no weights matches np.mean(); weights= changes the formula",
          lambda: ex1_plain_matches_mean is True and ex1_weighted_ok is True
          and ex1_weighted_differs is True),
    check("Exercise 2: groupby().mean() rejects weights=; groupby().apply()+np.average() is the real path",
          lambda: ex2_rejects_ok is True and ex2_an_ok is True and ex2_binh_ok is True),
    check("Exercise 3: a NaN in either values or weights poisons the whole average to NaN",
          lambda: ex3_values_nan_poisons is True and ex3_weights_nan_poisons is True
          and ex3_clean_is_real is True),
]

print("\nAll green — lesson 114 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
