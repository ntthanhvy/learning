# Practice 122 — binascii: bytes as hex text, and a fast checksum
# Run:  cd ~/learning/python && uv run python3 practice/122_binascii.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import binascii


# ---------------------------------------------------------------------------
# Exercise 1 — round-trip bytes through hexlify()/unhexlify().
# Write hex_round_trip(data) that returns a tuple (hexed, matches) where
# `hexed` is the str form of binascii.hexlify(data) (decode it with
# .decode("ascii")), and `matches` is True only if unhexlify()-ing hexed
# back (re-encoded to bytes first) equals the original `data`.
def hex_round_trip(data):
    # TODO: hexed_bytes = binascii.hexlify(data)
    # hexed = hexed_bytes.decode("ascii")
    # back = binascii.unhexlify(hexed)
    # return hexed, back == data
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — catch binascii.Error on malformed hex input.
# Write safe_unhexlify(hex_bytes) that returns binascii.unhexlify(hex_bytes)
# on valid input, or the string "invalid" if it raises binascii.Error
# (odd length, or a non-hex-digit character).
def safe_unhexlify(hex_bytes):
    # TODO: try: return binascii.unhexlify(hex_bytes)
    # except binascii.Error: return "invalid"
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — chunked crc32() matches the whole-data checksum.
# Write chunked_crc32(chunks) that computes a running crc32 checksum across
# an iterable of bytes chunks, threading the running integer value back in
# as crc32()'s second argument each call, and returns the final checksum.
def chunked_crc32(chunks):
    # TODO: checksum = 0
    # for chunk in chunks:
    #     checksum = binascii.crc32(chunk, checksum)
    # return checksum
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
    hexed, matches = hex_round_trip(b"Hello, Python!")
    return hexed == "48656c6c6f2c20507974686f6e21" and matches is True


def _ex2():
    return (
        safe_unhexlify(b"48656c6c6f") == b"Hello"
        and safe_unhexlify(b"abc") == "invalid"
        and safe_unhexlify(b"zz") == "invalid"
    )


def _ex3():
    whole = binascii.crc32(b"Hello, Python!")
    return chunked_crc32([b"Hello, ", b"Python", b"!"]) == whole


results = [
    check("Ex 1: hex_round_trip encodes and decodes back correctly", _ex1),
    check("Ex 2: safe_unhexlify catches binascii.Error on bad input", _ex2),
    check("Ex 3: chunked_crc32 matches a single whole-data checksum", _ex3),
]
print("\nAll green — lesson 122 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
