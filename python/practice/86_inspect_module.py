# Practice 86 — inspect: asking a function about its own signature
# Run:  cd ~/learning/python && uv run python3 practice/86_inspect_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import inspect


def greet(name, greeting="Hello", *, loud=False):
    """Say hello to someone."""
    return f"{greeting}, {name}!"


# ---------------------------------------------------------------------------
# Exercise 1 — read a function's parameters into a plain dict.
# Write param_defaults(func) that returns a dict mapping each of func's
# parameter names to its default value, using inspect.signature(func).
# A parameter with no declared default should map to inspect.Parameter.empty
# (don't try to replace it with None — that would hide a real difference).
def param_defaults(func):
    # TODO: sig = inspect.signature(func)
    #       return {name: p.default for name, p in sig.parameters.items()}
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — work out the full set of arguments a specific call would use.
# Write resolved_arguments(func, *args, **kwargs) that binds args/kwargs
# against func's signature, fills in any missing parameters with their
# declared defaults, and returns the result as a plain dict (name -> value).
# Hint: inspect.signature(func).bind(*args, **kwargs), then .apply_defaults(),
# then .arguments is already a dict-like mapping — wrap it in dict(...).
def resolved_arguments(func, *args, **kwargs):
    # TODO: sig = inspect.signature(func)
    #       bound = sig.bind(*args, **kwargs)
    #       bound.apply_defaults()
    #       return dict(bound.arguments)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — describe an arbitrary object's kind.
# Write describe_kind(obj) that returns "function" if inspect.isfunction(obj)
# is True, "class" if inspect.isclass(obj) is True, "builtin" if
# inspect.isbuiltin(obj) is True, or "other" if none of those match.
# Check function/class/builtin in that order.
def describe_kind(obj):
    # TODO: if inspect.isfunction(obj):
    #           return "function"
    #       if inspect.isclass(obj):
    #           return "class"
    #       if inspect.isbuiltin(obj):
    #           return "builtin"
    #       return "other"
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
    defaults = param_defaults(greet)
    return (
        defaults.get("name") is inspect.Parameter.empty
        and defaults.get("greeting") == "Hello"
        and defaults.get("loud") is False
    )


def _ex2():
    only_name = resolved_arguments(greet, "Alice")
    override_loud = resolved_arguments(greet, "Bob", loud=True)
    return (
        only_name == {"name": "Alice", "greeting": "Hello", "loud": False}
        and override_loud == {"name": "Bob", "greeting": "Hello", "loud": True}
    )


def _ex3():
    class Foo:
        pass

    return (
        describe_kind(greet) == "function"
        and describe_kind(int) == "class"
        and describe_kind(len) == "builtin"
        and describe_kind(Foo()) == "other"
    )


results = [
    check("Ex 1: param_defaults() reads names, defaults & Parameter.empty", _ex1),
    check("Ex 2: resolved_arguments() binds args and fills in defaults", _ex2),
    check("Ex 3: describe_kind() tells function/class/builtin/other apart", _ex3),
]
print("\nAll green — lesson 86 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
