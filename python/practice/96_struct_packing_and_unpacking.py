# Practice 96 — struct: packing and unpacking binary data
# Run:  cd ~/learning/python && uv run python3 practice/96_struct_packing_and_unpacking.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import struct


# ---------------------------------------------------------------------------
# Exercise 1 — pack and unpack a multi-field record.
# Given a 4-byte magic tag (bytes), a 1-byte version (int), a 2-byte count
# (int), and a 4-byte float average, pack them into one big-endian, no-
# padding buffer using the format string ">4sBHf", and return the packed
# bytes.
def pack_record(magic, version, count, average):
    # TODO: return struct.pack(">4sBHf", magic, version, count, average)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — unpack a record back into its fields.
# Given bytes produced by pack_record() (or an equivalent buffer), unpack
# them with the same format string ">4sBHf" and return the resulting tuple
# (magic, version, count, average).
def unpack_record(data):
    # TODO: return struct.unpack(">4sBHf", data)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — compute a format's exact byte size.
# Given a struct format string, return how many bytes it takes to pack,
# without packing anything — use struct.calcsize().
def format_size(fmt):
    # TODO: return struct.calcsize(fmt)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — handle a wrongly sized buffer gracefully.
# Given a format string and a bytes buffer, try to unpack the buffer with
# that format. If it succeeds, return the resulting tuple. If it raises
# struct.error (e.g. the buffer is too short or too long for the format),
# catch it and return the string "bad buffer" instead of letting the
# exception escape.
def safe_unpack(fmt, data):
    # TODO: try:
    #           return struct.unpack(fmt, data)
    #       except struct.error:
    #           return "bad buffer"
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
    packed = pack_record(b"TEMP", 1, 42, 21.5)
    return packed == struct.pack(">4sBHf", b"TEMP", 1, 42, 21.5)


def _ex2():
    data = struct.pack(">4sBHf", b"TEMP", 1, 42, 21.5)
    result = unpack_record(data)
    return tuple(result) == (b"TEMP", 1, 42, 21.5)


def _ex3():
    return format_size(">4sBHf") == 11 and format_size(">i") == 4


def _ex4():
    good = safe_unpack(">i", struct.pack(">i", 7))
    bad = safe_unpack(">i", b"\x00\x00")
    return tuple(good) == (7,) and bad == "bad buffer"


results = [
    check("Ex 1: pack_record() packs a multi-field big-endian buffer", _ex1),
    check("Ex 2: unpack_record() reverses pack_record() exactly", _ex2),
    check("Ex 3: format_size() matches calcsize() for two formats", _ex3),
    check("Ex 4: safe_unpack() catches struct.error on a bad buffer", _ex4),
]
print("\nAll green — lesson 96 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
