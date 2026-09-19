# Practice 53 — collections.deque & namedtuple
# Run:  cd ~/learning/python && uv run python3 practice/53_deque_and_namedtuple.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from collections import deque
from collections import namedtuple


# ---------------------------------------------------------------------------
# Exercise 1 — work both ends of a deque.
# Start from `deque(["b", "c"])`, then:
#   - appendleft "a" onto the left end
#   - append "d" onto the right end
# Return the resulting deque.
def build_queue():
    q = deque(["b", "c"])
    # TODO: q.appendleft("a")
    ...
    # TODO: q.append("d")
    ...
    return q


# ---------------------------------------------------------------------------
# Exercise 2 — pop from both ends.
# Given a deque `q`, pop one item off the left end and one off the right
# end, and return them as a (left, right) tuple. Use popleft() and pop().
def pop_both_ends(q):
    # TODO: left = q.popleft()
    # TODO: right = q.pop()
    # TODO: return (left, right)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — a fixed-size sliding window with maxlen.
# Build a deque with maxlen=3, append each value in `values` one at a time,
# and return the final deque's contents as a plain list.
values = [10, 20, 30, 40, 50]


def last_n(values, n):
    # TODO: window = deque(maxlen=n)
    #       for v in values:
    #           window.append(v)
    #       return list(window)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — a namedtuple read both by name and by position.
# Build a namedtuple type called "Point" with fields "x" and "y", make an
# instance with x=3, y=4, and return it.
def make_point():
    # TODO: Point = namedtuple("Point", ["x", "y"])
    #       return Point(3, 4)
    ...


# ---------------------------------------------------------------------------
# Exercise 5 — namedtuple immutability.
# Given a namedtuple instance `p`, attempt to set p.x = 10 and return True
# if that raises AttributeError, False otherwise (don't let the exception
# escape this function).
def raises_on_mutation(p):
    try:
        # TODO: p.x = 10
        ...
        return False
    except AttributeError:
        return True


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


PointType = namedtuple("Point", ["x", "y"])

results = [
    check("Ex 1: build_queue appends/appendlefts onto the right ends",
          lambda: build_queue() == deque(["a", "b", "c", "d"])),
    check("Ex 2: pop_both_ends pops left then right correctly",
          lambda: pop_both_ends(deque(["a", "b", "c", "d"])) == ("a", "d")),
    check("Ex 3: last_n keeps only the most recent n items",
          lambda: last_n(values, 3) == [30, 40, 50]),
    check("Ex 4: make_point returns a namedtuple readable by name and position",
          lambda: (make_point().x, make_point().y, make_point()[0], make_point()[1]) == (3, 4, 3, 4)),
    check("Ex 5: mutating a namedtuple field raises AttributeError",
          lambda: raises_on_mutation(PointType(3, 4)) is True),
]
print("\nAll green — lesson 53 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
