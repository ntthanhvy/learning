# Practice 31 — __hash__: why a custom __eq__ can silently break dict and set
# Run:  cd ~/learning/python && uv run python3 practice/31_hash_eq_and_mutability.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

# ---------------------------------------------------------------------------
# Exercise 1 — a plain class is hashable by default.
# Nothing to fill in here — this exercise is a live demonstration that a
# plain class (no __eq__ defined) is hashable out of the box, using the
# default identity-based __hash__ inherited from object.
class PlainPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def run_plain_point_hashable():
    p = PlainPoint(1, 2)
    hash(p)                  # would raise TypeError if this were unhashable
    d = {p: "first point"}
    return p in d


# ---------------------------------------------------------------------------
# Exercise 2 — defining __eq__ alone makes a class unhashable.
# Complete UnsafeMoney's __eq__ (compare by .cents, guarding with isinstance
# and returning NotImplemented for an unrelated type, exactly like Day 30).
# Do NOT add a __hash__ method — the point of this exercise is to observe
# Python's implicit-None rule kick in once __eq__ exists.
class UnsafeMoney:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        if not isinstance(other, UnsafeMoney):
            ...               # TODO: return NotImplemented
        ...                   # TODO: return self.cents == other.cents


def run_unsafe_money_unhashable():
    eq_result = UnsafeMoney(500) == UnsafeMoney(500)   # exercises the __eq__ TODOs above
    try:
        hash(UnsafeMoney(500))
        hashable = "should have raised TypeError"
    except TypeError:
        hashable = "raised TypeError as expected"
    return eq_result, hashable


# ---------------------------------------------------------------------------
# Exercise 3 — writing a matching __hash__ restores hashability.
# Complete Money.__hash__ so it hashes the same field __eq__ compares
# (self.cents), using the built-in hash() function on that field.
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __hash__(self):
        ...                   # TODO: return hash(self.cents)


def run_money_hashable():
    hash(Money(500))          # should not raise
    return "hashable"


# ---------------------------------------------------------------------------
# Exercise 4 — equal Money objects share one dict slot.
# Using Money from Exercise 3: two separately constructed Money(500)
# objects should compare equal AND hash equal, so inserting both into a
# dict under Money keys leaves only one entry, with the second insert's
# value winning (normal dict-overwrite behavior).
def run_money_shared_slot():
    prices = {Money(500): "first", Money(500): "second"}
    return len(prices), prices[Money(500)]


# ---------------------------------------------------------------------------
# Exercise 5 — the mutable-class wrong-bucket bug, observed live.
# Complete Tag.__hash__ (hash self.label, same mistake the lesson warns
# against — Tag.label CAN be reassigned after construction). Then watch
# run_tag_wrong_bucket demonstrate the bug: after mutating .label post
# insertion, membership testing by the new state fails even though the
# object is still physically inside the set.
class Tag:
    def __init__(self, label):
        self.label = label

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        return self.label == other.label

    def __hash__(self):
        ...                   # TODO: return hash(self.label) -- intentionally unsafe, see lesson

    def __repr__(self):
        return f"Tag({self.label!r})"


def run_tag_wrong_bucket():
    t = Tag("draft")
    seen = {t}
    t.label = "published"
    # t is still physically inside `seen` (same object), but lookup by the
    # new state should fail — the wrong-bucket bug the lesson describes.
    still_contains_by_identity = any(item is t for item in seen)
    findable_by_new_value = Tag("published") in seen
    return still_contains_by_identity, findable_by_new_value


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
    check("Ex 1: a plain class is hashable by default",
          lambda: run_plain_point_hashable() is True),
    check("Ex 2: __eq__ compares by value, and defining it alone makes the class unhashable",
          lambda: run_unsafe_money_unhashable() == (True, "raised TypeError as expected")),
    check("Ex 3: a matching __hash__ restores hashability",
          lambda: run_money_hashable() == "hashable"),
    check("Ex 4: equal Money objects share one dict slot",
          lambda: run_money_shared_slot() == (1, "second")),
    check("Ex 5: mutating a stored Tag's field breaks lookup by new value",
          lambda: run_tag_wrong_bucket() == (True, False)),
]
print("\nAll green — lesson 31 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
