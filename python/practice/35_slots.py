# Practice 35 — __slots__: trading dynamic attributes for memory and safety
# Run:  cd ~/learning/python && uv run python3 practice/35_slots.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Exercise 1 — add __slots__ to a plain class.
# Give Point exactly two slots, "x" and "y" (a tuple of strings), so a
# declared field still works normally but an undeclared one raises
# AttributeError instead of silently succeeding.
class Point:
    # TODO: declare __slots__ here, as a tuple of the two field names below.

    def __init__(self, x, y):
        self.x = x
        self.y = y


def run_point_slots():
    p = Point(1, 2)
    coords = (p.x, p.y)                 # declared attributes: should just work
    has_dict = hasattr(p, "__dict__")   # a slotted instance has no __dict__
    try:
        p.z = 99                        # undeclared attribute: should raise
        typo_blocked = False
    except AttributeError:
        typo_blocked = True
    return coords, has_dict, typo_blocked


# ---------------------------------------------------------------------------
# Exercise 2 — every class in an inheritance chain needs its own __slots__.
# Base already declares __slots__ = ("a",). Child currently declares none,
# so instances silently regain a __dict__ (the bug this exercise fixes).
# Give Child its own __slots__ containing only the ONE new field it adds
# ("b") — not "a", which already lives in Base's slots.
class Base:
    __slots__ = ("a",)


class Child(Base):
    pass   # TODO: add __slots__ here, containing only "b"


def run_child_slots():
    c = Child()
    c.a = 1
    c.b = 2
    has_dict = hasattr(c, "__dict__")
    try:
        c.z = 99
        typo_blocked = False
    except AttributeError:
        typo_blocked = True
    return (c.a, c.b), has_dict, typo_blocked


# ---------------------------------------------------------------------------
# Exercise 3 — convert a Day-7-style @dataclass to slots=True.
# Record below is written exactly like Day 7's SalesRow. Add the slots=True
# keyword to its @dataclass decorator so instances lose their __dict__,
# while __init__/__repr__/__eq__ keep working exactly as before.
@dataclass  # TODO: add slots=True inside these parentheses
class Record:
    city: str
    amount: int


def run_record_slots():
    r1 = Record("Hanoi", 120)
    r2 = Record("Hanoi", 120)
    equal = (r1 == r2)                  # __eq__ should still work
    text = repr(r1)                     # __repr__ should still work
    has_dict = hasattr(r1, "__dict__")
    try:
        r1.region = "North"
        typo_blocked = False
    except AttributeError:
        typo_blocked = True
    return equal, "Record(city='Hanoi', amount=120)" == text, has_dict, typo_blocked


# ---------------------------------------------------------------------------
# Exercise 4 — write a function that reports whether an object has an
# instance __dict__ at all. Use hasattr(obj, "__dict__") — the same check
# used above — so it works uniformly on any object, slotted or not.
def has_instance_dict(obj):
    ...   # TODO: return True if obj has a __dict__, False otherwise


def run_has_instance_dict():
    class Plain:
        def __init__(self):
            self.a = 1

    class Slotted:
        __slots__ = ("a",)
        def __init__(self):
            self.a = 1

    return has_instance_dict(Plain()), has_instance_dict(Slotted())


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
    check("Ex 1: Point's declared fields work, __dict__ is gone, typo raises",
          lambda: run_point_slots() == ((1, 2), False, True)),
    check("Ex 2: Child's own slot plus Base's slot work, __dict__ stays gone",
          lambda: run_child_slots() == ((1, 2), False, True)),
    check("Ex 3: dataclass(slots=True) keeps eq/repr, drops __dict__, blocks extras",
          lambda: run_record_slots() == (True, True, False, True)),
    check("Ex 4: has_instance_dict distinguishes a plain object from a slotted one",
          lambda: run_has_instance_dict() == (True, False)),
]
print("\nAll green — lesson 35 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
