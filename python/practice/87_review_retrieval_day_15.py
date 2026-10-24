# Practice 87 — review day 15: retrieval across Days 84-86
# Run:  cd ~/learning/python && uv run python3 practice/87_review_retrieval_day_15.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 84, 85, and 86.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import inspect
import traceback
import warnings


# ---------------------------------------------------------------------------
# Exercise 1 (Day 84 — traceback: capture a bad record's full traceback as a
# str with format_exc(), while a batch keeps processing)
def parse_batch(records):
    """For each item in `records`, try int(item). On success, append it to
    `good`. On a ValueError, append {"record": item, "error": <the full
    traceback text from traceback.format_exc()>} to `bad`. One bad record
    must not stop the rest of the batch from being processed.
    Return (good, bad)."""
    # TODO: good, bad = [], []
    #       for item in records:
    #           try:
    #               good.append(int(item))
    #           except ValueError:
    #               bad.append({"record": item, "error": traceback.format_exc()})
    #       return good, bad
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 85 — warnings: warn on a suspicious value, still return one,
# and catch that warning in-process instead of letting it print)
def parse_rate(value):
    """If value > 1, call warnings.warn() with a message containing the
    word "percent" and category UserWarning, then divide value by 100.
    In every case (warned or not) return the (possibly divided) value."""
    # TODO: if value > 1:
    #           warnings.warn(f"rate {value} looks like a percent", UserWarning)
    #           value = value / 100
    #       return value
    pass


def rate_with_warning_count(value):
    """Call parse_rate(value) inside a warnings.catch_warnings(record=True)
    block with simplefilter("always"), and return (result, count) where
    result is parse_rate's return value and count is how many warnings
    were caught."""
    # TODO: with warnings.catch_warnings(record=True) as caught:
    #           warnings.simplefilter("always")
    #           result = parse_rate(value)
    #           return result, len(caught)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 86 — inspect: read a function's parameter names and
# defaults back out with inspect.signature(), without calling it)
def describe_params(func):
    """Return a dict mapping each of func's parameter names to its default
    value, using inspect.signature(func). A parameter with no declared
    default should map to inspect.Parameter.empty (do not replace it
    with None — that would hide a real difference)."""
    # TODO: sig = inspect.signature(func)
    #       return {name: p.default for name, p in sig.parameters.items()}
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    good, bad = parse_batch(["10", "20", "oops", "40"])
    if good != [10, 20, 40] or len(bad) != 1:
        return False
    text = bad[0]["error"]
    return (
        bad[0]["record"] == "oops"
        and isinstance(text, str)
        and text.strip().splitlines()[-1].startswith("ValueError")
    )


def _ex2():
    only_warns, count_warned = rate_with_warning_count(50)
    quiet, count_quiet = rate_with_warning_count(0.5)
    return only_warns == 0.5 and count_warned == 1 and quiet == 0.5 and count_quiet == 0


def _greet(name, greeting="Hello", *, loud=False):
    return f"{greeting}, {name}!"


def _ex3():
    defaults = describe_params(_greet)
    return (
        defaults.get("name") is inspect.Parameter.empty
        and defaults.get("greeting") == "Hello"
        and defaults.get("loud") is False
    )


results = [
    check("Ex 1 (Day 84): format_exc() captures a bad record's traceback, batch keeps going", _ex1),
    check("Ex 2 (Day 85): warn() fires on a suspicious value and is catchable in-process", _ex2),
    check("Ex 3 (Day 86): signature() reads names/defaults, including Parameter.empty", _ex3),
]

print("\nAll green — lesson 87 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
