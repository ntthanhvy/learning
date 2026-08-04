# Practice 8 — Exceptions: catching failure on purpose
# Run:  cd ~/learning/python && uv run python3 practice/08_exceptions.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# Builds on Day 7's SalesRow/extract() shape: today makes that pipeline
# survive a bad row instead of crashing on it.

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Exercise 1 — catch a ValueError narrowly instead of crashing.
# Write safe_int(text) that returns int(text) if it parses, or None if it
# raises ValueError. Catch ONLY ValueError — nothing broader.
def safe_int(text):
    ...                              # TODO:
    # try:
    #     return int(text)
    # except ValueError:
    #     return None


# ---------------------------------------------------------------------------
# Exercise 2 — tell two exception types apart with separate except clauses.
# Write describe_lookup(d, key) that looks up d[key] and converts it with
# int(...), returning one of three strings:
#   "missing key"  if key isn't in d at all       (KeyError)
#   "bad value"    if d[key] can't convert to int  (ValueError)
#   "ok: <n>"      if it converts, e.g. "ok: 5"
def describe_lookup(d, key):
    ...                              # TODO:
    # try:
    #     n = int(d[key])
    # except KeyError:
    #     return "missing key"
    # except ValueError:
    #     return "bad value"
    # else:
    #     return f"ok: {n}"


# ---------------------------------------------------------------------------
# Exercise 3 — finally: count every attempt, success or failure.
# Write count_attempts(values) that calls int(v) on each item in values,
# ignoring ValueError, but increments a counter once per item regardless of
# outcome (use try/except/finally). Return the final counter.
def count_attempts(values):
    ...                              # TODO:
    # attempts = 0
    # for v in values:
    #     try:
    #         int(v)
    #     except ValueError:
    #         pass
    #     finally:
    #         attempts += 1
    # return attempts


# ---------------------------------------------------------------------------
# Exercise 4 — define and raise a custom exception.
# Define InvalidSalesRow as a custom exception (subclass Exception).
# Write parse_amount(row) that returns int(row["amount"]), but raises
# InvalidSalesRow(f"bad amount in row: {row}") instead of a bare ValueError
# when the conversion fails.
class InvalidSalesRow(Exception):
    pass


def parse_amount(row):
    ...                              # TODO:
    # try:
    #     return int(row["amount"])
    # except ValueError:
    #     raise InvalidSalesRow(f"bad amount in row: {row}")


# ---------------------------------------------------------------------------
# Exercise 5 — wire a narrow except into an extract()-style generator so one
# bad row doesn't stop the rest.
@dataclass
class SalesRow:
    city: str
    amount: int


def extract(raw_rows):
    # raw_rows: an iterable of dicts like {"city": "Hanoi", "amount": "120"}
    ...                              # TODO: a generator function —
    # for row in raw_rows:
    #     try:
    #         yield SalesRow(city=row["city"], amount=int(row["amount"]))
    #     except ValueError:
    #         continue


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _raises_invalid_sales_row():
    try:
        parse_amount({"city": "Hanoi", "amount": "oops"})
    except InvalidSalesRow:
        return True
    except Exception:
        return False
    return False


results = [
    check("Ex 1: safe_int() returns the int, or None on a ValueError",
          lambda: safe_int("42") == 42 and safe_int("") is None and safe_int("nope") is None),
    check("Ex 2: describe_lookup() tells KeyError, ValueError, and success apart",
          lambda: (describe_lookup({"a": "5"}, "a") == "ok: 5"
                   and describe_lookup({"a": "x"}, "a") == "bad value"
                   and describe_lookup({"a": "5"}, "b") == "missing key")),
    check("Ex 3: count_attempts() counts every item via finally, success or failure",
          lambda: count_attempts(["1", "x", "3", "y", "5"]) == 5),
    check("Ex 4: InvalidSalesRow is a custom Exception, raised by parse_amount() on bad input",
          lambda: (issubclass(InvalidSalesRow, Exception)
                   and parse_amount({"city": "Hanoi", "amount": "120"}) == 120
                   and _raises_invalid_sales_row())),
    check("Ex 5: extract() is a generator that skips bad rows and keeps yielding good ones",
          lambda: list(extract([
              {"city": "Hanoi", "amount": "120"},
              {"city": "Danang", "amount": "oops"},
              {"city": "HCMC", "amount": "80"},
          ])) == [SalesRow(city="Hanoi", amount=120), SalesRow(city="HCMC", amount=80)]),
]

print("\nAll green — lesson 8 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
