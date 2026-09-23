# Practice 57 — dataclasses.field() and frozen=True
# Run:  cd ~/learning/python && uv run python3 practice/57_dataclass_field_and_frozen.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from dataclasses import FrozenInstanceError, dataclass, field


# ---------------------------------------------------------------------------
# Exercise 1 — fix a mutable default with default_factory.
# Define a dataclass `Cart` with one field, `items`, a list, defaulting to a
# fresh empty list per instance (NOT a plain `= []`, which would raise
# ValueError and, even if it didn't, would share one list across instances).
@dataclass
class Cart:
    # TODO: items: list = field(default_factory=list)
    items: list = None


# ---------------------------------------------------------------------------
# Exercise 2 — hide a field from repr.
# Define a dataclass `User` with fields `name` (str) and `password` (str),
# where `password` never shows up in the auto-generated repr string.
@dataclass
class User:
    name: str
    # TODO: password: str = field(repr=False)
    password: str = ""


# ---------------------------------------------------------------------------
# Exercise 3 — exclude a field from equality.
# Define a dataclass `Record` with fields `value` (int) and `id` (int,
# default 0), where two Records with the same `value` but different `id`
# still compare equal with ==.
@dataclass
class Record:
    value: int
    # TODO: id: int = field(default=0, compare=False)
    id: int = 0


# ---------------------------------------------------------------------------
# Exercise 4 — make a dataclass immutable.
# Define a frozen dataclass `Point` with fields `x` and `y` (both int), such
# that assigning to `.x` or `.y` after construction raises FrozenInstanceError.
# TODO: @dataclass(frozen=True)
@dataclass
class Point:
    x: int
    y: int


# ---------------------------------------------------------------------------
# Exercise 5 — combine frozen=True with field().
# Define a frozen dataclass `Config` with fields:
#   host: str
#   api_key: str, hidden from repr
#   retries: int, defaulting to 3, excluded from equality
# TODO: @dataclass(frozen=True)
@dataclass
class Config:
    host: str
    # TODO: api_key: str = field(repr=False)
    api_key: str = ""
    # TODO: retries: int = field(default=3, compare=False)
    retries: int = 0


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
    c1 = Cart()
    c2 = Cart()
    c1.items.append("apple")
    return c1.items == ["apple"] and c2.items == []


def _ex2():
    u = User("Ann", "secret")
    r = repr(u)
    return "Ann" in r and "secret" not in r


def _ex3():
    r1 = Record(5, id=1)
    r2 = Record(5, id=2)
    r3 = Record(9, id=1)
    return r1 == r2 and r1 != r3


def _ex4():
    p = Point(1, 2)
    try:
        p.x = 99
        return False
    except FrozenInstanceError:
        return p.x == 1 and p.y == 2


def _ex5():
    cfg = Config("api.example.com", "sk-secret")
    r = repr(cfg)
    if "sk-secret" in r:
        return False
    try:
        cfg.retries = 10
        return False
    except FrozenInstanceError:
        pass
    cfg2 = Config("api.example.com", "sk-secret", retries=999)
    return cfg == cfg2


results = [
    check("Ex 1: Cart's items field uses default_factory, not a shared list", _ex1),
    check("Ex 2: User's password is excluded from repr", _ex2),
    check("Ex 3: Record's id is excluded from equality", _ex3),
    check("Ex 4: Point is frozen — mutation raises FrozenInstanceError", _ex4),
    check("Ex 5: Config combines frozen=True with field() correctly", _ex5),
]
print("\nAll green — lesson 57 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
