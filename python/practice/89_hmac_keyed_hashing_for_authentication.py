# Practice 89 — hmac: keyed hashing for message authentication
# Run:  cd ~/learning/python && uv run python3 practice/89_hmac_keyed_hashing_for_authentication.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import hashlib
import hmac


# ---------------------------------------------------------------------------
# Exercise 1 — compute a keyed tag.
# Given a key and a message (both bytes), return the hex digest of the
# HMAC-SHA256 tag for them.
def tag_for(key, msg):
    # TODO: return hmac.new(key, msg, hashlib.sha256).hexdigest()
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — hmac is not the same as hashing a concatenation.
# Given a key and a message (both bytes), return a tuple of two hex digests:
# (the real HMAC-SHA256 tag, a plain sha256 hash of key + msg concatenated).
# The caller checks that these two values differ.
def real_tag_vs_naive_concat(key, msg):
    # TODO: real = hmac.new(key, msg, hashlib.sha256).hexdigest()
    #       naive = hashlib.sha256(key + msg).hexdigest()
    #       return (real, naive)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — incremental update() matches the one-shot call.
# Given a key and a message (both bytes), build one hmac object with the
# whole message passed at construction time, and a second hmac object built
# with no msg, fed the same bytes via .update() afterward. Return both of
# their hex digests as a tuple: (one_shot, incremental).
def one_shot_vs_incremental(key, msg):
    # TODO: one_shot = hmac.new(key, msg, hashlib.sha256).hexdigest()
    #       mac = hmac.new(key, digestmod=hashlib.sha256)
    #       mac.update(msg)
    #       return (one_shot, mac.hexdigest())
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
    key = b"shared-secret-key"
    msg = b'{"order_id": 42, "amount": 19.99}'
    different_key_tag = hmac.new(b"different-key", msg, hashlib.sha256).hexdigest()
    result = tag_for(key, msg)
    return (
        isinstance(result, str)
        and len(result) == 64
        and result == hmac.new(key, msg, hashlib.sha256).hexdigest()
        and result != different_key_tag
    )


def _ex2():
    key = b"shared-secret-key"
    msg = b"hello world"
    real, naive = real_tag_vs_naive_concat(key, msg)
    return (
        real == hmac.new(key, msg, hashlib.sha256).hexdigest()
        and naive == hashlib.sha256(key + msg).hexdigest()
        and real != naive
    )


def _ex3():
    key = b"shared-secret-key"
    msg = b"hello world"
    one_shot, incremental = one_shot_vs_incremental(key, msg)
    return one_shot == incremental == hmac.new(key, msg, hashlib.sha256).hexdigest()


results = [
    check("Ex 1: tag_for() computes a real HMAC-SHA256 tag, keyed correctly", _ex1),
    check("Ex 2: the real hmac tag differs from a naive sha256(key + msg) hash", _ex2),
    check("Ex 3: incremental update() matches the one-shot hmac.new() call", _ex3),
]
print("\nAll green — lesson 89 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
