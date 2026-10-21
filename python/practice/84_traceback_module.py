# Practice 84 — traceback: capturing failure as text
# Run:  cd ~/learning/python && uv run python3 practice/84_traceback_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import io
import traceback

RECORDS = ["10", "20", "oops", "40"]


# ---------------------------------------------------------------------------
# Exercise 1 — capture a caught exception's full traceback as a str.
# Write capture_one(bad_value) that tries int(bad_value) inside a try/except
# ValueError, and in the except block returns traceback.format_exc().
# (Assume bad_value always raises ValueError when passed to int().)
def capture_one(bad_value):
    # TODO: try:
    #           int(bad_value)
    #       except ValueError:
    #           return traceback.format_exc()
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — confirm the captured text's last line names the exception.
# Write last_line(text) that returns the final non-empty line of a
# traceback string, with no leading/trailing whitespace. Hint: text.strip()
# then .splitlines()[-1].
def last_line(text):
    # TODO: return text.strip().splitlines()[-1]
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — redirect print_exc() into an io.StringIO with file=.
# Write capture_via_print_exc(bad_value) that tries int(bad_value), and on
# ValueError creates buf = io.StringIO(), calls traceback.print_exc(file=buf)
# instead of format_exc(), and returns buf.getvalue().
def capture_via_print_exc(bad_value):
    # TODO: try:
    #           int(bad_value)
    #       except ValueError:
    #           buf = io.StringIO()
    #           traceback.print_exc(file=buf)
    #           return buf.getvalue()
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — process a batch: good records parse, bad ones keep their
# traceback text, and no single bad record stops the run. Write
# process_batch(records) that returns (good, bad) where good is a list of
# the successfully parsed ints and bad is a list of
# {"record": r, "error": <traceback text from format_exc()>} dicts, one
# per record that raised ValueError.
def process_batch(records):
    # TODO: good, bad = [], []
    #       for r in records:
    #           try:
    #               good.append(int(r))
    #           except ValueError:
    #               bad.append({"record": r, "error": traceback.format_exc()})
    #       return good, bad
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
    text = capture_one("oops")
    return isinstance(text, str) and "ValueError" in text and "Traceback" in text


def _ex2():
    text = capture_one("oops")
    return last_line(text) == "ValueError: invalid literal for int() with base 10: 'oops'"


def _ex3():
    text = capture_via_print_exc("oops")
    return isinstance(text, str) and last_line(text) == (
        "ValueError: invalid literal for int() with base 10: 'oops'"
    )


def _ex4():
    good, bad = process_batch(RECORDS)
    if good != [10, 20, 40] or len(bad) != 1:
        return False
    entry = bad[0]
    return (
        entry["record"] == "oops"
        and "ValueError" in entry["error"]
        and "Traceback" in entry["error"]
    )


results = [
    check("Ex 1: format_exc() captures a full traceback as a str", _ex1),
    check("Ex 2: the captured text's last line names the exception", _ex2),
    check("Ex 3: print_exc(file=...) redirects into an io.StringIO", _ex3),
    check("Ex 4: a batch keeps parsing past one bad record, with its traceback saved", _ex4),
]
print("\nAll green — lesson 84 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
