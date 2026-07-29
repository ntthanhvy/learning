# Plan: Python Intensive

Two phases, per the mission. Phase 1 is date-locked with pre-assigned filenames
(same convention as `go/`); Phase 2 is open-ended and sequential (same
convention as `backend/` and `data/`).

## Phase 1 — Intensive week: the language, through data handling

Seven days, one lesson each, **date-locked**. The generator must use exactly
these filenames on exactly these dates, and must not pre-generate ahead.

| Day | Date | Lesson | File |
|-----|------|--------|------|
| 1 | 2026-07-29 | Names, objects & mutability | `0001-names-objects-and-mutability.html` |
| 2 | 2026-07-30 | Comprehensions & slicing: retiring the loop | `0002-comprehensions-and-slicing.html` |
| 3 | 2026-07-31 | dict & set: grouping without pandas | `0003-dict-set-and-grouping.html` |
| 4 | 2026-08-01 | Functions that pull their weight | `0004-functions-args-and-key.html` |
| 5 | 2026-08-02 | Iterators & generators: lazy pipelines | `0005-iterators-and-generators.html` |
| 6 | 2026-08-03 | Files, formats & context managers | `0006-files-formats-and-with.html` |
| 7 | 2026-08-04 | Dataclasses, typing & an ETL capstone | `0007-dataclasses-typing-capstone.html` |

The week is deliberately ordered so each day is a prerequisite of the next:
the object model explains why comprehensions build new lists; comprehensions
make `dict`/`set` grouping readable; grouping needs `key=` functions;
`key=` functions lead into generators; generators make file streaming make
sense; and the capstone spends all seven.

**Day 7 produces a working end-to-end ETL script** using only the standard
library — the tangible proof of the phase.

## Phase 2 — Open-ended main track: from language to service

Starts **2026-08-05**, sequential numbering from `0008-…`, no date-locking,
~20 min/day. Ordering is a spine, not a schedule — adapt to learning records.

**2a. Rounding out the language** (~1 week)
- Exceptions: raising, catching narrowly, custom exception types, `try/finally`
- Modules, packages, imports, `__name__`, project layout
- Environments and dependencies with `uv`; reading `pyproject.toml`
- Testing with `pytest`: assertions, fixtures, parametrize
- Decorators, and why they appear everywhere in FastAPI
- `pathlib`, `datetime`/timezones, `logging` (the three most-used stdlib corners left)

**2b. Backend in Python — FastAPI + pydantic** (main phase)
- HTTP handlers, path/query params, status codes
- pydantic models: validation, coercion, custom validators, settings
- Request/response schemas and why the type hints *are* the contract
- Dependency injection, and structuring an app beyond one file
- `async`/`await`: what it buys, when it doesn't, and blocking-call traps
- Talking to PostgreSQL from Python; where the `backend/` course's concepts land
- Testing endpoints with `httpx`; errors, middleware, and a deployable shape

Revisit this plan when Phase 2a ends — the backend depth should be driven by
what work and interviews actually demand by then.
