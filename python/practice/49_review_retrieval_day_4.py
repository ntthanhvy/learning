# Practice 49 — review day 4: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/49_review_retrieval_day_4.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 8, 11, 17,
# 24, 32, and 41. Replace each `...` (or the marked TODO body) and re-run
# until every check prints ✓. Try each from memory before reopening the old
# lesson.
#
# Exercises 2, 3, and 4 test the same *rules* Days 11, 17, and 24 taught
# (fixture setup/teardown, coercion+validation, and a handled exception
# never reaching middleware's own try/except) using plain stdlib Python —
# a hand-rolled setup/teardown log, a small manual coercion function, and a
# plain function chain standing in for call_next — rather than running real
# pytest, pydantic, or FastAPI, so this file stays standard-library-only,
# matching Days 44 and 45's precedent for topics whose original lesson
# needed a third-party package.

from typing import Protocol, runtime_checkable


# ---------------------------------------------------------------------------
# Exercise 1 (Day 8 — exceptions: catch the exact type, never a bare except)
# safe_parse_amount should return int(text) if it parses, or None if int()
# raises ValueError — catch ONLY ValueError, not a bare except.
def safe_parse_amount(text):
    # TODO: try: return int(text)
    #       except ValueError: return None
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 11 — pytest fixtures: code after yield is teardown, always)
# Simulate a fixture's setup/teardown with a plain function taking a `log`
# list and a function `use_resource` representing the test body. Append
# "setup" before calling use_resource(), and MUST append "teardown" after —
# even if use_resource() raises. The exception should still propagate back
# out to the caller once teardown has run (the same always-runs guarantee
# as a context manager's __exit__ or a finally block).
def run_with_fixture(log, use_resource):
    # TODO:
    #     log.append("setup")
    #     try:
    #         use_resource()
    #     finally:
    #         log.append("teardown")
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 17 — pydantic: coercion converts, a plain dict/dataclass
# would not)
# coerce_price should behave like a pydantic float field: given a string
# that parses as a float ("12.5"), return the coerced float. Given a value
# that can't parse (e.g. "nope"), raise ValueError — pydantic's
# ValidationError is itself built from this same raise mechanism (Day 8).
def coerce_price(value):
    # TODO: return float(value)   # raises ValueError on its own for bad input
    ...


# ---------------------------------------------------------------------------
# Exercise 4 (Day 24 — ASGI middleware: a handled exception never reaches
# middleware's own try/except around call_next)
# `call_next` here is a plain function representing "everything downstream".
# `logging_middleware` must call call_next(request), and — matching the
# lesson's exact finding — read response["status_code"] unconditionally
# from whatever call_next returns, appending {"path": ..., "status_code": ...}
# to `log`. It must NOT wrap call_next in its own try/except that assumes
# it will ever see a handled exception (call_next already resolves any
# handled failure into a normal response before returning).
def logging_middleware(request, call_next, log):
    # TODO:
    #     response = call_next(request)
    #     log.append({"path": request["path"], "status_code": response["status_code"]})
    #     return response
    ...


def call_next_with_handled_exception(request):
    # Simulates: a route raised an exception, but a registered
    # @app.exception_handler already turned it into a normal response —
    # so call_next() just returns, no exception ever propagates here.
    return {"status_code": 409}


# ---------------------------------------------------------------------------
# Exercise 5 (Day 32 — classmethod: cls(...) not the hardcoded class name)
# Money.from_dollars must be a @classmethod alternative constructor that
# builds cents from a dollar string, calling cls(...) — not Money(...) by
# name — so a subclass inheriting it unmodified still builds itself.
class Money:
    def __init__(self, cents):
        self.cents = cents

    # TODO: add @classmethod above this def, and use cls(...) in the body
    def from_dollars(dollars_str):
        cents = round(float(dollars_str) * 100)
        ...  # TODO: return cls(cents)


class GiftCardMoney(Money):
    pass


# ---------------------------------------------------------------------------
# Exercise 6 (Day 41 — typing.Protocol: structural typing, no inheritance
# needed)
# Define a @runtime_checkable Protocol named HasName requiring a name()
# method returning a str. Employee below never inherits from HasName and
# never imports it, but must still satisfy it structurally.
# TODO: uncomment and fill in
# @runtime_checkable
# class HasName(Protocol):
#     def name(self) -> str: ...
HasName = None  # TODO: replace with the @runtime_checkable Protocol above


class Employee:
    def name(self) -> str:
        return "Ada"


class NoNameHere:
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


def _ex2_teardown_runs_even_on_exception():
    log = []

    def boom():
        raise ValueError("boom")

    try:
        run_with_fixture(log, boom)
    except ValueError:
        pass
    return log == ["setup", "teardown"]


def _ex3_bad_input_raises():
    try:
        coerce_price("nope")
        return False
    except ValueError:
        return True


def _ex4_middleware_logs_final_status_unconditionally():
    log = []
    request = {"path": "/orders"}
    response = logging_middleware(request, call_next_with_handled_exception, log)
    return (
        response == {"status_code": 409}
        and log == [{"path": "/orders", "status_code": 409}]
    )


def _ex5_classmethod_builds_subclass_via_cls():
    if not hasattr(Money, "from_dollars"):
        return False
    m = Money.from_dollars("5.00")
    gc = GiftCardMoney.from_dollars("5.00")
    return (
        isinstance(m, Money) and m.cents == 500
        and isinstance(gc, GiftCardMoney) and gc.cents == 500
    )


def _ex6_protocol_is_structural():
    if HasName is None:
        return False
    return isinstance(Employee(), HasName) and not isinstance(NoNameHere(), HasName)


results = [
    check("Ex 1: safe_parse_amount catches ValueError narrowly, returns None on bad input",
          lambda: safe_parse_amount("42") == 42 and safe_parse_amount("nope") is None),
    check("Ex 2: run_with_fixture always appends teardown, even when the body raises",
          _ex2_teardown_runs_even_on_exception),
    check("Ex 3: coerce_price converts a valid string, raises ValueError on a bad one",
          lambda: coerce_price("12.5") == 12.5 and _ex3_bad_input_raises()),
    check("Ex 4: logging_middleware reads the final status unconditionally after call_next",
          _ex4_middleware_logs_final_status_unconditionally),
    check("Ex 5: Money.from_dollars uses cls(...), so a subclass builds itself",
          _ex5_classmethod_builds_subclass_via_cls),
    check("Ex 6: HasName is a runtime_checkable Protocol satisfied structurally",
          _ex6_protocol_is_structural),
]

print("\nAll green — lesson 49 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
