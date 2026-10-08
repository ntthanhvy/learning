# Practice 71 — review day 11: retrieval across Days 68-70
# Run:  cd ~/learning/python && uv run python3 practice/71_review_retrieval_day_11.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 68, 69, and 70.
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓. Try each from memory before reopening the old lesson.

import statistics
import subprocess
from decimal import Decimal


# ---------------------------------------------------------------------------
# Exercise 1 (Day 68 — subprocess: argument list, not shell=True; check the
# result by hand, then let check=True raise CalledProcessError on failure)
def run_ok(args):
    """Run `args` (a list of strings) and return its captured stdout as text.
    Use the argument-list form (never shell=True) and capture_output=True,
    text=True."""
    # TODO: result = subprocess.run(args, capture_output=True, text=True)
    #       return result.stdout
    ...


def run_and_report_failure(args):
    """Run `args` with check=True. If the command fails, catch the raised
    CalledProcessError and return its .returncode. If it succeeds, return 0."""
    # TODO: try:
    #           subprocess.run(args, check=True, capture_output=True, text=True)
    #           return 0
    #       except subprocess.CalledProcessError as e:
    #           return e.returncode
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 69 — statistics: mean() is pulled by outliers, median()
# mostly isn't; stdev() measures spread that mean() alone hides)
def mean_and_median(amounts):
    """Return (mean, median) of `amounts` as a tuple, via statistics.mean()
    and statistics.median()."""
    # TODO: return statistics.mean(amounts), statistics.median(amounts)
    ...


def stdev_of(amounts):
    """Return the sample standard deviation of `amounts` via statistics.stdev()."""
    # TODO: return statistics.stdev(amounts)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 70 — decimal: build Decimal from strings, never floats, to
# sum a list of prices exactly instead of letting float sums drift)
def sum_prices_exactly(raw_prices):
    """raw_prices is a list of price strings, e.g. ["19.99", "0.10"]. Return
    their exact sum as a Decimal, built from the strings directly."""
    # TODO: return sum(Decimal(p) for p in raw_prices)
    ...


def float_sum_drifts(raw_prices):
    """Return True if summing raw_prices as plain floats does NOT exactly
    equal summing them as Decimals (i.e. float drift is detectable).
    Compare via Decimal(float_total), not float(decimal_total) -- rounding
    a Decimal back to float can mask the drift that converting the float's
    own exact binary value to Decimal reveals."""
    # TODO: float_total = sum(float(p) for p in raw_prices)
    #       return Decimal(float_total) != sum_prices_exactly(raw_prices)
    ...


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_captures_stdout_via_argument_list():
    out = run_ok(["echo", "hello", "world"])
    return out is not None and out.strip() == "hello world"


def _ex1_check_true_reports_failure_returncode():
    rc = run_and_report_failure(["ls", "/no/such/path/at/all"])
    return isinstance(rc, int) and rc != 0


def _ex1_check_true_reports_zero_on_success():
    rc = run_and_report_failure(["echo", "ok"])
    return rc == 0


def _ex2_mean_pulled_by_outlier_median_is_not():
    amounts = [20, 25, 22, 21, 500]
    mean, median = mean_and_median(amounts)
    return mean > 100 and median == 22


def _ex2_stdev_differs_for_same_mean_lists():
    tight = [48, 50, 52, 49, 51]
    spread = [10, 90, 50, 95, 5]
    return (
        statistics.mean(tight) == statistics.mean(spread)
        and stdev_of(tight) < 5
        and stdev_of(spread) > 30
    )


def _ex3_decimal_sum_is_exact():
    raw_prices = ["19.99", "5.01", "3.33", "0.10", "0.10", "0.10"]
    return sum_prices_exactly(raw_prices) == Decimal("28.63")


def _ex3_float_sum_drift_is_detected():
    raw_prices = ["19.99", "5.01", "3.33", "0.10", "0.10", "0.10"]
    return float_sum_drifts(raw_prices) is True


results = [
    check("Ex 1: subprocess.run() with an argument list captures stdout",
          _ex1_captures_stdout_via_argument_list),
    check("Ex 1: check=True surfaces a nonzero returncode via CalledProcessError",
          _ex1_check_true_reports_failure_returncode),
    check("Ex 1: check=True reports 0 when the command actually succeeds",
          _ex1_check_true_reports_zero_on_success),
    check("Ex 2: mean() is pulled by an outlier while median() mostly ignores it",
          _ex2_mean_pulled_by_outlier_median_is_not),
    check("Ex 2: two same-mean lists can still have very different stdev()",
          _ex2_stdev_differs_for_same_mean_lists),
    check("Ex 3: summing price strings with Decimal gives an exact total",
          _ex3_decimal_sum_is_exact),
    check("Ex 3: the equivalent float sum visibly drifts from that exact total",
          _ex3_float_sum_drift_is_detected),
]

print("\nAll green — lesson 71 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
