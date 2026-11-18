# Practice 112 — threading.Lock: protecting shared state by hand
# Run:  cd ~/learning/python && uv run python3 practice/112_threading_lock.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import threading
import time


# ---------------------------------------------------------------------------
# Exercise 1 — reproduce the unprotected-counter race condition for real.
# Write racy_counter(num_threads, bumps_per_thread) that:
#   - creates a shared counter starting at 0
#   - defines a bump() function that, bumps_per_thread times:
#       temp = counter
#       time.sleep(0)      <- widens the race window, do not skip this
#       counter = temp + 1
#     (use a `nonlocal` or a one-item list/dict to let bump() update the
#     counter defined in this function's scope)
#   - starts num_threads threads all running bump(), joins them all
#   - returns the final counter value
# The final value should usually come out LOWER than
# num_threads * bumps_per_thread, because this version has no lock.
def racy_counter(num_threads, bumps_per_thread):
    # TODO:
    # state = {"counter": 0}
    #
    # def bump():
    #     for _ in range(bumps_per_thread):
    #         temp = state["counter"]
    #         time.sleep(0)
    #         state["counter"] = temp + 1
    #
    # threads = [threading.Thread(target=bump) for _ in range(num_threads)]
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # return state["counter"]
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — fix Exercise 1 with a threading.Lock. Write
# locked_counter(num_threads, bumps_per_thread) with the identical shape,
# except every read-sleep-write sequence happens inside `with lock:`.
# The final value must come out EXACTLY num_threads * bumps_per_thread,
# every single time this is run.
def locked_counter(num_threads, bumps_per_thread):
    # TODO:
    # state = {"counter": 0}
    # lock = threading.Lock()
    #
    # def bump():
    #     for _ in range(bumps_per_thread):
    #         with lock:
    #             temp = state["counter"]
    #             time.sleep(0)
    #             state["counter"] = temp + 1
    #
    # threads = [threading.Thread(target=bump) for _ in range(num_threads)]
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # return state["counter"]
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — several threads safely appending to one shared list. Write
# collect_results(items) that:
#   - creates one shared list `results` and one threading.Lock
#   - starts one thread per item in `items`, where each thread's target
#     function computes item * 2 and appends it to `results` inside
#     `with lock:` (the lock protects the .append() call itself)
#   - joins every thread
#   - returns results, sorted (order of completion isn't guaranteed, so
#     sort before comparing)
def collect_results(items):
    # TODO:
    # results = []
    # lock = threading.Lock()
    #
    # def worker(value):
    #     doubled = value * 2
    #     with lock:
    #         results.append(doubled)
    #
    # threads = [threading.Thread(target=worker, args=(item,)) for item in items]
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # return sorted(results)
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
    # The race should make the final count come out wrong (lower than
    # expected) at least once across a few attempts -- the whole point.
    expected = 4 * 500
    for _ in range(5):
        result = racy_counter(4, 500)
        if result is None:
            return False
        if result != expected:
            return True
    return False


def _ex2():
    expected = 4 * 500
    for _ in range(3):
        result = locked_counter(4, 500)
        if result != expected:
            return False
    return True


def _ex3():
    result = collect_results([1, 2, 3, 4, 5])
    return result == [2, 4, 6, 8, 10]


results = [
    check("Ex 1: unprotected counter shows a real race (wrong total at least once)", _ex1),
    check("Ex 2: threading.Lock makes the counter exactly right every single run", _ex2),
    check("Ex 3: several threads append to one shared list safely via a lock", _ex3),
]
print("\nAll green — lesson 112 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
