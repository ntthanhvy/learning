# Practice 109 — multiprocessing: sidestepping the GIL for real CPU work
# Run:  cd ~/learning/python && uv run python3 practice/109_multiprocessing_sidestepping_the_gil.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import os
from multiprocessing import Process, Queue, Pool


# ---------------------------------------------------------------------------
# Exercise 1 — start a Process, join it, and confirm it really is a separate
# OS process (a different pid from the parent). Write child_pid(q) as the
# target function: it should put os.getpid() onto the given queue `q`.
# Then write run_child_and_get_pid() that:
#   - creates a multiprocessing.Queue
#   - starts a Process with target=child_pid, args=(q,)
#   - joins it
#   - returns (parent_pid, child_pid_value) where parent_pid is this
#     process's own os.getpid(), and child_pid_value is whatever the
#     child put on the queue
def child_pid(q):
    # TODO:
    # q.put(os.getpid())
    pass


def run_child_and_get_pid():
    # TODO:
    # q = Queue()
    # p = Process(target=child_pid, args=(q,))
    # p.start()
    # child_value = q.get()
    # p.join()
    # return (os.getpid(), child_value)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — pass a result back through a Queue instead of relying on a
# shared variable (a plain shared variable would NOT work here -- the child
# has its own private memory). Write produce_list(q, items) as the target:
# it should put a new list, [item * 2 for item in items], onto `q`.
# Then write run_doubling(items) that:
#   - creates a Queue
#   - starts a Process with target=produce_list, args=(q, items)
#   - gets the result off the queue
#   - joins the process
#   - returns the result
def produce_list(q, items):
    # TODO:
    # q.put([item * 2 for item in items])
    pass


def run_doubling(items):
    # TODO:
    # q = Queue()
    # p = Process(target=produce_list, args=(q, items))
    # p.start()
    # result = q.get()
    # p.join()
    # return result
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — Pool.map(): run one function across several inputs using
# worker processes, confirming results come back in input order. Write
# cube(x) (module-level, so it stays picklable) returning x ** 3.
# Then write run_pool_map(values) that:
#   - opens a Pool with 2 worker processes (use it as a context manager)
#   - calls pool.map(cube, values)
#   - returns the result as a plain list
def cube(x):
    # TODO:
    # return x ** 3
    pass


def run_pool_map(values):
    # TODO:
    # with Pool(2) as p:
    #     return list(p.map(cube, values))
    pass


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
    parent_pid, child_value = run_child_and_get_pid()
    if parent_pid is None or child_value is None:
        return False
    return child_value != parent_pid


def _ex2():
    result = run_doubling([1, 2, 3, 4])
    return result == [2, 4, 6, 8]


def _ex3():
    result = run_pool_map([1, 2, 3, 4])
    return result == [1, 8, 27, 64]


if __name__ == "__main__":
    results = [
        check("Ex 1: Process + Queue confirm the child has a different pid", _ex1),
        check("Ex 2: a result crosses the process boundary via Queue, not a shared var", _ex2),
        check("Ex 3: Pool.map() runs across worker processes, results in input order", _ex3),
    ]
    print("\nAll green — lesson 109 done. 🎉" if all(results)
          else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
