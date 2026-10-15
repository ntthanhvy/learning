# Practice 98 — pd.date_range(): building the calendar grid, instead of
# trusting the one you were sent
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/98_date_range.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: a basic start+periods+freq range.
# ex1_range = pd.date_range("2026-03-01", periods=4, freq="D")
ex1_range = ...
try:
    ex1_len_ok = bool(len(ex1_range) == 4)
    ex1_first_ok = bool(ex1_range[0] == pd.Timestamp("2026-03-01"))
    ex1_last_ok = bool(ex1_range[-1] == pd.Timestamp("2026-03-04"))
    ex1_type_ok = bool(isinstance(ex1_range, pd.DatetimeIndex))
except Exception:
    ex1_len_ok = False
    ex1_first_ok = False
    ex1_last_ok = False
    ex1_type_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Sections 1/2: wrong parameter counts and removed freq aliases
# all raise ValueError.
# Call 1: pd.date_range("2026-01-01") -- only 1 of 4 given, should raise.
ex2_underspecified_raised = False
try:
    ...
except ValueError:
    ex2_underspecified_raised = True
except Exception:
    ex2_underspecified_raised = False

# Call 2: pd.date_range("2026-01-01", "2026-01-10", periods=5, freq="D")
# -- all 4 given, should raise.
ex2_overspecified_raised = False
try:
    ...
except ValueError:
    ex2_overspecified_raised = True
except Exception:
    ex2_overspecified_raised = False

# Call 3: pd.date_range("2026-01-01", periods=3, freq="M") -- removed alias,
# should raise ValueError (use "ME" instead).
ex2_old_alias_raised = False
try:
    ...
except ValueError:
    ex2_old_alias_raised = True
except Exception:
    ex2_old_alias_raised = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 3: finding missing days in a sparse time series by
# building the real calendar grid and reindexing onto it.
sparse = pd.Series(
    [10, 20, 30],
    index=pd.to_datetime(["2026-02-01", "2026-02-03", "2026-02-05"]),
)
# ex3_full_grid = pd.date_range(sparse.index.min(), sparse.index.max(), freq="D")
ex3_full_grid = ...
# ex3_filled = sparse.reindex(ex3_full_grid)
ex3_filled = ...
try:
    ex3_grid_len_ok = bool(len(ex3_full_grid) == 5)
    ex3_missing_days = ex3_filled[ex3_filled.isna()].index
    ex3_missing_count_ok = bool(len(ex3_missing_days) == 2)
    ex3_missing_dates_ok = bool(
        set(ex3_missing_days) == {pd.Timestamp("2026-02-02"), pd.Timestamp("2026-02-04")}
    )
except Exception:
    ex3_grid_len_ok = False
    ex3_missing_count_ok = False
    ex3_missing_dates_ok = False

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
    check("Exercise 1: start+periods+freq='D' builds a 4-day DatetimeIndex",
          lambda: ex1_len_ok is True
          and ex1_first_ok is True
          and ex1_last_ok is True
          and ex1_type_ok is True),
    check("Exercise 2: wrong parameter counts and the removed freq='M' alias all raise ValueError",
          lambda: ex2_underspecified_raised is True
          and ex2_overspecified_raised is True
          and ex2_old_alias_raised is True),
    check("Exercise 3: date_range() + reindex() reveal the 2 missing calendar days as NaN",
          lambda: ex3_grid_len_ok is True
          and ex3_missing_count_ok is True
          and ex3_missing_dates_ok is True),
]

print("\nAll green — lesson 98 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
