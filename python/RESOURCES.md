# Python Intensive — Resources

Ground every lesson in these. Prefer the official docs for behavior, the named
authors for *why*. Cite inline; each lesson recommends exactly one primary source.

## Knowledge — the language

- [Docs: The Python Tutorial](https://docs.python.org/3/tutorial/)
  The official guided introduction. Use for: the canonical spelling of any core-language feature; ch. 4–5 (control flow, data structures) back the whole intensive week.
- [Docs: The Python Language Reference — Data model](https://docs.python.org/3/reference/datamodel.html)
  Authoritative on objects, identity, and special methods. Use for: Day 1's names-vs-objects claims, and any "why does it behave like that" question.
- [Article: "Facts and Myths about Python names and values" — Ned Batchelder](https://nedbatchelder.com/text/names.html)
  The clearest explanation anywhere of assignment, aliasing, and mutability, with diagrams. Use for: Day 1 — this is the primary source for the object model.
- [Book: _Fluent Python_, 2nd ed. — Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
  The standard text on idiomatic Python. Use for: depth on the data model, sequences, iterators/generators, and dataclasses. (Paid — the docs cover the same ground for this course's purposes.)
- [Docs: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
  Official guide to `sorted()`, `key=`, and stability. Use for: Day 4 — the shortest path to sorting fluency.
- [Docs: `itertools`](https://docs.python.org/3/library/itertools.html) · [`collections`](https://docs.python.org/3/library/collections.html)
  The two stdlib modules that replace most hand-written data-munging loops. Use for: Days 3 and 5; the `itertools` recipes section is lesson-grade on its own.
- [Talk/course: "Generators: The Final Frontier" — David Beazley](https://www.dabeaz.com/generators/)
  Deep, practical treatment of generators as data-pipeline building blocks. Use for: Day 5's lazy-pipeline framing.
- [Blog: Trey Hunner](https://treyhunner.com/blog/archives/)
  Careful, beginner-aware writing on comprehensions, unpacking, and looping idioms. Use for: Day 2 — good at explaining *when not to* use a comprehension.
- [Docs: `dataclasses`](https://docs.python.org/3/library/dataclasses.html) · [`typing`](https://docs.python.org/3/library/typing.html)
  Use for: Day 7 — structuring records and reading annotated signatures.
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
  Use for: naming and layout conventions, so written code looks like the ecosystem's.

## Knowledge — backend (Phase 2b)

- [Docs: FastAPI](https://fastapi.tiangolo.com/)
  Unusually good official tutorial — genuinely teaches the concepts, not just the API. Use for: the whole backend phase; the "Tutorial - User Guide" is the spine.
- [Docs: pydantic](https://docs.pydantic.dev/latest/)
  Use for: validation, coercion rules, custom validators, and settings management.
- [Docs: pytest](https://docs.pytest.org/en/stable/)
  Use for: Phase 2a testing lessons; fixtures and `parametrize` especially.
- [Docs: uv — Astral](https://docs.astral.sh/uv/)
  The environment/dependency tool this course already uses to run practice files. Use for: the environments lesson.

## Practice

- [Exercism — Python track](https://exercism.org/tracks/python)
  Free, mentored, idiom-focused exercises. Use for: retrieval practice after a lesson; its feedback targets idiomatic style, which suits this course's goal.
- [Advent of Code](https://adventofcode.com/)
  Parsing-heavy puzzles solvable with the stdlib alone. Use for: realistic "messy input → structured records" drills, especially after Days 5–6.

## Wisdom — communities

- [r/learnpython](https://www.reddit.com/r/learnpython/)
  High-volume, beginner-friendly, fast answers. Use for: "is this idiomatic?" questions while the fundamentals are still settling.
- [Python Discord](https://www.pythondiscord.com/)
  Large, well-moderated, with live help channels. Use for: real-time unblocking and code review from practitioners.

## Gaps

- No source chosen yet for **Python-specific interview prep** (the data/backend interview framing lives in `data/RESOURCES.md`) — find one when Phase 2b starts.
- No canonical free text for FastAPI *architecture* beyond one file — the official docs stop at structure basics. Look for a well-regarded project-layout reference before the "structuring an app" lesson.
