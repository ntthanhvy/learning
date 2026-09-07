# Practice 41 — typing extras: Protocol, TypedDict, and generics
# Run:  cd ~/learning/python && uv run python3 practice/41_typing_extras.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from typing import Protocol, TypedDict, TypeVar, Generic, runtime_checkable


# ---------------------------------------------------------------------------
# Exercise 1 — Protocol: structural typing ("if it quacks like a duck").
# Define a Protocol named Named with one method: name(self) -> str.
# Any class with a matching name() method satisfies it — no inheritance
# needed. Add @runtime_checkable so isinstance() works against it below.
@runtime_checkable
class Named(Protocol):
    # TODO: def name(self) -> str: ...
    ...


class Employee:
    def __init__(self, full_name):
        self.full_name = full_name

    def name(self) -> str:
        return self.full_name


class Product:
    def __init__(self, label):
        self.label = label

    def name(self) -> str:
        return self.label


class NotNamed:
    pass


def greet(item: Named) -> str:
    return f"Hello, {item.name()}!"


def run_protocol_checks():
    emp = Employee("Ada")
    prod = Product("Widget")
    other = NotNamed()
    return (greet(emp), greet(prod), isinstance(emp, Named), isinstance(other, Named))


# ---------------------------------------------------------------------------
# Exercise 2 — TypedDict: a dict with a fixed, named, typed shape.
# Define a TypedDict named Order with keys: sku (str), qty (int),
# unit_price (float).
class Order(TypedDict):
    # TODO: sku: str
    #       qty: int
    #       unit_price: float
    ...


def order_total(order: Order) -> float:
    return order["qty"] * order["unit_price"]


def run_typeddict_checks():
    order: Order = {"sku": "A1", "qty": 3, "unit_price": 2.5}
    return (order_total(order), sorted(order.keys()))


# ---------------------------------------------------------------------------
# Exercise 3 — Generic: a class parameterized over a type, so type checkers
# track what's inside without writing one class per element type.
# Define Box(Generic[T]) with __init__(self, item: T) storing self.item,
# and a method get(self) -> T returning it.
T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, item: T):
        # TODO: self.item = item
        ...

    def get(self) -> T:
        # TODO: return self.item
        ...


def run_generic_checks():
    int_box: Box[int] = Box(42)
    str_box: Box[str] = Box("hi")
    return (int_box.get(), str_box.get())


# ---------------------------------------------------------------------------
# Exercise 4 — a generic function using a TypeVar, not just a generic class.
# Write first_or_default(items: list[T], default: T) -> T that returns
# items[0] if items is non-empty, else default. One TypeVar, so the
# return type is tied to whichever type was actually passed in.
def first_or_default(items, default):
    # TODO: return items[0] if items else default
    ...


def run_typevar_function_checks():
    return (
        first_or_default([1, 2, 3], 0),
        first_or_default([], 0),
        first_or_default(["a"], "z"),
    )


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
    check("Ex 1: Protocol is satisfied structurally, no inheritance needed",
          lambda: run_protocol_checks() == ("Hello, Ada!", "Hello, Widget!", True, False)),
    check("Ex 2: TypedDict keys/values behave like a plain dict at runtime",
          lambda: run_typeddict_checks() == (7.5, ["qty", "sku", "unit_price"])),
    check("Ex 3: Generic[T] Box works the same for any T",
          lambda: run_generic_checks() == (42, "hi")),
    check("Ex 4: a TypeVar-based function ties return type to the input type",
          lambda: run_typevar_function_checks() == (1, 0, "a")),
]
print("\nAll green — lesson 41 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
