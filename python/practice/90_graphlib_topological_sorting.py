# Practice 90 — graphlib: ordering tasks by their dependencies
# Run:  cd ~/learning/python && uv run python3 practice/90_graphlib_topological_sorting.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from graphlib import TopologicalSorter, CycleError


# ---------------------------------------------------------------------------
# Exercise 1 — build a dependency graph and read off a valid order.
# Given a dict mapping each node to a list of its own predecessors (same
# shape TopologicalSorter's constructor accepts directly), return a list:
# a valid topological order of all the nodes.
def build_order(graph):
    # TODO: ts = TopologicalSorter(graph)
    #       return list(ts.static_order())
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — detect a cycle and recover the loop it reports.
# Given a dict shaped the same way as Exercise 1, but this time its
# dependencies contain a cycle, call static_order() and catch the
# resulting CycleError. Return the exception's second constructor argument
# (the list of nodes forming the cycle, e.g. ['x', 'y', 'x']) — or None if
# no CycleError was raised.
def find_cycle(graph):
    # TODO: ts = TopologicalSorter(graph)
    #       try:
    #           list(ts.static_order())
    #           return None
    #       except CycleError as e:
    #           return e.args[1]
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — which steps could run at the same time.
# Given a dict shaped the same way as Exercise 1, use the manual
# prepare()/get_ready()/done() protocol to return a list of tuples: one
# tuple per batch, in the order the batches became ready (each tuple is
# whatever get_ready() returned for that batch, sorted for a stable
# comparison).
def ready_batches(graph):
    # TODO: ts = TopologicalSorter(graph)
    #       ts.prepare()
    #       batches = []
    #       while ts.is_active():
    #           ready = ts.get_ready()
    #           batches.append(tuple(sorted(ready)))
    #           ts.done(*ready)
    #       return batches
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
    graph = {"a": [], "b": ["a"], "c": ["a", "b"]}
    order = build_order(graph)
    if not isinstance(order, list) or sorted(order) != ["a", "b", "c"]:
        return False
    position = {node: i for i, node in enumerate(order)}
    return position["a"] < position["b"] < position["c"]


def _ex2():
    graph = {"x": ["y"], "y": ["x"]}
    cycle = find_cycle(graph)
    return (
        isinstance(cycle, list)
        and len(cycle) >= 2
        and cycle[0] == cycle[-1]
        and set(cycle) == {"x", "y"}
    )


def _ex3():
    graph = {"b": ["a"], "c": ["a"], "d": ["b", "c"]}
    batches = ready_batches(graph)
    return batches == [("a",), ("b", "c"), ("d",)]


results = [
    check("Ex 1: build_order() returns a valid topological order", _ex1),
    check("Ex 2: find_cycle() recovers the exact cycle CycleError reports", _ex2),
    check("Ex 3: ready_batches() groups independent steps together", _ex3),
]
print("\nAll green — lesson 90 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
