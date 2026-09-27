# Practice 81 — pd.to_datetime(format=): stop guessing, start declaring
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/81_to_datetime_format.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# An ambiguous, slash-separated date column: is "01/02/2026" 1 Feb or 2 Jan?
ambiguous = pd.Series(["01/02/2026", "03/04/2026"])

# ---------------------------------------------------------------------------
# Exercise 1 — parse `ambiguous` with NO format= given at all, and confirm
# pandas silently defaults to US-style MONTH-FIRST parsing (Section 1).
# ex1_default = pd.to_datetime(ambiguous)
try:
    ex1_default = pd.to_datetime(...)
    ex1_first_month = ex1_default.iloc[0].month
    ex1_first_day = ex1_default.iloc[0].day
except Exception:
    ex1_first_month = ex1_first_day = None

# ---------------------------------------------------------------------------
# Exercise 2 — parse the SAME `ambiguous` Series again, this time passing the
# correct day-first format explicitly, and confirm the reading flips to
# DAY-FIRST (Section 2). Fill in the format string itself.
# ex2_format = "%d/%m/%Y"
try:
    ex2_format = ...
    ex2_explicit = pd.to_datetime(ambiguous, format=ex2_format)
    ex2_first_month = ex2_explicit.iloc[0].month
    ex2_first_day = ex2_explicit.iloc[0].day
except Exception:
    ex2_first_month = ex2_first_day = None

# ---------------------------------------------------------------------------
# Exercise 3 — a mismatched format= raises ValueError by default; combined
# with errors="coerce" it turns EVERY non-matching row into NaT, including a
# genuinely valid date that just doesn't match the declared pattern. Fill in
# the errors= value that turns the crash into NaT instead (Section 3).
# ex3_errors_value = "coerce"
mismatched = pd.Series(["2026-01-05", "not-a-date"])
ex3_raised_without_coerce = False
try:
    pd.to_datetime(mismatched, format="%d/%m/%Y")
except ValueError:
    ex3_raised_without_coerce = True
except Exception:
    ex3_raised_without_coerce = False

try:
    ex3_errors_value = ...
    ex3_coerced = pd.to_datetime(mismatched, format="%d/%m/%Y", errors=ex3_errors_value)
    ex3_all_nat = bool(ex3_coerced.isna().all())
except Exception:
    ex3_all_nat = None

# ---------------------------------------------------------------------------
# Exercise 4 — a genuinely mixed-format column (one row YYYY-MM-DD, one row
# DD/MM/YYYY) needs format="mixed" instead of one fixed pattern. Fill in that
# value so both rows parse without raising (Section 3).
# ex4_format_value = "mixed"
mixed = pd.Series(["2026-01-05", "06/01/2026"])
try:
    ex4_format_value = ...
    ex4_parsed = pd.to_datetime(mixed, format=ex4_format_value)
    ex4_no_nat = bool(ex4_parsed.notna().all())
except Exception:
    ex4_no_nat = None

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
    check("Exercise 1: no format= given defaults to month-first (Jan 2nd, not Feb 1st)",
          lambda: ex1_first_month == 1 and ex1_first_day == 2),
    check("Exercise 2: explicit day-first format= flips the reading to Feb 1st",
          lambda: ex2_format == "%d/%m/%Y"
          and ex2_first_month == 2 and ex2_first_day == 1),
    check("Exercise 3: mismatched format= raises ValueError alone, NaT-everywhere under errors=",
          lambda: ex3_raised_without_coerce is True
          and ex3_errors_value == "coerce" and ex3_all_nat is True),
    check("Exercise 4: format=\"mixed\" parses a genuinely mixed-format column without raising",
          lambda: ex4_format_value == "mixed" and ex4_no_nat is True),
]

print("\nAll green — lesson 81 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
