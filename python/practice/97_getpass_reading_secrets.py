# Practice 97 — getpass: reading a secret without echoing it
# Run:  cd ~/learning/python && uv run python3 practice/97_getpass_reading_secrets.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import getpass
import io
import sys
import warnings


# ---------------------------------------------------------------------------
# Exercise 1 — build the right getpass.getpass() call.
# Given a prompt string, call getpass.getpass() with that exact prompt and
# return whatever it returns. (We'll feed stdin from a StringIO in the
# check below, so this runs safely with no real terminal involved.)
def read_secret(prompt):
    # TODO: return getpass.getpass(prompt)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — confirm GetPassWarning is a catchable UserWarning subclass.
# Return True if getpass.GetPassWarning is a subclass of UserWarning,
# False otherwise. Use issubclass() — don't guess, check it directly.
def warning_is_user_warning():
    # TODO: return issubclass(getpass.GetPassWarning, UserWarning)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — call getpass.getpass() with stdin redirected (no real tty)
# and capture the warning it raises instead of letting it print to stderr.
# Use warnings.catch_warnings(record=True) with simplefilter("always"),
# call getpass.getpass(prompt) inside the block, and return the *name* of
# the category of the first warning caught (a string, e.g. "GetPassWarning").
# If no warning was caught, return None.
def capture_fallback_warning(prompt):
    # TODO: with warnings.catch_warnings(record=True) as caught:
    #           warnings.simplefilter("always")
    #           getpass.getpass(prompt)
    #       if caught:
    #           return caught[0].category.__name__
    #       return None
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — treat getpass.getuser() as a default, not as proof of
# identity. Given a possibly-None `claimed_user` argument, return
# `claimed_user` if it is not None, otherwise fall back to whatever
# getpass.getuser() reports. Never call getuser() when claimed_user is
# already given — the point is using it only as the fallback default.
def resolve_user(claimed_user):
    # TODO: return claimed_user if claimed_user is not None else getpass.getuser()
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
    result = _with_redirected_stdin("s3cr3t\n", read_secret, "Password: ")
    return result == "s3cr3t"


def _ex2():
    return warning_is_user_warning() is True


def _ex3():
    category_name = _with_redirected_stdin(
        "whatever\n", capture_fallback_warning, "Password: "
    )
    return category_name == "GetPassWarning"


def _ex4():
    given = resolve_user("alice") == "alice"
    fallback = resolve_user(None) == getpass.getuser()
    return given and fallback


results = [
    check("Ex 1: read_secret() returns getpass.getpass()'s result", _ex1),
    check("Ex 2: GetPassWarning is confirmed as a UserWarning subclass", _ex2),
    check("Ex 3: capture_fallback_warning() names the GetPassWarning category", _ex3),
    check("Ex 4: resolve_user() only falls back to getuser() when needed", _ex4),
]
print("\nAll green — lesson 97 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
