# Practice 32 — @classmethod and @staticmethod
# Run:  cd ~/learning/python && uv run python3 practice/32_classmethod_and_staticmethod.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

# ---------------------------------------------------------------------------
# Exercise 1 — @classmethod as an alternative constructor.
# Complete Money.from_dollars: parse a dollars string like "5.00" into cents
# (round(float(dollars_str) * 100)), then return a new instance via cls(...)
# — not Money(...) by name, so Exercise 3's subclass check works correctly.
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __repr__(self):
        return f"Money({self.cents})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    @classmethod
    def from_dollars(cls, dollars_str):
        ...                   # TODO: cents = round(float(dollars_str) * 100)
        ...                   # TODO: return cls(cents)

    @staticmethod
    def is_valid_dollars(dollars_str):
        try:
            return float(dollars_str) >= 0
        except ValueError:
            return False


def run_from_dollars():
    return Money.from_dollars("5.00")


# ---------------------------------------------------------------------------
# Exercise 2 — @staticmethod: no self, no cls, just a grouped check.
# Money.is_valid_dollars is already written above (nothing to fill in there);
# complete parse_amount() below to use it as a guard before calling
# Money.from_dollars, returning None for an invalid amount instead of
# letting a ValueError escape.
def parse_amount(dollars_str):
    if not Money.is_valid_dollars(dollars_str):
        ...                   # TODO: return None
    ...                       # TODO: return Money.from_dollars(dollars_str)


def run_parse_amount():
    good = parse_amount("12.50")
    bad = parse_amount("not a number")
    return good, bad


# ---------------------------------------------------------------------------
# Exercise 3 — an inherited classmethod builds the subclass, not the parent.
# Nothing to fill in here — GiftCard inherits from_dollars unmodified.
# Because Exercise 1's from_dollars calls cls(cents) rather than
# Money(cents), calling GiftCard.from_dollars(...) should return a
# GiftCard instance, not a plain Money instance.
class GiftCard(Money):
    pass


def run_subclass_builds_itself():
    card = GiftCard.from_dollars("10.00")
    return type(card).__name__, card.cents


# ---------------------------------------------------------------------------
# Exercise 4 — sort the three method shapes.
# Given three unlabeled method bodies below (as plain functions standing in
# for method bodies, each written as it would appear inside a class),
# decide which decorator each one needs based on what it touches:
#   - reads/writes an instance's own state (self.___)      -> "instance"
#   - builds and returns a new instance via the class (cls) -> "classmethod"
#   - touches neither self nor cls                          -> "staticmethod"
#
# def body_a(self):
#     return self.cents / 100
#
# def body_b(cls, s):
#     return cls(round(float(s) * 100))
#
# def body_c(s):
#     return s.strip().startswith("$")
#
# Fill in classify_methods() to return the three answers in order (a, b, c).
def classify_methods():
    ...                       # TODO: return "instance", "classmethod", "staticmethod"


def run_classify_methods():
    return classify_methods()


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
    check("Ex 1: Money.from_dollars builds a Money via cls(...)",
          lambda: run_from_dollars() == Money(500)),
    check("Ex 2: parse_amount uses the staticmethod guard before constructing",
          lambda: run_parse_amount() == (Money(1250), None)),
    check("Ex 3: an inherited classmethod builds the subclass, not the parent",
          lambda: run_subclass_builds_itself() == ("GiftCard", 1000)),
    check("Ex 4: correctly classifies instance / classmethod / staticmethod",
          lambda: run_classify_methods() == ("instance", "classmethod", "staticmethod")),
]
print("\nAll green — lesson 32 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
