# Practice 50 — abstract base classes: enforcing a shape by inheritance
# Run:  cd ~/learning/python && uv run python3 practice/50_abstract_base_classes.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Exercise 1 — a basic ABC with one @abstractmethod.
# Define PaymentMethod(ABC) with one abstract method: charge(self, amount).
# Its body should just be `...` (never used, only enforced).
class PaymentMethod(ABC):
    # TODO: @abstractmethod
    #       def charge(self, amount): ...
    ...


class CardPayment(PaymentMethod):
    def charge(self, amount):
        return f"charged ${amount} to card"


class BrokenPayment(PaymentMethod):
    pass  # deliberately incomplete — do not fix this class, the test needs it broken


def run_abstractmethod_checks():
    card_result = CardPayment().charge(10)
    try:
        BrokenPayment()
        broken_raised = False
    except TypeError:
        broken_raised = True
    return (card_result, broken_raised)


# ---------------------------------------------------------------------------
# Exercise 2 — the ABC itself can never be instantiated directly, even
# though it's fully declared (PaymentMethod above already has its one
# abstract method marked). Confirm that instantiating PaymentMethod itself
# raises TypeError.
def run_abc_not_instantiable_check():
    try:
        PaymentMethod()
        return False
    except TypeError:
        # TODO: return True
        ...


# ---------------------------------------------------------------------------
# Exercise 3 — stacking @abstractmethod under @property (Day 30/37).
# Define Shape(ABC) with an abstract property `area` returning float.
# Then Square(Shape) must implement it as a real @property.
class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        ...


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self) -> float:
        # TODO: return self.side ** 2
        ...


def run_abstract_property_checks():
    sq = Square(4)
    return sq.area


# ---------------------------------------------------------------------------
# Exercise 4 — a small registry that only accepts fully-implemented
# PaymentMethod subclasses. Write register(cls) that returns True if
# cls(*args) can be instantiated without TypeError (using no-arg
# instantiation attempt is enough here — CardPayment and BrokenPayment
# both take no __init__ args beyond self), and False if it raises TypeError.
def register(cls):
    try:
        cls()
        # TODO: return True
        ...
    except TypeError:
        return False


def run_registry_checks():
    return (register(CardPayment), register(BrokenPayment))


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
    check("Ex 1: complete subclass works, incomplete one raises TypeError at construction",
          lambda: run_abstractmethod_checks() == ("charged $10 to card", True)),
    check("Ex 2: the ABC itself can never be instantiated directly",
          lambda: run_abc_not_instantiable_check() is True),
    check("Ex 3: @abstractmethod stacked under @property is enforced as a property",
          lambda: run_abstract_property_checks() == 16),
    check("Ex 4: a registry function distinguishes complete from incomplete subclasses",
          lambda: run_registry_checks() == (True, False)),
]
print("\nAll green — lesson 50 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
