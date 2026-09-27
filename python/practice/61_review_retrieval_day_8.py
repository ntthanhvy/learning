# Practice 61 — review day 8: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/61_review_retrieval_day_8.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 46, 50, 51,
# 53, 54, and 56. Replace each `...` (or the marked TODO body) and re-run
# until every check prints ✓. Try each from memory before reopening the old
# lesson.

from abc import ABC, abstractmethod
from collections import deque
import heapq
from operator import itemgetter
import random


# ---------------------------------------------------------------------------
# Exercise 1 (Day 46 — a format spec renders a NEW string; it never mutates
# the original value being formatted)
# format_price(price) should return price formatted with a thousands
# separator and exactly two decimal places, e.g. 1234.5 -> "1,234.50".
def format_price(price):
    # TODO: return f"{price:,.2f}"
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 50 — abc.ABC refuses to instantiate a subclass that hasn't
# overridden every @abstractmethod)
# PaymentMethod requires a charge(amount) method. CardPayment implements it;
# BrokenPayment (below, already complete) deliberately does not, to prove
# the ABC blocks it.
class PaymentMethod(ABC):
    @abstractmethod
    def charge(self, amount):
        ...


class CardPayment(PaymentMethod):
    # TODO: def charge(self, amount):
    #           return f"charged {amount}"
    ...


class BrokenPayment(PaymentMethod):
    pass  # intentionally incomplete — do not add charge() here


# ---------------------------------------------------------------------------
# Exercise 3 (Day 51 — heapq.heappop always returns the current smallest item)
# top_n_smallest(values, n) should push every value onto a heap, then pop n
# times, returning the results as a list in the order they were popped
# (ascending).
def top_n_smallest(values, n):
    heap = []
    for v in values:
        heapq.heappush(heap, v)
    # TODO: return [heapq.heappop(heap) for _ in range(n)]
    ...


# ---------------------------------------------------------------------------
# Exercise 4 (Day 53 — deque(maxlen=N) automatically drops the oldest item
# once full, no manual trimming needed)
# last_n_seen(values, n) should feed each value into a deque(maxlen=n) via
# append, then return the deque's current contents as a plain list.
def last_n_seen(values, n):
    window = deque(maxlen=n)
    # TODO: for v in values:
    #           window.append(v)
    #       return list(window)
    ...


# ---------------------------------------------------------------------------
# Exercise 5 (Day 54 — random.seed(n) makes the following sequence of calls
# reproducible; the same seed always yields the same sequence)
# seeded_rolls(seed, count) should seed the random module with `seed`, then
# return a list of `count` calls to random.randint(1, 6), in order.
def seeded_rolls(seed, count):
    random.seed(seed)
    # TODO: return [random.randint(1, 6) for _ in range(count)]
    ...


# ---------------------------------------------------------------------------
# Exercise 6 (Day 56 — itemgetter with two keys returns a tuple, sorted left
# to right, exactly like ORDER BY city, amount)
# sort_by_city_then_amount(rows) should return rows sorted by "city" first,
# breaking ties on "amount", using a single itemgetter call as the key.
def sort_by_city_then_amount(rows):
    # TODO: return sorted(rows, key=itemgetter("city", "amount"))
    ...


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_format_price_untouched_original():
    price = 1234.5
    label = format_price(price)
    return label == "1,234.50" and price == 1234.5


def _ex2_complete_subclass_instantiates():
    return CardPayment().charge(10) == "charged 10"


def _ex2_incomplete_subclass_raises_type_error():
    try:
        BrokenPayment()
        return False
    except TypeError:
        return True


def _ex3_smallest_three_in_ascending_order():
    return top_n_smallest([42, 17, 8, 91, 23, 5], 3) == [5, 8, 17]


def _ex4_window_keeps_only_last_n():
    return last_n_seen([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def _ex4_window_shorter_than_maxlen_keeps_all():
    return last_n_seen([1, 2], 5) == [1, 2]


def _ex5_same_seed_same_sequence():
    first = seeded_rolls(7, 5)
    second = seeded_rolls(7, 5)
    return first == second and len(first) == 5 and all(1 <= r <= 6 for r in first)


def _ex6_sorts_city_then_amount():
    rows = [
        {"city": "Hanoi", "amount": 120},
        {"city": "Hanoi", "amount": 80},
        {"city": "Danang", "amount": 200},
    ]
    result = sort_by_city_then_amount(rows)
    return result == [
        {"city": "Danang", "amount": 200},
        {"city": "Hanoi", "amount": 80},
        {"city": "Hanoi", "amount": 120},
    ]


results = [
    check("Ex 1: format_price renders a comma/decimal string, leaves the float untouched",
          _ex1_format_price_untouched_original),
    check("Ex 2: a complete ABC subclass instantiates; an incomplete one raises TypeError",
          lambda: _ex2_complete_subclass_instantiates() and _ex2_incomplete_subclass_raises_type_error()),
    check("Ex 3: top_n_smallest pops the heap's smallest items in ascending order",
          _ex3_smallest_three_in_ascending_order),
    check("Ex 4: deque(maxlen=n) keeps only the last n items, or fewer if not yet full",
          lambda: _ex4_window_keeps_only_last_n() and _ex4_window_shorter_than_maxlen_keeps_all()),
    check("Ex 5: seeding random with the same value reproduces the identical sequence",
          _ex5_same_seed_same_sequence),
    check("Ex 6: itemgetter('city', 'amount') sorts by city first, breaking ties on amount",
          _ex6_sorts_city_then_amount),
]

print("\nAll green — lesson 61 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
