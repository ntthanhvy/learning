# Python Intensive — working notes & conventions

Authoritative for lesson generation. `daily-lessons-prompt.md` defers to this file.

## Course conventions

Identical to `data/` unless stated:

- Every jargon term gets `<dfn data-en="…" data-vn="…">term</dfn>` and the page
  loads `../assets/gloss.js`. **No inline translations in prose.** Every new
  term also gets a row in `reference/glossary.html`.
- Quizzes use `../assets/quiz.js`. Options within one question must have the
  same word count — position and length must carry no signal.
- Every lesson ends with `<script src="../assets/nav.js"></script>` and is
  registered in `assets/nav.js` `LESSONS` (new reference sheets go in `REFS`).
- Every lesson: one tangible win, ~20 min, cites `RESOURCES.md`, recommends one
  primary source, and closes with a reminder to ask the teacher follow-ups —
  Vietnamese welcome.
- `assets/quiz.js` here differs from `data/`'s by one character: the
  `QUIZ_COURSE` regex includes `python`. If assets are ever re-copied from
  another course, re-add it or quiz results stop reaching the DB.

## The hard rule: no pandas

`MISSION.md` puts pandas and NumPy out of scope — they belong to `data/`, which
is running in parallel and is 21 lessons deep. **Never teach a pandas API in
this course.** A one-line contrast ("pandas spells this `groupby`") is allowed
and useful; a worked pandas example is not.

This matters operationally: on 2026-07-23..24 two generators produced
overlapping lessons on the same topics under different numbers and blocked
every `git pull` for a week. Topic overlap between courses is the same failure
in slower motion. When a topic could belong to either course, ask: *is the
subject the language, or the library?* Language → here. Library → `data/`.

## Learner profile

Can read and understand simple Python; **everything else is being built from
zero**. Do not use a construct before the lesson that teaches it — in
particular comprehensions (Day 2), `key=` functions and `lambda` (Day 4),
generators (Day 5), and type hints (Day 7). Before Day 2, code samples use
plain `for` loops on purpose.

Strong SQL, and pandas *concepts* are landing in parallel via `data/`. Use both
as bridges — "this is `GROUP BY`, done by hand" — but never re-teach either.

## Phase 1 is date-locked

`PLAN.md` pre-assigns Days 1–7 to exact filenames and dates
(2026-07-29 → 2026-08-04). Use them exactly; do not pre-generate ahead of the
date. From 2026-08-05 the course goes open-ended and sequential from
`0008-…`, following the Phase 2 spine in `PLAN.md` — adapt ordering to the
learning records rather than marching through it.

## Practice files

`practice/NN_<name>.py`, one per lesson, mirroring `data/`'s self-checking
style but **standard library only** — no third-party imports, so `uv run
python3 practice/NN_x.py` needs no `--with`. Each file is a series of small
TODOs with a `check()` that prints ✓/✗ per task and a final tally.

Before shipping a practice file, verify in a scratch dir that (a) the shipped
form runs and reports ✗ for the unsolved TODOs without crashing, and (b) a
solved copy prints all ✓. A traceback instead of a ✗ is a bug — the file must
fail *gracefully* so the learner sees which task failed.

## Generation log

- 2026-07-29 — Course created in a live session (not the headless run), on the
  user's request for a Python course majoring in data handling, pipelines, and
  wrangling, then backend. Scope was negotiated with the user: complement
  `data/` rather than overlap it (hence the no-pandas rule), FastAPI + pydantic
  for the backend phase, intensive week first then open-ended. Day 1 was
  written by hand in that session, so the headless run on 2026-07-29 was
  already past — Day 2 (2026-07-30) is the first lesson CI generates here.
- 2026-07-29 — **DB schema touched.** `course_progress` had a CHECK constraint
  allowing only `go|rust|backend|data`, so the first `record-progress python …`
  was rejected outright. Widened it to include `python`:
  `ALTER TABLE course_progress DROP CONSTRAINT course_progress_course_check;`
  then re-added with `python` in the array. There is **no migration file
  anywhere in the repo** — the schema lives only in the Neon DB, so this note
  is the only record of the change. Any future course needs the same widening,
  plus the `QUIZ_COURSE` regex in that course's `assets/quiz.js`, or its
  progress and quiz results vanish silently.
