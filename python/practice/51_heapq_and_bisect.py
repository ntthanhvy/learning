# Practice 51 — heapq & bisect: sorted-order structures without re-sorting
# Run:  cd ~/learning/python && uv run python3 practice/51_heapq_and_bisect.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import heapq
import bisect


# ---------------------------------------------------------------------------
# Exercise 1 — a min-heap of (priority, name) tuples.
# Push the three tasks below onto `heap` with heapq.heappush, then pop them
# all off with heapq.heappop, collecting the popped items into a list in
# the order they come out.
def run_heap_push_pop():
    heap = []
    for item in [(3, "write report"), (1, "fix outage"), (2, "review PR")]:
        # TODO: heapq.heappush(heap, item)
        ...
    popped = []
    while heap:
        # TODO: popped.append(heapq.heappop(heap))
        ...
    return popped


# ---------------------------------------------------------------------------
# Exercise 2 — top-N without a full sort.
# Given `scores`, return the 3 largest values using heapq.nlargest.
scores = [42, 17, 93, 8, 61, 75, 29]


def top_three(values):
    # TODO: return heapq.nlargest(3, values)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — bisect_right to bucket a score into a grade band.
# grades holds sorted cutoffs; labels has one more entry than grades.
# Use bisect.bisect_right to find the right label for a given score.
grades = [60, 70, 80, 90]
labels = ["F", "D", "C", "B", "A"]


def grade_for(score):
    # TODO: i = bisect.bisect_right(grades, score)
    #       return labels[i]
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — bisect.insort to insert into a sorted list in place.
# Insert `value` into the already-sorted `seq`, keeping it sorted, and
# return the resulting list.
def insert_sorted(seq, value):
    # TODO: bisect.insort(seq, value)
    #       return seq
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


results = [
    check("Ex 1: heap pops items out in ascending priority order",
          lambda: run_heap_push_pop() == [(1, "fix outage"), (2, "review PR"), (3, "write report")]),
    check("Ex 2: heapq.nlargest finds the top 3 without a full sort",
          lambda: top_three(scores) == [93, 75, 61]),
    check("Ex 3: bisect_right buckets a score into the right grade band",
          lambda: (grade_for(85), grade_for(90), grade_for(59)) == ("B", "A", "F")),
    check("Ex 4: bisect.insort keeps a list sorted after inserting",
          lambda: insert_sorted([60, 75, 90], 82) == [60, 75, 82, 90]),
]
print("\nAll green — lesson 51 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
