# Practice 33 — enum: naming a closed set of choices
# Run:  cd ~/learning/python && uv run python3 practice/33_enum.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from enum import Enum, auto

# ---------------------------------------------------------------------------
# Exercise 1 — define a Status Enum with explicit string values.
# Fill in the three members below: PENDING = "pending", SHIPPED = "shipped",
# CANCELLED = "cancelled".
class Status(Enum):
    PENDING = ...     # TODO: "pending"
    SHIPPED = ...     # TODO: "shipped"
    CANCELLED = ...   # TODO: "cancelled"


def run_status_values():
    return Status.PENDING.value, Status.SHIPPED.value, Status.CANCELLED.value


# ---------------------------------------------------------------------------
# Exercise 2 — a function that only accepts a real Status member.
# Complete mark_shipped so it returns True only when given the actual
# Status.SHIPPED member, and False for anything else — including the plain
# string "shipped", which must NOT be treated as equal to Status.SHIPPED.
def mark_shipped(value):
    ...               # TODO: return value == Status.SHIPPED


def run_mark_shipped():
    real_member = mark_shipped(Status.SHIPPED)
    lookalike_string = mark_shipped("shipped")
    return real_member, lookalike_string


# ---------------------------------------------------------------------------
# Exercise 3 — auto() and definition-order iteration.
# Complete the Priority Enum using auto() for each of its three members,
# in this order: LOW, MEDIUM, HIGH.
class Priority(Enum):
    LOW = ...      # TODO: auto()
    MEDIUM = ...   # TODO: auto()
    HIGH = ...     # TODO: auto()


def run_priority_order():
    return [member.name for member in Priority]


# ---------------------------------------------------------------------------
# Exercise 4 — lookup by value (call syntax) and by name (index syntax).
# Complete lookup_both() to return a tuple of:
#   - the Status member whose value is "cancelled" (call syntax: Status(...))
#   - the Status member named "PENDING" (index syntax: Status[...])
def lookup_both():
    ...               # TODO: by_value = Status("cancelled")
    ...               # TODO: by_name = Status["PENDING"]
    ...               # TODO: return by_value, by_name


def run_lookup_both():
    return lookup_both()


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
    check("Ex 1: Status members hold the expected explicit string values",
          lambda: run_status_values() == ("pending", "shipped", "cancelled")),
    check("Ex 2: a real Status member matches, a lookalike string does not",
          lambda: run_mark_shipped() == (True, False)),
    check("Ex 3: auto() gives Priority three distinct members in definition order",
          lambda: run_priority_order() == ["LOW", "MEDIUM", "HIGH"]),
    check("Ex 4: lookup by value and by name both return the right member",
          lambda: run_lookup_both() == (Status.CANCELLED, Status.PENDING)),
]
print("\nAll green — lesson 33 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
