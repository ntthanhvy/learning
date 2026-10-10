# Practice 73 — concurrent.futures: running I/O-bound work at the same time
# Run:  cd ~/learning/python && uv run python3 practice/73_concurrent_futures_threadpoolexecutor.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import time
from concurrent.futures import ThreadPoolExecutor


# ---------------------------------------------------------------------------
# Exercise 1 — a plain loop vs. ThreadPoolExecutor.map() over the same slow
# calls. Write both functions below; slow_call(n) is already provided.
def slow_call(n):
    time.sleep(0.3)
    return n * n


# Write sequential_calls(items) that returns [slow_call(n) for n in items]
# using a plain loop/comprehension — no threading.
def sequential_calls(items):
    # TODO: return [slow_call(n) for n in items]
    pass


# Write concurrent_calls(items) that runs slow_call across `items` using
# ThreadPoolExecutor(max_workers=len(items)).map(), inside a `with` block,
# and returns the results as a list (map() returns an iterator — wrap it
# in list()).
def concurrent_calls(items):
    # TODO: with ThreadPoolExecutor(max_workers=len(items)) as pool:
    #           return list(pool.map(slow_call, items))
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — submit() + Future.result(): start two differently-timed
# calls, read the faster one back first. Write run_two(pool) that, given
# an already-open ThreadPoolExecutor `pool`:
#   - submits slow_call2("slow", 0.3)
#   - submits slow_call2("fast", 0.02)
#   - returns a tuple (fast_future.result(), slow_future.result())
#     i.e. the FAST result read first, then the slow one.
def slow_call2(name, delay):
    time.sleep(delay)
    return f"{name} done"


def run_two(pool):
    # TODO: slow_future = pool.submit(slow_call2, "slow", 0.3)
    #       fast_future = pool.submit(slow_call2, "fast", 0.02)
    #       return (fast_future.result(), slow_future.result())
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — an exception raised inside a submitted call re-surfaces at
# .result(), instead of disappearing silently. Write call_that_fails(pool)
# that, given an already-open ThreadPoolExecutor `pool`:
#   - submits boom() (defined below, which always raises ValueError)
#   - calls .result() on the returned future inside a try/except ValueError
#   - returns True if ValueError was caught, False if nothing was raised
def boom():
    raise ValueError("background failure")


def call_that_fails(pool):
    # TODO: future = pool.submit(boom)
    #       try:
    #           future.result()
    #           return False
    #       except ValueError:
    #           return True
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


def _ex1_correctness():
    items = [1, 2, 3]
    seq = sequential_calls(items)
    conc = concurrent_calls(items)
    if seq is None or conc is None:
        return False
    return seq == [1, 4, 9] and conc == [1, 4, 9]


def _ex1_speed():
    items = [0, 1, 2, 3, 4]
    start = time.perf_counter()
    sequential_calls(items)
    sequential_elapsed = time.perf_counter() - start

    start = time.perf_counter()
    concurrent_calls(items)
    concurrent_elapsed = time.perf_counter() - start

    # five 0.3s calls: sequential ~1.5s, concurrent ~0.3s -- concurrent
    # should be well under half the sequential time.
    return concurrent_elapsed < (sequential_elapsed / 2)


def _ex2():
    with ThreadPoolExecutor(max_workers=2) as pool:
        result = run_two(pool)
    if result is None:
        return False
    return result == ("fast done", "slow done")


def _ex3():
    with ThreadPoolExecutor(max_workers=1) as pool:
        result = call_that_fails(pool)
    return result is True


results = [
    check("Ex 1a: sequential_calls() and concurrent_calls() agree on the result", _ex1_correctness),
    check("Ex 1b: ThreadPoolExecutor.map() is meaningfully faster than a plain loop", _ex1_speed),
    check("Ex 2: submit()+result() reads the faster future back first, slow one second", _ex2),
    check("Ex 3: an exception inside a submitted call re-raises at .result()", _ex3),
]
print("\nAll green — lesson 73 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
