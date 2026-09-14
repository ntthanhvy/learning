# Practice 48 — Reading someone else's code out loud
# Run:  cd ~/learning/python && uv run python3 practice/48_code_walkthrough_answer_shape.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Each exercise gives a small, unfamiliar-looking stdlib-only function built
# from mechanisms already taught in earlier lessons (cited in each comment).
# Fill in the matching `..._walkthrough()` function so it returns a dict with
# exactly three keys — purpose / shape / sharp_edge — following Lesson 48's
# three-move code-walkthrough shape. The checks only verify *structure* (three
# distinct, non-trivial sentences), not correctness, so re-read the cited
# lesson if a sharp edge feels shaky. Replace each `...` and re-run until
# every check prints ✓.

REQUIRED_PARTS = ("purpose", "shape", "sharp_edge")


# ---------------------------------------------------------------------------
# Exercise 1 — Day 1 (mutable defaults) + Day 2 (comprehensions).
# def collect_tags(items, seen=[]):
#     seen += [t for row in items for t in row.get("tags", [])]
#     return seen
# Walk through it: what does it do, how does it get there, and what is the
# one detail a careless reading would miss?
def collect_tags_walkthrough():
    # TODO: return {
    #     "purpose": "...",
    #     "shape": "...",
    #     "sharp_edge": "...",
    # }
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — Day 5 (generators) + Day 6 (context managers).
# def read_nonblank_lines(path):
#     with open(path) as f:
#         for line in f:
#             stripped = line.strip()
#             if stripped:
#                 yield stripped
# Walk through it.
def read_nonblank_lines_walkthrough():
    # TODO: return the three-part dict.
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — Day 12 (decorators) + Day 36 (functools.lru_cache).
# from functools import lru_cache
# def log_calls(fn):
#     @lru_cache(maxsize=None)
#     def wrapper(*args):
#         print(f"called with {args}")
#         return fn(*args)
#     return wrapper
# Walk through it.
def log_calls_walkthrough():
    # TODO: return the three-part dict.
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — Day 30/37 (@property) + Day 31 (__eq__/__hash__).
# class Point:
#     def __init__(self, x, y):
#         self._x, self._y = x, y
#     @property
#     def x(self):
#         return self._x
#     def __eq__(self, other):
#         return (self._x, self._y) == (other._x, other._y)
# Walk through it.
def point_class_walkthrough():
    # TODO: return the three-part dict.
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


def is_well_formed(answer, min_words=5):
    """Structural check only: a dict with the three required keys, each a
    distinct, non-trivial sentence (at least `min_words` words, and no two
    parts identical to each other)."""
    if not isinstance(answer, dict):
        return False
    if set(answer.keys()) != set(REQUIRED_PARTS):
        return False
    sentences = [str(answer[part]).strip() for part in REQUIRED_PARTS]
    if any(len(s.split()) < min_words for s in sentences):
        return False
    # every part must be genuinely different text, not copy-pasted
    if len(set(sentences)) != len(sentences):
        return False
    return True


results = [
    check("Ex 1: collect_tags_walkthrough has all three well-formed parts",
          lambda: is_well_formed(collect_tags_walkthrough())),
    check("Ex 2: read_nonblank_lines_walkthrough has all three well-formed parts",
          lambda: is_well_formed(read_nonblank_lines_walkthrough())),
    check("Ex 3: log_calls_walkthrough has all three well-formed parts",
          lambda: is_well_formed(log_calls_walkthrough())),
    check("Ex 4: point_class_walkthrough has all three well-formed parts",
          lambda: is_well_formed(point_class_walkthrough())),
]
print("\nAll green — lesson 48 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
