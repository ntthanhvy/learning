# Practice 79 — review day 13: retrieval across Days 76-78
# Run:  cd ~/learning/python && uv run python3 practice/79_review_retrieval_day_13.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 76, 77, and 78.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import json
import secrets
from dataclasses import asdict, dataclass, is_dataclass
from datetime import datetime
from pprint import pformat


@dataclass
class Order:
    city: str
    placed_at: datetime


# ---------------------------------------------------------------------------
# Exercise 1 (Day 76 — json: write a default= function that lets
# json.dumps() serialize a dataclass holding a datetime field)
def json_default(value):
    """Return a JSON-safe stand-in for `value`:
    - if value is a datetime instance, return value.isoformat()
    - if value is a dataclass instance (is_dataclass(value)), return
      dataclasses.asdict(value)
    - otherwise raise TypeError(f"not JSON serializable: {type(value)}")"""
    # TODO: if isinstance(value, datetime):
    #           return value.isoformat()
    #       if is_dataclass(value):
    #           return asdict(value)
    #       raise TypeError(f"not JSON serializable: {type(value)}")
    pass


def dump_order(order):
    """Return json.dumps(order, default=json_default)."""
    # TODO: return json.dumps(order, default=json_default)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 77 — secrets: generate a token_hex value, then confirm
# secrets.compare_digest() agrees with == on both a match and a mismatch)
def token_and_compare():
    """Generate token = secrets.token_hex(16), then return a tuple
    (token, match_ok, mismatch_ok) where:
      match_ok is True if secrets.compare_digest(token, token) is True
      mismatch_ok is True if secrets.compare_digest(token, "0"*len(token))
        is False (unless the token happens to BE all zeros, which is
        astronomically unlikely and not something to special-case)."""
    # TODO: token = secrets.token_hex(16)
    #       match_ok = secrets.compare_digest(token, token) is True
    #       mismatch_ok = secrets.compare_digest(token, "0" * len(token)) is False
    #       return (token, match_ok, mismatch_ok)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 78 — pprint: use pformat() with sort_dicts=False to
# confirm insertion order is preserved instead of alphabetical order)
def insertion_key_order(record):
    """Call pformat(record, sort_dicts=False), then return a list of
    record's top-level keys (record.keys()), ordered by where each key's
    quoted name first appears in that formatted text."""
    # TODO: text = pformat(record, sort_dicts=False)
    #       return sorted(record.keys(), key=lambda k: text.index(repr(k)))
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
    order = Order("Hanoi", datetime(2026, 10, 16, 9, 0))
    text = dump_order(order)
    if not isinstance(text, str):
        return False
    back = json.loads(text)
    return back == {"city": "Hanoi", "placed_at": "2026-10-16T09:00:00"}


def _ex2():
    result = token_and_compare()
    if result is None:
        return False
    token, match_ok, mismatch_ok = result
    return (
        isinstance(token, str)
        and len(token) == 32
        and match_ok is True
        and mismatch_ok is True
    )


def _ex3():
    record = {"user": {"id": 42, "name": "An"}, "orders": [1, 2, 3]}
    order = insertion_key_order(record)
    return order == ["user", "orders"]


results = [
    check("Ex 1 (Day 76): default=json_default lets dumps() serialize a dataclass+datetime", _ex1),
    check("Ex 2 (Day 77): compare_digest() agrees with == on a match and a mismatch", _ex2),
    check("Ex 3 (Day 78): sort_dicts=False preserves original insertion order", _ex3),
]

print("\nAll green — lesson 79 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
