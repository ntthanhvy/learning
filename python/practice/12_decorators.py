# Practice 12 — Decorators
# Run:  cd ~/learning/python && uv run python3 practice/12_decorators.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# Builds on Day 4's "a function is a value": a decorator is just a function
# that takes a function and returns a new one wrapped around it, and @ is
# sugar for `name = decorator(name)` right where the function is defined.

import functools


# ---------------------------------------------------------------------------
# Exercise 1 — a plain decorator: wrap a function's return value.
# Write a decorator `shout(func)` that returns a `wrapper(*args, **kwargs)`
# calling func(*args, **kwargs) and returning the result in upper case.
def shout(func):
    ...                              # TODO:
    # def wrapper(*args, **kwargs):
    #     result = func(*args, **kwargs)
    #     return result.upper()
    # return wrapper


@shout
def greet(name):
    return f"hello, {name}"


# ---------------------------------------------------------------------------
# Exercise 2 — a counting decorator: track how many times a function ran.
# Write a decorator `count_calls(func)` whose wrapper increments
# wrapper.calls by 1 every time it's called, then returns func's own result.
# Set wrapper.calls = 0 before returning wrapper, so it starts at zero.
def count_calls(func):
    ...                              # TODO:
    # def wrapper(*args, **kwargs):
    #     wrapper.calls += 1
    #     return func(*args, **kwargs)
    # wrapper.calls = 0
    # return wrapper


@count_calls
def ping():
    return "pong"


# ---------------------------------------------------------------------------
# Exercise 3 — a decorator that takes its own argument: @repeat(n).
# Write `repeat(times)` that returns a real decorator, which wraps func so
# that calling the wrapped function calls func `times` times in a row and
# returns a LIST of all `times` results, in order.
def repeat(times):
    def decorator(func):              # placeholder decorator so @repeat(3)
        return func                   # below doesn't crash at import time —
    return decorator                  # TODO: make this actually repeat `times`
    # def decorator(func):
    #     def wrapper(*args, **kwargs):
    #         return [func(*args, **kwargs) for _ in range(times)]
    #     return wrapper
    # return decorator


@repeat(3)
def roll():
    return 4  # pretend dice roll, fixed for a deterministic check


# ---------------------------------------------------------------------------
# Exercise 4 — functools.wraps: keep the original function's identity.
# Write a decorator `noisy(func)` whose wrapper just calls func and returns
# its result unchanged, but uses @functools.wraps(func) on wrapper so
# noisy(...).{__name__,__doc__} still match the original function's.
def noisy(func):
    ...                              # TODO:
    # @functools.wraps(func)
    # def wrapper(*args, **kwargs):
    #     return func(*args, **kwargs)
    # return wrapper


@noisy
def add(a, b):
    """Add two numbers."""
    return a + b


# ---------------------------------------------------------------------------
# Exercise 5 — manual equivalence: @decorator is sugar for name = decorator(name).
# Write plain_double(func) — no @ syntax anywhere in its own definition —
# whose wrapper calls func and doubles a numeric result. Then apply it to
# `triple_it` the LONG way, by rebinding the name yourself (no @ line).
def plain_double(func):
    ...                              # TODO:
    # def wrapper(*args, **kwargs):
    #     return func(*args, **kwargs) * 2
    # return wrapper


def triple_it(n):
    return n * 3


triple_it = ...                     # TODO: triple_it = plain_double(triple_it)


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
    check("Ex 1: @shout wraps greet() and upper-cases its return value",
          lambda: greet("an") == "HELLO, AN"),
    check("Ex 2: @count_calls tracks how many times ping() actually ran",
          lambda: (ping() == "pong" and ping() == "pong" and ping.calls == 2)),
    check("Ex 3: @repeat(3) calls roll() three times, returns a list of 3",
          lambda: roll() == [4, 4, 4]),
    check("Ex 4: @functools.wraps(func) preserves add()'s __name__/__doc__",
          lambda: (add(2, 3) == 5 and add.__name__ == "add"
                   and add.__doc__ == "Add two numbers.")),
    check("Ex 5: triple_it = plain_double(triple_it) doubles the tripled result",
          lambda: triple_it(2) == 12),
]

print("\nAll green — lesson 12 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
