# Data Pipelines — working notes & conventions

Authoritative for lesson generation. `daily-lessons-prompt.md` defers to this file.

## Course conventions

Identical to `python/` unless stated:

- Every jargon term gets `<dfn data-en="…" data-vn="…">term</dfn>`, and the page
  loads `../assets/gloss.js`. **No inline translations in prose.** Every new
  term also gets a row in `reference/glossary.html` under that lesson's heading.
  Check that the term isn't already there first.
- Quizzes use `../assets/quiz.js`. Options within one question must have the
  same word count, so position and length carry no signal. Recount after
  every edit.
- Every lesson ends with `<script src="../assets/nav.js"></script>` and is
  registered in `assets/nav.js` `LESSONS`. New reference sheets go in `REFS`.
- Every lesson: one tangible win, cites `RESOURCES.md` inline, recommends one
  primary source, and closes with a reminder to ask the teacher follow-ups.
  Vietnamese is welcome.
- `assets/quiz.js`'s `QUIZ_COURSE` regex includes `dataeng`. If assets are
  ever re-copied from another course, re-add it or quiz results stop being
  tagged to this course.
- Lesson length: **~30–45 min during Phase 1** (reading ≤ 10 min, the rest
  building), **~20 min in Phase 2**.

## Scope boundaries (the overlap rule)

Four sibling courses run in parallel. On 2026-07-23..24, overlapping generation
blocked every `git pull` for a week (see `python/NOTES.md`), and topic overlap
is the same failure in slow motion.

- **pandas / NumPy** → `data/`. Never use pandas in this course's code: the
  producer, consumer and loader are plain Python plus confluent-kafka and
  psycopg.
- **Python language features** → `python/`. Use them freely (the learner has
  48 lessons there) but don't teach them. A one-line reminder is fine.
- **API design, schema design, idempotency *as a concept*** → `backend/`. Use
  them as bridges ("this is the idempotency key from backend, applied to a
  consumer") and don't re-derive them.
- **This course owns:** dbt, Kafka, Airflow, dimensional modelling in the
  warehouse, and pipeline-level reliability (delivery semantics, backfills,
  data tests).

## Depth is uneven on purpose

Per `MISSION.md`: **dbt goes deep, Kafka and Airflow go to working level.** In
practice:

- dbt lessons are fully hands-on and may introduce advanced features.
- Kafka and Airflow lessons build only what the portfolio needs to *run*.
  Everything else (Connect, Schema Registry internals, Streams, executors,
  multi-broker ops) is taught as concept plus diagram plus quiz, with no local
  setup. If a Kafka/Airflow lesson's build step needs a new container or a new
  install, stop and ask whether the portfolio actually needs it.

## Learner profile

See `learning-records/0001-baseline-sql-strong-pipeline-tools-new.md`. Short
version: strong SQL and Postgres; Python fluent enough via `python/`; dbt and
Kafka hands-on new; Airflow lightly used (edited existing DAGs, possibly 2.x).
Bridge from SQL and from `backend/` concepts. Expect the difficulty spike on
Days 5–6 (Kafka).

## The portfolio repo is the practice file

There is no `practice/` directory. The learner builds in their own public repo,
`food-delivery-pipeline`, created on Day 1 and **outside this workspace**. CI
can't see or push to it, so:

- Each lesson's build section gives exact file paths *relative to that repo*
  and complete code for anything that is scaffolding. Give *partial* code with
  TODOs only for the part that is the day's skill: the learner writes the dbt
  model or the test from memory.
- Each build section ends with a **Verify** block: the command to run and the
  expected output (row counts, `PASS=… ERROR=0`, offsets). That is the feedback
  loop. Make expected output specific enough that a wrong result is obvious.
- Never assume the previous day's build step was completed. Open each lesson
  with a one-line "you should have…" check plus the command that proves it.
- The domain names in `PLAN.md` ("The domain") are fixed. Don't rename tables,
  columns, topics or marts between lessons.

## Verifying code before shipping (CI)

The learner's repo isn't available, so verify snippets in a scratch dir under
the repo root (e.g. `.scratch_dataeng_verify/`, deleted afterwards; `/tmp` has
been out of bounds in the sandboxed run):

- **dbt:** lay out a minimal project (`dbt_project.yml`, a `profiles.yml`
  pointing at an unreachable Postgres, and the models) and run
  `uv run --with "dbt-postgres==1.11.0" dbt parse --profiles-dir .`. It needs no
  database. Confirmed 2026-09-14 that it catches broken `ref()`/`source()`
  names and Jinja errors. **dbt still exits 0 through a pipe**, so grep its
  output for `Error` rather than trusting the exit code.
- **Python (producer/consumer/loader/DAG files):** `uv run python3 -m py_compile file.py`
  at minimum. For an Airflow DAG, also try
  `uv run --with "apache-airflow==3.3.1" python3 -c "import runpy; runpy.run_path('dag.py')"`
  if time allows. It is a heavy install, so skip it and note the skip if it
  times out.
- **SQL run directly against Postgres** (raw DDL, `ON CONFLICT`) can't be
  executed in CI. Hand-check it against the Postgres docs, and say in the
  generation log that it was not executed.
- **docker compose files:** check indentation and image tags carefully. Pinned
  images are `postgres:17` and `apache/kafka:4.3.1`. Don't use `latest`.

## Phase 1 is date-locked

`PLAN.md` assigns Days 1–7 to exact filenames and dates
(2026-09-15 → 2026-09-21). Use them exactly and don't generate ahead of the
date. From 2026-09-22 the course goes open-ended and sequential from `0008-…`
along the Phase 2 spine, adapted to the learning records.

## Generation log

- 2026-09-14: **Course created** in a live session on the user's request for a
  dbt/Kafka/Airflow course. Mission negotiated with the user: a **portfolio
  project** (not interview prep, not current work), **mixed depth** (dbt deep,
  Kafka and Airflow closer to concepts), a **one-week intensive first**, the
  code in a **separate public repo**, **food-delivery** domain (chosen over
  e-commerce, GitHub Archive, payments, air quality, taxi and a Wikipedia
  feed), starting **2026-09-15**. No lesson was written by hand, so Day 1 is
  generated by CI on 2026-09-15. Versions pinned from PyPI/Docker Hub on
  creation day (see MISSION.md). The `course_progress` CHECK constraint was
  widened to include `dataeng`, the same kind of change as `python/`'s on
  2026-07-29; there is still no migration file.
