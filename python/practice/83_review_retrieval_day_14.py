# Practice 83 — review day 14: retrieval across Days 80-82
# Run:  cd ~/learning/python && uv run python3 practice/83_review_retrieval_day_14.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 80, 81, and 82.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import base64
import csv
import difflib
import io
import json

OLD_CONFIG = ["host = localhost", "port = 8000", "debug = true"]
NEW_CONFIG = ["host = localhost", "port = 8000", "debug = false"]

ROWS = [["name", "qty"], ["bolt", "10"], ["nut", "25"]]


# ---------------------------------------------------------------------------
# Exercise 1 (Day 80 — difflib: find exactly which line changed between two
# small configs using unified_diff())
def changed_line(old, new):
    """Return the single removed-line text (without its leading '-') from
    difflib.unified_diff(old, new, lineterm=""), by finding the one line
    in the diff that starts with "-" but not "---"."""
    # TODO: diff = list(difflib.unified_diff(old, new, lineterm=""))
    #       removed = [line for line in diff if line.startswith("-") and not line.startswith("---")]
    #       return removed[0][1:]  # drop the leading "-"
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 81 — io: round-trip CSV rows through an io.StringIO with
# csv.writer()/csv.reader(), no real file involved)
def csv_roundtrip(rows):
    """Write `rows` into a fresh io.StringIO with csv.writer(), then parse
    that same text straight back out with csv.reader() (remember to
    seek(0) before reading, or wrap the text in a second StringIO) and
    return the parsed rows as a list of lists of str."""
    # TODO: buf = io.StringIO()
    #       writer = csv.writer(buf)
    #       for row in rows:
    #           writer.writerow(row)
    #       buf.seek(0)
    #       return list(csv.reader(buf))
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 82 — base64: encode a BytesIO's contents so they can
# travel inside a JSON string)
def bytesio_to_json_token(data):
    """Create buf = io.BytesIO(data), read its contents back out (after
    seeking to 0), base64.b64encode() those bytes, decode the result to a
    plain str via .decode("ascii"), wrap it as {"token": <that str>}, and
    return json.dumps() of that dict."""
    # TODO: buf = io.BytesIO(data)
    #       buf.seek(0)
    #       raw = buf.read()
    #       token = base64.b64encode(raw).decode("ascii")
    #       return json.dumps({"token": token})
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
    return changed_line(OLD_CONFIG, NEW_CONFIG) == "debug = true"


def _ex2():
    return csv_roundtrip(ROWS) == ROWS


def _ex3():
    text = bytesio_to_json_token(b"hello world")
    if not isinstance(text, str):
        return False
    payload = json.loads(text)
    return base64.b64decode(payload["token"]) == b"hello world"


results = [
    check("Ex 1 (Day 80): unified_diff() isolates the one changed line", _ex1),
    check("Ex 2 (Day 81): csv rows survive a round trip through StringIO", _ex2),
    check("Ex 3 (Day 82): BytesIO contents travel inside a JSON string via base64", _ex3),
]

print("\nAll green — lesson 83 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
