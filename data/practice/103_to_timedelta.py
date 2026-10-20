# Practice 103 — pd.to_timedelta(): parsing durations, the datetime sibling
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/103_to_timedelta.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1 & 3: a duration string parses to a real
# timedelta64-backed result, usable in arithmetic against a parsed datetime.
order_date = pd.to_datetime("2026-01-01")

# ex1_sla = pd.to_timedelta("3 days")
ex1_sla = ...
# ex1_due = order_date + ex1_sla
ex1_due = ...
try:
    ex1_is_timedelta_ok = bool(isinstance(ex1_sla, pd.Timedelta))
    ex1_due_ok = bool(ex1_due == pd.Timestamp("2026-01-04"))
except Exception:
    ex1_is_timedelta_ok = False
    ex1_due_ok = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 1 & 2: a bare number needs unit= to be meaningful,
# and pairing unit= with a string input raises ValueError instead of
# silently picking one.
ex2_five_hours = ...
# ex2_five_hours = pd.to_timedelta(5, unit="h")


def unit_with_string_raises(value, unit):
    # Call pd.to_timedelta(value, unit=unit) -- value is already a string
    # like "1 day", so pairing it with a numeric unit is a contradiction.
    # Return True if it raises ValueError, False if it succeeds, and let
    # any other exception type propagate.
    # try:
    #     pd.to_timedelta(value, unit=unit)
    #     return False
    # except ValueError:
    #     return True
    ...


# ex2_raised = unit_with_string_raises("1 day", "h")
ex2_raised = ...
try:
    ex2_five_hours_ok = bool(ex2_five_hours == pd.Timedelta(hours=5))
    ex2_raised_ok = bool(ex2_raised is True)
except Exception:
    ex2_five_hours_ok = False
    ex2_raised_ok = False

# ---------------------------------------------------------------------------
# Exercise 3 — Section 2: errors="coerce" turns an unparseable entry into
# NaT while leaving a valid one untouched.
durations = ["1 days", "not-a-duration"]

# ex3_result = pd.to_timedelta(durations, errors="coerce")
ex3_result = ...
try:
    ex3_first_ok = bool(ex3_result[0] == pd.Timedelta(days=1))
    ex3_second_is_nat_ok = bool(pd.isna(ex3_result[1]))
except Exception:
    ex3_first_ok = False
    ex3_second_is_nat_ok = False

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
    check("Exercise 1: a duration string parses to a Timedelta, usable in datetime arithmetic",
          lambda: ex1_is_timedelta_ok is True
          and ex1_due_ok is True),
    check("Exercise 2: unit= works on a bare number but raises ValueError paired with a string",
          lambda: ex2_five_hours_ok is True
          and ex2_raised_ok is True),
    check("Exercise 3: errors=\"coerce\" turns a bad entry into NaT, leaves a valid one alone",
          lambda: ex3_first_ok is True
          and ex3_second_is_nat_ok is True),
]

print("\nAll green — lesson 103 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