- 2026-07-30 — **Day 2 generated** (`lessons/0002-comprehensions-and-slicing.html`),
  the first lesson this headless run actually produced end-to-end. Taught list
  comprehensions ground-up as the one-line form of "empty list, loop, append,
  return" (Day 1's `clean()` from section 6 rewritten as the running example),
  enough dict/set comprehension to recognize the `{}`-with-colon /
  `{}`-without-colon shapes (explicitly not mastery — that's Day 3), and
  slicing (`seq[start:stop:step]`, stop-exclusive, negative index, step).
  Bridged from SQL per the baseline record (`SELECT/FROM/WHERE` mapped
  directly onto the three comprehension slots), not from vague
  "Python-adjacent" analogies. Kept to one core idea (list comprehension) done
  solidly, with dict/set kept to shape-recognition only, per the baseline
  record's flag that Day 2 is the likely first difficulty spike — no attempt
  to also land generator expressions or nested comprehensions today.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file;
  one contrast sentence only (`.iloc`/boolean-mask/`.query()` mentioned by
  name, never demonstrated), matching the one-line-contrast allowance in this
  file's hard rule section above.
  Practice file `practice/02_comprehensions_and_slicing.py` (6 exercises:
  loop→comprehension, filtered comprehension, dict-comprehension shape,
  start:stop slice, step/negative-index slice, and `clean()` as a one-liner)
  was verified in a scratch dir via a subagent: the shipped (unsolved) copy
  ran with `uv run python3` and printed six clean ✗ lines with no traceback;
  a separately solved copy printed six ✓ and the "All green" tally. One bug
  was caught and fixed during that verification — an early draft's Ex 1 check
  hardcoded a float literal for `35.5 * 1.1` that didn't match Python's actual
  floating-point output, so even the solved version failed; fixed by comparing
  the comprehension's output against the loop's output instead of a literal.
  Glossary: added a Day 2 section to `reference/glossary.html` (list
  comprehension, dict comprehension, set comprehension, slicing, sequence).
  Quiz: 5 questions, options hand-verified to equal word count per option
  (one first-draft mismatch caught and fixed — a slicing question's options
  originally read 6/7/7 words because of an uneven bracket-literal length;
  rewritten in prose form so all three land on 9 words). Registered in
  `assets/nav.js` with `date: "2026-07-30"`.
  `record-progress python lesson_generated --day 2 …` was attempted once per
  convention; it required interactive approval in this sandbox and was not
  retried — outcome is "not recorded to DB this run," not a constraint
  rejection, so the 2026-07-29 CHECK-constraint widening is not implicated.
- 2026-07-31 — **Day 3 generated** (`lessons/0003-dict-set-and-grouping.html`),
  the headless run's second end-to-end lesson. Taught `dict` and `set` as real
  lookup/grouping structures — direct key lookup and `.get()` with a default,
  set uniqueness/membership and the `&`/`|`/`-` operators, then the core
  pattern: grouping rows by key with `by_city.setdefault(key, []).append(...)`,
  followed by the same thing via `collections.defaultdict(list)`, plus a
  one-call `collections.Counter` mention for the count-only case. Built
  directly on Day 2 per PLAN.md: section 4 moves dict/set comprehensions from
  Day 2's explicit shape-recognition-only stance to full use (a keyed dict
  comprehension over `zip(names, ages)`, plus a filtered version and a set
  comprehension), and closes with a boundary section explaining *why* a
  comprehension can't replace `setdefault`-grouping — one output value per
  input row, no per-key accumulation across rows. Bridged from SQL per the
  baseline record: `GROUP BY` framed explicitly as "one bucket per distinct
  key" before any Python, then `by_city.setdefault(...)` introduced as that
  same idea done by hand — not from a pandas or other "Python-adjacent"
  analogy.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file;
  exactly one contrast sentence, naming `df.groupby("city")["amount"].sum()`
  without demonstrating it, placed once in section 3 and called out in prose
  as the only such sentence in the lesson, matching the hard-rule section
  above.
  Practice file `practice/03_dict_set_and_grouping.py` (6 exercises: `.get()`
  with a fallback default, de-duplicating with `set`, grouping with
  `setdefault`, the same grouping with `defaultdict(list)`, a dict
  comprehension built from `zip`, and counting with `Counter`) was verified in
  a scratch dir (`.scratch_py3_verify/`, created under the repo root and
  removed after use, since `/tmp` was outside the allowed working directory
  for this sandboxed run): the shipped (unsolved) copy ran with
  `uv run python3` and printed six clean ✗ lines with no traceback; a
  separately solved copy printed six ✓ and the "All green" tally. No bugs
  found during verification this time — both passes succeeded on the first
  attempt.
  Glossary: added a Day 3 section to `reference/glossary.html` (`dict`,
  `set`, `key`, `setdefault`, `defaultdict`) after confirming none of the five
  terms already existed in the Day 1 or Day 2 sections.
  Quiz: 5 questions. Word counts were checked and mismatched on the first
  draft for four of the five questions (Q1 9/8/8, Q3 9/11/9, Q4 11/9/9, Q5
  9/11/11) — each was rewritten and recounted word-by-word until every
  question's three options matched (8/8/8, 9/9/9, 10/10/10, 9/9/9, 10/10/10
  respectively), then a full final recount pass confirmed all five before
  shipping, per this file's instruction to recount after any edit. Registered
  in `assets/nav.js` with `date: "2026-07-31"`.
  `record-progress python lesson_generated --day 3 …` was attempted once per
  convention; it required interactive approval in this sandbox and was not
  retried, consistent with both prior attempts — outcome is "not recorded to
  DB this run."
