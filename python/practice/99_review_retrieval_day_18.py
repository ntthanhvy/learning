# Practice 99 — review day 18: retrieval across Days 96-98
# Run:  cd ~/learning/python && uv run python3 practice/99_review_retrieval_day_18.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 96, 97, and 98.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import getpass
import io
import struct
import sys
import warnings
from string import Template


# ---------------------------------------------------------------------------
# Exercise 1 (Day 96 — struct: pack/unpack a multi-field record with an
# explicit byte order, and catch struct.error on a wrong-sized buffer)
def pack_record(magic, version, count, average):
    """Pack magic (4 bytes), version (1-byte int), count (2-byte int), and
    average (4-byte float) into one big-endian, no-padding buffer using the
    format string ">4sBHf"."""
    # TODO: return struct.pack(">4sBHf", magic, version, count, average)
    ...


def safe_unpack(fmt, data):
    """Try struct.unpack(fmt, data). If it succeeds, return the resulting
    tuple. If it raises struct.error, catch it and return the string
    "bad buffer" instead of letting the exception escape."""
    # TODO: try:
    #           return struct.unpack(fmt, data)
    #       except struct.error:
    #           return "bad buffer"
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 97 — getpass: confirm GetPassWarning is a catchable
# UserWarning subclass, using a redirected stdin so no real terminal is
# needed)
def capture_fallback_warning(prompt):
    """Call getpass.getpass(prompt) inside a
    warnings.catch_warnings(record=True) block with simplefilter("always"),
    and return the *name* of the first warning category caught (a string,
    e.g. "GetPassWarning"). Return None if no warning was caught."""
    # TODO: with warnings.catch_warnings(record=True) as caught:
    #           warnings.simplefilter("always")
    #           getpass.getpass(prompt)
    #       if caught:
    #           return caught[0].category.__name__
    #       return None
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 98 — string.Template: fill a template with
# .safe_substitute() so a missing placeholder is left untouched instead of
# raising)
def render_safe(text, values):
    """Build a Template from text and return the result of calling
    .safe_substitute() with the values dict — it must never raise, even
    when a key the template needs is missing."""
    # TODO: return Template(text).safe_substitute(values)
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


def _with_redirected_stdin(text, fn, *args):
    old_stdin = sys.stdin
    sys.stdin = io.StringIO(text)
    try:
        return fn(*args)
    finally:
        sys.stdin = old_stdin


def _ex1():
    packed = pack_record(b"TEMP", 1, 42, 21.5)
    if packed != struct.pack(">4sBHf", b"TEMP", 1, 42, 21.5):
        return False

    good = safe_unpack(">i", struct.pack(">i", 7))
    bad = safe_unpack(">i", b"\x00\x00")  # only 2 bytes, format needs 4
    return tuple(good) == (7,) and bad == "bad buffer"


def _ex2():
    category_name = _with_redirected_stdin(
        "whatever\n", capture_fallback_warning, "Password: "
    )
    return category_name == "GetPassWarning"


def _ex3():
    result = render_safe("Hello $name, balance $amount.", {"name": "Dao"})
    return result == "Hello Dao, balance $amount."


results = [
    check("Ex 1 (Day 96): pack/unpack round-trips and struct.error is caught", _ex1),
    check("Ex 2 (Day 97): getpass falls back and raises a catchable GetPassWarning", _ex2),
    check("Ex 3 (Day 98): safe_substitute() leaves a missing placeholder untouched", _ex3),
]

print("\nAll green — lesson 99 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
