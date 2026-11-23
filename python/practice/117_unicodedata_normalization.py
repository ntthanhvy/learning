# Practice 117 — unicodedata: when two identical-looking strings aren't equal
# Run:  cd ~/learning/python && uv run python3 practice/117_unicodedata_normalization.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import unicodedata


# ---------------------------------------------------------------------------
# Exercise 1 — two strings that print identically but fail ==, because one
# letter was built from a different number of underlying code points (one
# precomposed code point vs. a base letter plus a separate combining mark).
# Write same_after_normalizing(a, b) that returns True if `a` and `b` become
# equal once BOTH are normalized to Unicode form "NFC" with
# unicodedata.normalize(), False otherwise.
def same_after_normalizing(a, b):
    # TODO: return unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — deduplicate a list of "same-looking" strings correctly. A
# plain `set(values)` would keep both a precomposed and a decomposed copy
# of the same visible text as two different entries, because set membership
# uses == under the hood, which compares raw code points.
# Write dedupe_normalized(values) that returns a list of the UNIQUE values
# after normalizing every item to NFC first (use unicodedata.normalize()),
# preserving the order each normalized value first appears in, with no
# duplicates. (Hint: build the result by walking `values` once, normalizing
# each item, and only keeping the first occurrence of each normalized form.)
def dedupe_normalized(values):
    # TODO: walk values, normalize each with unicodedata.normalize("NFC", v),
    # and return a list of the first-seen normalized forms, no duplicates.
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — identify a mystery character hiding inside a string by name.
# Write name_of_char(ch) that uses unicodedata.name() to return the official
# Unicode name of the single character `ch` as a string (e.g. "A" ->
# "LATIN CAPITAL LETTER A").
def name_of_char(ch):
    # TODO: return unicodedata.name(ch)
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


# precomposed "café" (e-acute is ONE code point) vs. "cafe" + a separate
# combining acute accent (TWO code points for the same visible letter).
PRECOMPOSED = "café"
DECOMPOSED = "cafe" + "́"


def _ex1():
    # The two spellings print identically but are NOT == without normalizing.
    return (
        PRECOMPOSED != DECOMPOSED
        and same_after_normalizing(PRECOMPOSED, DECOMPOSED) is True
        and same_after_normalizing("hello", "world") is False
    )


def _ex2():
    values = [PRECOMPOSED, "banana", DECOMPOSED, "banana", "apple"]
    result = dedupe_normalized(values)
    # PRECOMPOSED and DECOMPOSED normalize to the same NFC form, so only the
    # first-seen spelling survives; "banana" appears once despite 2 copies.
    return result == [PRECOMPOSED, "banana", "apple"]


def _ex3():
    return (
        name_of_char("A") == "LATIN CAPITAL LETTER A"
        and name_of_char("5") == "DIGIT FIVE"
    )


results = [
    check("Ex 1: normalizing both sides to NFC fixes the == comparison", _ex1),
    check("Ex 2: deduplicating after normalizing removes the look-alike copy", _ex2),
    check("Ex 3: unicodedata.name() identifies a character by its official name", _ex3),
]
print("\nAll green — lesson 117 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
