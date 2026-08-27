# Practice 30 — Making your own objects behave like built-ins
# Run:  cd ~/learning/python && uv run python3 practice/30_object_model_dunder_and_property.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

# ---------------------------------------------------------------------------
# Exercise 1 — __repr__.
# Complete Point.__repr__ so it returns a string that looks like valid
# Python that could rebuild the object, e.g. "Point(1, 2)" for Point(1, 2).
# Note: the class line itself must stay definable even before you fill in
# the method, so the TODO body lives inside the method, not the class line.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        ...                       # TODO: return f"Point({self.x}, {self.y})"


def run_point_repr():
    return repr(Point(1, 2))


# ---------------------------------------------------------------------------
# Exercise 2 — __eq__ and __lt__, then sorted() with no key=.
# Complete Version so that:
#   - __eq__ compares two Versions by their .major/.minor tuple
#   - __lt__ compares the same way (tuple comparison does the right thing:
#     (1, 9) < (1, 10) is True, exactly like real version ordering)
#   - both return NotImplemented (not False!) when `other` isn't a Version
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __repr__(self):
        return f"Version({self.major}, {self.minor})"

    def __eq__(self, other):
        if not isinstance(other, Version):
            ...                   # TODO: return NotImplemented
        ...                       # TODO: return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            ...                   # TODO: return NotImplemented
        ...                       # TODO: return (self.major, self.minor) < (other.major, other.minor)


def run_version_eq():
    return Version(1, 9) == Version(1, 9), Version(1, 9) == Version(1, 10)


def run_version_sorted():
    versions = [Version(2, 0), Version(1, 10), Version(1, 9)]
    return sorted(versions)


# ---------------------------------------------------------------------------
# Exercise 3 — NotImplemented against an unrelated type.
# Using Version.__eq__ from above, comparing a Version to a plain int should
# neither raise nor return True — Python falls back to False once both
# sides return NotImplemented. Confirm that fallback happens cleanly.
def run_version_eq_unrelated():
    return Version(1, 0) == 5


# ---------------------------------------------------------------------------
# Exercise 4 — operator overloading with __add__.
# Complete Vector.__add__ so that Vector(a, b) + Vector(c, d) returns a new
# Vector(a + c, b + d) — componentwise addition, a new object each time.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        ...                       # TODO: return Vector(self.x + other.x, self.y + other.y)


def run_vector_add():
    return Vector(1, 2) + Vector(3, 4)


# ---------------------------------------------------------------------------
# Exercise 5 — @property with a validating setter.
# Complete Temperature so that:
#   - .celsius is a plain stored attribute (set in __init__)
#   - .fahrenheit is a @property computed from self.celsius (C * 9/5 + 32)
#   - .fahrenheit also has a @fahrenheit.setter that converts back to
#     celsius (F - 32) * 5/9 and stores it in self.celsius
#   - the setter raises ValueError if the resulting celsius would be
#     below -273.15 (absolute zero) — validate on write, like Day 17's
#     pydantic validators, just scoped to one attribute here
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        ...                       # TODO: return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        ...                       # TODO: compute new_celsius, raise ValueError if < -273.15, else self.celsius = new_celsius


def run_temperature_read():
    t = Temperature(0)
    return t.fahrenheit


def run_temperature_write():
    t = Temperature(100)
    t.fahrenheit = 32
    return t.celsius


def run_temperature_validates():
    t = Temperature(0)
    try:
        t.fahrenheit = -1000
        return "should have raised"
    except ValueError:
        return "raised ValueError as expected"


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
    check("Ex 1: Point.__repr__ looks like valid Python",
          lambda: run_point_repr() == "Point(1, 2)"),
    check("Ex 2a: Version.__eq__ compares by value, not identity",
          lambda: run_version_eq() == (True, False)),
    check("Ex 2b: sorted() orders Versions with no key= needed",
          lambda: run_version_sorted() == [Version(1, 9), Version(1, 10), Version(2, 0)]),
    check("Ex 3: Version == int falls back to False, doesn't raise",
          lambda: run_version_eq_unrelated() is False),
    check("Ex 4: Vector.__add__ combines componentwise into a new Vector",
          lambda: run_vector_add() == Vector(4, 6)),
    check("Ex 5a: Temperature.fahrenheit reads as a computed property",
          lambda: run_temperature_read() == 32),
    check("Ex 5b: Temperature.fahrenheit setter converts back to celsius",
          lambda: run_temperature_write() == 0),
    check("Ex 5c: Temperature.fahrenheit setter rejects below absolute zero",
          lambda: run_temperature_validates() == "raised ValueError as expected"),
]
print("\nAll green — lesson 30 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
