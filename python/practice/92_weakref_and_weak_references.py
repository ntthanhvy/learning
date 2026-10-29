# Practice 92 — weakref: references that don't keep things alive
# Run:  cd ~/learning/python && uv run python3 practice/92_weakref_and_weak_references.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import gc
import weakref


class Node:
    def __init__(self, name):
        self.name = name


# ---------------------------------------------------------------------------
# Exercise 1 — a weak reference does not keep its target alive.
# Given an object, return a weakref.ref to it. The caller will delete every
# other strong reference to the object afterward and expect calling your
# returned ref to then return None.
def make_weak_ref(obj):
    # TODO: return weakref.ref(obj)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — WeakValueDictionary as a self-cleaning cache.
# Given a weakref.WeakValueDictionary and a key/value pair, store the pair
# in the dictionary (as you would in a plain dict) and return the
# WeakValueDictionary itself.
def cache_weakly(wvd, key, value):
    # TODO: wvd[key] = value
    #       return wvd
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — finalize(): schedule cleanup, read back whether it has run.
# Given an object and a zero-argument callable `callback`, register a
# weakref.finalize() that calls `callback` when the object is collected.
# Return the finalize object itself (the caller checks its .alive attribute
# before and after deleting the object).
def schedule_cleanup(obj, callback):
    # TODO: return weakref.finalize(obj, callback)
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
    obj = Node("temp")
    ref = make_weak_ref(obj)
    if not isinstance(ref, weakref.ReferenceType):
        return False
    still_alive = ref() is obj
    del obj
    gc.collect()
    return still_alive and ref() is None


def _ex2():
    wvd = weakref.WeakValueDictionary()
    obj = Node("cached")
    result = cache_weakly(wvd, "k", obj)
    if result is not wvd or wvd["k"] is not obj:
        return False
    del obj
    gc.collect()
    return "k" not in wvd and len(wvd) == 0


def _ex3():
    ran = []
    obj = Node("finalized")
    f = schedule_cleanup(obj, lambda: ran.append(True))
    if not isinstance(f, weakref.finalize) or not f.alive:
        return False
    del obj
    gc.collect()
    return f.alive is False and ran == [True]


results = [
    check("Ex 1: make_weak_ref() returns None once the object is collected", _ex1),
    check("Ex 2: cache_weakly() stores in a WeakValueDictionary that self-cleans", _ex2),
    check("Ex 3: schedule_cleanup() runs its callback exactly once on collection", _ex3),
]
print("\nAll green — lesson 92 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
