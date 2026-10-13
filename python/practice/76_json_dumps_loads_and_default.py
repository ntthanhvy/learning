# Practice 76 — json.dumps/loads, indent, and default=
# Run:  cd ~/learning/python && uv run python3 practice/76_json_dumps_loads_and_default.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import json
from dataclasses import asdict, dataclass, is_dataclass
from datetime import datetime


# ---------------------------------------------------------------------------
# Exercise 1 — round-trip a dict through json.dumps()/json.loads() as a
# string, with no file involved at all. Write roundtrip_record(record) that
# takes a dict, converts it to a JSON string with json.dumps(), converts
# that string back to a dict with json.loads(), and returns a tuple
# (text, back) of (the JSON string, the rebuilt dict).
def roundtrip_record(record):
    # TODO: text = json.dumps(record)
    #       back = json.loads(text)
    #       return (text, back)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — format output with indent=2 and confirm it contains real
# newlines. Write pretty(record) that returns json.dumps(record, indent=2).
def pretty(record):
    # TODO: return json.dumps(record, indent=2)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — write a default= function that lets json.dumps() serialize
# a dataclass instance holding a datetime field. Write json_default(value)
# that:
#   - if value is a datetime instance, returns value.isoformat()
#   - if value is a dataclass instance (is_dataclass(value)), returns
#     dataclasses.asdict(value)
#   - otherwise raises TypeError(f"not JSON serializable: {type(value)}")
def json_default(value):
    # TODO: if isinstance(value, datetime):
    #           return value.isoformat()
    #       if is_dataclass(value):
    #           return asdict(value)
    #       raise TypeError(f"not JSON serializable: {type(value)}")
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — use json_default from Exercise 3 to serialize a dataclass
# instance that holds a datetime field. Write dump_order(order) that
# returns json.dumps(order, default=json_default).
def dump_order(order):
    # TODO: return json.dumps(order, default=json_default)
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
@dataclass
class Order:
    city: str
    placed_at: datetime


def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    record = {"city": "Hanoi", "amount": 120, "tags": ["retail", "q3"]}
    result = roundtrip_record(record)
    if result is None:
        return False
    text, back = result
    return isinstance(text, str) and back == record


def _ex2():
    record = {"city": "Hanoi", "amount": 120}
    text = pretty(record)
    return isinstance(text, str) and "\n" in text and json.loads(text) == record


def _ex3():
    order = Order("Hanoi", datetime(2026, 10, 13, 9, 0))
    converted_dt = json_default(order.placed_at)
    converted_order = json_default(order)
    dt_ok = converted_dt == order.placed_at.isoformat()
    order_ok = converted_order == asdict(order)
    raised = False
    try:
        json_default(object())
    except TypeError:
        raised = True
    return dt_ok and order_ok and raised


def _ex4():
    order = Order("Hanoi", datetime(2026, 10, 13, 9, 0))
    text = dump_order(order)
    if not isinstance(text, str):
        return False
    back = json.loads(text)
    return back == {"city": "Hanoi", "placed_at": "2026-10-13T09:00:00"}


results = [
    check("Ex 1: a dict round-trips through json.dumps()/loads() as a string", _ex1),
    check("Ex 2: indent=2 produces readable text with real newlines", _ex2),
    check("Ex 3: json_default() converts a datetime and a dataclass, raises on the rest", _ex3),
    check("Ex 4: default=json_default lets dumps() serialize a dataclass with a datetime", _ex4),
]
print("\nAll green — lesson 76 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
