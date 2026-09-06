# Practice 40 — contextlib: suppress() and ExitStack
# Run:  cd ~/learning/python && uv run python3 practice/40_contextlib_utilities.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from contextlib import suppress, ExitStack


# ---------------------------------------------------------------------------
# Exercise 1 — suppress() ignores exactly the named exception type(s).
# Look up "missing" in the given dict and return its value, but if the key
# isn't there, suppress the KeyError and return None instead. Use
# `with suppress(KeyError):` — do not use try/except by hand here.
def lookup_or_none(d, key):
    result = None
    # TODO: with suppress(KeyError):
    #           result = d[key]
    ...
    return result


def run_lookup_checks():
    found = lookup_or_none({"a": 1, "b": 2}, "a")
    missing = lookup_or_none({"a": 1, "b": 2}, "z")
    return (found, missing)


# ---------------------------------------------------------------------------
# Exercise 2 — suppress() does NOT catch other exception types.
# Call fn() inside `with suppress(KeyError):`. If fn() raises KeyError, the
# with block should swallow it and this function returns "suppressed".
# If fn() raises anything else, do NOT catch it here — let it propagate.
def call_suppressing_keyerror(fn):
    # TODO: with suppress(KeyError):
    #           fn()
    #           return "ran without raising"
    #       return "suppressed"
    ...


def run_other_exception_checks():
    def raises_keyerror():
        raise KeyError("missing")

    def raises_valueerror():
        raise ValueError("boom")

    suppressed = call_suppressing_keyerror(raises_keyerror)
    propagated = False
    try:
        call_suppressing_keyerror(raises_valueerror)
    except ValueError:
        propagated = True
    return (suppressed, propagated)


# ---------------------------------------------------------------------------
# Exercise 3 — ExitStack enters a runtime-built list of context managers.
# `resources` is a list of already-constructed context manager objects
# (see Resource below). Use ExitStack to enter every one of them inside a
# single with block, appending each entered object to a list, then return
# that list. All resources must be entered via stack.enter_context(). Note:
# by the time this function returns, the with block has already exited, so
# every resource has already logged its own "close" too — that's expected.
class Resource:
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def __enter__(self):
        self.log.append(f"open {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.log.append(f"close {self.name}")
        return False


def enter_all(resources):
    entered = []
    # TODO: with ExitStack() as stack:
    #           for r in resources:
    #               entered.append(stack.enter_context(r))
    ...
    return entered


def run_enter_all_checks():
    log = []
    resources = [Resource("a", log), Resource("b", log), Resource("c", log)]
    entered = enter_all(resources)
    names_entered = [r.name for r in entered]
    return (names_entered, log)


# ---------------------------------------------------------------------------
# Exercise 4 — ExitStack still closes everything already opened if the
# block raises partway through. Enter every resource in `resources`, then
# raise ValueError. Let the ValueError propagate out of this function — do
# not catch it here. (The point: closing still has to happen via ExitStack's
# own guarantee, not by adding your own try/except.)
def enter_all_then_raise(resources):
    # TODO: with ExitStack() as stack:
    #           for r in resources:
    #               stack.enter_context(r)
    #           raise ValueError("boom")
    ...


def run_raise_checks():
    log = []
    resources = [Resource("a", log), Resource("b", log), Resource("c", log)]
    raised = False
    try:
        enter_all_then_raise(resources)
    except ValueError:
        raised = True
    return (raised, log)


# ---------------------------------------------------------------------------
# Exercise 5 — stack.callback() registers a plain cleanup function.
# Inside a single `with ExitStack() as stack:` block: enter `resource`,
# register `cleanup_fn` via stack.callback(), then append "body" to `log`.
# cleanup_fn takes no arguments.
def enter_with_callback(resource, cleanup_fn, log):
    # TODO: with ExitStack() as stack:
    #           stack.enter_context(resource)
    #           stack.callback(cleanup_fn)
    #           log.append("body")
    ...


def run_callback_checks():
    log = []
    resource = Resource("x", log)
    enter_with_callback(resource, lambda: log.append("ran callback"), log)
    return log


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
    check("Ex 1: suppress() lets a found key through, swallows a missing one",
          lambda: run_lookup_checks() == (1, None)),
    check("Ex 2: suppress(KeyError) ignores KeyError, lets ValueError propagate",
          lambda: run_other_exception_checks() == ("suppressed", True)),
    check("Ex 3: ExitStack enters every resource via enter_context()",
          lambda: run_enter_all_checks() == (
              ["a", "b", "c"],
              ["open a", "open b", "open c", "close c", "close b", "close a"])),
    check("Ex 4: ExitStack closes everything already opened when the block raises",
          lambda: run_raise_checks() == (
              True, ["open a", "open b", "open c", "close c", "close b", "close a"])),
    check("Ex 5: stack.callback() runs at the same point __exit__ would",
          lambda: run_callback_checks() == ["open x", "body", "ran callback", "close x"]),
]
print("\nAll green — lesson 40 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
