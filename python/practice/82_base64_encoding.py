# Practice 82 — base64: binary data as plain text
# Run:  cd ~/learning/python && uv run python3 practice/82_base64_encoding.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import base64
import json

DATA = b"hello world"
URL_RISKY_BYTES = bytes([251, 255, 191])  # standard b64 of this contains + and /
RECORD = {"user": "an", "id": 42}


# ---------------------------------------------------------------------------
# Exercise 1 — round-trip bytes through base64. Write roundtrip(data) that
# encodes data with base64.b64encode(), decodes the result back with
# base64.b64decode(), and returns the decoded bytes.
def roundtrip(data):
    # TODO: encoded = base64.b64encode(data)
    #       return base64.b64decode(encoded)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — turn encoded bytes into a plain str for embedding elsewhere.
# Write encode_to_str(data) that returns base64.b64encode(data) decoded
# to a str via .decode("ascii").
def encode_to_str(data):
    # TODO: return base64.b64encode(data).decode("ascii")
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — confirm urlsafe_b64encode() swaps the URL-unsafe characters.
# Write urlsafe_differs(data) that returns a tuple of
# (base64.b64encode(data), base64.urlsafe_b64encode(data)) and relies on
# the caller to check they differ when the standard form contains + or /.
def urlsafe_differs(data):
    # TODO: standard = base64.b64encode(data)
    #       urlsafe = base64.urlsafe_b64encode(data)
    #       return (standard, urlsafe)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — embed an encoded token inside a JSON payload and get the
# original bytes back out. Write json_embed_roundtrip(record) that:
#   1. json.dumps(record) to text, then base64.b64encode()s that text
#      (encoded as utf-8 first) into a token str via .decode("ascii")
#   2. wraps {"token": token} and runs it through json.dumps()/json.loads()
#   3. base64.b64decode()s the token back, decodes utf-8, json.loads()s it
# and returns the final dict, which should equal the original record.
def json_embed_roundtrip(record):
    # TODO: text = json.dumps(record)
    #       token = base64.b64encode(text.encode("utf-8")).decode("ascii")
    #       payload = json.loads(json.dumps({"token": token}))
    #       restored_text = base64.b64decode(payload["token"]).decode("utf-8")
    #       return json.loads(restored_text)
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
    return roundtrip(DATA) == DATA


def _ex2():
    token = encode_to_str(DATA)
    return isinstance(token, str) and base64.b64decode(token) == DATA


def _ex3():
    pair = urlsafe_differs(URL_RISKY_BYTES)
    standard, urlsafe = pair
    return (
        standard == base64.b64encode(URL_RISKY_BYTES)
        and urlsafe == base64.urlsafe_b64encode(URL_RISKY_BYTES)
        and standard != urlsafe
    )


def _ex4():
    return json_embed_roundtrip(RECORD) == RECORD


results = [
    check("Ex 1: b64encode()/b64decode() round-trips the original bytes", _ex1),
    check("Ex 2: encoded bytes decode to a plain str for embedding", _ex2),
    check("Ex 3: urlsafe_b64encode() swaps +// for -/_ vs standard", _ex3),
    check("Ex 4: a base64 token survives a json.dumps()/loads() round trip", _ex4),
]
print("\nAll green — lesson 82 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
