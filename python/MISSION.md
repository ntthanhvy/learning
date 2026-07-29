# Mission: Python Intensive — the Language Itself, for Data Work and Backend

## Why
Every other course here treats Python as a tool already owned. `data/` says it outright — "Python: working but basic … don't assume fluency" — and then teaches pandas *around* the language, glossing comprehensions and lambdas as jargon rather than teaching them. The result is a real ceiling: I can read simple Python and follow a pandas lesson, but I can't write Python fluently from a blank file, don't know the standard library, and couldn't build a Python service.

This course closes that gap. It teaches **Python the language and its standard library**, using data handling, pipelines, and wrangling as the vehicle — then extends into the backend work Python is actually hired for. The point is to stop borrowing fluency from `data/` and own it.

## Success looks like
- Write a data pipeline from an empty file with no framework: read a messy CSV/JSON, clean and reshape the records, aggregate them, and write the result out — using only the standard library, no pandas.
- Reach for the idiom instead of the loop: comprehensions, unpacking, `sorted(key=…)`, `dict`/`set` as lookup structures, `collections` (`defaultdict`, `Counter`), and `itertools`.
- Explain Python's object model out loud: names vs objects, mutability, why `b = a` aliases, why a mutable default argument is a trap, and when a copy is needed.
- Build lazy pipelines with iterators and generators, and explain why `yield` lets a 10 GB file stream through constant memory.
- Structure records with `dataclasses` and type hints, and read a fully annotated function signature without hesitation.
- Build and test a small FastAPI + pydantic service: request/response models, validation, dependency injection, async I/O, and `pytest` coverage of it.
- Judge when a plain Python script is right and when to reach for pandas — knowing both, rather than defaulting to one.

## Success does NOT look like
Encyclopedic API recall. The goal is fluency in the ~20% of Python that carries 80% of real data and backend work, plus the vocabulary to find the rest in the docs.

## Constraints
- **Starting point: can read and understand simple Python; everything else needs building from the ground up.** Do not assume comprehensions, decorators, generators, `*args`, or type hints are known — each is taught explicitly before use.
- Strong SQL, and `data/` is running in parallel — use SQL and the already-taught pandas *concepts* as bridges ("this is `GROUP BY` with a `defaultdict`"), but never re-teach either.
- Phase 1 is a 7-day date-locked intensive; Phase 2 is open-ended ~20 min/day. See `PLAN.md`.
- Python 3.12+ via `uv`. No system-wide installs; practice files run with `uv run python3 …` and are self-checking.
- Runs alongside `data/` and `backend/` — keep lessons to one tangible win, ~20 min.

## Out of scope
- **pandas and NumPy** — that is `data/`'s job, and duplicating it is explicitly forbidden. This course may *reference* a pandas equivalent for contrast in a single line, never teach it.
- Machine learning, data science, notebooks, visualization.
- Django, Flask, and ORMs (SQLAlchemy beyond vocabulary) — the backend phase is FastAPI + pydantic only.
- Packaging for distribution (PyPI, wheels), C extensions, CPython internals beyond what explains behavior.
- Async beyond what a FastAPI service needs — no deep asyncio event-loop internals.
