# Practice 104 — types.SimpleNamespace: attribute access without a class
# Run:  cd ~/learning/python && uv run python3 practice/104_types_simplenamespace.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import json
import types


# ---------------------------------------------------------------------------
# Exercise 1 — build a SimpleNamespace from keyword arguments.
# Given a dict of field names/values, return the types.SimpleNamespace built
# from it (hint: unpack the dict as keyword arguments with **).
def make_namespace(fields):
    # TODO: return types.SimpleNamespace(**fields)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — catch the AttributeError a missing attribute raises.
# Given a SimpleNamespace and an attribute name (a string), return the
# attribute's value if it's set. If reading it raises AttributeError,
# return the given default instead of letting the exception propagate.
# (hint: getattr(ns, name) raises the same AttributeError a dot-lookup
# would; wrap it in try/except rather than reaching for getattr's own
# default argument, to practice handling the exception directly.)
def get_or_default(ns, name, default):
    # TODO: try:
    #           return getattr(ns, name)
    #       except AttributeError:
    #           return default
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — parse JSON straight into nested SimpleNamespace objects.
# Given a JSON string, return the parsed result using object_hook so that
# every JSON object (including nested ones) becomes a types.SimpleNamespace
# instead of a plain dict.
def parse_as_namespaces(json_text):
    # TODO: return json.loads(json_text, object_hook=lambda d: types.SimpleNamespace(**d))
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — convert a SimpleNamespace back into a plain dict.
# Given a SimpleNamespace, return an ordinary dict with the same
# names/values (hint: vars(ns) returns the backing dict directly).
def namespace_to_dict(ns):
    # TODO: return vars(ns)
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
    ns = make_namespace({"name": "Ana", "age": 30})
    return isinstance(ns, types.SimpleNamespace) and ns.name == "Ana" and ns.age == 30


def _ex2():
    ns = types.SimpleNamespace(name="Ana")
    found = get_or_default(ns, "name", "nobody")
    missing = get_or_default(ns, "age", 0)
    return found == "Ana" and missing == 0


def _ex3():
    result = parse_as_namespaces('{"name": "Ana", "address": {"city": "Hanoi"}}')
    return (
        isinstance(result, types.SimpleNamespace)
        and result.name == "Ana"
        and isinstance(result.address, types.SimpleNamespace)
        and result.address.city == "Hanoi"
    )


def _ex4():
    ns = types.SimpleNamespace(name="Ana", age=30)
    d = namespace_to_dict(ns)
    return isinstance(d, dict) and not isinstance(d, types.SimpleNamespace) and d == {"name": "Ana", "age": 30}


results = [
    check("Ex 1: make_namespace() builds a SimpleNamespace from a dict", _ex1),
    check("Ex 2: get_or_default() reports a fallback without raising", _ex2),
    check("Ex 3: parse_as_namespaces() builds nested SimpleNamespace objects", _ex3),
    check("Ex 4: namespace_to_dict() converts back to a plain dict", _ex4),
]
print("\nAll green — lesson 104 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
