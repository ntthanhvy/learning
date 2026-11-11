# Practice 105 — locale: formatting numbers the way a reader expects
# Run:  cd ~/learning/python && uv run python3 practice/105_locale_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import locale

# Set up a known locale once for every exercise below. en_US.UTF-8 is used
# because it's confirmed available in this course's own environment; a real
# deployment should check with `locale -a` (shell) rather than assume.
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


# ---------------------------------------------------------------------------
# Exercise 1 — read back the active locale after setting it.
# Return the result of locale.getlocale() — a tuple like ('en_US', 'UTF-8').
def current_locale():
    # TODO: return locale.getlocale()
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — group a large integer with thousands separators.
# Given an int, return it as a string with thousands grouping applied
# (hint: locale.format_string("%d", n, grouping=True)).
def grouped_int(n):
    # TODO: return locale.format_string("%d", n, grouping=True)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — format a number as currency.
# Given a float, return it formatted as currency with thousands grouping
# (hint: locale.currency(amount, grouping=True)).
def as_currency(amount):
    # TODO: return locale.currency(amount, grouping=True)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — parse a locale-grouped number string back to a float.
# Given a string like "12,345,678.9", return it parsed as a float with the
# thousands separator correctly stripped (hint: locale.atof(text)).
def parse_grouped_float(text):
    # TODO: return locale.atof(text)
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


def _ex1():
    result = current_locale()
    return isinstance(result, tuple) and result[0] == "en_US"


def _ex2():
    return grouped_int(1234567) == "1,234,567"


def _ex3():
    return as_currency(1234567.5) == "$1,234,567.50"


def _ex4():
    return parse_grouped_float("12,345,678.9") == 12345678.9


results = [
    check("Ex 1: current_locale() reports the active en_US locale", _ex1),
    check("Ex 2: grouped_int() inserts thousands separators", _ex2),
    check("Ex 3: as_currency() formats with symbol and grouping", _ex3),
    check("Ex 4: parse_grouped_float() strips the thousands separator", _ex4),
]
print("\nAll green — lesson 105 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
