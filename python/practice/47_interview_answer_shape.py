# Practice 47 — Structuring a spoken technical answer
# Run:  cd ~/learning/python && uv run python3 practice/47_interview_answer_shape.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Each exercise asks for the four-part answer shape (claim / mechanism /
# example / contrast) from Lesson 47, applied to a mechanism from an earlier
# lesson. Fill in each function so it returns a dict with exactly those four
# keys, each mapped to a short sentence (a real one — the checks only verify
# *structure*, not correctness, so re-read the cited lesson if a claim feels
# shaky). Replace each `...` and re-run until every check prints ✓.

REQUIRED_PARTS = ("claim", "mechanism", "example", "contrast")


# ---------------------------------------------------------------------------
# Exercise 1 — Day 1: why is a mutable default argument (def f(items=[]))
# a trap? Return the four-part shape as a dict.
def mutable_default_argument_answer():
    # TODO: return {
    #     "claim": "...",
    #     "mechanism": "...",
    #     "example": "...",
    #     "contrast": "...",
    # }
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — Day 5: why does a generator let a 10 GB file stream through
# constant memory, where a list comprehension over the same file would not?
def generator_vs_list_answer():
    # TODO: return the four-part dict.
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — Day 30/37: what does @property let a class do that a plain
# attribute can't?
def property_answer():
    # TODO: return the four-part dict.
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — Day 20: what actually happens when a blocking call sits
# inside an async def route handler?
def blocking_call_in_async_answer():
    # TODO: return the four-part dict.
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
    """Structural check only: a dict with the four required keys, each a
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
    check("Ex 1: mutable_default_argument_answer has all four well-formed parts",
          lambda: is_well_formed(mutable_default_argument_answer())),
    check("Ex 2: generator_vs_list_answer has all four well-formed parts",
          lambda: is_well_formed(generator_vs_list_answer())),
    check("Ex 3: property_answer has all four well-formed parts",
          lambda: is_well_formed(property_answer())),
    check("Ex 4: blocking_call_in_async_answer has all four well-formed parts",
          lambda: is_well_formed(blocking_call_in_async_answer())),
]
print("\nAll green — lesson 47 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
