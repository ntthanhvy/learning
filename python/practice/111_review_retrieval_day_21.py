# Practice 111 — review day 21: retrieval across Days 108-110
# Run:  cd ~/learning/python && uv run python3 practice/111_review_retrieval_day_21.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 108, 109, and 110.
# Replace each `...`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import queue
import threading
from fractions import Fraction
from multiprocessing import Process, Queue as MPQueue


# ---------------------------------------------------------------------------
# Exercise 1 (Day 108 — queue.Queue: a producer and a consumer thread
# handing items through safely, with task_done()/join() confirming the
# work actually finished, not merely dequeued)
def run_producer_consumer(items):
    """Start one producer thread that put()s every item in `items` onto a
    shared queue.Queue, and one worker thread that get()s each item,
    doubles it, appends the result to a list, and calls task_done() on it.
    Use q.join() to wait until every item is truly finished, then return
    the list of doubled results (any order is fine)."""
    q = queue.Queue()
    results = []

    def producer():
        for item in items:
            q.put(item)

    def worker():
        while True:
            item = q.get()
            results.append(item * 2)
            # TODO: tell the queue this item is fully processed
            # q.task_done()

    # TODO: start a producer thread and a daemon worker thread, then
    #       q.join() to block until every put() item has had task_done()
    #       called on it, and return results.
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 109 — multiprocessing: a child Process computing a
# result and passing it back through a multiprocessing.Queue, never a
# plain shared variable)
def _square_into_queue(n, q):
    q.put(n * n)


def square_in_child_process(n):
    """Start a multiprocessing.Process that calls _square_into_queue(n, q)
    for a fresh multiprocessing.Queue q, join it, and return the single
    value the child put() onto that queue."""
    # TODO: q = MPQueue()
    #       p = Process(target=_square_into_queue, args=(n, q))
    #       p.start()
    #       result = q.get()
    #       p.join()
    #       return result
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 110 — fractions: exact sums from integer pairs, and
# building from a str to avoid the float-construction trap)
def exact_third_sum():
    """Return Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3) -- should
    be exactly equal to 1, not a near-miss float."""
    # TODO: return Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)
    ...


def fraction_from_string(text):
    """Return a Fraction built from the given string (e.g. "1/10"),
    never passing through a float literal."""
    # TODO: return Fraction(text)
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


def _ex1():
    out = run_producer_consumer([1, 2, 3])
    return out is not None and sorted(out) == [2, 4, 6]


def _ex2():
    if __name__ != "__main__":
        return False
    return square_in_child_process(6) == 36


def _ex3():
    total = exact_third_sum()
    tenth = fraction_from_string("1/10")
    return total == 1 and tenth == Fraction(1, 10)


if __name__ == "__main__":
    results = [
        check("Ex 1 (Day 108): producer/consumer queue finishes via task_done()/join()", _ex1),
        check("Ex 2 (Day 109): child Process returns a result via multiprocessing.Queue", _ex2),
        check("Ex 3 (Day 110): exact Fraction sum and str-built Fraction, no float imprecision", _ex3),
    ]

    print("\nAll green — lesson 111 done. 🎉" if all(results)
          else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
