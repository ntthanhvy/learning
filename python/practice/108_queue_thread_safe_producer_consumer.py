# Practice 108 — queue: handing work between threads safely
# Run:  cd ~/learning/python && uv run python3 practice/108_queue_thread_safe_producer_consumer.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import queue
import threading


# ---------------------------------------------------------------------------
# Exercise 1 — a producer thread and a consumer thread sharing one
# queue.Queue, with no manual lock. Write run_producer_consumer(items) that:
#   - creates a plain queue.Queue()
#   - starts one thread that puts every item from `items` (in order) onto
#     the queue
#   - starts a second thread that gets len(items) items off the queue and
#     appends each one to a list
#   - joins both threads, then returns the consumer's list
def run_producer_consumer(items):
    # TODO:
    # q = queue.Queue()
    # results = []
    #
    # def producer():
    #     for item in items:
    #         q.put(item)
    #
    # def consumer():
    #     for _ in range(len(items)):
    #         results.append(q.get())
    #
    # t1 = threading.Thread(target=producer)
    # t2 = threading.Thread(target=consumer)
    # t1.start(); t2.start()
    # t1.join(); t2.join()
    # return results
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — put_nowait()/get_nowait() on a bounded queue, catching Full
# and Empty instead of blocking. Write bounded_overflow(maxsize) that:
#   - creates queue.Queue(maxsize=maxsize)
#   - put_nowait()s `maxsize` plain integers (0, 1, 2, ... up to maxsize-1)
#     onto it, so the queue is now completely full
#   - tries one more put_nowait() (any value) inside a try/except that
#     catches queue.Full; set a bool `overflowed` to True if Full was raised
#   - get_nowait()s every item off (there are exactly `maxsize` of them)
#   - tries one more get_nowait() inside a try/except that catches
#     queue.Empty; set a bool `drained` to True if Empty was raised
#   - returns (overflowed, drained) -- both should end up True
def bounded_overflow(maxsize):
    # TODO:
    # q = queue.Queue(maxsize=maxsize)
    # for n in range(maxsize):
    #     q.put_nowait(n)
    #
    # overflowed = False
    # try:
    #     q.put_nowait("one too many")
    # except queue.Full:
    #     overflowed = True
    #
    # for _ in range(maxsize):
    #     q.get_nowait()
    #
    # drained = False
    # try:
    #     q.get_nowait()
    # except queue.Empty:
    #     drained = True
    #
    # return (overflowed, drained)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — task_done()/join(): confirm a worker thread's work is fully
# finished, not just removed from the queue. Write run_worker_and_join(items)
# that:
#   - creates a plain queue.Queue()
#   - starts one daemon worker thread that loops forever: gets an item,
#     appends item * 2 to a shared list, then calls q.task_done()
#     (this is the part a learner must not skip -- without it, join() below
#     hangs forever)
#   - puts every item from `items` onto the queue
#   - calls q.join() to block until every item has had task_done() called
#   - returns the shared list (sorted, for a deterministic comparison)
def run_worker_and_join(items):
    # TODO:
    # q = queue.Queue()
    # processed = []
    #
    # def worker():
    #     while True:
    #         item = q.get()
    #         processed.append(item * 2)
    #         q.task_done()
    #
    # threading.Thread(target=worker, daemon=True).start()
    # for item in items:
    #     q.put(item)
    # q.join()
    # return sorted(processed)
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond, timeout_note=None):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    items = ["a", "b", "c", "d"]
    result = run_producer_consumer(items)
    return result == items


def _ex2():
    result = bounded_overflow(3)
    if result is None:
        return False
    return result == (True, True)


def _ex3():
    result = run_worker_and_join([1, 2, 3, 4])
    return result == [2, 4, 6, 8]


results = [
    check("Ex 1: producer and consumer threads exchange items in order via Queue", _ex1),
    check("Ex 2: put_nowait()/get_nowait() raise Full/Empty on a bounded queue", _ex2),
    check("Ex 3: task_done()/join() confirm every item was fully processed", _ex3),
]
print("\nAll green — lesson 108 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
