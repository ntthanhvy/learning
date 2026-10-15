# Practice 78 — pprint: readable nested data at a glance
# Run:  cd ~/learning/python && uv run python3 practice/78_pprint.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

from pprint import pformat

RECORD = {
    "user": {"id": 42, "name": "An", "roles": ["admin", "billing"]},
    "orders": [{"sku": "A1", "qty": 3}, {"sku": "B2", "qty": 1}],
}


# ---------------------------------------------------------------------------
# Exercise 1 — format RECORD with pformat() using the default settings.
# Write format_default(record) that returns pformat(record).
def format_default(record):
    # TODO: return pformat(record)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — format RECORD with sort_dicts=True (the default, but pass it
# explicitly here) and return the top-level keys in the order they appear
# in the formatted text. Write sorted_key_order(record) that calls
# pformat(record, sort_dicts=True) and returns a list of the record's
# top-level keys (record.keys()), ordered by where each key's quoted name
# first appears in that formatted text.
def sorted_key_order(record):
    # TODO: text = pformat(record, sort_dicts=True)
    #       return sorted(record.keys(), key=lambda k: text.index(repr(k)))
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — same as Exercise 2, but with sort_dicts=False, which should
# preserve insertion order instead of alphabetical order. Write
# insertion_key_order(record) that calls pformat(record, sort_dicts=False)
# and returns the top-level keys ordered the same way as Exercise 2.
def insertion_key_order(record):
    # TODO: text = pformat(record, sort_dicts=False)
    #       return sorted(record.keys(), key=lambda k: text.index(repr(k)))
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — confirm a narrower width= produces strictly more lines than
# the default width on the same data. Write line_counts(record) that
# returns a tuple (default_lines, narrow_lines): the number of lines in
# pformat(record) and the number of lines in pformat(record, width=20).
def line_counts(record):
    # TODO: default_text = pformat(record)
    #       narrow_text = pformat(record, width=20)
    #       return (len(default_text.splitlines()), len(narrow_text.splitlines()))
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
    text = format_default(RECORD)
    return isinstance(text, str) and "\n" in text and "roles" in text


def _ex2():
    order = sorted_key_order(RECORD)
    return order == ["orders", "user"]


def _ex3():
    order = insertion_key_order(RECORD)
    return order == ["user", "orders"]


def _ex4():
    result = line_counts(RECORD)
    if not (isinstance(result, tuple) and len(result) == 2):
        return False
    default_lines, narrow_lines = result
    return narrow_lines > default_lines


results = [
    check("Ex 1: pformat() returns a multi-line string for nested data", _ex1),
    check("Ex 2: sort_dicts=True orders top-level keys alphabetically", _ex2),
    check("Ex 3: sort_dicts=False preserves original insertion order", _ex3),
    check("Ex 4: a narrower width= produces strictly more lines", _ex4),
]
print("\nAll green — lesson 78 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
