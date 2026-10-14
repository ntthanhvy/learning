# Practice 77 — secrets: tokens and timing-safe compare
# Run:  cd ~/learning/python && uv run python3 practice/77_secrets_tokens_and_compare.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import string
import secrets


# ---------------------------------------------------------------------------
# Exercise 1 — generate a token_hex value of the exact expected length, and
# confirm two separate calls never collide. Write make_hex_token(nbytes)
# that returns secrets.token_hex(nbytes).
def make_hex_token(nbytes):
    # TODO: return secrets.token_hex(nbytes)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — generate a token_urlsafe value containing no characters that
# would need URL-escaping. Write make_urlsafe_token(nbytes) that returns
# secrets.token_urlsafe(nbytes).
def make_urlsafe_token(nbytes):
    # TODO: return secrets.token_urlsafe(nbytes)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — build a fixed-length PIN from a custom alphabet using
# secrets.choice(). Write make_pin(length) that returns a string of
# `length` characters, each independently drawn from string.digits via
# secrets.choice().
def make_pin(length):
    # TODO: return "".join(secrets.choice(string.digits) for _ in range(length))
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — confirm secrets.compare_digest() agrees with == on both a
# match and a mismatch. Write safe_equal(a, b) that returns
# secrets.compare_digest(a, b).
def safe_equal(a, b):
    # TODO: return secrets.compare_digest(a, b)
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
    a = make_hex_token(16)
    b = make_hex_token(16)
    if not isinstance(a, str) or not isinstance(b, str):
        return False
    return len(a) == 32 and len(b) == 32 and a != b and all(c in string.hexdigits for c in a)


def _ex2():
    a = make_urlsafe_token(16)
    b = make_urlsafe_token(16)
    if not isinstance(a, str) or not isinstance(b, str):
        return False
    safe_chars = set(string.ascii_letters + string.digits + "-_")
    return a != b and len(a) > 0 and all(c in safe_chars for c in a) and all(c in safe_chars for c in b)


def _ex3():
    pin = make_pin(6)
    if not isinstance(pin, str) or len(pin) != 6:
        return False
    if not all(c in string.digits for c in pin):
        return False
    # two independently generated PINs of reasonable length should usually differ
    other = make_pin(6)
    return pin != other or len(set(make_pin(6) for _ in range(5))) > 1


def _ex4():
    token = secrets.token_hex(16)
    same = token
    different = "0" * len(token)
    match_ok = safe_equal(token, same) is True
    mismatch_ok = safe_equal(token, different) is False
    agrees_with_eq = (safe_equal(token, same) == (token == same)) and (
        safe_equal(token, different) == (token == different)
    )
    return match_ok and mismatch_ok and agrees_with_eq


results = [
    check("Ex 1: token_hex(16) returns 32 hex chars, no collisions across calls", _ex1),
    check("Ex 2: token_urlsafe(16) returns only URL-safe characters", _ex2),
    check("Ex 3: make_pin(6) builds a 6-digit PIN from secrets.choice()", _ex3),
    check("Ex 4: compare_digest() agrees with == on a match and a mismatch", _ex4),
]
print("\nAll green — lesson 77 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
