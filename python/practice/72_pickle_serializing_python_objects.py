# Practice 72 — pickle: serializing Python objects
# Run:  cd ~/learning/python && uv run python3 practice/72_pickle_serializing_python_objects.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import pickle
import tempfile
from dataclasses import dataclass


@dataclass
class Order:
    city: str
    amount: float


# ---------------------------------------------------------------------------
# Exercise 1 — round-trip a dataclass instance through pickle bytes.
# Write roundtrip_bytes(order) that returns pickle.loads(pickle.dumps(order))
# — json.dumps(order) would raise TypeError on this same object, but pickle
# has no trouble with it.
def roundtrip_bytes(order):
    # TODO: return pickle.loads(pickle.dumps(order))
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — write then read back a list of objects through a binary file.
# Write roundtrip_file(orders, path) that:
#   - opens path in "wb" mode and calls pickle.dump(orders, f)
#   - opens path in "rb" mode and calls pickle.load(f)
#   - returns what pickle.load(f) gave back
def roundtrip_file(orders, path):
    # TODO:
    # with open(path, "wb") as f:
    #     pickle.dump(orders, f)
    # with open(path, "rb") as f:
    #     return pickle.load(f)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — confirm a restored object is equal but not the same object.
# Write is_equal_but_new(order) that returns a tuple (equal, same) where:
#   - equal is True if the round-tripped copy == the original
#   - same is True if the round-tripped copy IS the original (should be False)
def is_equal_but_new(order):
    # TODO:
    # restored = pickle.loads(pickle.dumps(order))
    # return (restored == order, restored is order)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — explain the untrusted-data risk in your own words.
# Write why_not_untrusted() returning a short string that mentions both
# "pickle" (or "unpickl") and "code" — e.g. explaining that loading a
# maliciously crafted pickle byte string can run arbitrary code.
def why_not_untrusted():
    # TODO: return "unpickling untrusted data can run arbitrary code"
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
    order = Order("Hanoi", 120.0)
    result = roundtrip_bytes(order)
    if result is None:
        return False
    return result == order and isinstance(result, Order)


def _ex2():
    orders = [Order("Hanoi", 120.0), Order("Hue", 75.5)]
    with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as tmp:
        path = tmp.name
    try:
        result = roundtrip_file(orders, path)
    finally:
        import os
        os.unlink(path)
    if result is None:
        return False
    return result == orders


def _ex3():
    order = Order("Da Nang", 42.0)
    result = is_equal_but_new(order)
    if result is None:
        return False
    equal, same = result
    return equal is True and same is False


def _ex4():
    result = why_not_untrusted()
    if result is None:
        return False
    text = result.lower()
    return ("pickl" in text) and ("code" in text)


results = [
    check("Ex 1: dataclass round-trips through pickle bytes", _ex1),
    check("Ex 2: a list round-trips through a binary pickle file", _ex2),
    check("Ex 3: restored copy is equal but not the same object", _ex3),
    check("Ex 4: can explain the untrusted-data code-execution risk", _ex4),
]
print("\nAll green — lesson 72 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
