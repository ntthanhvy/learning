# Practice 81 — io.StringIO & io.BytesIO: file-shaped objects with no file
# Run:  cd ~/learning/python && uv run python3 practice/81_io_stringio_bytesio.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import csv
import io
import json

ROWS = [["name", "qty"], ["bolt", "10"], ["nut", "25"]]
CSV_TEXT = "name,qty\nbolt,10\nnut,25\n"
RECORD = {"id": 1, "name": "An"}


# ---------------------------------------------------------------------------
# Exercise 1 — write ROWS into a fresh io.StringIO using csv.writer(), then
# return everything written so far via .getvalue().
# Write rows_to_csv_text(rows) that creates buf = io.StringIO(), gets
# writer = csv.writer(buf), calls writer.writerow(row) for each row in
# rows, and returns buf.getvalue().
def rows_to_csv_text(rows):
    # TODO: buf = io.StringIO()
    #       writer = csv.writer(buf)
    #       for row in rows:
    #           writer.writerow(row)
    #       return buf.getvalue()
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — parse a CSV string without ever opening a real file. Write
# parse_csv_text(text) that wraps text in io.StringIO(text), runs it
# through csv.reader(), and returns the result as a list of rows.
def parse_csv_text(text):
    # TODO: return list(csv.reader(io.StringIO(text)))
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — round-trip a dict through JSON using a StringIO as the
# "file". Write json_roundtrip(record) that creates buf = io.StringIO(),
# calls json.dump(record, buf), then buf.seek(0) to rewind, and returns
# json.load(buf).
def json_roundtrip(record):
    # TODO: buf = io.StringIO()
    #       json.dump(record, buf)
    #       buf.seek(0)
    #       return json.load(buf)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — confirm why .seek(0) matters on a BytesIO. Write
# write_then_read(data) that creates buf = io.BytesIO(), writes data to
# it, then returns a tuple of (immediate read result with no seek,
# read result after buf.seek(0)) — in that order. The first element
# should come back empty since the position is still at the end.
def write_then_read(data):
    # TODO: buf = io.BytesIO()
    #       buf.write(data)
    #       without_seek = buf.read()
    #       buf.seek(0)
    #       with_seek = buf.read()
    #       return (without_seek, with_seek)
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
    text = rows_to_csv_text(ROWS)
    return text == "name,qty\r\nbolt,10\r\nnut,25\r\n"


def _ex2():
    return parse_csv_text(CSV_TEXT) == ROWS


def _ex3():
    return json_roundtrip(RECORD) == RECORD


def _ex4():
    result = write_then_read(b"hello world")
    return result == (b"", b"hello world")


results = [
    check("Ex 1: csv.writer() into a StringIO, read back via getvalue()", _ex1),
    check("Ex 2: csv.reader() parses a StringIO-wrapped string directly", _ex2),
    check("Ex 3: json.dump()/load() round-trip through a StringIO", _ex3),
    check("Ex 4: BytesIO needs seek(0) before a write can be read back", _ex4),
]
print("\nAll green — lesson 81 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
