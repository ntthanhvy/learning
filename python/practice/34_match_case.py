# Practice 34 — match/case: structural pattern matching
# Run:  cd ~/learning/python && uv run python3 practice/34_match_case.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from dataclasses import dataclass
from enum import Enum


# ---------------------------------------------------------------------------
# Exercise 1 — a sequence pattern that checks length and unpacks at once.
# Complete describe_point so a 2-item tuple returns "2D", a 3-item tuple
# returns "3D", and anything else returns "unknown" — using match/case with
# sequence patterns, not len()/if.
def describe_point(point):
    match point:
        case (x, y):
            ...           # TODO: return "2D"
        case (x, y, z):
            ...           # TODO: return "3D"
        case _:
            ...           # TODO: return "unknown"


def run_describe_point():
    return describe_point((1, 2)), describe_point((1, 2, 3)), describe_point((1,))


# ---------------------------------------------------------------------------
# Exercise 2 — a class pattern with a guard clause.
# Status and Order are given. Complete classify_order using match/case:
#   - an Order with status PENDING and total > 1000 -> "needs approval"
#   - any other Order with status PENDING            -> "active"
#   - anything else                                  -> "other"
# The guard (`if total > 1000`) must be attached to the PENDING+large case
# only, so a small pending order still reaches the plain PENDING case below it.
class Status(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    status: Status
    total: float


def classify_order(order):
    match order:
        case Order(status=Status.PENDING, total=t) if t > 1000:
            ...           # TODO: return "needs approval"
        case Order(status=Status.PENDING):
            ...           # TODO: return "active"
        case _:
            ...           # TODO: return "other"


def run_classify_order():
    big = classify_order(Order(Status.PENDING, 5000))
    small = classify_order(Order(Status.PENDING, 10))
    cancelled = classify_order(Order(Status.CANCELLED, 10))
    return big, small, cancelled


# ---------------------------------------------------------------------------
# Exercise 3 — an OR-pattern combining two enum members into one branch.
# Complete is_active so PENDING or SHIPPED both return True via a single
# case using the | operator (not two separate case lines), and CANCELLED
# returns False.
def is_active(order):
    match order:
        case Order(status=Status.PENDING | Status.SHIPPED):
            ...           # TODO: return True
        case _:
            ...           # TODO: return False


def run_is_active():
    return (
        is_active(Order(Status.PENDING, 1)),
        is_active(Order(Status.SHIPPED, 1)),
        is_active(Order(Status.CANCELLED, 1)),
    )


# ---------------------------------------------------------------------------
# Exercise 4 — an unguarded capture pattern is irrefutable; a guarded one isn't.
# An unguarded bare-name case (`case cmd:`) placed before another case is a
# SyntaxError in Python itself — CPython proves the later case can never run
# and refuses to start. A *guarded* capture (`case cmd if <condition>:`) is
# fine before other cases, since the guard can fail and let match fall
# through. Complete handler so that:
#   - "special" (only "special") matches the special-case branch first
#   - "quit" returns "bye"
#   - anything else returns f"got {cmd}"
# using a guarded capture pattern for the first branch, ahead of "quit".
def handler(command):
    match command:
        case cmd if cmd == "special":
            ...           # TODO: return "handled specially"
        case "quit":
            ...           # TODO: return "bye"
        case cmd:
            ...           # TODO: return f"got {cmd}"


def run_handler_fix():
    return handler("special"), handler("quit"), handler("go")


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
    check("Ex 1: sequence pattern distinguishes 2D, 3D, and unknown",
          lambda: run_describe_point() == ("2D", "3D", "unknown")),
    check("Ex 2: class pattern + guard picks needs-approval/active/other correctly",
          lambda: run_classify_order() == ("needs approval", "active", "other")),
    check("Ex 3: OR-pattern treats PENDING and SHIPPED as active, CANCELLED not",
          lambda: run_is_active() == (True, True, False)),
    check("Ex 4: guarded capture, 'quit' literal, and fallback capture all pick correctly",
          lambda: run_handler_fix() == ("handled specially", "bye", "got go")),
]
print("\nAll green — lesson 34 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
