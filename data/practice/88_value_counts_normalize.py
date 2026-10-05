# Practice 88 — value_counts(normalize=True): percentages and the dropna= trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/88_value_counts_normalize.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — basic normalize=True: proportions instead of raw counts
# (Section 1). Fill in the keyword value to pass.
# ex1_normalize_value = True
ex1_normalize_value = ...
try:
    ex1_value_is_real_true = ex1_normalize_value is True
    ex1_series = pd.Series(["North", "North", "North", "South", "South"])
    ex1_result = ex1_series.value_counts(normalize=ex1_normalize_value)
    ex1_north = round(float(ex1_result["North"]), 2)
    ex1_south = round(float(ex1_result["South"]), 2)
    ex1_sum = round(float(ex1_result.sum()), 6)
except Exception:
    ex1_value_is_real_true = False
    ex1_north = None
    ex1_south = None
    ex1_sum = None

# ---------------------------------------------------------------------------
# Exercise 2 — the Section 2 trap: with a real missing value present, the
# default dropna=True computes proportions over the non-null rows only, so
# it gives a DIFFERENT answer than dropna=False. Fill in the dropna value
# that includes the missing value in the denominator.
# ex2_dropna_value = False
ex2_dropna_value = ...
try:
    ex2_value_is_real_false = ex2_dropna_value is False
    ex2_series = pd.Series(["North", "South", "North", "North", "South", None])
    # 6 rows total, 1 missing
    ex2_default = ex2_series.value_counts(normalize=True)  # dropna=True default
    ex2_explicit = ex2_series.value_counts(normalize=True, dropna=ex2_dropna_value)

    ex2_default_north = round(float(ex2_default["North"]), 4)
    ex2_explicit_north = round(float(ex2_explicit["North"]), 4)
    ex2_default_sum = round(float(ex2_default.sum()), 6)
    ex2_explicit_sum = round(float(ex2_explicit.sum()), 6)
    ex2_explicit_has_more_rows = len(ex2_explicit) > len(ex2_default)
    ex2_different_north_pct = ex2_default_north != ex2_explicit_north
except Exception:
    ex2_value_is_real_false = False
    ex2_default_north = None
    ex2_explicit_north = None
    ex2_default_sum = None
    ex2_explicit_sum = None
    ex2_explicit_has_more_rows = None
    ex2_different_north_pct = None

# ---------------------------------------------------------------------------
# Exercise 3 — per-group normalize (Section 3): groupby(...)[col].value_counts
# (normalize=True) normalizes WITHIN each group, so each group's own
# proportions sum to 1.0 independently. Fill in the grouping column name.
# ex3_group_col = "customer"
ex3_group_col = ...
try:
    ex3_df = pd.DataFrame({
        "customer": ["An", "An", "An", "Binh", "Binh"],
        "region": ["North", "North", "South", "North", "South"],
    })
    ex3_result = ex3_df.groupby(ex3_group_col)["region"].value_counts(normalize=True)
    ex3_an_north = round(float(ex3_result.loc["An", "North"]), 4)
    ex3_an_sum = round(float(ex3_result.loc["An"].sum()), 6)
    ex3_binh_sum = round(float(ex3_result.loc["Binh"].sum()), 6)
except Exception:
    ex3_an_north = None
    ex3_an_sum = None
    ex3_binh_sum = None

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
    check("Exercise 1: value_counts(normalize=True) gives proportions summing to 1.0",
          lambda: ex1_value_is_real_true is True
          and ex1_north == 0.6 and ex1_south == 0.4 and ex1_sum == 1.0),
    check("Exercise 2: dropna=False changes the denominator and the reported percentage",
          lambda: ex2_value_is_real_false is True
          and ex2_default_sum == 1.0 and ex2_explicit_sum == 1.0
          and ex2_explicit_has_more_rows is True
          and ex2_default_north == 0.6
          and ex2_different_north_pct is True),
    check("Exercise 3: groupby(...).value_counts(normalize=True) sums to 1.0 PER group",
          lambda: ex3_an_north == 0.6667 and ex3_an_sum == 1.0 and ex3_binh_sum == 1.0),
]

print("\nAll green — lesson 88 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
