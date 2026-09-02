# Practice 36 — functools: memoizing, freezing arguments, and folding
# Run:  cd ~/learning/python && uv run python3 practice/36_functools.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from functools import lru_cache, partial, reduce


# ---------------------------------------------------------------------------
# Exercise 1 — add @lru_cache to a call-counting function.
# slow_double should be decorated with lru_cache so a repeat call with the
# same argument does NOT re-run the body (and so does not bump call_count
# again).
call_count = 0

# TODO: add @lru_cache(maxsize=None) directly above the def below.
def slow_double(n):
    global call_count
    call_count += 1
    return n * 2


def run_slow_double():
    global call_count
    call_count = 0
    slow_double(3)   # miss: runs for real, call_count -> 1
    slow_double(3)   # hit: same argument, call_count stays 1
    slow_double(4)   # miss: new argument, call_count -> 2
    return call_count


# ---------------------------------------------------------------------------
# Exercise 2 — read cache_info() to report hits vs. misses.
# Call counted_square with 5, 5, 5, 6 (in that order) and return the
# resulting (hits, misses) from its cache_info().
@lru_cache(maxsize=None)
def counted_square(n):
    return n * n


def run_cache_info():
    counted_square.cache_clear()   # start from a clean cache every run
    # TODO: call counted_square with 5, 5, 5, 6 in that order.
    info = counted_square.cache_info()
    return info.hits, info.misses


# ---------------------------------------------------------------------------
# Exercise 3 — build a narrower function with partial.
# power(base, exp) is defined below. Use partial to build cube, a callable
# that fixes exp=3 and takes only base.
def power(base, exp):
    return base ** exp


cube = None   # TODO: cube = partial(power, exp=3)


def run_partial_cube():
    return cube(2), cube(3)   # expect (8, 27)


# ---------------------------------------------------------------------------
# Exercise 4 — a custom aggregate with reduce, including the empty case.
# Return the longest string in `words` using reduce (not max()) — the
# combining function should keep whichever of the two strings it's given
# is longer. Pass "" as reduce's third (initial) argument so an empty list
# returns "" instead of raising TypeError.
def longest_word(words):
    ...   # TODO: return reduce(..., words, "")


def run_longest_word():
    return longest_word(["cat", "elephant", "dog"]), longest_word([])


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
    check("Ex 1: lru_cache skips the repeat call, call_count stays at 2",
          lambda: run_slow_double() == 2),
    check("Ex 2: cache_info reports 2 hits, 2 misses for 5,5,5,6",
          lambda: run_cache_info() == (2, 2)),
    check("Ex 3: partial(power, exp=3) fixes exp, base still open",
          lambda: run_partial_cube() == (8, 27)),
    check("Ex 4: reduce finds the longest word, empty list returns ''",
          lambda: run_longest_word() == ("elephant", "")),
]
print("\nAll green — lesson 36 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
