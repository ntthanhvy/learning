# Practice 85 — warnings: flagging trouble without stopping
# Run:  cd ~/learning/python && uv run python3 practice/85_warnings_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import warnings


# ---------------------------------------------------------------------------
# Exercise 1 — warn and keep going.
# Write parse_rate(value) that, if value > 1, calls warnings.warn() with a
# message containing the word "percent" and category UserWarning, then
# divides value by 100. In every case (warned or not) it returns the
# (possibly divided) value.
def parse_rate(value):
    # TODO: if value > 1:
    #           warnings.warn(f"rate {value} looks like a percent", UserWarning)
    #           value = value / 100
    #       return value
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — catch a warning instead of letting it print.
# Write catch_one_warning(func, *args) that runs func(*args) inside a
# warnings.catch_warnings(record=True) block with simplefilter("always"),
# and returns (result, caught) where result is func's return value and
# caught is the list of warnings collected.
def catch_one_warning(func, *args):
    # TODO: with warnings.catch_warnings(record=True) as caught:
    #           warnings.simplefilter("always")
    #           result = func(*args)
    #           return result, caught
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — escalate a warning category into a real exception.
# Write warn_as_error(message) that, inside its own body, calls
# warnings.filterwarnings("error", category=UserWarning) and then
# warnings.warn(message, UserWarning) — and returns the str() of the
# UserWarning raised as a result (catch it with try/except UserWarning).
def warn_as_error(message):
    # TODO: warnings.filterwarnings("error", category=UserWarning)
    #       try:
    #           warnings.warn(message, UserWarning)
    #       except UserWarning as e:
    #           return str(e)
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
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = parse_rate(50)
        warned = len(caught) == 1 and "percent" in str(caught[0].message)
    with warnings.catch_warnings(record=True) as caught2:
        warnings.simplefilter("always")
        result2 = parse_rate(0.5)
        quiet = len(caught2) == 0
    return result == 0.5 and warned and result2 == 0.5 and quiet


def _ex2():
    result, caught = catch_one_warning(parse_rate, 50)
    return (
        result == 0.5
        and len(caught) == 1
        and "percent" in str(caught[0].message)
        and caught[0].category is UserWarning
    )


def _ex3():
    # Reset to a known filter state first so earlier exercises/filters
    # already installed in this process can't mask the "error" filter.
    with warnings.catch_warnings():
        warnings.resetwarnings()
        text = warn_as_error("bad input")
        return text == "bad input"


results = [
    check("Ex 1: warn() fires on a suspicious value but execution continues", _ex1),
    check("Ex 2: catch_warnings(record=True) collects a warning for inspection", _ex2),
    check("Ex 3: filterwarnings('error', ...) turns a warning into a real exception", _ex3),
]
print("\nAll green — lesson 85 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
