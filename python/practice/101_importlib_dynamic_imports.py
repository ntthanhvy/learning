# Practice 101 — importlib: imports as data, not syntax
# Run:  cd ~/learning/python && uv run python3 practice/101_importlib_dynamic_imports.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import importlib
import importlib.util


# ---------------------------------------------------------------------------
# Exercise 1 — load a module by a runtime string name.
# Given a module name as a string, import it with importlib.import_module()
# and return the resulting module object.
def load_module(name):
    # TODO: return importlib.import_module(name)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — call a function on a dynamically loaded module, found by name.
# Given a module name and a function name (both strings), load the module,
# look up the function on it with getattr(), call it with *args, and return
# the result. (Two steps: import_module(), then getattr().)
def call_by_name(module_name, func_name, *args):
    # TODO: mod = importlib.import_module(module_name)
    #       fn = getattr(mod, func_name)
    #       return fn(*args)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — check importability without raising.
# Given a module name, return True if importlib.util.find_spec() finds it
# (does not return None), and False if it returns None. Must not raise even
# when the name doesn't exist.
def can_import(name):
    # TODO: return importlib.util.find_spec(name) is not None
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — handle a missing module gracefully.
# Given a module name, try importlib.import_module(name). If it succeeds,
# return the module's __name__ attribute. If it raises ModuleNotFoundError,
# return the string "missing" instead of letting the exception propagate.
def safe_import_name(name):
    # TODO: try:
    #           return importlib.import_module(name).__name__
    #       except ModuleNotFoundError:
    #           return "missing"
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
    mod = load_module("math")
    return mod is not None and mod.sqrt(16) == 4.0


def _ex2():
    result = call_by_name("statistics", "mean", [1, 2, 3])
    return result == 2


def _ex3():
    found = can_import("os")
    not_found = can_import("definitely_not_a_real_module_xyz")
    return found is True and not_found is False


def _ex4():
    ok_name = safe_import_name("json")
    missing_name = safe_import_name("definitely_not_a_real_module_xyz")
    return ok_name == "json" and missing_name == "missing"


results = [
    check("Ex 1: load_module() imports a module from a runtime string", _ex1),
    check("Ex 2: call_by_name() loads a module and calls a function on it", _ex2),
    check("Ex 3: can_import() reports True/False without raising", _ex3),
    check("Ex 4: safe_import_name() handles a missing module gracefully", _ex4),
]
print("\nAll green — lesson 101 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
