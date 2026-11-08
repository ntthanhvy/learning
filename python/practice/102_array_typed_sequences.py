# Practice 102 — array: typed sequences without a list's per-item overhead
# Run:  cd ~/learning/python && uv run python3 practice/102_array_typed_sequences.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import array
import sys


# ---------------------------------------------------------------------------
# Exercise 1 — build a typed array from a typecode and an iterable.
# Given a typecode string and an iterable of values, return the
# array.array built from them.
def make_array(typecode, values):
    # TODO: return array.array(typecode, values)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — catch the TypeError a mismatched value raises.
# Given an existing array.array and a value, try appending the value to it.
# If it succeeds, return True. If it raises TypeError, return False instead
# of letting the exception propagate. (Do not mutate the caller's array
# permanently -- append to a copy, e.g. array.array(arr.typecode, arr).)
def can_append(arr, value):
    # TODO: copy = array.array(arr.typecode, arr)
    #       try:
    #           copy.append(value)
    #           return True
    #       except TypeError:
    #           return False
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — measure the memory gap between an equivalent list and array.
# Given a typecode and a range of n non-cached int values (hint: use
# range(1000, 1000 + n) to avoid Python's small-int cache skewing the
# result), return the ratio of the list's total size (its own size plus
# every element's own size) to the array's total size, as a float.
def memory_ratio(typecode, n):
    # TODO: values = range(1000, 1000 + n)
    #       lst = list(values)
    #       arr = array.array(typecode, values)
    #       list_total = sys.getsizeof(lst) + sum(sys.getsizeof(x) for x in lst)
    #       array_total = sys.getsizeof(arr)
    #       return list_total / array_total
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — round-trip an array's bytes through tobytes()/frombytes().
# Given an array.array, return a new array (same typecode, built from an
# empty array.array(arr.typecode)) rebuilt from arr.tobytes() via
# frombytes(), and confirm it holds the same values as the original.
def roundtrip_bytes(arr):
    # TODO: rebuilt = array.array(arr.typecode)
    #       rebuilt.frombytes(arr.tobytes())
    #       return rebuilt
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
    a = make_array('i', [1, 2, 3])
    return isinstance(a, array.array) and a.typecode == 'i' and list(a) == [1, 2, 3]


def _ex2():
    original = array.array('i', [1, 2, 3])
    ok_int = can_append(original, 4)
    ok_float = can_append(original, 3.5)
    # the caller's array must be untouched by either call
    unchanged = list(original) == [1, 2, 3]
    return ok_int is True and ok_float is False and unchanged


def _ex3():
    ratio = memory_ratio('l', 100_000)
    # a list of 100,000 non-cached ints should use noticeably more total
    # memory than the equivalent packed array -- comfortably more than 2x.
    return isinstance(ratio, float) and ratio > 2.0


def _ex4():
    original = array.array('i', [10, 20, 30, 40])
    rebuilt = roundtrip_bytes(original)
    return (
        isinstance(rebuilt, array.array)
        and rebuilt.typecode == original.typecode
        and list(rebuilt) == list(original)
    )


results = [
    check("Ex 1: make_array() builds a typed array from a typecode", _ex1),
    check("Ex 2: can_append() reports True/False without raising", _ex2),
    check("Ex 3: memory_ratio() shows array's packed-storage advantage", _ex3),
    check("Ex 4: roundtrip_bytes() rebuilds an equal array via tobytes/frombytes", _ex4),
]
print("\nAll green — lesson 102 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
