# Practice 38 — Regular expressions: pattern-matching text with re
# Run:  cd ~/learning/python && uv run python3 practice/38_regular_expressions.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import re


# ---------------------------------------------------------------------------
# Exercise 1 — validate a whole field against a shape with fullmatch().
# A SKU code looks like "ABC-1234": exactly 3 uppercase letters, a literal
# hyphen, then exactly 4 digits. Write is_valid_sku so it returns True only
# when the *entire* string matches that shape, False otherwise (including
# on lowercase letters, wrong digit counts, or extra trailing characters).
def is_valid_sku(code):
    # TODO: return re.fullmatch(r"[A-Z]{3}-\d{4}", code) is not None
    ...


def run_sku_checks():
    return (
        is_valid_sku("ABC-1234"),
        is_valid_sku("abc-1234"),
        is_valid_sku("ABC-123"),
        is_valid_sku("ABC-12345"),
    )


# ---------------------------------------------------------------------------
# Exercise 2 — pull every number out of a string with findall().
# Given a free-text string, return a list of every run of digits it
# contains, as strings, in the order they appear.
def extract_numbers(text):
    # TODO: return re.findall(r"\d+", text)
    ...


def run_extract_numbers():
    return extract_numbers("room 12, row 4, seat 100")


# ---------------------------------------------------------------------------
# Exercise 3 — named groups to pull structured pieces out of one line.
# A log line looks like "2026-09-04 ERROR disk full" — a date, a
# level (all caps letters), and a message (everything after, to the end).
# Write parse_log_line so it returns a dict with keys "date", "level", and
# "message" pulled out via named groups, or None if the line doesn't match
# that shape at all.
LOG_PATTERN = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>[A-Z]+) (?P<message>.+)")


def parse_log_line(line):
    # TODO: m = LOG_PATTERN.fullmatch(line)
    #       return m.groupdict() if m else None
    ...


def run_parse_log_line():
    ok = parse_log_line("2026-09-04 ERROR disk full")
    bad = parse_log_line("not a log line at all")
    return ok, bad


# ---------------------------------------------------------------------------
# Exercise 4 — redact digits from a string with sub().
# Replace every run of digits in text with the literal string "###",
# leaving everything else untouched.
def redact_numbers(text):
    # TODO: return re.sub(r"\d+", "###", text)
    ...


def run_redact_numbers():
    return redact_numbers("call 555-1234 or 555-5678")


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: is_valid_sku uses fullmatch to check the whole string's shape",
          lambda: run_sku_checks() == (True, False, False, False)),
    check("Ex 2: extract_numbers pulls every digit run out in order",
          lambda: run_extract_numbers() == ["12", "4", "100"]),
    check("Ex 3: parse_log_line returns named groups, or None on no match",
          lambda: run_parse_log_line() == (
              {"date": "2026-09-04", "level": "ERROR", "message": "disk full"},
              None,
          )),
    check("Ex 4: redact_numbers replaces every digit run with ###",
          lambda: run_redact_numbers() == "call ###-### or ###-###"),
]
print("\nAll green — lesson 38 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
