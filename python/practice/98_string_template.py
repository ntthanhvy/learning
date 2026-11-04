# Practice 98 — string.Template: substitution without evaluation
# Run:  cd ~/learning/python && uv run python3 practice/98_string_template.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from string import Template


# ---------------------------------------------------------------------------
# Exercise 1 — build a Template and fill it with substitute().
# Given template text and a dict of values, build a Template from the text
# and return the result of calling .substitute() with that dict.
def render(text, values):
    # TODO: return Template(text).substitute(values)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — a missing placeholder raises KeyError.
# Given template text and a dict of values (deliberately missing a key the
# template needs), call .substitute() and return the *name* of the missing
# key from the KeyError (a plain string, e.g. "amount" — not "'amount'").
# If substitute() does not raise, return None.
def missing_key_name(text, values):
    # TODO: try:
    #           Template(text).substitute(values)
    #       except KeyError as e:
    #           return str(e).strip("'\"")
    #       return None
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — safe_substitute() leaves an unfillable placeholder untouched.
# Given template text and a dict of values (possibly missing a key), return
# the result of calling .safe_substitute() with that dict — it must never
# raise, even when a key is missing.
def render_safe(text, values):
    # TODO: return Template(text).safe_substitute(values)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — read a template's required names before filling it in.
# Given template text, return the sorted list of identifier names the
# template requires (use .get_identifiers()).
def required_names(text):
    # TODO: return sorted(Template(text).get_identifiers())
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
    return render("Hello $name, you have $count items.",
                   {"name": "Alice", "count": 3}) == "Hello Alice, you have 3 items."


def _ex2():
    return missing_key_name("Hello $name, balance $amount.", {"name": "Bob"}) == "amount"


def _ex3():
    result = render_safe("Hello $name, balance $amount.", {"name": "Carol"})
    return result == "Hello Carol, balance $amount."


def _ex4():
    return required_names("$name owes $amount to $payee") == ["amount", "name", "payee"]


results = [
    check("Ex 1: render() fills a Template via substitute()", _ex1),
    check("Ex 2: missing_key_name() names the KeyError's missing key", _ex2),
    check("Ex 3: render_safe() leaves an unfillable placeholder untouched", _ex3),
    check("Ex 4: required_names() lists a template's identifiers, sorted", _ex4),
]
print("\nAll green — lesson 98 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
