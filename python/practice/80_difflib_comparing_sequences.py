# Practice 80 — difflib: comparing sequences of text
# Run:  cd ~/learning/python && uv run python3 practice/80_difflib_comparing_sequences.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import difflib

OLD_LINES = ["host = localhost", "port = 8000", "debug = true"]
NEW_LINES = ["host = localhost", "port = 9000", "debug = true"]

KNOWN_FIELDS = ["username", "password", "email"]


# ---------------------------------------------------------------------------
# Exercise 1 — run unified_diff() on OLD_LINES/NEW_LINES and return the list
# of lines in the result that start with a single "-" (removed) marker.
# Write removed_lines(old, new) that calls
# difflib.unified_diff(old, new, lineterm="") and returns every line in the
# result that starts with "-" but not "---" (that's the file-header line,
# not a removed-content line).
def removed_lines(old, new):
    # TODO: diff = list(difflib.unified_diff(old, new, lineterm=""))
    #       return [line for line in diff if line.startswith("-") and not line.startswith("---")]
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — same diff, but return the lines that start with a single "+"
# (added) marker, excluding the "+++" file-header line.
# Write added_lines(old, new) with the same shape as Exercise 1.
def added_lines(old, new):
    # TODO: diff = list(difflib.unified_diff(old, new, lineterm=""))
    #       return [line for line in diff if line.startswith("+") and not line.startswith("+++")]
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — confirm an unchanged line appears in the diff with no -/+
# prefix (a plain leading space, since unified_diff() shows context lines
# that way). Write unchanged_context_lines(old, new) that returns every
# line in the diff that starts with a single space " " (context, not a
# header and not a @@ hunk marker).
def unchanged_context_lines(old, new):
    # TODO: diff = list(difflib.unified_diff(old, new, lineterm=""))
    #       return [line for line in diff if line.startswith(" ")]
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — compute a SequenceMatcher ratio between two identical
# strings and confirm it is exactly 1.0. Write identical_ratio(text) that
# returns difflib.SequenceMatcher(None, text, text).ratio().
def identical_ratio(text):
    # TODO: return difflib.SequenceMatcher(None, text, text).ratio()
    pass


# ---------------------------------------------------------------------------
# Exercise 5 — find the single best match for a misspelled word among
# KNOWN_FIELDS. Write best_match(word, candidates) that returns the first
# (best) result of difflib.get_close_matches(word, candidates, n=1), or
# None if there is no match at all.
def best_match(word, candidates):
    # TODO: matches = difflib.get_close_matches(word, candidates, n=1)
    #       return matches[0] if matches else None
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
    result = removed_lines(OLD_LINES, NEW_LINES)
    return result == ["-port = 8000"]


def _ex2():
    result = added_lines(OLD_LINES, NEW_LINES)
    return result == ["+port = 9000"]


def _ex3():
    result = unchanged_context_lines(OLD_LINES, NEW_LINES)
    return result == [" host = localhost", " debug = true"]


def _ex4():
    return identical_ratio("colour") == 1.0


def _ex5():
    return best_match("usrname", KNOWN_FIELDS) == "username"


results = [
    check("Ex 1: unified_diff() marks a removed line with a single '-'", _ex1),
    check("Ex 2: unified_diff() marks an added line with a single '+'", _ex2),
    check("Ex 3: unchanged lines show as plain context, no -/+ prefix", _ex3),
    check("Ex 4: SequenceMatcher ratio on identical strings is 1.0", _ex4),
    check("Ex 5: get_close_matches() finds the misspelled word's match", _ex5),
]
print("\nAll green — lesson 80 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
