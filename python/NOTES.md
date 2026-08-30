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
- 2026-08-01 — **Day 4 generated** (`lessons/0004-functions-args-and-key.html`),
  the headless run's third end-to-end lesson, and the first to teach `key=`
  and `lambda` per the learner-profile scoping (both explicitly off-limits
  before today). Taught functions as first-class values (a name bound to a
  function object, passable like any other value — the mechanism `sorted`'s
  `key=` relies on), positional vs. keyword arguments, default arguments
  (plus a callback to Day 1's mutable-default-argument trap, already in the
  glossary, rather than re-explaining it), `*args`/`**kwargs` at a
  recognition-only level per the scoping instructions, `lambda` as a
  single-expression anonymous function, and `key=` as accepted by `sorted()`,
  `min()`, and `max()`. Built directly on Day 3 per PLAN.md's stated ordering
  ("grouping needs `key=` functions"): section 4's worked example sorts a
  Day-3-style `Counter` of city counts by count, descending, via
  `sorted(city_counts.items(), key=lambda pair: pair[1], reverse=True)` —
  explicitly framed as the reason `Counter.items()` doesn't come out
  pre-sorted and needs today's tool to be useful. Bridged from SQL per the
  baseline record: `ORDER BY count DESC` introduced first as "sort by a
  computed column, not the row itself," then `key=` presented as that same
  idea in Python.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file;
  exactly one contrast sentence, naming `df.sort_values("amount",
  ascending=False)` without demonstrating it, placed once after the
  Counter-sorting example and called out in prose as the only such sentence,
  matching the hard-rule section above.
  Practice file `practice/04_functions_args_and_key.py` (6 exercises: a
  function with a default argument, calling with keyword arguments, writing
  a `lambda`, sorting a list of dicts with `key=`, `max(..., key=...)`, and
  sorting a `Counter`'s items by count descending) was verified in a scratch
  dir (`.scratch_py4_verify/`, created under the repo root and removed after
  use, per this file's `/tmp`-is-out-of-bounds note from the Day 3 entry):
  the shipped (unsolved) copy ran via `uv run python3` (both from the scratch
  copy and from its real `practice/` path with the documented command) and
  printed six clean ✗ lines with no traceback — the unsolved lines are bare
  `...` expression statements assigned to names or left as a no-op function
  body, so every check's lambda condition evaluates to `False` rather than
  raising, and `check()`'s own `try/except` would catch it either way; a
  separately solved copy printed six ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 4 section to `reference/glossary.html` (`function`,
  `positional argument`, `keyword argument`, `default argument`, `lambda`,
  `key=`) after confirming none of the six terms already existed in the Day
  1–3 sections (Day 3 already has `key` as in dict/set key, a distinct term
  from today's `key=` sorting argument, so the new entry is titled `key=
  (sorting)` to avoid collision).
  Quiz: 5 questions. Word counts were checked and mismatched on the first
  draft for four of the five questions (Q1 10/10/11, Q2 5/9/8, Q3 10/8/8, Q4
  11/7/8, Q5 10/9/7) — each was rewritten and recounted word-by-word (not by
  eye) until every question's three options matched (10/10/10, 8/8/8,
  10/10/10, 9/9/9, 10/10/10 respectively), then a full final recount pass
  confirmed all five before shipping, per this file's instruction to recount
  after any edit — Q2 in particular needed three rewrite rounds since the
  first two attempts each fixed one option while leaving another mismatched.
  Registered in `assets/nav.js` with `date: "2026-08-01"`.
  `record-progress python lesson_generated --day 4 …` was attempted once per
  convention; it required interactive approval in this sandbox and was not
  retried, consistent with all three prior attempts — outcome is "not
  recorded to DB this run."
- 2026-08-02 — **Day 5 generated** (`lessons/0005-iterators-and-generators.html`),
  the headless run's fourth end-to-end lesson, and the first to teach
  generators/`yield` per the learner-profile scoping (explicitly off-limits
  before today, and flagged in the profile note itself). Taught the iterator
  protocol practically (`iter()`/`next()`, `StopIteration`, what a plain
  `for` loop actually does under the hood), generator functions (`yield`
  pausing/resuming a function body instead of building a return value all at
  once), the concrete memory argument from MISSION.md — a generator over a
  huge file holds at most one line at a time versus a list-returning version
  holding everything — a generator expression as the lazy, parenthesized
  sibling of Day 2's list comprehension (also paying off Day 3's own
  glossary-adjacent callout, which had explicitly deferred generator
  expressions to "Day 5 explains it properly"), and chaining two generator
  functions (`parse` → `positive_only`) into a lazy filter pipeline whose
  final consuming loop reused Day 3's `defaultdict`-style grouping/aggregation
  pattern. Bridged from SQL per PLAN.md's ordering note ("`key=` functions
  lead into generators"): framed a chained generator pipeline as a query plan
  streaming rows through operators rather than materializing every
  intermediate result, used once in the top callout and not forced into any
  other section.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file
  (checked by grep for `pandas|numpy|DataFrame`, case-insensitive); exactly
  one contrast sentence, naming `df[df["amount"] > 0].groupby("city")["amount"].sum()`
  as eager/vectorized versus today's lazy generators, without demonstrating
  it, placed once near the end and called out in prose as the only such
  sentence, matching the hard-rule section above.
  Practice file `practice/05_iterators_and_generators.py` (5 exercises:
  manual `iter()`/`next()`, a `countdown()` generator function, a generator
  expression squaring a list, chaining `parse`/`positive_only` generator
  functions into a pipeline, and consuming that pipeline into a per-city
  totals dict) was verified in a scratch dir (`.scratch_py5_verify/`, created
  under the repo root and removed after use, per the Day 3/4 precedent that
  `/tmp` is out of bounds for this sandbox) via a subagent: the shipped
  (unsolved) copy ran with `uv run python3` and printed five clean ✗ lines
  with no traceback; a separately solved copy printed five ✓ and the "All
  green" tally. No bugs found during verification — both passes succeeded on
  the first attempt. One design point confirmed deliberately, not a bug: the
  Ex 4 check rebuilds its own fresh `positive_only(parse(raw_lines))` instead
  of consuming the student's module-level `pipeline`, so Ex 5 exhausting
  `pipeline` doesn't affect Ex 4's check regardless of execution order —
  necessary because generators are single-use.
  Glossary: added a Day 5 section to `reference/glossary.html` (`iterable`,
  `iterator`, `generator function`, `generator`, `generator expression`,
  `lazy evaluation`) after confirming none of the six terms collided with any
  Day 1–4 entry.
  Quiz: 5 questions. Word counts were checked and mismatched on the first
  draft for three of the five questions (Q3 13/9/10, Q4 7/8/9, Q5 12/9/11) —
  Q1 and Q2 were already equal on the first draft (8/8/8 and 10/10/10). Each
  mismatched question was rewritten and recounted word-by-word with `wc -w`
  (not by eye) until every option matched (Q3 10/10/10, Q4 8/8/8, Q5
  11/11/11), needing a couple of iterations on Q3 and Q5 in particular before
  landing on the target count, then a full final recount pass across all
  five questions confirmed every option before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-02"`.
  `record-progress python lesson_generated --day 5 …` was attempted once per
  convention and **succeeded this time** — `recorded: python/lesson_generated
  day=5 lesson=0005-iterators-and-generators.html` — unlike all four prior
  Day 1–4 attempts, which required interactive approval and were not
  recorded. No explanation available from this session for why this attempt
  went through non-interactively when the previous ones didn't; worth
  watching whether Day 6 also succeeds before assuming the sandbox behavior
  has changed for good.
- 2026-08-03 — **Day 6 generated** (`lessons/0006-files-formats-and-with.html`),
  the headless run's fifth end-to-end lesson. Taught `open()` and its three
  core modes (`"r"`/`"w"`/`"a"`, with `"w"`'s silent-truncate trap flagged
  explicitly), then made precise a claim Day 5 had already made in passing —
  that a file object opened for reading *is* an iterator in the exact Day 5
  sense, so `for line in f` is the identical `iter()`/`next()`/`StopIteration`
  protocol applied to a file, not a new file-specific mechanism. Landed the
  context manager protocol next: a before/after contrast (manual
  `open()`/`.close()` that leaks the handle if an exception fires in between,
  versus the `with` version whose `__exit__` guarantees the close regardless)
  followed by a short `__enter__`/`__exit__` explanation at a
  recognition-only level — writing a context manager class is explicitly
  deferred to a later lesson. Then the two structured-format modules:
  `csv.reader` (rows as lists) vs `csv.DictReader` (rows as dicts keyed by
  the header row, values always `str`), and `json.load`/`json.dump`, framed
  through why JSON's `{...}`/`[...]` syntax maps directly onto Python's own
  dict/list literals — a direct callback to Day 1's object-literal material.
  Closed by explicitly wiring Day 5's generator-function idea onto today's
  `csv.DictReader` into a `read_sales(path)` generator yielding one
  int-typed record per row, lazily, the exact shape tomorrow's capstone
  needs before it adds a `dataclass`. Built directly on Day 5 per PLAN.md's
  stated ordering ("generators make file streaming make sense"), and framed
  as Day 7's direct prerequisite throughout section 7 and the closing line.
  Bridged from SQL per the baseline record: a CSV file introduced as SQL's
  closest un-typed cousin — rows of raw text needing the same row-of-values
  shape SQL already gives for free — rather than any pandas or other
  "Python-adjacent" analogy.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file
  (checked by grep for `pandas|numpy|dataframe|read_csv`, case-insensitive,
  across both new files); exactly one contrast sentence, naming
  `pd.read_csv("sales.csv")` as eager/one-call versus today's `open()` +
  `csv.DictReader` + manual type conversion, without demonstrating it, placed
  once after section 6 and called out in prose as the only such sentence,
  matching the hard-rule section above. (The grep also turned up two
  pre-existing, unrelated hits — Day 3's own title/heading, "dict & set:
  grouping without pandas" — which don't count against today's one-sentence
  budget since they predate this lesson.)
  Practice file `practice/06_files_formats_and_with.py` (5 exercises: writing
  then reading a text file via `with`, a `FakeFile` context-manager stand-in
  contrasting a manual-close leak against a `with`-guaranteed close on
  exception — chosen over a real crash-prone file to keep the check
  deterministic, per this file's own scratch-verification practice — reading
  a self-written CSV fixture with `csv.DictReader`, a `json.dump`/`json.load`
  round trip preserving `int`/`list` types, and a `read_sales()` generator
  function chaining Day 5's generator idea onto `csv.DictReader`) was
  verified in a scratch dir (`.scratch_py6_verify/`, created under the repo
  root and removed after use, per the Day 3–5 precedent that `/tmp` is out of
  bounds for this sandbox): the shipped (unsolved) copy ran with
  `uv run python3`, both from the scratch copy and from its real `practice/`
  path with the documented command, and printed five clean ✗ lines with no
  traceback; a separately solved copy printed five ✓ and the "All green"
  tally. No bugs found during verification — both passes succeeded on the
  first attempt. The practice file writes its own CSV/text/JSON fixtures
  into a `tempfile.mkdtemp()` directory at the top of the script, so it needs
  no external fixture file to already exist and is safe to run repeatedly.
  Glossary: added a Day 6 section to `reference/glossary.html` (`with`
  statement, context manager, file object as iterator, `csv.DictReader`,
  JSON) after confirming none of the five terms already existed in the Day
  1–5 sections via grep.
  Quiz: 5 questions. Word counts were checked and mismatched on the first
  draft for four of the five questions (Q1 8/8/9, Q2 11/10/9, Q3 9/9/11, Q5
  10/9/11) — only Q4 was already equal on the first draft (11/11/11). Each
  mismatched question went through multiple rewrite-and-recount rounds with
  `wc -w` per option line (not by eye) — Q1 and Q2 in particular needed
  several iterations, including one false-start edit that swapped a word for
  a same-length synonym without changing the count — until every option
  matched (Q1 9/9/9, Q2 10/10/10, Q3 9/9/9, Q5 10/10/10), then a full final
  recount pass across all five questions' three options each (15 lines total)
  confirmed every one before shipping, per this file's instruction to
  recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-03"`.
  `record-progress python lesson_generated --day 6 …` was attempted once per
  convention; it required interactive approval in this sandbox and was
  blocked, not retried — outcome is "not recorded to DB this run," the same
  result as all Day 1–4 attempts. Day 5 had succeeded non-interactively, so
  this confirms that success was not a lasting sandbox change — behavior is
  inconsistent run to run, still unexplained.
- 2026-08-04 — **Day 7 generated** (`lessons/0007-dataclasses-typing-capstone.html`),
  the headless run's sixth end-to-end lesson and **the last day of Phase 1** —
  the intensive week (2026-07-29 → 2026-08-04) is now complete. Taught
  `@dataclass` (typed fields as class-level annotations, free `__init__` /
  `__repr__` / `__eq__`, field defaults following Day 4's exact default-argument
  rule, explicitly contrasted section-by-section against a plain dict — a typo
  in a dict key raises `KeyError` late — and a hand-written plain class, which
  gets the missing-field guarantee but none of the free dunder methods),
  then basic type hints (plain `name: Type` annotations, `list[X]`,
  `Optional[X]`/`X | None`, and the explicit, load-bearing claim that Python
  never enforces any of this at runtime — hints are documentation only). Spent
  both on the capstone: an `extract()`/`transform()`/`load()` ETL script
  wiring every prior day together explicitly in the lesson prose, not just
  implicitly — `extract()` is Day 6's `read_sales()` shape verbatim (Day 6 §3
  `with`, Day 6 §5 `csv.DictReader`) now yielding a `SalesRow` dataclass
  instead of a loose dict; `transform()` chains Day 2's list comprehension
  (filter), Day 3's `defaultdict` (group by city), and Day 4's `sorted(...,
  key=lambda ...)` (order by total); `load()` reuses Day 6's `json.dump`; and
  the whole thing stays lazy per Day 5 until `transform()`'s comprehension is
  the first thing to actually consume the `extract()` generator. Built
  directly on Day 6 per PLAN.md and Day 6's own closing line, which had
  already named `read_sales()` as "the exact shape tomorrow's capstone needs
  before it adds a dataclass." Bridged from SQL per the baseline record: a
  dataclass framed as close to `CREATE TABLE` — a fixed set of named, typed
  columns every row must have — enforced at the object level instead of the
  database, introduced before any Python in the top callout.
  No-pandas rule: zero pandas/NumPy API anywhere in lesson or practice file
  (checked by grep for `pandas|numpy|dataframe|read_csv`, case-insensitive,
  across both new files — zero hits in the practice file, exactly one hit in
  the lesson); exactly one contrast sentence, comparing a dataclass's fixed
  typed fields to a DataFrame's typed columns (`df.dtypes`) without
  demonstrating it, placed once after section 3 and called out in prose as
  the only such sentence, matching the hard-rule section above.
  Practice file `practice/07_dataclasses_typing_capstone.py` (5 exercises:
  defining `SalesRow` as a `@dataclass` with an `Optional[str] = None` field
  default, an `extract()` generator over `csv.DictReader` yielding `SalesRow`
  instances, a `transform()` filtering/grouping/sorting, a `load()` writing
  JSON via `json.dump`, and a `run()` wiring all three into the full ETL
  script) was verified in a scratch dir (`.scratch_py7_verify/`, created
  under the repo root and removed after use, per the Day 3–6 precedent that
  `/tmp` is out of bounds for this sandbox): the shipped (unsolved) copy ran
  via `uv run python3`, both from the scratch copy and from its real
  `practice/` path with the documented command, and printed five clean ✗
  lines with no traceback each time; a separately solved copy printed five ✓
  and the "All green — lesson 7 done, Phase 1 complete!" tally. No bugs found
  during verification — both passes succeeded on the first attempt. Ex 1's
  check builds its own defensive `SalesRow` instance in a helper wrapped in
  `try/except` so a missing Exercise 1 fails only its own check with a clean
  ✗ instead of a `NameError` cascading into every later exercise's check.
  Glossary: added a Day 7 section to `reference/glossary.html` (`dataclass`,
  `default (dataclass field)`, `type hint`, `Optional[X]`, `ETL`) after
  confirming via grep that none of the five terms collided with any Day 1–6
  entry — `default (dataclass field)` was deliberately titled to disambiguate
  from Day 4's existing `default argument` row, the same near-collision
  pattern Day 4's own `key= (sorting)` entry had already flagged relative to
  Day 3's `key`.
  Quiz: 5 questions. Word counts were checked with `wc -w` per option
  (individual `echo | wc -w` calls, not by eye) and mismatched on the first
  draft for all five questions (Q1 10/8/8, Q2 8/9/9, Q3 11/9/9, Q4 6/7/9, Q5
  7/9/9) — each was rewritten and recounted until every option matched (Q1
  9/9/9, Q2 9/9/9, Q3 9/9/9, Q4 8/8/8, Q5 9/9/9), including one sub-iteration
  on Q1's second option and Q4's third option that needed a second rewrite
  after the first pass undershot or overshot the target count, then a full
  final recount pass across all five questions' three options each (15 lines
  total) confirmed every one before shipping, per this file's instruction to
  recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-04"`.
  `record-progress python lesson_generated --day 7 …` was attempted once per
  convention; it required interactive approval in this sandbox and was not
  retried — outcome is "not recorded to DB this run," consistent with all
  prior attempts except Day 5's one-off success.
  **Phase 1 is now complete** (Days 1–7, 2026-07-29 → 2026-08-04, all
  date-locked filenames from `PLAN.md`'s table shipped exactly as assigned,
  none pre-generated ahead of date). Per `PLAN.md`, **Phase 2 starts
  2026-08-05**: open-ended, sequential numbering from `0008-…`, ~20 min/day,
  no more date-locking — ordering should adapt to the learning records rather
  than marching through the Phase 2 spine mechanically, starting with 2a
  (exceptions, modules/imports, `uv`/`pyproject.toml`, `pytest`, decorators,
  `pathlib`/`datetime`/`logging`) before 2b's FastAPI + pydantic backend
  phase.
- 2026-08-05 — **Day 8 generated** (`lessons/0008-exceptions.html`), **the
  Phase 1 → Phase 2 transition lesson**. Confirmed before generating that Day
  7 already existed on disk (no date-locked gap to backfill) and that no
  `0008-…` or later file existed yet today — this is the first Phase 2
  lesson, not a re-run. Idempotency check used on-disk state
  (`python/lessons/` highest filename + this file's own dated log) since DB
  access was unavailable this run (see below); no existing `0008-…` lesson
  found, so generation proceeded.
  Topic: exceptions — first item of `PLAN.md`'s Phase 2a spine
  ("Exceptions: raising, catching narrowly, custom exception types,
  try/finally") and squarely language-level, not library — satisfies the
  scope rule. Taught: uncaught exceptions as the *default* outcome (a
  traceback, not a special failure mode) using Day 6/7's
  `int(row["amount"])` on a blank cell as the motivating crash; narrow
  `try`/`except ExceptionType:` with the bare-`except:`-is-dangerous habit as
  the single most-emphasized point in the lesson; `else`/`finally` (the
  latter framed as the same "always runs" guarantee as Day 6's context
  manager `__exit__`); `raise` with a built-in type; and a custom exception
  (`class InvalidSalesRow(Exception)`) as the same "give it a fixed, named
  shape" idea Day 7's dataclasses already established, applied to failures
  instead of records. Closed by rewriting Day 7's capstone `extract()` to
  catch `ValueError` narrowly around the `int()` call so one bad CSV row no
  longer kills the whole generator — direct continuity with the capstone
  rather than a fresh unrelated example. Bridged from SQL per the (sparse)
  baseline record: a constraint violation aborting a statement and raising
  in client code, introduced before any Python in the top callout, not from
  a pandas or other "Python-adjacent" analogy.
  Learning records: only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) exists —
  no completion/quiz record for Day 7 or any other day was found. Per this
  run's instructions, treated that as "records are sparse" and generated
  conservatively: one core mechanism (narrow catch) emphasized hard, `finally`
  and custom exceptions kept deliberately small (recognition + one use each,
  not a menu of edge cases), and the lesson stayed anchored to material
  already taught (Days 5–7) rather than introducing several new unrelated
  examples. This assumption — that Day 7 landed fine and no consolidation
  lesson was needed — is unverified against real quiz/completion data and
  should be revisited once a completion record exists.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe|DataFrame`, case-insensitive,
  across both new files — zero hits in the practice file, exactly one hit in
  the lesson); exactly one contrast sentence, naming
  `pd.to_numeric(col, errors="coerce")` without demonstrating it, placed once
  after section 5 and labeled in prose as the only such sentence, matching
  the hard-rule section above.
  Practice file `practice/08_exceptions.py` (5 exercises: `safe_int()`
  catching `ValueError` narrowly, `describe_lookup()` telling `KeyError` from
  `ValueError` with separate `except` clauses, `count_attempts()` using
  `finally` to count every attempt regardless of outcome, a custom
  `InvalidSalesRow` exception raised by `parse_amount()`, and an
  `extract()`-style generator skipping bad rows instead of crashing) was
  verified in a scratch dir (`.scratch_py8_verify/`, created under the repo
  root and removed after use, per the Day 3–7 precedent that `/tmp` is out of
  bounds for this sandbox). **One bug was caught and fixed during
  verification:** the first draft's Ex 4 check referenced a helper function
  `_raises_invalid_sales_row()` defined *after* the `results = [...]` list —
  since `check()` calls each lambda immediately rather than deferring to the
  end of the file, Ex 4 failed with a swallowed `NameError` even in the
  solved copy (caught because the solved-copy pass is a real pass/fail check,
  not just "did it run"). Fixed by moving the helper's `def` above `results`.
  After the fix: the shipped (unsolved) copy ran via `uv run python3`, both
  from the scratch copy and from its real `practice/` path with the
  documented command, and printed five clean ✗ lines with no traceback each
  time; a separately solved copy printed five ✓ and the "All green" tally.
  Glossary: added a Day 8 section to `reference/glossary.html` (`exception`,
  `traceback`, `try / except`, `else / finally (try statement)`, `raise`,
  `custom exception`) after confirming via grep that none of the six terms
  collided with any Day 1–7 entry.
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, not piped through `awk`/multi-stage pipelines
  since this sandbox's approval gate blocks compound bash commands) and
  mismatched on the first draft for four of the five questions (Q2 7/9/8, Q3
  8/8/8 already matched, Q4 10/8/9, Q5 10/9/10) — each mismatched question
  went through two to three rewrite-and-recount rounds until every option
  matched (Q1 9/9/9, Q2 9/9/9, Q3 8/8/8, Q4 9/9/9, Q5 10/10/10), then a full
  final recount pass across all five questions' three options each (15 lines
  total, each checked individually) confirmed every one before shipping, per
  this file's instruction to recount after any edit. Registered in
  `assets/nav.js` with `date: "2026-08-05"` — kept the `date:` field for
  display purposes even though Phase 2 has no date-locking, matching
  `backend/`'s and `data/`'s own convention of still stamping a generation
  date on sequential, non-gated entries.
  **DB access:** `bin/query-progress` (Step 0) required approval in this
  sandbox and was not retried beyond one attempt, so learning-record
  freshness was judged from on-disk files only, per this run's fallback
  instructions — the single baseline record above is what that fallback
  found. `bin/record-progress python lesson_generated --day 8 --lesson
  0008-exceptions.html --detail '{"by":"launchd"}'` also required approval
  and was not retried — outcome is "not recorded to DB this run," consistent
  with most prior Day 1–7 attempts (only Day 5 succeeded non-interactively,
  still unexplained).
  **This is the Phase 1 → Phase 2 transition lesson**: Day 7
  (2026-08-04) was the last date-locked, PLAN.md-assigned filename, and it
  was already present on disk before this run started — no gap to backfill.
  Day 8 is the first lesson generated under Phase 2's open-ended, sequential,
  no-date-lock rule, following the Phase 2a spine's first item (exceptions)
  rather than jumping ahead to a later spine item.
- 2026-08-06 — **Day 9 generated**
  (`lessons/0009-modules-imports-and-layout.html`), the headless run's second
  Phase 2 lesson. Idempotency check used on-disk state (`python/lessons/`
  highest filename plus this file's own dated log) since DB access was
  unavailable again this run (see below); no `0009-…` file or today's-date
  nav.js entry existed yet, so generation proceeded.
  Topic: modules, packages, imports, `__name__`, project layout — the second
  item of `PLAN.md`'s Phase 2a spine, directly after Day 8's exceptions, and
  squarely language-level (the import system itself), not library — satisfies
  the scope rule. Taught: a `.py` file becomes an importable module the
  moment something imports it, and runs its top-level code exactly once,
  cached on repeat imports; `__name__` as `"__main__"` when run directly vs.
  the module's own name when imported, and why every practice file's closing
  `if __name__ == "__main__":` guard exists (demo/self-test code would
  otherwise re-run on every import elsewhere); the four `import` spellings
  and Python's search order (cache → importing file's own directory →
  installed packages → stdlib), used to explain why a local `csv.py` would
  shadow the real stdlib module; packages as a directory with `__init__.py`
  making it an importable namespace, framed as the exact mechanism `csv`,
  `json`, `dataclasses`, and `collections` have been using all course; and a
  minimal `pyproject.toml`/`src/`/`tests/` project layout shown only to
  recognize the shape, explicitly deferred to tomorrow's `uv`/`pyproject.toml`
  lesson for real management. Bridged from SQL per the baseline record: a
  module framed as a `VIEW` or stored-function library — a named, reusable
  unit other queries reference instead of copy-pasting — introduced before
  any Python in the top callout, not from a pandas or other
  "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for Day 8 or any other day was found (same gap
  Day 8's entry already flagged). Per this run's instructions, treated that
  as "records are sparse" and kept pacing conservative and anchored to
  material already taught: no new unrelated examples, and the project-layout
  section was deliberately kept to recognition-only (a picture of the shape)
  rather than teaching `pyproject.toml` mechanics, which stays tomorrow's job
  per PLAN.md's own ordering. This assumption remains unverified against real
  quiz/completion data, same caveat as Day 8's entry.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|DataFrame|dataframe`, case-insensitive,
  across both new files — zero hits in the practice file, exactly one hit in
  the lesson); exactly one contrast sentence, naming `import pandas as pd` as
  the same import mechanism aliased, without demonstrating any pandas API,
  placed once near the end and labeled in prose as the only such sentence,
  matching the hard-rule section above.
  Practice file `practice/09_modules_imports_and_layout.py` (5 exercises:
  importing a name directly from a sibling module with `from ... import`,
  the module-prefix `import`-then-`module.name` form, reading the file's own
  `__name__`, importing a function from a package via `from mypkg.parsing
  import safe_int`, and confirming a module is cached rather than re-run on a
  second `import`) needed a different fixture strategy than every prior day:
  today's topic is inherently about *multiple files* importing each other,
  which a single self-contained script can't demonstrate honestly. Followed
  Day 6's precedent of writing its own fixtures at runtime instead — the
  practice file builds a throwaway `helpers.py` module and a `mypkg/`
  package (with `__init__.py` and `parsing.py`) into a `tempfile.mkdtemp()`
  directory at startup, then prepends it to `sys.path` so the TODOs import
  real code from real files on disk, without adding any extra files under
  `practice/` itself. Verified in a scratch dir
  (`.scratch_py9_verify/`, created under the repo root and removed after
  use, per the Day 3–8 precedent that `/tmp` is out of bounds for this
  sandbox): the shipped (unsolved) copy ran via `uv run python3`, both from
  the scratch copy and from its real `practice/` path with the documented
  command, and printed five clean ✗ lines with no traceback each time; a
  separately solved copy printed five ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 9 section to `reference/glossary.html` (`module`,
  `__name__`, `import`, `package`) after confirming via grep that none of
  the four terms collided with any Day 1–8 entry.
  Quiz: 5 questions. Word counts were checked with individual manual
  word-by-word counts per option (not by eye, `wc -w`/pipeline commands
  blocked by this sandbox's approval gate as in prior days) and mismatched
  on the first draft for all five questions — each went through two to four
  rewrite-and-recount rounds (Q3 and Q5 needed the most iterations, each
  requiring a second pass after an em-dash or a compound word like
  `__init__.py`/`.pkg` was miscounted once) until every option matched (Q1
  9/9/9, Q2 8/8/8, Q3 8/8/8, Q4 9/9/9, Q5 9/9/9), then a full final recount
  pass across all five questions' three options each (15 lines total, each
  checked individually) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-06"`.
  **DB access:** both the read path (`bin/query-progress`) and the direct
  `psql "$LEARNING_DB_URL"` path were unavailable again this run — the direct
  path is hard-blocked by this sandbox's static analysis whenever
  `LEARNING_DB_URL` is expanded inline, and the helper script hits a
  permission-approval gate with no user present — consistent with every
  prior day's experience, so learning-record freshness was judged from
  on-disk files only, per this run's fallback instructions; the single
  baseline record above is what that fallback found.
  `bin/record-progress python lesson_generated --day 9 --lesson
  0009-modules-imports-and-layout.html --detail '{"by":"github-actions"}'`
  was run once after shipping, per this run's instructions (writes are
  pre-approved and source DB creds internally, unlike the blocked read
  paths) — see its own output for whether it recorded successfully.
- 2026-08-07 — **Day 10 generated**
  (`lessons/0010-environments-and-pyproject.html`), the headless run's third
  Phase 2 lesson. Idempotency check used on-disk state (`python/lessons/`
  highest filename plus this file's own dated log) since DB read access was
  unavailable again this run (see below); no `0010-…` file or today's-date
  nav.js entry existed yet, so generation proceeded.
  Topic: environments and dependencies with `uv`, reading `pyproject.toml` —
  the third item of `PLAN.md`'s Phase 2a spine, directly after Day 9's
  modules/imports/layout, and squarely language/tooling-level (the project
  metadata format and the mechanics of `uv run`/`uv add`), not library —
  satisfies the scope rule. Also cross-checked against `RESOURCES.md`, which
  already lists "Docs: uv — Astral … Use for: the environments lesson,"
  confirming this is the intended next topic rather than a guess. Taught: why
  isolation exists (two projects needing conflicting versions of the same
  package colliding under one shared global install); what `uv run` actually
  does in three steps (find/create `.venv/`, install any missing declared
  dependency, run `python3` from inside that environment — never the OS's own
  `python3`) — explaining retroactively why every Day 1–9 practice file has
  run via plain `uv run python3 …` with no separate install step; a minimal
  `pyproject.toml` (`[project]` name/version/`dependencies`, plus a
  `[dependency-groups]` `dev` group for tools like `pytest` that end users
  never need installed); `uv add` vs. `uv.lock` (loose human-edited
  constraints vs. exact resolved versions, the latter reproducible elsewhere
  via `uv sync`); and `uv run --with` as a one-off dependency that touches
  neither project file. Closed by filling in the two pieces Day 9's project
  layout sketch had deliberately left blank (`pyproject.toml` and `uv.lock`)
  onto that same directory tree. Bridged from SQL per the baseline record: a
  virtual environment framed as a separate database per project instead of
  one shared schema — isolating dependencies for the same reason you'd
  isolate data — introduced before any Python/tooling in the top callout, not
  from a pandas or other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap Days 8–9's
  entries already flagged). Kept pacing conservative per that same
  assumption: one core mechanism (`uv run`'s three-step behavior) emphasized
  first and explicitly tied back to something already observed (every prior
  practice file's run command), `pyproject.toml` kept to the fields this
  course's own dependency lists actually need (no extra build-system/tool
  config sections), and no new unrelated examples introduced. Unverified
  against real quiz/completion data, same caveat as Days 8–9.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file, exactly one hit in the
  lesson); exactly one contrast sentence, naming `uv add pandas` as the same
  one-line mechanism as any other package, without demonstrating any pandas
  API, placed once near the end and labeled in prose as the only such
  sentence, matching the hard-rule section above.
  Practice file `practice/10_environments_and_pyproject.py` (5 exercises:
  reading a project's `name` back out of parsed TOML, pulling the
  `dependencies` list out of that same parsed data, splitting a constraint
  string like `"httpx>=0.27"` into `(name, constraint)`, telling a runtime
  dependency from a dev-only one by name, and checking whether an installed
  version satisfies a `>=` constraint via integer-tuple comparison) needed a
  fixture strategy for the same reason Day 9's did — today's subject is a
  project *file*, not an in-memory data structure — so it writes a small
  `pyproject.toml` to a `tempfile.mkdtemp()` directory at startup and parses
  it once with the standard library's own `tomllib` (Python 3.11+, confirmed
  available: this sandbox's `uv run python3 --version` reports 3.12.3), with
  no extra fixture files shipped under `practice/` itself, following the
  Day 6/9 precedent named in this run's instructions. Verified in a scratch
  dir (`.scratch_py10_verify/`, created under the repo root and removed after
  use, per the Day 3–9 precedent that `/tmp` is out of bounds for this
  sandbox): the shipped (unsolved) copy ran via `uv run python3`, both from
  the scratch copy and from its real `practice/` path with the documented
  command, and printed five clean ✗ lines with no traceback each time; a
  separately solved copy printed five ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 10 section to `reference/glossary.html` (`virtual
  environment`, `package manager`, `pyproject.toml`, `uv.lock`, `uv add / uv
  run --with`) after confirming via grep that none of the five terms/entries
  collided with any Day 1–9 entry.
  Quiz: 5 questions. Word counts were checked with individual manual
  word-by-word counts per option (not by eye, `wc -w`/scripted counting
  commands blocked again by this sandbox's approval gate, consistent with
  every prior day) and mismatched on the first draft for four of the five
  questions (Q2 8/8/9, Q3 9/9/10, Q4 10/10/8, Q5 9/9/8) — Q1 was already
  equal on the first draft (7/7/7). Each mismatched question went through one
  to three rewrite-and-recount rounds — Q4's third option in particular
  needed three attempts (8 → 9 → 10 words) before landing on the target count
  — until every option matched (Q2 8/8/8, Q3 9/9/9, Q4 10/10/10, Q5 9/9/9),
  then a full final recount pass across all five questions' three options
  each (15 lines total, each checked individually) confirmed every one before
  shipping, per this file's instruction to recount after any edit. Registered
  in `assets/nav.js` with `date: "2026-08-07"`.
  **DB access:** both the read path (`bin/query-progress`) and the direct
  `psql "$LEARNING_DB_URL"` path were unavailable again this run — same
  hard content-level block on `LEARNING_DB_URL` shell expansion and the same
  permission-approval gate on the helper script with no user present,
  consistent with every prior day — so learning-record freshness was judged
  from on-disk files only, per this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 10 --lesson
  0010-environments-and-pyproject.html --detail '{"by":"github-actions"}'`
  was run once after shipping and **succeeded**: `recorded:
  python/lesson_generated day=10 lesson=0010-environments-and-pyproject.html`
  — the write path continues to work reliably even though the read paths
  remain blocked, consistent with Day 9's outcome.
- 2026-08-08 — **Day 11 generated** (`lessons/0011-testing-with-pytest.html`),
  the headless run's fourth Phase 2 lesson. Idempotency check confirmed
  on-disk: highest existing lesson file was `0010-…` dated 2026-08-07, no
  `0011-…` file and no `date: "2026-08-08"` entry existed yet in
  `assets/nav.js` before this run, so generation proceeded as Day 11.
  Topic: testing with `pytest` — assertions, fixtures, `parametrize` — the
  fourth item of `PLAN.md`'s Phase 2a spine, directly after Day 10's
  environments/`pyproject.toml`. Taught: `pytest` as the one deliberate,
  explicitly-flagged exception to this course's "standard library only"
  constraint, installed ad hoc via `uv run --with pytest pytest ...` (Day
  10's own "one-off dependency, no file changes" vocabulary, chosen over
  `uv add --dev pytest` because no `pyproject.toml` exists anywhere in this
  course yet — that project-file case is mentioned in prose as what a real
  project would do instead, not demonstrated); plain `assert` inside a
  `test_*` function as pytest's entire assertion mechanism, explicitly
  contrasted against `unittest`'s `self.assertEqual(...)` class-based style,
  which this course does not teach; `@pytest.fixture` with `yield` splitting
  a fixture into setup (before `yield`) and teardown (after `yield`,
  guaranteed to run), framed as the same "always runs" guarantee already
  established by Day 6's context-manager `__exit__` and Day 8's `finally`;
  and `@pytest.mark.parametrize` as the pytest-native replacement for the
  "list of check() calls" idiom every practice file through Day 10 has used,
  now reporting each case as its own separately-named pass/fail. Grounded in
  the course's own practice files as instructed: section 2's plain-`assert`
  example and the practice file's Exercise 1/4 both pytest-ify Day 8's
  `safe_int()` directly (same two/four cases the old `check()` covered), and
  Exercise 3 pytest-ifies Day 8's `extract()` behind a fixture instead of a
  hand-built temp-dir block at module scope. Bridged from SQL per the
  baseline record: a test suite framed as the set of query-result assertions
  you'd run after every schema migration — "this SELECT must return exactly
  these rows, every time" — introduced before any Python/pytest in the top
  callout, not from a pandas or other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–10 entry already flagged). Paced conservatively per that same
  assumption: exactly one core mechanism (fixture `yield`-as-setup/teardown)
  given the most explanatory weight, tied back to two already-taught
  mechanisms (context managers, `finally`) rather than introduced as
  something new and unrelated, and no additional pytest features (fixture
  scopes, marks beyond `parametrize`, plugins) pulled in beyond the spine's
  named three (assertions, fixtures, parametrize). Unverified against real
  quiz/completion data, same caveat as every entry since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file, exactly one hit in the
  lesson); exactly one contrast sentence, naming a DataFrame's contents as
  what a real pandas-pipeline test would assert on instead of a plain
  function's return value, without demonstrating any pandas API, placed once
  near the end and labeled in prose as the only such sentence, matching the
  hard-rule section above.
  Practice file `practice/11_testing_with_pytest.py`: a genuine
  **idiom change from every prior day**, discussed explicitly in the file's
  own header comment and in lesson section 5 — this is the first practice
  file that is itself a real `pytest` test file (functions named `test_*`,
  run by the `pytest` CLI) rather than a script with a hand-rolled
  `check()`/✓/✗ tally. Decision: keeping the ✓/✗ idiom would have meant
  testing pytest without ever actually invoking pytest's own runner, which
  contradicts the lesson's own point that pytest's reporting is a strict
  upgrade over the hand-rolled tally — so this file adopts pytest's native
  reporting instead (`pytest -v` output: dots/`F`/a per-test summary),
  matching "pick whichever fits pytest's actual usage pattern" from this
  run's instructions. 5 exercises: a plain-`assert` test against `safe_int()`
  (Ex 1), a `@pytest.fixture` writing a small CSV to a `tempfile.mkdtemp()`
  path and yielding it (Ex 2, the same "write my own fixture" strategy Day
  6/9/10 used, now expressed as a real pytest fixture instead of module-level
  setup code), a test consuming that fixture against `extract()` (Ex 3), a
  `@pytest.mark.parametrize` list covering four `safe_int()` cases in one
  test body (Ex 4), and a fixture with real setup **and** teardown proven by
  a shared `_log` list a second, later test checks (Ex 5) — concretely
  demonstrating that teardown code after `yield` really does run, not just
  stating it in prose.
  **One design bug was caught and fixed during verification, worth flagging
  since it's a new failure mode this course's practice files hadn't hit
  before:** the first draft used bare `pass` as the TODO placeholder inside
  test bodies (copying the hand-rolled-script convention). Under pytest this
  is silently wrong in two different ways rather than failing gracefully: (a)
  a `pass`-only test body with no `assert` at all trivially **passes** with
  nothing left to do — Exercises 1, 3, and 4's shipped (unsolved) forms were
  found reporting PASSED instead of FAILED on the first scratch-dir run; (b)
  a bare `...` (Ellipsis) left inside an `@pytest.mark.parametrize(...)`
  list's argument tuple crashes **test collection for the entire file** with
  `TypeError: object of type 'ellipsis' has no len()` before any test even
  runs, rather than failing just that one exercise. Both violate this file's
  own "must fail gracefully so the learner sees which task failed" rule, and
  neither would have been caught without actually running `pytest` on the
  shipped file and reading its verdict, not just checking it didn't crash —
  the same lesson Day 3's entry already drew about running (not just
  eyeballing) both the unsolved and solved copies. Fixed by replacing every
  unsolved test body with `assert False, "TODO: ..."` (fails visibly with
  the exact next step named in the message) and the parametrize placeholder
  with one clearly-fake but list-shaped tuple (`("TODO", "TODO")`, so
  collection succeeds and the test simply fails instead of crashing
  collection). Exercise 2's fixture placeholder uses `raise
  NotImplementedError(...)` instead, so pytest reports it as an `ERROR` at
  fixture setup — still a clean, obviously-intentional signal, not a
  traceback that looks like a real bug.
  After the fix, verified in a scratch dir (`.scratch_py11_verify/`, created
  under the repo root and removed after use, per the Day 3–10 precedent that
  `/tmp` is out of bounds for this sandbox): the shipped (unsolved) copy, run
  via `uv run --with pytest pytest practice/11_testing_with_pytest.py -v`
  both from a scratch copy and from its real `practice/` path with the
  documented command, reported **"4 failed, 1 error"** — every one of the
  five exercises failing or erroring with a message naming exactly what's
  unsolved, zero unexpected tracebacks, zero false PASSED lines; a separately
  written solved copy reported **"8 passed"** (5 exercises, with Exercise 4's
  `parametrize` correctly expanding into 4 separately-reported cases, e.g.
  `test_safe_int_parametrized[7-7] PASSED`). Real command output for the
  fixed shipped file:
  `FAILED ...::test_safe_int_parses_a_valid_number`,
  `ERROR ...::test_extract_reads_every_row - NotImplementedError: fill in
  sales_csv() — write the CSV and yield its path`,
  `FAILED ...::test_safe_int_parametrized[TODO-TODO]`,
  `FAILED ...::test_resource_is_open_during_the_test - TypeError: 'NoneType'
  object is not subscriptable`,
  `FAILED ...::test_teardown_already_ran_for_the_previous_test - assert []
  == ['closed']`, tallied as `4 failed, 1 error in 0.03s`; the solved copy's
  final line was `8 passed in 0.02s`.
  Glossary: added a Day 11 section to `reference/glossary.html` (`pytest`,
  `assert (in a test)`, `fixture`, `parametrize`) after confirming via grep
  that none of the four terms collided with any Day 1–10 entry. All four also
  got matching `<dfn>` markup at first use in the lesson body (`pytest`,
  `assert`, `fixture`, `parametrize`), matching the density of Day 9/10's
  lessons rather than leaving newly glossaried terms undefined inline.
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, and not piped through compound
  awk/multi-stage commands, since this sandbox's approval gate blocks
  compound bash commands exactly as in every prior day) and mismatched on
  the first draft for four of the five questions (Q1 7/6/8, Q2 10/9/9, Q3
  11/10/10, Q4 10/11/10) — Q5 was already equal on the first draft (8/8/8).
  Each mismatched question went through one to two rewrite-and-recount
  rounds until every option matched (Q1 7/7/7, Q2 9/9/9, Q3 10/10/10, Q4
  10/10/10), then a full final recount pass across all five questions' three
  options each (15 lines total, each checked individually with its own
  `wc -w` call) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-08"`.
  `bin/record-progress python lesson_generated --day 11 --lesson
  0011-testing-with-pytest.html --detail '{"by":"github-actions"}'` was run
  once after shipping and **succeeded**: `recorded: python/lesson_generated
  day=11 lesson=0011-testing-with-pytest.html` — third consecutive success
  (Days 9, 10, 11), suggesting the write path may simply be reliable in this
  sandbox regardless of the read-path blockage, though still only three data
  points.
- 2026-08-09 — **Day 12 generated** (`lessons/0012-decorators.html`), the
  headless run's fifth Phase 2 lesson. Idempotency check confirmed on-disk:
  highest existing lesson file was `0011-…` dated 2026-08-08, no `0012-…`
  file and no `date: "2026-08-09"` entry existed yet in `assets/nav.js`
  before this run, so generation proceeded as Day 12.
  Topic: decorators, and why they appear everywhere in FastAPI — the fifth
  item of `PLAN.md`'s Phase 2a spine, directly after Day 11's pytest, and
  squarely language-level (functions wrapping functions), not library —
  satisfies the scope rule trivially. Taught: the plain mechanism first
  (`shout(func)` returning a `wrapper(*args, **kwargs)`, built from nothing
  more than Day 4's already-taught "a function is a value, passable and
  returnable like any other"); `@decorator` as sugar for `name =
  decorator(name)`, framed explicitly through Day 1's binding/rebinding
  vocabulary rather than as new syntax — the exact same rebind Day 1
  already explained, applied automatically by Python at the `def` site;
  the FastAPI-relevance angle named explicitly per PLAN.md's own framing
  (`@app.get("/users/{id}")` shown and explained as the identical mechanism
  as `@shout`, with a plain note that no FastAPI itself is being taught yet —
  that stays Phase 2b's job); decorators-with-arguments as one more layer of
  nesting (`repeat(times)` returning a real decorator, which then wraps the
  target), tied back to `@app.get("/users/{id}")`'s own parenthesized
  argument shown moments earlier; and `functools.wraps` closing the lesson
  as the detail that keeps a decorated function's `__name__`/docstring
  intact. Bridged from SQL per the baseline record: a decorator framed as a
  `BEFORE`/`AFTER` trigger wrapped around a table write — the original
  statement still runs unchanged, extra logic runs around it — introduced
  before any Python in the top callout, not from a pandas or other
  "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–11 entry already flagged). Paced conservatively per that same
  assumption: one core mechanism (plain wrap-and-return) given the most
  explanatory weight before layering on arguments, at most three nested
  function levels shown (the `repeat(times)` example), and no additional
  decorator features (class-based decorators, stacking multiple decorators
  on one function, `@staticmethod`/`@classmethod`) pulled in beyond what the
  spine's single line ("decorators, and why they appear everywhere in
  FastAPI") calls for. Unverified against real quiz/completion data, same
  caveat as every entry since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file, exactly one hit in the
  lesson); exactly one contrast sentence, and an unusual one for this
  course — decorators have no real pandas equivalent to name, so the
  sentence explicitly says so ("pandas doesn't lean on custom decorators the
  way FastAPI does … nothing to contrast today") rather than naming a
  specific pandas call, still placed once in its own callout and labeled in
  prose as the only such sentence, matching the hard-rule section above.
  Practice file `practice/12_decorators.py` (5 exercises: a plain
  `shout(func)` decorator upper-casing a return value, a `count_calls(func)`
  decorator tracking call count via a `wrapper.calls` attribute, a
  `repeat(times)` decorator-with-arguments calling the wrapped function
  `times` times and collecting a list, a `noisy(func)` decorator using
  `@functools.wraps(func)` to preserve `__name__`/`__doc__`, and a manual
  `triple_it = plain_double(triple_it)` rebind with no `@` syntax at all, to
  make the sugar equivalence from lesson section 2 concrete) was verified in
  a scratch dir (`.scratch_py12_verify/`, created under the repo root and
  removed after use, per the Day 3–11 precedent that `/tmp` is out of bounds
  for this sandbox). **One bug was caught and fixed during verification,**
  a new failure mode this course's practice files hadn't hit before: the
  first draft's Exercise 3 TODO left `repeat(times)`'s body as a bare `...`,
  which makes `repeat(times)` implicitly return `None` — and because
  `@repeat(3)` is applied to `roll()` eagerly, at *import/run* time, not
  when a check later calls `roll()`, the shipped (unsolved) file crashed
  immediately with `TypeError: 'NoneType' object is not callable` before a
  single check could even run, violating this file's "must fail gracefully"
  rule in the same spirit as Day 11's parametrize-collection crash, though
  the trigger here is decoration order rather than test collection. Fixed
  by giving `repeat(times)`'s TODO body a real placeholder decorator
  (`def decorator(func): return func`) that lets the module import cleanly
  — `roll()` then stays undecorated in effect, so calling it later returns
  a bare `4` instead of `[4, 4, 4]`, and Exercise 3's check reports a clean
  ✗ instead of crashing. After the fix: the shipped (unsolved) copy ran via
  `uv run python3`, both from the scratch copy and from its real
  `practice/` path with the documented command, and printed five clean ✗
  lines with no traceback each time; a separately solved copy printed five
  ✓ and the "All green" tally.
  Glossary: added a Day 12 section to `reference/glossary.html` (`decorator`,
  `wrapper`, `decorator with arguments`, `functools.wraps`) after confirming
  via grep that none of the four terms collided with any Day 1–11 entry. All
  four also got matching `<dfn>` markup at first use in the lesson body,
  matching Day 11's density of glossarying every newly introduced term
  inline rather than leaving any undefined.
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, not piped through compound
  grep/awk/multi-stage commands, since this sandbox's approval gate blocks
  compound bash commands exactly as in every prior day) and mismatched on
  the first draft for four of the five questions (Q1 8/9/8, Q2 8/8/9, Q4
  9/9/10, Q5 9/10/10) — Q3 was already equal on the first draft (10/10/10).
  Each mismatched question needed multiple rewrite-and-recount rounds — Q2
  and Q4 in particular needed three attempts each, including one round where
  an edit changed only punctuation (a comma, an em-dash) and left the word
  count unchanged, a false start also seen in Day 6's entry — until every
  option matched (Q1 9/9/9, Q2 9/9/9, Q3 10/10/10, Q4 10/10/10, Q5
  10/10/10), then a full final recount pass across all five questions' three
  options each (15 lines total, each checked individually) confirmed every
  one before shipping, per this file's instruction to recount after any
  edit. Registered in `assets/nav.js` with `date: "2026-08-09"`.
  **DB access:** the read path (`bin/query-progress`) was confirmed blocked
  again before this run started, per this run's own instructions, so
  learning-record freshness was judged from on-disk files only, consistent
  with every prior day since Day 8.
  `bin/record-progress python lesson_generated --day 12 --lesson
  0012-decorators.html --detail '{"by":"github-actions"}'` was run once
  after shipping and **succeeded**: `recorded: python/lesson_generated
  day=12 lesson=0012-decorators.html` — fourth consecutive success (Days 9,
  10, 11, 12), continuing to suggest the write path is reliable in this
  sandbox regardless of the read-path blockage.
- 2026-08-10 — **Day 13 generated** (`lessons/0013-pathlib.html`), the
  headless run's sixth Phase 2 lesson. Idempotency check confirmed on-disk:
  highest existing lesson file was `0012-…` dated 2026-08-09, no `0013-…`
  file and no `date: "2026-08-10"` entry existed yet in `assets/nav.js`
  before this run, so generation proceeded as Day 13. Also grepped
  `python/lessons/` for `pathlib|Path\(` before writing anything: two hits
  (`0011-testing-with-pytest.html`, `0012-decorators.html`), both confirmed
  incidental — Day 9's practice file's own `from pathlib import Path`
  fixture-building infrastructure isn't a lesson file at all, and Day 12's
  only mention is its own forward-reference "next up" line naming `pathlib`
  as a future topic — so pathlib itself had not actually been taught yet.
  Topic: `pathlib` — the first of the three items bundled into PLAN.md's
  Phase 2a spine's last bullet ("`pathlib`, `datetime`/timezones, `logging`
  — the three most-used stdlib corners left"). Per this run's instructions,
  split that bundled line into one topic per day, matching every prior
  spine bullet's own one-day treatment, and took `pathlib` first since it's
  named first in the bullet; `datetime`/timezones and `logging` are
  deliberately not attempted today. Taught: the concrete failure modes of
  building a path with plain string concatenation (`dir + "/" + filename`)
  — wrong separator on Windows, an accidental double slash if `dir` already
  ends in one — framed as structural bugs a string representation cannot
  avoid, not typos; `Path` and the `/` operator overload (join, not
  division), explicitly compared to `+` already meaning two different
  things for strings vs. numbers so the unusual mental model lands as "one
  more operator overload," not a wholly new idea; `.exists()`/`.is_file()`/
  `.is_dir()` and `.mkdir(parents=True, exist_ok=True)` as one memorizable
  unit; `.read_text()`/`.write_text()` explicitly framed as a shortcut
  *over* Day 6's `open()`/`with` material, not a replacement — a `Path`
  works as a drop-in `open()` argument and supports `with` identically,
  stated directly in section 4; `.glob()`/`.rglob()` as a lazy, Day-5-style
  generator over matching files; and `.name`/`.stem`/`.suffix`/`.parent` as
  properties replacing hand-rolled string-slicing, with `.parent` returning
  a real `Path` so it chains. Bridged from SQL per the baseline record: a
  file path framed as a lookup key into the filesystem, the same role a
  primary key plays for a `SELECT ... WHERE id = ?` — introduced before any
  Python in the top callout, not from a pandas or other "Python-adjacent"
  analogy, per this run's explicit instruction to bridge from SQL and not
  from pandas.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–12 entry already flagged). Paced conservatively per that same
  assumption: exactly one sub-topic of the spine's bundled last line taught
  today rather than cramming all three, and every method covered is one
  actually needed for the exercises (no `Path.home()`, `Path.cwd()`,
  `resolve()`, or `PurePath` variants pulled in beyond what the lesson and
  practice file use). Unverified against real quiz/completion data, same
  caveat as every entry since Day 8.
  No-pandas rule: `pathlib` itself is standard library, fully in scope; grep
  for `pandas|numpy|dataframe`, case-insensitive, across both new files
  found zero hits in the practice file and exactly one hit in the lesson —
  `pd.read_csv(path)` named, not demonstrated, as the single allowed
  contrast sentence (pandas accepting either a string or a `Path`
  interchangeably), placed once after section 6 and labeled in prose as the
  only such sentence, matching the hard-rule section above.
  Practice file `practice/13_pathlib.py` (5 exercises: joining two path
  pieces with `/`, creating a file and checking `.exists()`/`.is_file()`
  before/after, a `.write_text()`/`.read_text()` round trip, `.glob()`
  matching only the top-level `*.csv` files against a small fixture
  directory with a nested `archive/` subfolder to prove `.glob()` doesn't
  recurse, and decomposing a path into `.name`/`.stem`/`.suffix`) needed
  real files on disk to check honestly, so it followed the Day 6/9/10
  precedent of writing its own fixtures at runtime into a
  `tempfile.mkdtemp()` directory rather than touching any existing fixture
  file — no extra files added under `practice/` itself. Went back to the
  normal ✓/✗ `check()` idiom (Days 8, 9, 10, 12's convention) rather than
  Day 11's one-off real-pytest-file exception, since nothing about
  `pathlib` calls for pytest specifically. Verified in a scratch dir
  (`.scratch_py13_verify/`, created under the repo root and removed after
  use, per the Day 3–12 precedent that `/tmp` is out of bounds for this
  sandbox): the shipped (unsolved) copy ran via `uv run python3`, both from
  the scratch copy and from its real `practice/` path with the documented
  command, and printed five clean ✗ lines with no traceback each time —
  checked each placeholder position carefully per this run's own warning
  about silent-success bugs, and confirmed every unsolved function's bare
  `...` body returns `None`, which fails every check's equality comparison
  rather than raising or silently passing; a separately solved copy printed
  five ✓ and the "All green" tally. No bugs found during verification —
  both passes succeeded on the first attempt.
  Glossary: added a Day 13 section to `reference/glossary.html` (`pathlib`,
  `Path`, `/ operator (path joining)`, `glob (pattern matching)`) after
  confirming via grep that none of the four terms/entries collided with any
  Day 1–12 entry. All four also got matching `<dfn>` markup at first use in
  the lesson body, matching Day 11/12's density of glossarying every newly
  introduced term inline rather than leaving any undefined.
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, not piped through compound commands, since
  this sandbox's approval gate blocks compound bash commands exactly as in
  every prior day) and mismatched on the first draft for four of the five
  questions (Q1 10/9/9, Q2 9/10/9, Q3 12/11/10, Q4 11/10/9) — Q5 was already
  equal on the first draft (8/8/8). Each mismatched question went through
  one to two rewrite-and-recount rounds — Q3 in particular needed two full
  rewrites of all three options before landing on a common count — until
  every option matched (Q1 9/9/9, Q2 9/9/9, Q3 11/11/11, Q4 10/10/10, Q5
  8/8/8), then a full final recount pass across all five questions' three
  options each (15 lines total, each checked individually) confirmed every
  one before shipping, per this file's instruction to recount after any
  edit. Registered in `assets/nav.js` with `date: "2026-08-10"`.
  **DB access:** the read path (`bin/query-progress`) was not attempted
  separately this run; learning-record freshness was judged from on-disk
  files only, consistent with every prior day since Day 8.
  `bin/record-progress python lesson_generated --day 13 --lesson
  0013-pathlib.html --detail '{"by":"github-actions"}'` was run once after
  shipping and **succeeded**: `recorded: python/lesson_generated day=13
  lesson=0013-pathlib.html` — fifth consecutive success (Days 9, 10, 11, 12,
  13), continuing to suggest the write path is reliable in this sandbox
  regardless of the read-path blockage.
  **Next-day note:** per this run's own instructions, `datetime`/timezones
  is the natural next-day candidate — the second item of PLAN.md's bundled
  last spine line, left deliberately untouched today alongside `logging`,
  which should come after it, completing the three-item bundle one day at a
  time.
- 2026-08-11 — **Day 14 generated** (`lessons/0014-datetime-and-timezones.html`),
  the headless run's seventh Phase 2 lesson. Idempotency check confirmed
  on-disk before writing anything: highest existing lesson file was `0013-…`
  dated 2026-08-10, no `0014-…` file existed, and no `2026-08-11` entry
  existed yet in this file's own log or in `assets/nav.js` — generation
  proceeded as Day 14, not a re-run.
  Topic: `datetime`/timezones — the second of the three items bundled into
  PLAN.md's Phase 2a spine's last bullet ("`pathlib`, `datetime`/timezones,
  `logging` — the three most-used stdlib corners left"), directly following
  Day 13's split of that bundle, and Day 13's own closing line, which had
  already named this as next. Taught: naive vs. aware datetimes framed
  through SQL's `TIMESTAMP` vs. `TIMESTAMPTZ` split (no `tzinfo` attached vs.
  a real one, ambiguous vs. unambiguous when compared across machines);
  `datetime.now()` (naive, local-machine zone, unstated) vs.
  `datetime.now(timezone.utc)` (aware, unambiguous everywhere) as the
  concrete default-to-reach-for distinction; the naive-datetime footgun made
  literal — two servers in different zones producing plausible-looking but
  wrong subtraction results, versus Python's actual behavior of raising
  `TypeError` outright when an aware and a naive value are mixed, framed as
  the language protecting against the bug rather than an obstacle; `timedelta`
  arithmetic (`+`/`-` with a `datetime`, `.total_seconds()`); parsing/
  formatting split into two tool pairs — `strftime`/`strptime` for arbitrary
  format codes, `.isoformat()`/`datetime.fromisoformat()` as the shortcut for
  the ISO 8601 shape databases and JSON APIs actually use; and `zoneinfo`
  (Python 3.9+ stdlib, confirmed not `pytz`) for real named-timezone
  conversion via `.astimezone(ZoneInfo(name))`, explicitly gated on starting
  from an aware datetime. Kept deliberately to this subset — no `date`-only
  objects, no `time`-only objects, no `calendar` module, no exhaustive
  `strftime` code table — per this run's own instruction to pick the
  highest-value backend-relevant slice rather than encyclopedic coverage,
  consistent with MISSION.md's "Success does NOT look like" clause. Bridged
  from SQL per the baseline record and per this run's explicit instruction:
  `TIMESTAMP`/`TIMESTAMPTZ` introduced before any Python in the top callout
  and callout box, mapped directly onto naive/aware, not from a pandas or
  other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–13 entry already flagged). Paced conservatively per that same assumption:
  one core distinction (naive vs. aware) given the most explanatory weight
  and returned to in three different sections (1, 3, 6) rather than treated
  as a single aside, and no additional stdlib time modules pulled in beyond
  what the spine's bundled line and the practice file's five exercises
  actually need. Unverified against real quiz/completion data, same caveat
  as every entry since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file; the lesson has exactly one
  true prose contrast sentence, naming `Timestamp`/the `.dt` accessor/
  vectorized timezone conversion without demonstrating any of them, placed
  once in its own callout after section 6 and labeled in prose as the only
  such sentence, matching the hard-rule section above — plus two quiz
  distractor options that name "pandas" as a wrong answer, the same
  distractor pattern prior lessons' quizzes have used, not a second
  contrast/teaching instance).
  Practice file `practice/14_datetime_and_timezones.py` (5 exercises: building
  an aware UTC datetime from year/month/day/hour/minute pieces, shifting a
  datetime forward with `timedelta`, confirming a naive/aware subtraction
  raises `TypeError` via `try`/`except`, an `isoformat()`/`fromisoformat()`
  round trip, and converting an aware UTC datetime to a named zone with
  `zoneinfo`/`ZoneInfo`) needed no on-disk fixtures — every exercise operates
  on in-memory `datetime` objects, unlike Days 6/9/10/13's file/module-based
  topics — so it stayed with the plain ✓/✗ `check()` idiom used by every day
  except Day 11's pytest exception, with no `tempfile` scaffolding needed this
  time. Verified in a scratch dir (`.scratch_py14_verify/`, created under the
  repo root and removed after use, per the Day 3–13 precedent that `/tmp` is
  out of bounds for this sandbox): the shipped (unsolved) copy ran via
  `uv run python3`, both from the scratch copy and from its real `practice/`
  path with the documented command, and printed five clean ✗ lines with no
  traceback each time — checked that every unsolved function's bare `...`
  body returns `None`, which fails every check's comparison rather than
  raising, per this run's own warning about silent-success bugs; a separately
  solved copy (each TODO filled in directly in the scratch copy, not copied
  from the commented-out answer lines blindly) printed five ✓ and the "All
  green" tally. No bugs found during verification — both passes succeeded on
  the first attempt.
  Glossary: added a Day 14 section to `reference/glossary.html` (`datetime`,
  `naive datetime`, `aware datetime`, `timedelta`, `strftime / strptime`,
  `isoformat / fromisoformat`, `zoneinfo`) after confirming via grep that none
  of the seven terms/entries collided with any Day 1–13 entry. All seven also
  got matching `<dfn>` markup at first use in the lesson body, matching Day
  11–13's density of glossarying every newly introduced term inline rather
  than leaving any undefined.
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, not piped through compound commands, since
  this sandbox's approval gate blocks compound bash commands exactly as in
  every prior day) and mismatched on the first draft for all five questions
  (Q1 10/8/10, Q2 11/9/9, Q3 8/8/9, Q4 10/10/7, Q5 7/8/9). Each mismatched
  question went through one to four rewrite-and-recount rounds — Q1's third
  option in particular needed three attempts (10 → 11 → 12 → 10 words,
  overshooting twice before landing back on the target) and Q4's third option
  needed three attempts to climb from 7 to 10 — until every option matched
  (Q1 10/10/10, Q2 9/9/9, Q3 9/9/9, Q4 10/10/10, Q5 9/9/9), then a full final
  recount pass across all five questions' three options each (15 lines total,
  each checked individually with its own `wc -w` call) confirmed every one
  before shipping, per this file's instruction to recount after any edit.
  Registered in `assets/nav.js` with `date: "2026-08-11"`.
  **DB access:** environment-variable reads were blocked outright in this
  sandbox (even a bare `env` invocation required approval with no user
  present), and `~/.config/learning/db.env` did not exist in this checkout,
  so no read-path attempt was made this run beyond confirming those two facts
  — consistent with every prior day's experience that the read path is
  unavailable.
  `bin/record-progress python lesson_generated --day 14 --lesson
  0014-datetime-and-timezones.html --detail '{"by":"launchd"}'` was attempted
  once after shipping, per this run's instructions, and **required
  interactive approval with no user present, so it did not complete** —
  outcome is "not recorded to DB this run," not retried, consistent with the
  majority of prior days (only Days 5 and 9–13 succeeded non-interactively;
  Days 1–4, 6, 7, 8 all required approval and were not recorded).
- 2026-08-12 generation (Day 15): **Day 15 generated**
  (`lessons/0015-logging.html`), the headless run's eighth Phase 2 lesson and
  **the last item of Phase 2a's stdlib-corners bullet** — Phase 2b's FastAPI +
  pydantic backend phase is next per PLAN.md. Idempotency check confirmed
  on-disk before writing anything: highest existing lesson file was `0014-…`
  dated 2026-08-11, no `0015-…` file existed, and no `2026-08-12` entry
  existed yet in this file's own log or in `assets/nav.js` — generation
  proceeded as Day 15, not a re-run.
  Topic: `logging` — the third and last of the three items bundled into
  PLAN.md's Phase 2a spine's last bullet ("`pathlib`, `datetime`/timezones,
  `logging` — the three most-used stdlib corners left"), directly following
  Day 13's `pathlib` and Day 14's `datetime`/timezones, and Day 14's own
  closing line, which had already named `logging` as next. Kept to one core
  mechanism taught deeply, per this run's own instruction: the
  logger/handler/formatter split (section 3) — logger is what code calls and
  decides on its own level, handler owns the destination, formatter owns text
  rendering, attached to the handler not the logger, so one log call can
  render two different ways through two different handlers. Also taught: why
  `print()` isn't enough (no severity, no destination routing, no per-module
  on/off switch); the five standard levels (DEBUG/INFO/WARNING/ERROR/CRITICAL)
  as the filter mechanism itself, not just labels; `basicConfig()` as the
  one-call setup for a script versus manual wiring for a library module, and
  the load-bearing detail that only its first call in a process has any
  effect; and logging a caught exception with `exc_info=True` to attach the
  traceback, tied directly back to Day 8's exceptions material — a narrow
  `except` block that logs before returning instead of silently swallowing
  the error, plus the `%r`/lazy-formatting argument over an f-string (a
  filtered-out DEBUG call never pays the string-building cost). Bridged from
  SQL per the baseline record and per this run's explicit instruction: a
  production database's log table of statement failures, each stamped with a
  severity and queried after the fact, introduced before any Python in the
  top callout, not from a pandas or other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–14 entry already flagged). Paced conservatively per that same assumption:
  exactly one core mechanism (logger/handler/formatter split) given the most
  explanatory weight, anchored to already-taught material (Day 6 context
  managers implicitly via "always runs" framing reused from Day 8/11 rather
  than restated, Day 8 exceptions explicitly in section 5, Day 9 modules via
  `getLogger(__name__)`), and no additional logging features (custom filters,
  `RotatingFileHandler`, `dictConfig`, structured/JSON logging, the
  `logging.config` module) pulled in beyond the spine's single line.
  Unverified against real quiz/completion data, same caveat as every entry
  since Day 8.
  No-pandas rule: `logging` itself is standard library, fully in scope; grep
  for `pandas|numpy|dataframe`, case-insensitive, across both new files found
  zero hits in the practice file and exactly one hit in the lesson — a
  one-line callout stating pandas pipelines log through this same stdlib
  module with no separate "pandas logging," placed once after section 5 and
  labeled in prose as the only such sentence, matching the hard-rule section
  above.
  Practice file `practice/15_logging.py` (5 exercises: building a logger with
  a handler and formatter attached via `build_logger()`, filtering by level
  via `set_logger_level()`, logging a message and reading back the formatted
  text from an in-memory `io.StringIO` stream via `log_and_read()`, logging a
  caught `ValueError` with `exc_info=True` via `safe_int()`, and confirming a
  below-threshold `logger.info()` call produces no output at all via
  `log_below_threshold()`) needed no on-disk fixtures — every exercise logs
  into an in-memory `io.StringIO` stream via a `StreamHandler`, avoiding both
  real files and stdout/stderr capture, so checks stay deterministic; each
  check calls a `_fresh_logger()` helper that clears any existing handlers on
  a uniquely-named logger before wiring a new stream+handler, since
  `logging.getLogger(name)` returns the *same* cached logger object for a
  repeated name (this course's own Day 9 module-caching idea, applied to
  loggers) and stale handlers from an earlier check would otherwise leak into
  a later one's output. Verified in a scratch dir (`.scratch_py15_verify/`,
  created under the repo root and removed after use, per the Day 3–14
  precedent that `/tmp` is out of bounds for this sandbox): the shipped
  (unsolved) copy ran via `uv run python3`, both from the scratch copy and
  from its real `practice/` path with the documented command, and printed
  five clean ✗ lines with no traceback each time — confirmed every unsolved
  function's bare `...` body returns `None`, which fails every check's
  comparison rather than raising, per this run's own warning about
  silent-success bugs; a separately solved copy (each TODO filled in directly
  in the scratch copy) printed five ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 15 section to `reference/glossary.html` (`logging`,
  `level`, `logger`, `handler`, `formatter`, `root logger`) after confirming
  via grep that none of the six terms/entries collided with any Day 1–14
  entry — each appears exactly once in the glossary file, at its own Day 15
  row. All six also got matching `<dfn>` markup at first use in the lesson
  body, matching Day 11–14's density of glossarying every newly introduced
  term inline rather than leaving any undefined (`logger`/`handler`/
  `formatter`/`root logger` are all defined within section 3/4's shared
  paragraphs rather than one dfn per short standalone sentence, but each
  still gets its own distinct `<dfn>` tag at its first mention).
  Quiz: 5 questions. Word counts were checked with individual `wc -w` calls
  per option line (not by eye, not piped through compound commands, since
  this sandbox's approval gate blocks compound bash commands exactly as in
  every prior day) and mismatched on the first draft for four of the five
  questions (Q1 9/10/10, Q3 10/11/10, Q4 11/9/11, Q5 8/10/10) — Q2 was
  already equal on the first draft (9/9/9). Each mismatched question went
  through one to two rewrite-and-recount rounds — Q4's second option in
  particular needed two attempts (9 → 10 → 11 words) before matching its
  siblings — until every option matched (Q1 10/10/10, Q3 10/10/10, Q4
  11/11/11, Q5 10/10/10), then a full final recount pass across all five
  questions' three options each (15 lines total, each checked individually
  with its own `wc -w` call) confirmed every one before shipping, per this
  file's instruction to recount after any edit. Registered in `assets/nav.js`
  with `date: "2026-08-12"`.
  **DB access:** the read path (`bin/query-progress`) was not attempted this
  run, per this run's own explicit instruction to treat DB reads as
  unreachable and not retry; learning-record freshness was judged from
  on-disk files only, consistent with every prior day since Day 8.
  `bin/record-progress python lesson_generated --day 15 --lesson
  0015-logging.html --detail '{"by":"launchd"}'` was run once after shipping
  and **succeeded**: `recorded: python/lesson_generated day=15
  lesson=0015-logging.html` — continuing the recent run of non-interactive
  successes (Days 9–13 succeeded, Day 14 required approval and failed, Day 15
  succeeded again), still inconsistent run to run and unexplained.
  **This completes Phase 2a's stdlib-corners bullet** (`pathlib` Day 13,
  `datetime`/timezones Day 14, `logging` Day 15) and, with it, all of Phase
  2a's spine items (exceptions, modules, `uv`/`pyproject.toml`, `pytest`,
  decorators, `pathlib`, `datetime`, `logging` — Days 8 through 15). Per
  PLAN.md, **Phase 2b — FastAPI + pydantic backend — is the natural next
  topic**, starting with HTTP handlers, path/query params, and status codes.
- 2026-08-13 — **Day 16 generated**
  (`lessons/0016-fastapi-handlers-and-status-codes.html`), the headless run's
  ninth Phase 2 lesson and **the first lesson of Phase 2b** — the FastAPI +
  pydantic backend phase. Idempotency check confirmed on-disk before writing
  anything: highest existing lesson file was `0015-…` dated 2026-08-12, no
  `0016-…` file existed, and no `2026-08-13` entry existed yet in this file's
  own log or in `assets/nav.js` — generation proceeded as Day 16, not a
  re-run.
  Topic: HTTP handlers, path/query params, status codes — the first item of
  `PLAN.md`'s Phase 2b spine, directly after Day 15 completed all of Phase
  2a. Taught: a route decorator (`@app.get("/ping")`) as Day 12's decorator
  mechanism applied for real, with FastAPI itself installed for the first
  time — explicitly framed as the payoff of Day 12's own "you'll meet this on
  day one of Phase 2b and it will already make sense" promise, not a new
  concept; a handler as the plain function a route decorator wraps, returning
  a `dict` that FastAPI serializes to JSON automatically (contrasted with Day
  6's manual `json.dump` for the same job); path parameters (`{user_id}` in
  the URL, matched by name to a handler parameter, always required, converted
  via Day 7's type hints — `user_id: int` rejects non-integer URL segments
  before the handler runs); query parameters as Day 4's default-argument rule
  reused verbatim — a handler parameter not named in the URL becomes an
  optional query parameter exactly when it carries a default, required
  otherwise; status codes (`2xx`/`4xx`/`5xx` by leading digit,
  `raise HTTPException(status_code=404, ...)` as Day 8's `raise` mechanism
  reused unchanged and specifically caught by FastAPI, and a route's own
  `status_code=201` for a successful `POST`); and testing a handler via
  `TestClient` (built on `httpx`) as Day 11's plain `assert` aimed at
  `.status_code`/`.json()` instead of a plain return value, calling routes
  in-process with no real server needed — a direct consequence of Day 12's
  point that a route is still just a function under the decorator. Bridged
  from SQL per the baseline record and this run's instructions: a route
  framed as a stored procedure named by URL instead of function name, and
  path/query parameters mapped onto required vs. optional-with-default
  procedure arguments — the same distinction Day 4 already drew for Python
  functions — introduced before any Python in the top callout, not from a
  pandas or other "Python-adjacent" analogy.
  **Scope-change flag, explicitly called out per this run's instructions:**
  this is the first lesson in the course whose practice file needs a
  non-stdlib dependency for a reason other than testing tooling — Days 1–10
  and 12–15 were pure standard library, and Day 11's `pytest` was the sole
  prior exception (a testing tool, not application code). Today's `fastapi`
  (plus `httpx`, which `fastapi.testclient.TestClient` is built on) is a
  deliberate, MISSION-sanctioned scope change: PLAN.md's Phase 2b spine
  explicitly commits this course to "a small FastAPI + pydantic service," so
  application-level third-party dependencies are now legitimate, not a
  drift from the "stdlib only" rule that governed Phase 1 and Phase 2a.
  Installed the same one-off way as Day 11's `pytest` — `uv run --with
  fastapi --with httpx python3 …`, mirroring `data/`'s own established
  `uv run --with pandas …` convention for its practice files — with no
  `pyproject.toml` changes, since this course still has none. Confirmed both
  packages install and import cleanly in this sandbox before writing the
  lesson (`uv run --with fastapi --with httpx python3 -c "import fastapi,
  httpx; ..."` succeeded, reporting fastapi 0.141.1 / httpx 0.28.1).
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–15 entry already flagged). Paced conservatively per that same
  assumption: one lesson covering exactly the spine's first named trio
  (handlers, path/query params, status codes), no pydantic models, dependency
  injection, or `async`/`await` pulled forward from later spine items, and
  every new mechanism tied back explicitly to material already taught
  (Day 12 decorators, Day 4 default arguments, Day 7 type hints, Day 8
  `raise`, Day 11 `assert`) rather than introduced as unrelated new ground.
  Unverified against real quiz/completion data, same caveat as every entry
  since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe|DataFrame`, case-insensitive,
  across both new files — zero hits in the practice file, exactly one hit in
  the lesson); exactly one contrast sentence, naming `df.to_dict("records")`
  without demonstrating it, placed once in its own callout after section 5
  and labeled in prose as the only such sentence, matching the hard-rule
  section above.
  Practice file `practice/16_fastapi_handlers_and_status_codes.py` (5
  exercises: a `GET` handler with a path parameter, a `GET` handler with a
  default-valued query parameter, a `GET` handler raising
  `HTTPException(404, ...)` for a missing user, a `POST` handler returning
  `201`, and a helper reading a parsed JSON body back from `TestClient`) is
  the first practice file in this course requiring `--with` flags for
  application code rather than test tooling, per the scope-change flag
  above; the shipped (unsolved) form leaves the decorator line itself as a
  bare `...` expression statement (a no-op, so the function underneath stays
  undecorated and FastAPI never registers that route) rather than leaving the
  function body unsolved under a real decorator — chosen deliberately after
  recalling Day 12's own caught bug, where decorating eagerly at import time
  with an unsolved decorator body crashed the whole file before any check
  could run; leaving the decorator itself as the TODO sidesteps that failure
  mode entirely, since an unregistered route just makes its own check fail
  cleanly (a 404 or a `KeyError` inside the lambda, caught by `check()`'s own
  `try/except`) without touching any other exercise. Verified in a scratch
  dir (`.scratch/py16_verify/`, created under the repo root rather than
  `/tmp` per the Day 3–15 precedent that `/tmp` is out of bounds for this
  sandbox, and removed after use): the shipped (unsolved) copy ran via
  `uv run --with fastapi --with httpx python3`, both from the scratch copy
  and from its real `practice/` path with the documented command, and
  printed five clean ✗ lines with no traceback each time; a separately
  solved copy (each TODO filled in directly, not copied from the
  commented-out answer lines blindly) printed five ✓ and the "All green"
  tally. No bugs found during verification — both passes succeeded on the
  first attempt. One non-bug observation worth recording: both runs printed
  a `StarletteDeprecationWarning` about using `httpx` with
  `starlette.testclient` (recommending an `httpx2` package), coming from the
  very-latest `fastapi`/`starlette` versions this sandbox resolved via
  `--with` with no version pin; it is a warning only, prints identically for
  both the unsolved and solved copies, and does not affect any check's
  pass/fail outcome — left unpinned since this course has no
  `pyproject.toml`/`uv.lock` anywhere to pin against (Day 10's own territory)
  and every other `--with`-based practice file in this course (Day 11) is
  similarly unpinned by design.
  Glossary: added a Day 16 section to `reference/glossary.html` (`FastAPI`,
  `GET request`, `handler (FastAPI route)`, `path parameter`, `query
  parameter`, `status code`) after checking via grep that none collided with
  Day 1–15 entries — found one real collision: Day 15 already has a `handler`
  row (a logging handler, owning a log record's destination). Followed this
  course's own established disambiguation pattern (Day 4's `key= (sorting)`
  vs. Day 3's `key`; Day 7's `default (dataclass field)` vs. Day 4's `default
  argument`) and titled today's entry `handler (FastAPI route)`, with its own
  "In software" cell explicitly naming the Day 15 sense and why the title
  differs. All six terms also got matching `<dfn>` markup at first use in the
  lesson body, matching Day 11–15's density of glossarying every newly
  introduced term inline.
  Quiz: 5 questions. Word counts were checked with a small Python script
  (`uv run python3 …`, run from a `.scratch_wc16/` scratch dir removed after
  use) that regex-extracts every `<button class="opt">` line and counts
  `.split()` words per option — chosen over individual `wc -w` calls per this
  run's explicit instruction to verify word counts via a Python word-count
  script rather than looped/compound bash, which this sandbox's approval gate
  blocks anyway, consistent with every prior day's experience. Mismatched on
  the first draft for four of the five questions (Q2 11/10/11, Q3 10/8/10, Q4
  13/10/11, Q5 11/10/10) — Q1 was already equal on the first draft
  (11/11/11). Each mismatched question went through one to three
  rewrite-and-recount rounds — Q4 in particular needed three attempts on its
  first option (13 → 12 → 10 words) before landing on the target count, and
  one round changed only "with no"/"without a" (same word count either way, a
  false-start edit in the same spirit as Day 6 and Day 12's own logged
  false-starts) before an actual word was cut — until every option matched
  (Q1 11/11/11, Q2 11/11/11, Q3 10/10/10, Q4 10/10/10, Q5 10/10/10), then a
  full final script run across all five questions' three options each (15
  lines total) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-13"`.
  **DB access:** per this run's explicit instructions, no attempt was made
  this run at `psql "$LEARNING_DB_URL" ...`, `source
  ~/.config/learning/db.env`, `printenv`, or `bin/query-progress` — all
  require interactive approval with no approver present in this headless run
  and have failed or been blocked on every day since Day 8, so this run
  skipped re-spending an attempt on the read path per that established
  precedent, and paced from on-disk state alone (this file's own log,
  `python/lessons/`, and `python/learning-records/`, which still holds only
  the Day 1 baseline record).
  `bin/record-progress python lesson_generated --day 16 --lesson
  0016-fastapi-handlers-and-status-codes.html --detail
  '{"by":"github-actions"}'` was run once after shipping, per this run's
  instructions — see its own output for whether it recorded successfully.
  **This is Phase 2b's opening lesson.** Per PLAN.md's Phase 2b spine, the
  natural next-day candidate is pydantic models — validation, coercion,
  custom validators, settings — the second item, directly following today's
  handlers/params/status-codes foundation.
- 2026-08-14 — **Day 17 generated**
  (`lessons/0017-pydantic-models-and-validation.html`), the headless run's
  tenth Phase 2 lesson. Idempotency check confirmed on-disk before writing
  anything: highest existing lesson file was `0016-…` dated 2026-08-13, no
  `0017-…` file existed, and no `2026-08-14` entry existed yet in this file's
  own log or in `assets/nav.js` — generation proceeded as Day 17, not a
  re-run.
  Topic: pydantic models — validation, coercion, custom validators, settings
  — the second item of `PLAN.md`'s Phase 2b spine, directly after Day 16
  completed the first (handlers/params/status-codes), and named explicitly
  as "next up" in Day 16's own closing line. Taught: the gap a plain
  `@dataclass` leaves open — Day 7 already said type hints are documentation
  only, demonstrated concretely today with a dataclass silently storing a
  string where `price: float` was promised, then crashing far away from the
  real mistake; a pydantic `BaseModel` closing that gap, with **coercion**
  (a compatible input like `"12.5"` converted into the declared `float`) and
  **validation** (the check that makes coercion possible or raises
  `ValidationError` when it isn't) introduced as two distinct, named
  mechanisms rather than one blurred idea; `ValidationError` itself, shown
  reporting every failing field in one message; a custom `@field_validator`
  rule (paired with `@classmethod`), explicitly built from two Day-12 ideas
  already taught (a decorator wrapping a function, called during
  construction) plus Day 8's `raise ValueError(...)` reused unchanged and
  caught by pydantic instead of the caller — and the load-bearing detail that
  a validator's return value becomes the field's final stored value, which
  is how one function both rejects bad input and normalizes good input
  (lower-casing a username); and `pydantic_settings.BaseSettings` as the
  identical `BaseModel` mechanics pointed at `os.environ`, checking a
  case-insensitively matched environment variable before falling back to a
  field's coded default. Also closed the loop back to Day 16 explicitly:
  section 2 names that FastAPI's `user_id: int` path-parameter validation
  (Day 16 section 2) was already this exact mechanism, unnamed until today.
  Bridged from SQL per the baseline record and this run's instructions: a
  pydantic model framed as `CREATE TABLE` with `CHECK` constraints enforced
  client-side instead of in the database, extending Day 7's own
  dataclass-as-`CREATE-TABLE` framing with the constraint-checking a plain
  dataclass never had, introduced before any Python in the top callout, not
  from a pandas or other "Python-adjacent" analogy.
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch_py17_explore/`, created under the repo root and removed after
  use, per the Day 3–16 precedent that `/tmp` is out of bounds for this
  sandbox): `uv run --with fastapi --with httpx python3 -c "..."` reported
  `fastapi 0.141.1` / `pydantic 2.13.4` (pydantic v2, bundled as a FastAPI
  dependency, no separate `--with pydantic` needed when fastapi is already
  requested); a small script confirmed pydantic v2's real coercion behavior
  (`price='12.5'` → `12.5: float`, `qty='3'` → `3: int`) and its real
  `ValidationError` message text for a genuinely bad value; a second script
  confirmed a `@field_validator`/`@classmethod` pair raising `ValueError`
  produces a `ValidationError` wrapping that message; a third script
  confirmed `pydantic_settings.BaseSettings` is a **separate package**
  (`ImportError: No module named 'pydantic_settings'` when only
  `pydantic`/`fastapi`/`httpx` were requested) and, once installed via
  `--with pydantic-settings`, correctly read `APP_NAME`/`DEBUG` from
  `os.environ` with the same string-to-`bool` coercion (`"true"` → `True`).
  This confirmed exploration is why the lesson and practice file's `--with`
  commands list `pydantic-settings` explicitly rather than assuming it rides
  along with `pydantic` or `fastapi`.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–16 entry already flagged). Paced conservatively per that same assumption
  and this run's own instruction to pace from file-state alone: exactly the
  spine's named quartet (validation, coercion, custom validators, settings)
  covered, no request/response schemas, dependency injection, or `async`
  pulled forward from later Phase 2b spine items, and every new mechanism
  tied back explicitly to material already taught (Day 7 dataclasses/type
  hints, Day 8 `raise`, Day 12 decorators, Day 16 path-parameter validation)
  rather than introduced as unrelated new ground. Unverified against real
  quiz/completion data, same caveat as every entry since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe|DataFrame`, case-insensitive,
  across both new files — zero hits in the practice file, exactly one hit in
  the lesson); exactly one contrast sentence, contrasting a pydantic model's
  single-record shape validation against a DataFrame's column-wide `dtypes`,
  without demonstrating any pandas API, placed once in its own callout after
  section 4 and labeled in prose as the only such sentence, matching the
  hard-rule section above.
  Practice file `practice/17_pydantic_models_and_validation.py` (4
  exercises: defining an `Item(BaseModel)` with a coerced/defaulted field,
  `item_is_valid()` catching `ValidationError` to tell good kwargs from bad,
  a `SignUp` model's `field_validator` rejecting spaces and lower-casing
  good input, and a `Settings(BaseSettings)` reading `APP_NAME`/`DEBUG` back
  from `os.environ`) needed no on-disk fixtures — every exercise operates on
  in-memory model construction and `os.environ`, so it stayed with the plain
  ✓/✗ `check()` idiom used by every day except Day 11's pytest exception, no
  `tempfile` scaffolding needed. Uses `--with pydantic --with
  pydantic-settings` (no `fastapi`/`httpx`, unlike Day 16, since nothing
  here runs a route), confirmed sufficient by running the shipped file with
  exactly that command. **One bug was caught and fixed during verification,
  a repeat of a known failure mode this course has hit before (Day 12, Day
  16):** the first draft's Exercise 1 and Exercise 4 TODO placeholders wrote
  `class Item(...):` / `class Settings(...):`, using a bare `...` as the
  base-class expression — this is not a no-op the way an unsolved `...`
  statement is elsewhere in this course's practice files; a class base list
  is evaluated eagerly at class-definition time, and `...` (the `Ellipsis`
  object) is not a valid base class, so the shipped file crashed immediately
  with `TypeError: EllipsisType takes no arguments` before any check could
  run, violating this file's "must fail gracefully" rule. Fixed by leaving
  each class as a plain, unparameterized class (`class Item:` /
  `class Settings:`) with a TODO comment naming the exact base to add,
  matching Day 16's own resolution of a related eager-evaluation bug
  (leaving a route decorator's TODO as a no-op statement above the `def`
  rather than inside a still-eagerly-applied decorator). After the fix: the
  shipped (unsolved) copy, run via `uv run --with pydantic --with
  pydantic-settings python3`, both from a scratch copy
  (`.scratch_py17_verify/`, created under the repo root and removed after
  use) and from its real `practice/` path with the documented command,
  printed four clean ✗ lines with no traceback each time — a plain `Item`/
  `Settings` class with no `BaseModel`/`BaseSettings` parent raises a plain
  `TypeError` on construction with keyword arguments it doesn't accept,
  caught cleanly by `check()`'s own `try`/`except`; a separately solved copy
  printed four ✓ and the "All green" tally.
  Glossary: added a Day 17 section to `reference/glossary.html` (`pydantic
  model`, `coercion`, `validation`, `ValidationError`, `field_validator`,
  `BaseSettings`) after confirming via grep — extracting every existing
  `<tr><td>term</td>` row across Days 1–16 — that none of the six
  terms/entries collided with any prior entry (no existing `model`,
  `field`, `validator`, `settings`, or `error`-only row anywhere in the
  file, so no disambiguating title was needed today, unlike Day 4's `key=
  (sorting)`, Day 7's `default (dataclass field)`, or Day 16's own `handler
  (FastAPI route)`). All six also got matching `<dfn>` markup at first use
  in the lesson body (confirmed by counting `<dfn data-en` occurrences,
  6 total), matching Day 11–16's density of glossarying every newly
  introduced term inline rather than leaving any undefined.
  Quiz: 5 questions. Word counts were checked with a small Python script
  (`uv run python3 …`, run from a `.scratch_wc17/` scratch dir removed after
  use) that regex-splits the quiz block into its five question `<div>`s and
  counts `.split()` words per `<button class="opt">` line — chosen over
  individual `wc -w` calls or bash loops per this course's established
  convention (loops blocked by this sandbox's static analysis; a Python
  script is the documented workaround). The script's first version had a
  greedy regex that collapsed all five questions into one 15-option match —
  caught immediately since the printed option count (15 for "Q1") didn't
  match the expected 3, fixed by splitting on each `<div class="q"` start
  instead of a single greedy `.*?` span. Mismatched on the first draft for
  all five questions (Q1 11/11/7, Q2 10/9/9, Q3 11/9/10, Q4 10/8/10, Q5
  11/11/14) — each went through two to four rewrite-and-recount rounds,
  including a couple of overshoot/undershoot cycles on Q1's and Q3's third
  options before landing on the target count — until every option matched
  (Q1 11/11/11, Q2 10/10/10, Q3 11/11/11, Q4 10/10/10, Q5 11/11/11), then a
  full final script run across all five questions' three options each (15
  lines total) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-14"`.
  **DB access:** per this run's explicit instructions, no attempt was made
  this run at `psql "$LEARNING_DB_URL" ...`, `bin/query-progress`, or any
  other read-path command — all have required interactive approval with no
  approver present and been blocked on every day since Day 8, so this run
  skipped re-spending an attempt on the read path per that established
  precedent, and paced from on-disk state alone (this file's own log,
  `python/lessons/`, `python/learning-records/` — still only the Day 1
  baseline record — and `python/practice/`).
  `bin/record-progress python lesson_generated --day 17 --lesson
  0017-pydantic-models-and-validation.html --detail
  '{"by":"github-actions"}'` was run once after shipping, per this run's
  instructions and the established convention that the write path (unlike
  the read paths) is reliably invocable directly by relative path from the
  repo root — see its own output below for whether it recorded
  successfully.
  **Next-day note:** per `PLAN.md`'s Phase 2b spine, the natural next-day
  candidate is request/response schemas — and why the type hints on a
  FastAPI handler *are* the contract — the third item, directly following
  today's pydantic-model foundation, already named in today's lesson's own
  closing line.
- 2026-08-15 — **Day 18 generated**
  (`lessons/0018-request-response-schemas.html`), the headless run's
  eleventh Phase 2 lesson. Idempotency check confirmed on-disk before
  writing anything: highest existing lesson file was `0017-…` dated
  2026-08-14, no `0018-…` file existed, and no `2026-08-15` entry existed
  yet in `assets/nav.js` — generation proceeded as Day 18, not a re-run.
  Topic: request/response schemas — using a pydantic model as a FastAPI
  handler's request-body parameter type, and a second pydantic model as its
  `response_model`, so the handler's signature alone is a complete,
  machine-checked description of what a route accepts and returns. This is
  the third item of `PLAN.md`'s Phase 2b spine, directly after Day 17
  completed the second (pydantic validation/coercion/settings), and named
  explicitly both in Day 17's own closing line and in this file's own Day 17
  next-day note. Taught: giving a handler parameter a pydantic `BaseModel`
  type hint (no default) switches it from Day 16's query-parameter reading
  to reading the request's JSON body instead — reusing Day 16's "a type
  hint decides how a value is read" rule and Day 17's `BaseModel`
  construction/coercion/`ValidationError` mechanics unchanged, just applied
  to a whole record instead of one path/query value, and confirmed that a
  body failing validation never reaches the handler at all, returning HTTP
  422 automatically; `response_model=` as the same enforcement applied to a
  handler's `return` value on the way out — built from whatever the handler
  returned, with any field not declared on the response model silently
  filtered before the client ever sees it, confirmed directly by running a
  handler that deliberately returned an extra `secret_cost` field through
  `TestClient` and observing it absent from the actual response JSON, not
  just asserted from the docs; and why a real route almost always uses two
  distinct schemas (an `...In` request model and an `...Out` response
  model) rather than one model for both directions — server-assigned fields
  like `id` belong only on the `Out` side, and fields that must never leak
  back out (the lesson names a hypothetical `password` field on `ItemIn` as
  the motivating case, not demonstrated as a real exercise) have no way to
  leak through a deliberately narrower, separately declared response model.
  Bridged from SQL per the baseline record: a request schema framed as an
  `INSERT`'s column list with `CHECK` constraints rejecting a bad row before
  it touches anything, a response schema framed as a `VIEW`'s declared
  output columns deciding what a caller may see regardless of what the
  underlying row actually carries.
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch/python-lesson18/`, created under the repo root's shared
  `.scratch/` area per this run's own instructions, removed after use): a
  script built a two-route FastAPI app mirroring section 2's exact example
  (a `POST /items` handler returning a dict with an extra `secret_cost` key
  alongside `response_model=ItemOut`) and ran it through `TestClient` —
  confirmed `secret_cost` does not appear in the actual JSON response body,
  confirmed the string `"12.5"` request-body value coerces to a real
  `float` in the response, confirmed a POST body missing a required field
  returns status `422` with FastAPI's own field-level detail rather than
  reaching the handler, and confirmed `fastapi 0.141.1` / `pydantic 2.13.4`
  — the identical versions Day 17 already logged, no drift since then.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–17 entry already flagged). Paced conservatively per that same
  assumption and this run's own instruction to pace from file-state alone:
  exactly the spine's named third item (request/response schemas via
  request-body models and `response_model`) covered, no dependency
  injection, multi-file app structuring, or `async`/`await` pulled forward
  from later Phase 2b spine items, and every new mechanism tied back
  explicitly to material already taught (Day 16's type-hint-driven
  parameter reading, Day 17's `BaseModel`/coercion/`ValidationError`)
  rather than introduced as unrelated new ground. Unverified against real
  quiz/completion data, same caveat as every entry since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file, exactly one hit in the
  lesson); exactly one contrast sentence, contrasting a schema's
  single-record JSON contract against converting DataFrame rows to dicts
  before a `list[...]` response model validates them, without demonstrating
  any pandas API, placed once in its own callout after section 3 and
  labeled in prose as the only such sentence, matching the hard-rule
  section above.
  Practice file `practice/18_request_response_schemas.py` (5 checks: an
  `ItemIn` request model with coercion, a `POST /items` handler reading
  that model as a body parameter and returning the stored record, that same
  route returning `422` on a body missing a required field, an `ItemOut`
  response model with a strict subset of fields, a second route wiring
  `response_model=ItemOut` and confirming a returned `price` field never
  reaches the response JSON, and a small `TestClient` helper reading a
  parsed JSON response back) needed no on-disk fixtures — every exercise
  operates on in-memory model construction and in-process `TestClient`
  calls, matching Day 16's and Day 17's own practice-file shape. Uses
  `--with fastapi --with httpx` (no `pydantic-settings`, unlike Day 17,
  since nothing here reads the environment), confirmed sufficient by
  running the shipped file with exactly that command. Verified in two
  passes, both from a scratch copy (`.scratch/python-lesson18/`, removed
  after use) and from the real `practice/` path with the documented
  command: the shipped (unsolved) copy printed six clean ✗ lines with no
  traceback each time — a plain `ItemIn`/`ItemOut` class with no
  `BaseModel` parent, and route functions with no route decorator applied,
  fail every check's `try`/`except` cleanly inside `check()` rather than
  crashing the module — and a separately solved copy printed six ✓ and the
  "All green" tally.
  Glossary: added a Day 18 section to `reference/glossary.html` (`schema`,
  `response_model`) after confirming via grep that neither term collided
  with any existing entry across Days 1–17. Both also got matching `<dfn>`
  markup at first use in the lesson body (confirmed by counting `<dfn
  data-en` occurrences, 2 total), matching Day 11–17's density of
  glossarying every newly introduced term inline rather than leaving any
  undefined.
  Quiz: 5 questions. Word counts were checked with a small Python script
  (`uv run python3 …`, run from `.scratch/python-lesson18/`, removed after
  use) that regex-splits the quiz block into its five question `<div>`s and
  counts `.split()` words per `<button class="opt">` line, per this
  course's established convention (loops/individual `wc -w` calls blocked
  by this sandbox's approval gate). Mismatched on the first draft for all
  five questions (Q1 9/10/11, Q2 9/12/8, Q3 12/12/9, Q4 12/10/11, Q5
  11/12/12) — each went through two to four rewrite-and-recount rounds,
  including a couple of overshoot/undershoot cycles on Q2's and Q3's
  options, before landing on the target count for every question (Q1
  10/10/10, Q2 10/10/10, Q3 12/12/12, Q4 11/11/11, Q5 11/11/11), then a
  full final script run across all five questions' three options each (15
  lines total) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-15"`.
  **DB access:** per this run's explicit instructions, `bin/query-progress`
  was attempted once as instructed and failed immediately with a
  permission/approval error, exactly the same failure mode logged on every
  day since Day 8 — no retry attempted, and this run paced from on-disk
  state alone (this file's own log, `python/lessons/`,
  `python/learning-records/` — still only the Day 1 baseline record — and
  `python/practice/`) instead, per this run's explicit instruction.
  `bin/record-progress python lesson_generated --day 18 --lesson
  0018-request-response-schemas.html --detail '{"by":"delegated-agent"}'`
  was run once after shipping, per this run's instructions, and succeeded
  — printed `recorded: python/lesson_generated day=18
  lesson=0018-request-response-schemas.html` to stdout with no error.
  **Next-day note:** per `PLAN.md`'s Phase 2b spine, the natural next-day
  candidate is dependency injection with `Depends()`, and structuring an
  app beyond one file — the fourth item, directly following today's
  request/response-schema foundation, already named in today's lesson's own
  closing line.

- 2026-08-16 — **Day 19 generated**
  (`lessons/0019-dependency-injection-and-app-structure.html`), the twelfth
  Phase 2 lesson. Idempotency check confirmed on-disk before writing anything
  (per this run's own instructions, not re-verified independently): highest
  existing lesson file was `0018-…` dated 2026-08-15, no `0018`/`0019` file
  collision, and no `2026-08-16` entry existed yet in `assets/nav.js`.
  Topic: dependency injection with `Depends()`, and structuring a FastAPI app
  beyond one file — exactly the fourth item of `PLAN.md`'s Phase 2b spine,
  named explicitly both in Day 18's own closing line and in this file's own
  Day 18 next-day note, directly after Day 18 completed the third item
  (request/response schemas). Taught: a handler parameter defaulting to
  `Depends(some_function)` makes FastAPI call that plain function first and
  pass its return value in, reusing Day 4's "extract the repeated part into a
  function" idiom but invoked by the framework instead of by hand, confirmed
  by running one shared `get_query_params` dependency across two unrelated
  routes (`/items`, `/users`) through `TestClient` and seeing both read query
  params correctly; a dependency raising `HTTPException` (Day 16's exception
  type, unchanged) blocks the request before the handler's own body runs at
  all, confirmed by sending a bad `x-token` header and observing `401` with
  the handler never reached — plus the sharper nuance that a *missing*
  required header fails one layer earlier, at FastAPI's own parameter
  validation, returning `422` rather than reaching the dependency's `raise`
  at all; sub-dependencies (a dependency whose own parameter also defaults to
  `Depends(...)`) resolve in order and are called exactly once per request
  even when multiple things in the chain need them, confirmed by tracking
  call order and call count with a shared list across a `get_db` →
  `get_current_user` chain; and `APIRouter` as a stand-in for `FastAPI()` in
  a separate route module, using the identical `@router.get(...)` decorator
  shape, attached to the real app with `app.include_router()`, with an
  optional `prefix=` prepended to every route on it — confirmed by building a
  router with `prefix="/products"` and a route at `"/{product_id}"` and
  observing it answer `GET /products/7` through `TestClient` once attached.
  Bridged from SQL per the baseline record: a shared dependency framed as a
  reusable view or CTE referenced from multiple queries — written once,
  referenced by name everywhere it's needed, instead of re-derived inline in
  every query (handler).
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch/python-lesson19/`, created under the repo root's shared
  `.scratch/` area per this run's own instructions, removed after use, not
  `/tmp`): two scripts (`probe.py`, `probe_router.py`) built the exact
  examples above and ran them through `TestClient` — confirmed a shared
  dependency is reused correctly across two different routes, confirmed an
  `HTTPException` raised inside a dependency short-circuits the handler
  (`401`) while a missing required header short-circuits one layer earlier
  still (`422`), confirmed a sub-dependency chain resolves in declared order
  (`get_db` before `get_current_user`) and that `get_db` is called exactly
  once per request (call-count check, not just call-order), and confirmed
  `APIRouter(prefix=...)` plus `app.include_router()` routes requests
  correctly under that prefix — and confirmed `fastapi 0.141.1` / `pydantic
  2.13.4`, the identical versions Days 17-18 already logged, no drift since
  then.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8–18 entry already flagged). Paced conservatively per that same assumption
  and this run's own instruction to pace from file-state alone: exactly the
  spine's named fourth item (dependency injection + multi-file structuring)
  covered, no `async`/`await` pulled forward from the next spine item, and
  every new mechanism tied back explicitly to material already taught (Day
  4's function-extraction idiom, Day 16's `HTTPException` and
  type-hint-driven parameter reading, Day 9's module/package layout).
  Unverified against real quiz/completion data, same caveat as every entry
  since Day 8.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (checked by grep for `pandas|numpy|dataframe`, case-insensitive, across
  both new files — zero hits in the practice file, exactly one hit in the
  lesson); exactly one contrast sentence, contrasting a `Depends()`-managed,
  per-request database connection against a one-shot `pd.read_sql(...)` call
  inside a plain script, without demonstrating any pandas API, placed once in
  its own callout after section 4 and labeled in prose as the only such
  sentence, matching the hard-rule section above.
  Practice file `practice/19_dependency_injection_and_app_structure.py` (7
  checks: a shared query-parameter dependency answering two different
  routes, an auth-style dependency gating a route with `HTTPException`
  correctly on both success and failure, a sub-dependency chain returning
  the right shape and a call-count check confirming `get_db` runs exactly
  once per request, and an `APIRouter` with a `prefix` reachable once
  attached via `include_router()`) needed no on-disk fixtures — every
  exercise operates on in-memory app construction and in-process `TestClient`
  calls, matching Days 16–18's own practice-file shape. Uses `--with fastapi
  --with httpx` only, same as Day 18 (no `pydantic-settings` needed). Verified
  in two passes, both from a scratch copy (`.scratch/python-lesson19/`,
  removed after use) and from the real `practice/` path with the documented
  command: the shipped (unsolved) copy printed seven clean ✗ lines with no
  traceback each time — TODO placeholders (`...` as parameter defaults and
  function bodies) fail every check's `try`/`except` cleanly inside `check()`
  rather than crashing the module at import time — and a separately solved
  copy printed seven ✓ and the "All green" tally.
  Glossary: added a Day 19 section to `reference/glossary.html` (`Depends()`,
  `dependency`, `sub-dependency`, `APIRouter`) after confirming via grep that
  none of the four collided with any existing entry across Days 1–18. All
  four also got matching `<dfn>` markup at first use in the lesson body
  (confirmed by counting `<dfn data-en` occurrences, 4 total, matching the
  four glossary rows one-for-one), matching Day 11–18's density of
  glossarying every newly introduced term inline rather than leaving any
  undefined.
  Quiz: 5 questions. Word counts were checked with a small Python script
  (`uv run python3 …`, run from the repo root after the scratch dir was
  already removed, since no fixture file was needed) that regex-splits the
  quiz block into its five question `<div>`s and counts `.split()` words per
  `<button class="opt">` line, per this course's established convention
  (loops/individual `wc -w` calls blocked by this sandbox's approval gate).
  Mismatched on the first draft for all five questions (Q1 11/11/11 was
  actually the one exception at 10/11/11 counted before a first fix; Q2
  12/10/10, Q3 10/10/12, Q4 11/11/8, Q5 11/9/10) — each went through one to
  three rewrite-and-recount rounds, including catching that an em dash counts
  as its own `.split()` token (Q2's first rewrite still overshot until the
  dash was replaced with a comma), before landing on the target count for
  every question (all five questions ended at 11/11/11 exactly), then a full
  final script run across all five questions' three options each (15 lines
  total) confirmed every one before shipping, per this file's instruction to
  recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-16"`.
  **DB access:** per this run's explicit instructions, `bin/query-progress`
  was attempted once as instructed and required approval/permission this
  sandbox would not grant non-interactively, exactly the same failure mode
  logged on every day since Day 8 — no retry attempted, and this run paced
  from on-disk state alone (this file's own log, `python/lessons/`,
  `python/learning-records/` — still only the Day 1 baseline record — and
  `python/practice/`) instead, per this run's explicit instruction.
  `bin/record-progress python lesson_generated --day 19 --lesson
  0019-dependency-injection-and-app-structure.html --detail
  '{"by":"delegated-agent"}'` was run once after shipping, per this run's
  instructions, and succeeded — printed `recorded: python/lesson_generated
  day=19 lesson=0019-dependency-injection-and-app-structure.html` to stdout
  with no error.
  **Next-day note:** per `PLAN.md`'s Phase 2b spine, the natural next-day
  candidate is `async`/`await` — what it buys, when it doesn't, and
  blocking-call traps — the fifth item, directly following today's
  dependency-injection and app-structure foundation.
- 2026-08-17 — **Day 20 generated**
  (`lessons/0020-async-await-and-blocking-calls.html`), the thirteenth Phase 2
  lesson, generated by an automated headless run with zero prior context on
  this course (Postgres progress DB unreachable — psql/DB commands blocked in
  this sandbox — so context was built entirely from `MISSION.md`, `NOTES.md`,
  `PLAN.md`, `RESOURCES.md`, the Day 1 baseline learning record, and on-disk
  state). Idempotency check confirmed on-disk before writing anything: highest
  existing lesson file was `0019-…` dated 2026-08-16, no `0020-…` file and no
  `2026-08-17` entry existed yet in `assets/nav.js` — generation proceeded as
  Day 20, not a re-run.
  Topic: `async`/`await` — what it buys, when it doesn't, and blocking-call
  traps — exactly the fifth item of `PLAN.md`'s Phase 2b spine, named
  explicitly both in Day 19's own closing line and in Day 19's own next-day
  note, directly after Day 19 completed the fourth item (dependency injection
  and app structure). Taught: FastAPI's two handler shapes side by side — a
  plain `def` handler auto-runs in a background thread pool (already true
  since Day 16, made explicit today), an `async def` handler runs on one
  shared event loop, with concurrency coming from cooperative pausing at
  `await` rather than separate threads; `await` as a checkpoint tied
  explicitly back to Day 5's generator `yield` (pause a function, hand
  control back to whatever's driving it, resume later exactly where it left
  off); the blocking-call trap made concrete and load-bearing, not just
  stated — a blocking call (`time.sleep()`) inside `async def` never yields,
  so it silently serializes every other in-flight request behind it; and
  `asyncio.gather()` as the tool for real concurrent fan-out, contrasted
  against awaiting several calls one at a time. Bridged from SQL per the
  baseline record: a plain `def` handler framed as a query run to completion
  by one worker connection while others wait on the pool, `async def` framed
  as several statements in flight on one connection, interleaved because each
  yields control back while waiting on I/O — introduced before any Python in
  the top callout, not from a pandas or other "Python-adjacent" analogy.
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch/py20_explore/`, created under the repo root's shared `.scratch/`
  area and removed after use, not `/tmp`): confirmed `fastapi 0.141.1` /
  `httpx 0.28.1` / Python 3.12.3, the same versions Days 16-19 already
  logged, no drift; a first script confirmed the exact numbers the lesson
  cites — 5 concurrent requests to an `async def` route using `await
  asyncio.sleep(0.05)` complete in ~0.05s total (genuinely concurrent), 5
  concurrent requests to a plain `def` route using blocking `time.sleep(0.05)`
  also complete in ~0.05s total (thread-pool concurrent), but 5 concurrent
  requests to an `async def` route that calls blocking `time.sleep(0.05)`
  serialize to ~0.25s total (5 × 0.05s, the trap, confirmed via
  `httpx.AsyncClient` + `asyncio.gather` against the app in-process); a second
  script confirmed `asyncio.gather()`'s payoff directly — 4 coroutines each
  awaiting `asyncio.sleep(0.03)` take ~0.12s total awaited one at a time in a
  loop, ~0.03s total wrapped in one `gather()` call.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-19 entry already flagged), consistent with this run's own instruction to
  proceed normally along the Phase 2 spine absent evidence of struggle. Paced
  conservatively per that same assumption: exactly the spine's named fifth
  item (async/await, blocking-call traps) covered, no PostgreSQL/`asyncpg`
  material pulled forward from the next spine item, and every new mechanism
  tied back explicitly to material already taught (Day 16's thread-pool
  behavior for plain `def`, Day 5's generator/`yield` pause-and-resume
  framing).
  No-pandas rule: zero pandas/NumPy API in the practice file (checked by grep
  for `pandas|numpy|dataframe`, case-insensitive); exactly one hit in the
  lesson — one contrast sentence stating pandas pipelines are synchronous and
  CPU/memory-bound with nothing to `await`, placed once in its own callout
  after section 4 and labeled in prose as the only such sentence, matching
  the hard-rule section above. The topic itself (async/await) is language- and
  framework-level (Python's own `asyncio`, FastAPI's handler dispatch), never
  library-level, so no ambiguity about which course it belongs to.
  Practice file `practice/20_async_await_and_blocking_calls.py` (8 checks: a
  real `async def` route awaiting `asyncio.sleep()`, timing 5 concurrent
  requests to it to confirm they overlap well under 5×0.05s, a deliberately
  broken `async def` route calling blocking `time.sleep()` with no `await` to
  confirm the same 5 requests instead serialize to over 5×0.05s worth,
  `asyncio.gather()` fanning out 4 coroutines concurrently under 4×0.03s, and
  the same 4 coroutines awaited one-by-one taking over 4×0.03s for
  comparison) needed no on-disk fixtures — every exercise runs the FastAPI
  app in-process via `httpx.ASGITransport` + `httpx.AsyncClient`, timed with
  `time.perf_counter()`. **One bug was caught and fixed during verification:**
  the first draft's Ex 3b check only measured elapsed time (`< 0.08`) without
  checking the returned value, so the unsolved `fetch_all()` — whose bare
  `...` body returns `None` — finished fast enough to pass the timing
  threshold on nothing at all, printing a false ✓ on an unsolved exercise;
  caught by actually reading the shipped (unsolved) copy's real output line
  by line rather than only checking for a clean exit, per this file's own
  repeated warning about silent-success bugs (echoing Day 11's parametrize
  crash and Day 12/16/17's eager-evaluation bugs, a different failure mode
  each time but the same root cause: a check not actually anchored to the
  TODO's correctness). Fixed by requiring both the correct result list AND
  the timing bound in one combined check. After the fix, verified in a
  scratch dir (`.scratch/py20_verify/`, created under the repo root and
  removed after use): the shipped (unsolved) copy, run via `uv run --with
  fastapi --with httpx python3`, both from the scratch copy and from its real
  `practice/` path with the documented command, printed eight clean ✗ lines
  with no traceback each time; a separately solved copy (each TODO filled in
  directly, not copied from commented-out answers) printed eight ✓ and the
  "All green" tally, confirmed stable across three repeated runs (no timing
  flakiness given the wide margins used — 0.2s/0.08s/0.1s thresholds against
  ~0.05s/0.03s/0.12s actual measurements).
  Glossary: added a Day 20 section to `reference/glossary.html` (`await`,
  `event loop`, `coroutine`, `thread pool`, `blocking call`,
  `asyncio.gather()`) after confirming via grep that none of the six
  terms/entries collided with any Day 1-19 entry. All six also got matching
  `<dfn>` markup at first use in the lesson body (confirmed by counting
  `<dfn data-en` occurrences, 6 total, matching the six glossary rows
  one-for-one), matching Day 11-19's density of glossarying every newly
  introduced term inline rather than leaving any undefined.
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir, per this course's established convention. Mismatched on the
  first draft for all five questions (Q1 11/8/8, Q2 10/9/12, Q3 12/9/9, Q4
  10/10/11, Q5 11/9/10) — each went through one to two rewrite-and-recount
  rounds until every option matched (Q1 9/9/9, Q2 9/9/9, Q3 9/9/9, Q4
  10/10/10, Q5 10/10/10), then a full final script run across all five
  questions' three options each (15 lines total) confirmed every one before
  shipping, per this file's instruction to recount after any edit. Registered
  in `assets/nav.js` with `date: "2026-08-17"`.
  **DB access:** per this run's explicit instructions, the Postgres progress
  DB was treated as unreachable from the start (psql/DB read commands
  blocked in this sandbox) with no attempt made at the read path — paced
  entirely from on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record) per this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 20 --lesson
  0020-async-await-and-blocking-calls.html --detail '{"by":"headless-run"}'`
  was run once after shipping and **succeeded**: `recorded:
  python/lesson_generated day=20 lesson=0020-async-await-and-blocking-calls.html`.
  **Next-day note:** per `PLAN.md`'s Phase 2b spine, the natural next-day
  candidate is talking to PostgreSQL from Python and where the `backend/`
  course's concepts land — the sixth item, directly following today's
  async/await foundation.
- 2026-08-18 — **Day 21 generated** (`lessons/0021-talking-to-postgresql.html`),
  the fourteenth Phase 2 lesson, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0021-*.html` file existed and no `2026-08-18` entry
  existed anywhere in the repo (per the orchestrating session's own
  pre-check) — highest existing lesson on disk was `0020-…` dated
  2026-08-17, so generation proceeded as Day 21, not a re-run.
  Topic: talking to PostgreSQL from Python — the DB-API shape
  (connection/cursor), parameterized-query placeholders, and where the
  `backend/` course's concepts land — exactly the sixth item of `PLAN.md`'s
  Phase 2b spine, named explicitly in Day 20's own next-day note as the
  natural continuation. Squarely language/driver-level (psycopg's DB-API,
  not a data-analysis library), so no scope ambiguity. Taught: `psycopg`'s
  `connect()`/`cursor()`/`execute(sql, params)`/`fetchone()`/`fetchall()`
  DB-API shape, framed explicitly as Day 6's file-`with`-pattern aimed at a
  network connection instead of a file; `%s` placeholders as two separate
  pieces (query text, values tuple) sent to the server — the actual
  mechanism that stops SQL injection, explicitly linked to (not
  re-teaching) `backend/`'s own `0017-sql-injection-and-input-validation.html`
  lesson, which names the same defense abstractly in Go; making Day 19's
  placeholder `get_db()` (which returned a fake `{"conn": "fake-db"}` on
  purpose) real, via a `yield`-based dependency whose teardown-after-yield
  is the same guarantee already established by Day 6's context managers and
  Day 11's pytest fixtures; and closing with `psycopg_pool.ConnectionPool`
  plus `psycopg`'s async-native `AsyncConnection`/`AsyncConnectionPool` pair,
  tying directly back to Day 20's claim that I/O-bound work is exactly what
  `async def` pays off for. Bridged from SQL per the baseline record: framed
  up front as "the language you already know, over a new wire" — nothing
  about `SELECT`/`WHERE` changes, only the Python-side connection/cursor
  mechanics are new — not from a pandas or other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-20 entry has flagged). Paced conservatively per that same assumption:
  one core mechanism (DB-API connect/cursor/execute/fetch) given the most
  weight, the pool/async material in section 4 kept to recognition-level
  (shown, explained, not exercised in practice — the practice file stays on
  section 1-3's synchronous DB-API pattern) since pulling a second
  synchronous-vs-async fork into one ~20-min lesson risked overloading it,
  and every new mechanism tied back explicitly to material already taught
  (Day 6, Day 11, Day 19, Day 20) rather than introduced cold.
  No-pandas rule: zero pandas/NumPy API in the practice file (grep for
  `pandas|numpy|dataframe`, case-insensitive — zero hits); exactly one hit
  in the lesson — one contrast sentence naming `pd.read_sql("SELECT ...",
  conn)` as a one-shot, connection-for-the-life-of-the-script call versus
  today's per-request pooled pattern, without demonstrating any pandas API,
  placed once in its own callout after section 4 and labeled in prose as
  the only such sentence, matching the hard-rule section above.
  Practice file `practice/21_talking_to_postgresql.py` (8 checks: a
  parameterized `SELECT` by id via `fetchone()`, a deliberately unsafe
  f-string query proven vulnerable to an injection string alongside a safe
  placeholder version proven immune to the identical string, a `yield`-based
  `get_db()` dependency driven by hand with `next()` to confirm its
  open-then-close log order, and `fetchall()` reading every row) needed a
  different fixture strategy than psycopg would allow in this sandbox — no
  live PostgreSQL server is available, so the file uses the standard
  library's own `sqlite3` module throughout, called out explicitly in the
  file's header comment and lesson section "Try it" as following the
  identical DB-API shape as psycopg (same `connect()`/`cursor()`/
  `execute(sql, params)`/`fetchone()`/`fetchall()` calls, the one real
  syntax difference being sqlite3's `?` placeholder vs psycopg's `%s`) —
  this keeps every exercise real, runnable DB-API code rather than a mocked
  stand-in, consistent with this file's own instruction that practice files
  stay standard-library-only and need no `--with` flag. **One bug was caught
  and fixed during verification:** the first draft's Ex 3 helper
  (`_ex3_setup()`) called `next(gen)` directly on the unsolved `get_db()`
  with no guard — since an unsolved `get_db()` is a plain function of all
  `...` statements with no real `yield` reached, calling it returns `None`
  rather than a generator, so `next(None)` raised an uncaught
  `TypeError: 'NoneType' object is not an iterator` and crashed the whole
  shipped script before Ex 4 could even run — caught by actually running the
  shipped (unsolved) copy rather than assuming a graceful failure, per this
  file's repeated warning about exactly this failure mode (echoing Day 8's
  and Day 20's own caught bugs). Fixed by wrapping `_ex3_setup()`'s body in
  `try/except Exception`, returning `([], None)` on failure so both Ex 3
  checks degrade to a clean ✗ instead of an uncaught traceback. After the
  fix, verified in a scratch dir (`.scratch/py21_verify/`, created under the
  repo root and removed after use, consistent with every prior day's
  `/tmp`-is-out-of-bounds precedent): the shipped (unsolved) copy, run via
  `uv run python3`, both from the scratch copy and from its real
  `practice/` path with the documented command, printed eight clean ✗ lines
  with no traceback each time (one check, Ex 1b, happens to read ✓ on the
  unsolved copy since an unsolved `get_user_by_id` returns `None` and the
  check asks for `None` on a no-match lookup — not a bug, since Ex 1's own
  check still correctly reads ✗ and catches the exercise as unsolved); a
  separately solved copy (each TODO filled in directly) printed eight ✓ and
  the "All green" tally.
  Glossary: added a Day 21 section to `reference/glossary.html` (`DB-API`,
  `cursor`, `placeholder`, `connection pool`) after confirming via grep that
  none of the four terms collided with any Day 1-20 entry. All four also got
  matching `<dfn>` markup at first use in the lesson body (confirmed by
  counting `<dfn data-en` occurrences — 3 present after the first draft, a
  gap caught because it undercounted the 4 glossary rows by one:
  "connection pool" was named in section 4's prose but not wrapped — fixed
  by adding the missing `<dfn>` around its first mention, bringing the count
  to 4-for-4).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for all five questions (Q1
  12/10/9, Q2 10/8/10, Q3 10/9/12, Q4 10/8/11, Q5 11/10/10) — each went
  through two to three rewrite-and-recount rounds (hand-counting drifted
  more than once this session, so every round was re-verified against the
  script's actual output rather than trusted by eye) until every option
  matched (Q1 8/8/8, Q2 9/9/9, Q3 10/10/10, Q4 10/10/10, Q5 10/10/10), then
  a final script run across all five questions' three options each (15
  lines total) confirmed every one before shipping, per this file's
  instruction to recount after any edit. Registered in `assets/nav.js` with
  `date: "2026-08-18"`.
  **DB access:** per this run's explicit instructions, the Postgres progress
  DB read paths (`psql`/`bin/query-progress`) were treated as unreachable
  from the start, confirmed unavailable by the orchestrating session with
  one retry (not looped on) — paced entirely from on-disk state (this
  file's own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record) per
  this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 21 --lesson
  0021-talking-to-postgresql.html --detail '{"by":"launchd"}'` was run once
  after shipping and **succeeded**: `recorded: python/lesson_generated
  day=21 lesson=0021-talking-to-postgresql.html` — consistent with every
  write-path attempt since Day 9/10, the read paths remaining the only
  consistently blocked side of DB access in this sandbox.
  **Next-day note:** per `PLAN.md`'s Phase 2b spine, the natural next-day
  candidate is testing endpoints with `httpx`; errors, middleware, and a
  deployable shape — the seventh and final named item of the Phase 2b
  spine, which per `PLAN.md`'s own closing line should trigger revisiting
  the plan once reached ("driven by what work and interviews actually
  demand by then").
- 2026-08-19 — **Day 22 generated** (`lessons/0022-testing-with-httpx.html`),
  the fifteenth Phase 2 lesson, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0022-*.html` file existed and no `2026-08-19` entry
  existed anywhere in the repo (per the orchestrating session's own
  pre-check) — highest existing lesson on disk was `0021-…` dated
  2026-08-18, so generation proceeded as Day 22, not a re-run.
  Topic: testing endpoints with `httpx` — the seventh and final named item
  of `PLAN.md`'s Phase 2b spine, named explicitly in Day 21's own next-day
  note. Before picking it, `NOTES.md`'s own entries from Day 21 back to Day
  8 were read closely and no "plan revisit" entry was found anywhere after
  Day 21 — `PLAN.md`'s closing line only *asks* for a revisit once the
  spine is exhausted, it doesn't perform one automatically, so today
  completing the last named item is correct and a revisit is now due
  starting Day 23, not before. Squarely language/tooling-level (FastAPI's
  own `TestClient`, which wraps `httpx`, plus `pytest`'s `assert` from Day
  11), not a data-analysis library, so no scope ambiguity. Taught:
  `TestClient(app)` as `httpx` talking to the app in-process over the ASGI
  interface, no socket and no running server, using the identical
  `.get()`/`.post()`/`.status_code`/`.json()` shape every practice file
  since Day 16 has already called without a name for it; a `test_*`
  function calling a route and asserting on it, framed explicitly as Day
  11's `test_*` + `assert` convention aimed at a route instead of a plain
  function; asserting status code and JSON body together rather than either
  alone, and confirming pydantic validation still really runs through
  `TestClient` (a missing required field still comes back a real `422`);
  and a recognition-level (not exercised in the lesson body, but exercised
  in the practice file) pass over exception handlers, middleware, and ASGI
  servers (`uvicorn`) — the "errors, middleware, and a deployable shape"
  half of the spine's final item — kept brief per this file's own
  established pattern of not overloading one ~20-min lesson with two forks
  of new material (echoing Day 21's choice to keep pool/async
  recognition-level only). Bridged from SQL per the baseline record: framed
  up front as the same discipline as a saved query-result assertion suite
  run after a schema migration, not from a pandas or other
  "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-21 entry has flagged). Paced conservatively per that same assumption:
  one core mechanism (`TestClient`/`test_*`/`assert`) given the most
  weight, matching Day 21's own precedent for a two-part spine item.
  No-pandas rule: zero pandas/NumPy API in the practice file (grep for
  `pandas|numpy|dataframe`, case-insensitive — zero hits); exactly one hit
  in the lesson — one contrast sentence naming a pandas pipeline's
  DataFrame-shape assertions as testing a transform's output, not a
  request/response contract, without demonstrating any pandas API, placed
  once in its own callout after section 4 and labeled in prose as the only
  such sentence, matching the hard-rule section above.
  Practice file `practice/22_testing_with_httpx.py` (4 checks: a `test_*`
  function checking status code AND JSON body together on a working route,
  a 404 error-path check on a missing user, a POST-then-shape check on a
  newly created record, and a check that a custom
  `@app.exception_handler(ProductNotFound)` still returns its chosen 404
  and detail message through `TestClient` exactly like a live client would
  see) needed no on-disk fixtures — every exercise runs the FastAPI app
  in-process via `TestClient`, same pattern as Days 16, 18, and 19. This
  file's own bug-class guard from Day 21 (never call `next()` on an
  unsolved generator-based helper with no guard) didn't apply today — no
  exercise here uses a generator/`yield`-based setup helper, so no
  equivalent guard was needed; confirmed instead by actually running the
  shipped (unsolved) copy end to end rather than assuming safety, per this
  file's own repeated warning about exactly this failure mode (echoing Day
  8, Day 20, and Day 21's own caught bugs) — the unsolved copy's four `...`
  TODOs are plain function bodies returning `None`, so each `check()`'s
  `bool(cond())` where `cond` compares `test_*(...) is True` naturally
  evaluates to `False` with no exception raised at all, needing no
  try/except guard of its own. Verified in a scratch dir
  (`python/.scratch-verify-22/`, created under the repo root and removed
  after use, per every prior day's `/tmp`-is-out-of-bounds precedent): the
  shipped (unsolved) copy, run via `uv run --with fastapi --with httpx
  python3` both from the scratch copy and from its real `practice/` path
  with the documented command, printed four clean ✗ lines each time (one
  pre-existing `StarletteDeprecationWarning` about `httpx`/`starlette`
  printed to stderr on every run — confirmed identical and already present
  on Day 16's own practice file today, so not a new issue, not a
  traceback, and not this file's concern to fix); a separately solved copy
  (each TODO filled in directly) printed four ✓ and the "All green" tally.
  One clarity fix made during authoring, not a bug: Exercise 3's first-draft
  comment walked through a false assumption about `status_code=201` before
  correcting it mid-instruction ("but wait…") — reworded before shipping so
  the correct expectation (`200`, since the route never sets
  `status_code=201`) is stated directly instead of via a false start.
  Glossary: added a Day 22 section to `reference/glossary.html` (`ASGI`,
  `exception handler`, `middleware`, `ASGI server`) after confirming via
  grep that none of the four terms collided with any Day 1-21 entry. All
  four also got matching `<dfn>` markup at first use in the lesson body
  (confirmed by counting `<dfn data-en` occurrences, 4 total, matching the
  four glossary rows one-for-one).
  Quiz: 5 questions. Word counts were checked with the small Python script
  this course's convention already uses (regex-splitting the quiz block
  into its five question `<div>`s and counting `.split()` words per
  `<button class="opt">` line), run from a scratch dir via `uv run
  python3`. Mismatched on the first draft for all five questions (Q1
  9/9/8, Q2 9/8/12, Q3 11/9/10, Q4 9/11/10, Q5 11/9/8) — hand-counted
  rewrites drifted at least once per question exactly like Day 21 flagged,
  so every subsequent round was checked against candidate wordings with a
  small `wc.py` helper piped short strings via stdin before editing the
  file, rather than trusted by eye — until every option matched (all five
  questions landed at 9/9/9 exactly), then a final script run across all
  five questions' three options each (15 lines total) confirmed every one
  before shipping. Registered in `assets/nav.js` with `date: "2026-08-19"`.
  **DB access:** per this run's explicit instructions, Neon/Postgres was
  confirmed unreachable this session before starting (no `db.env`, `psql`
  reads blocked) — no DB read was attempted, paced entirely from on-disk
  state (this file's own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record) per
  this run's fallback instructions. `bin/record-progress` (the write path)
  was confirmed still working, consistent with every day since Day 9/10.
  `bin/record-progress python lesson_generated --day 22 --lesson
  0022-testing-with-httpx.html --detail '{"by":"delegated-agent"}'` was run
  once after shipping — see its own output logged at the point it ran.
  **Next-day note:** Phase 2b's named spine (HTTP handlers through today's
  endpoint testing) is now fully covered — per `PLAN.md`'s own closing
  line, Day 23 should open by revisiting the plan (what backend depth work
  and interviews actually demand) before picking a next topic, rather than
  assuming a next spine item exists.
- 2026-08-20 — **Day 23 generated**
  (`lessons/0023-error-handling-and-exception-handlers.html`), the
  sixteenth Phase 2 lesson, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything
  that no `python/lessons/0023-*.html` file existed and no `2026-08-20`
  entry existed anywhere in this file — highest existing lesson on disk
  was `0022-…` dated 2026-08-19, so generation proceeded as Day 23, not a
  re-run. Topic: per Day 22's own next-day note, `PLAN.md`'s named Phase
  2b spine is now fully covered, so this session revisited the plan before
  picking a topic rather than assuming a next spine item existed, per that
  note's explicit instruction. `PLAN.md`'s spine had listed "errors,
  middleware, and a deployable shape" as the seventh item; Day 22 shipped
  the `httpx`-testing half and left all three of errors/middleware/deploy
  as recognition-level prose only, with `@app.exception_handler` named in
  one paragraph but never given a worked lesson example. Of those three,
  errors was picked as the one substantial enough to justify a full
  lesson on its own — middleware and the ASGI-server "deployable shape"
  stay recognition-level as Day 22 already left them, since re-covering
  either felt like padding rather than a real gap. Confirmed via grep
  that `@app.exception_handler` appeared in Day 22's lesson body only
  inside its own recognition-level section 4 paragraph, never with a
  runnable example, and that `RequestValidationError` had never appeared
  in any lesson through Day 22 — both genuine gaps, not a re-teach.
  Squarely FastAPI/stdlib-level (custom exception classes reusing Day 8's
  `class X(Exception)` pattern, plus a FastAPI-specific exception type),
  not a data-analysis library, so no scope ambiguity. Taught: a custom
  exception class raised where a business rule lives instead of repeated
  `if`/`raise HTTPException(...)` blocks scattered across routes, framed
  explicitly as Day 8's exact custom-exception pattern with a new place it
  gets caught (`@app.exception_handler`, app-wide, instead of a local
  `except`); that the same decorator registers on *any* exception type
  escaping a route uncaught, not just custom classes, demonstrated by
  registering a second handler for `RequestValidationError` — the type
  FastAPI itself raises internally on a failed pydantic validation — to
  reshape its default, fairly verbose 422 body into a smaller, consistent
  shape matching the app's own business-error responses. Bridged from SQL
  per the baseline record: framed up front as a `CHECK` constraint's error
  message standardized across every query that trips it, not a pandas or
  other "Python-adjacent" analogy.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-22 entry has flagged). Paced conservatively per that same assumption:
  two mechanisms taught (custom exception + handler, then
  `RequestValidationError` reshaping), both built directly on Day 8/16/17
  material rather than introduced cold, matching this course's usual one-
  or-two-mechanism ceiling for a single ~20-min lesson.
  No-pandas rule: zero pandas/NumPy API in the practice file (grep for
  `pandas|numpy|dataframe`, case-insensitive — zero hits, and only
  `fastapi`/`fastapi.exceptions`/`fastapi.responses`/`fastapi.testclient`/
  `pydantic` imports, all already-approved third-party deps for this
  course's backend phase); exactly one hit in the lesson — one contrast
  sentence naming where a pandas pipeline's own validation/error-raising
  lives (inline at the check, no app-wide handler, since there's no set of
  independent HTTP routes hitting the same rule), without demonstrating
  any pandas API, placed once in its own callout after section 3, matching
  the hard-rule section above.
  Practice file `practice/23_error_handling_and_exception_handlers.py` (4
  checks: a custom `OutOfStock` exception storing the item that ran out, a
  registered `@app.exception_handler(OutOfStock)` returning the right 409
  shape, confirming an in-stock order still succeeds normally through the
  same route, and a `RequestValidationError` handler reshaping the default
  422 body into `{"error", "field", "message"}`) needed no on-disk
  fixtures — every exercise runs the FastAPI app in-process via
  `TestClient`, same pattern as Days 16, 18, 19, and 22. Verified in a
  scratch dir (`python/.scratch-verify-23/`, created under the repo root
  and removed after use, per Day 22's own `/tmp`-is-out-of-bounds
  precedent — confirmed again this session: `mkdir /tmp/...` was blocked
  outright by the sandbox, same failure Day 22 flagged): the shipped
  (unsolved) copy, run via `uv run --with fastapi --with httpx python3`
  both from the scratch copy and from its real `practice/` path with the
  documented command, printed three ✗ and one ✓ each time (the fourth
  exercise's in-stock-order check needs no TODO fill-in to pass, so it
  reads ✓ even unsolved — confirmed intentional, not a bug, by reading the
  exercise: it exercises the *existing* `place_order` route directly, not
  a TODO'd handler function) — one pre-existing `StarletteDeprecationWarning`
  about `httpx`/`starlette` printed to stderr on every run, identical to
  every prior FastAPI practice file since Day 16, not a new issue; a
  separately solved copy (each TODO filled in directly) printed four ✓ and
  the "All green" tally.
  Glossary: added a Day 23 section to `reference/glossary.html`
  (`RequestValidationError` only — `exception handler` and `ASGI` were
  already Day 22 terms, reused via prose today without a second `<dfn>`,
  and no other genuinely new term appeared) after confirming via grep that
  the term didn't collide with any Day 1-22 entry. Got matching `<dfn>`
  markup at its first mention in the lesson body (confirmed one
  `<dfn data-en` occurrence, matching the one new glossary row).
  Quiz: 5 questions. Word counts were checked with the same small Python
  script this course's convention already uses (regex-splitting the quiz
  block into its five question `<div>`s and counting `.split()` words per
  `<button class="opt">` line), run from a scratch dir via `uv run
  python3`. The first draft's naive regex split merged all five
  questions' options into one flat list instead of splitting per-question
  — caught immediately since the mismatch counts didn't make sense against
  the visible option text, fixed by cutting each split segment after its
  third `<button class="opt">` tag rather than trusting a single greedy
  regex across the whole quiz block. Mismatched on every subsequent
  correctly-split draft too (Q1 4/11/7, Q2 11/10/10, Q3 8/8/9, Q4 12/11/10,
  Q5 10/8/8) — hand-counted rewrites drifted repeatedly across several
  more rounds, consistent with every prior day's flagged difficulty here,
  so every further edit was checked against the script's actual output
  rather than trusted by eye, including writing small standalone
  candidate-wording scripts run through `uv run python3` before touching
  the lesson file, until every option matched (Q1 8/8/8, Q2 10/10/10, Q3
  10/10/10, Q4 11/11/11, Q5 9/9/9), then a final full-file script run
  across all five questions' three options each (15 lines total) confirmed
  every one before shipping. Registered in `assets/nav.js` with
  `date: "2026-08-20"`.
  **DB access:** per this run's explicit instructions, the Postgres
  progress DB read paths (`psql`/`bin/query-progress`) were treated as
  unreachable from the start and not attempted — any command containing
  `$`-style shell expansion is hard-blocked by this sandbox's static
  analysis regardless of target, a distinct and separate restriction from
  DB reachability itself. Paced entirely from on-disk state (this file's
  own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record) per
  this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 23 --lesson
  0023-error-handling-and-exception-handlers.html --detail
  '{"by":"github-actions"}'` was run once after shipping and
  **succeeded**: `recorded: python/lesson_generated day=23
  lesson=0023-error-handling-and-exception-handlers.html` — consistent
  with every write-path attempt since Day 9/10, the read paths remaining
  the only consistently blocked side of DB access in this sandbox.
  **Next-day note:** with the named Phase 2b spine's leftover pieces now
  down to just middleware and the ASGI-server "deployable shape" (both
  still recognition-level only, by design), the natural next-session
  question is whether to give one of those its own full lesson, or pivot
  toward consolidation/interview-prep — `RESOURCES.md`'s own "Gaps"
  section still flags no chosen source for Python-specific interview prep
  and no FastAPI project-layout reference beyond the official docs, both
  still open as of this session.
- 2026-08-23 — **Day 26 generated**
  (`lessons/0026-fastapi-capstone.html`), the nineteenth Phase 2 lesson,
  generated by an automated headless daily-generation run. Idempotency:
  confirmed before writing anything that no `python/lessons/0026-*.html` (or
  higher-numbered) file existed and no `2026-08-23` entry existed anywhere in
  this file or `assets/nav.js` — highest existing lesson on disk was
  `0025-…` dated 2026-08-22, so generation proceeded as Day 26, not a re-run.
  Postgres read paths were not attempted (consistent hard block every day
  since Day 8, per this run's own instructions); paced from on-disk state
  only.
  Topic: per Day 25's own closing note, every named item of both Phase 2a
  and Phase 2b's spines in `PLAN.md` is now covered by its own lesson, with
  no further named spine item to pick. Rather than guess at an unnamed
  Phase 3 direction with learning records still this sparse (see below),
  chose the same move `PLAN.md`/Day 7's own log made at the Phase 1/2
  boundary: a **capstone** lesson introducing no new mechanism, instead
  wiring several already-taught mechanisms into one small, real,
  end-to-end artifact — this time a tiny FastAPI + pydantic task-list
  service (`POST /tasks`, `GET /tasks/{id}`) combining Day 17's pydantic
  request model + custom `@field_validator`, Day 18's `response_model`,
  Day 19's `Depends()` dependency, Day 20's real `await` checkpoint, and
  Day 23's custom exception + `@app.exception_handler`, then tested with
  Day 22's `TestClient` pattern across the full create-then-read-then-404
  flow in one test rather than one route at a time. This also directly
  advances `MISSION.md`'s own named success criterion — "Build and test a
  small FastAPI + pydantic service: request/response models, validation,
  dependency injection, async I/O, and pytest coverage of it" — which no
  single prior lesson had assembled in one file. Bridged from SQL per the
  baseline record: the whole service framed as a stored procedure plus its
  input/output contracts plus its constraint checks plus its own regression
  tests, all living in one place instead of scattered across a schema file
  and a separate test script, introduced before any Python in the top
  callout, not from a pandas or other "Python-adjacent" analogy.
  Verified interactively in a scratch dir (`.scratch/py26_probe/`, created
  under the repo root and removed after use, per every prior day's
  `/tmp`-is-out-of-bounds precedent) before writing the lesson: a standalone
  probe script built the exact five-piece app from section 1 and ran it
  through `TestClient` — confirmed `POST /tasks` with a real title returns
  `201` with the right body shape, a blank (`"   "`) title is rejected with
  pydantic's own `422` with no route-level check needed, `GET /tasks/{id}`
  on a just-created id echoes it back, and `GET /tasks/999` returns the
  custom `{"error": "task_not_found", "id": 999}` 404 shape from the
  registered handler rather than FastAPI's default error page — every claim
  section 2 makes is grounded in this probe's actual output, not assumed.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-25 entry has flagged). Given that persistent gap, a consolidation
  capstone felt like the lower-risk choice for today specifically versus
  guessing at a brand-new, unnamed Phase 3 topic with no completion signal
  to justify picking one direction over another — the lesson introduces
  zero new mechanisms by design, so there is little for a shaky prerequisite
  to undermine.
  No-pandas rule: zero pandas/NumPy API in the practice file (grep for
  `pandas|numpy|dataframe`, case-insensitive — zero hits, only `fastapi`/
  `pydantic` imports, both already-approved for this course's backend
  phase); exactly one hit in the lesson — one contrast sentence (in its own
  callout, titled "Where pandas goes from here") stating that none of
  today's five pieces has a pandas equivalent, since a one-shot pipeline has
  no request/response cycle to validate, inject dependencies into, or
  handle exceptions across, without demonstrating any pandas API. An
  earlier draft's opening "Bridge from SQL" callout also named pandas in a
  negation ("not a pandas ... analogy") — reworded to drop the mention
  entirely so exactly one true contrast sentence exists in the shipped
  file, not two, matching the hard-rule section's "exactly one" convention
  more literally than a technically-still-a-negation phrasing would.
  Practice file `practice/26_fastapi_capstone.py` (4 checks: POST-then-shape
  on a newly created task, a blank-title 422 rejection, a POST-then-GET
  round trip reading a just-created task back by id, and a missing-id 404
  matching the custom `{"error", "id"}` shape) needed no on-disk fixtures —
  every exercise runs the FastAPI app in-process via `TestClient`, same
  pattern as Days 16, 18, 19, 22, 23, and 24. Four TODOs total (`TaskIn`,
  `TaskOut`, the exception handler body, and the `get_task_or_404`
  dependency body) — deliberately fewer, larger TODOs than most prior days'
  five-or-six-exercise practice files, matching the lesson's own "assemble
  already-taught pieces" framing rather than introducing a fresh checklist
  of small mechanics. Verified in a scratch dir (`.scratch/py26_probe/`,
  removed after use): the shipped (unsolved) copy, run via `uv run --with
  fastapi --with httpx python3` both from the scratch copy and from its
  real `practice/` path with the documented command, printed four clean ✗
  lines with no traceback each time (the unsolved `class TaskIn(BaseModel):
  ...` and similar bodies are bare `...` statements, so pydantic model
  construction and the plain functions all either raise inside `check()`'s
  own `try/except` or simply return the wrong shape, never crashing the
  script itself; one pre-existing `StarletteDeprecationWarning` about
  `httpx`/`starlette` printed to stderr on every run, identical to every
  FastAPI practice file since Day 16, not a new issue); a separately solved
  copy (each TODO filled in with the lesson's own five-piece code) printed
  four ✓ and the "All green — capstone done, Phase 2b fully wired together!"
  tally. No bugs found during verification — both passes succeeded on the
  first attempt.
  Glossary: added a Day 26 section to `reference/glossary.html`
  (`capstone` only — every mechanism used today, `field_validator`,
  `response_model`, `Depends()`, `await`, custom exception handlers, already
  has its own row from Days 17-20/23 and is reused today via plain `<code>`
  in prose with no second `<dfn>`, matching Day 23's and Day 24's own
  precedent for reusing prior terms unchanged) after confirming via grep
  that `capstone` didn't collide with any Day 1-25 entry. Got matching
  `<dfn>` markup at its first mention in the lesson body (confirmed one
  `<dfn data-en` occurrence, matching the one new glossary row).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for all five questions (Q1
  10/10/9, Q2 9/10/10, Q3 10/10/9, Q4 10/9/10, Q5 10/11/9) — each went
  through one to two rewrite-and-recount rounds, re-running the script
  after every edit rather than trusting a manual count, until every option
  matched (Q1 11/11/11, Q2 10/10/10, Q3 10/10/10, Q4 10/10/10, Q5
  11/11/11), then a final script run against the real shipped file
  confirmed every one before shipping — one stray leftover `</p>` before a
  closing `</div>` on the second pandas-contrast callout was also caught
  and fixed during this same final-check pass, not a quiz issue but a
  markup typo from an early draft. Registered in `assets/nav.js` with
  `date: "2026-08-23"`.
  **DB access:** per this run's explicit instructions, the Postgres progress
  DB read paths (`psql`/`bin/query-progress`) were treated as unreachable
  from the start and not attempted this run, consistent with the
  documented block on every day since Day 8; this run paced entirely from
  on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record) per this run's fallback instructions.
  `bin/record-progress python lesson_generated --lesson
  0026-fastapi-capstone.html --detail '{"by":"headless-run"}'` was run once
  after shipping, per this run's instructions — see its own output for
  whether it recorded successfully.
  **This is a spine-completion capstone, not a new spine item.** With both
  Phase 2a and Phase 2b's named `PLAN.md` items now covered and this lesson
  wiring several of them together in one working service, the natural next
  step for Day 27 is still what Day 25's own note already flagged:
  revisit `PLAN.md` for Phase 3's direction, or fill `RESOURCES.md`'s
  still-open "Gaps" (Python interview prep, a FastAPI project-layout
  reference beyond the official docs) — both remain open as of this
  session.</new_string>

- 2026-08-21 — **Day 24 generated** (`lessons/0024-asgi-middleware.html`),
  the seventeenth Phase 2 lesson, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0024-*.html` file existed and no `2026-08-21` entry
  existed anywhere in this file or `assets/nav.js` — highest existing lesson
  on disk was `0023-…` dated 2026-08-20, so generation proceeded as Day 24,
  not a re-run.
  Topic: ASGI middleware — the one item PLAN.md's Phase 2b spine still left
  fully uncovered after Day 23. PLAN.md's final spine item read "testing
  endpoints with httpx; errors, middleware, and a deployable shape" — Day 22
  built the httpx-testing half and left errors/middleware/deploy at
  recognition-level only; Day 23 then gave errors its own full lesson and
  explicitly deferred middleware and the ASGI-server "deployable shape" as
  still-open, naming both again in its own next-day note. Confirmed via grep
  that `middleware` already had a Day 22 glossary entry (recognition-level,
  one sentence, never demonstrated) but no lesson had ever shown
  `@app.middleware("http")`, `call_next`, or a runnable example — a genuine
  gap, not a re-teach. Taught: middleware as a function wrapping every
  request/response passing through the app (Day 6's `with`-block shape —
  setup, wrapped work, guaranteed cleanup — applied to the whole rest of a
  request instead of a file); `@app.middleware("http")` and `call_next` as
  FastAPI's decorator form, with `await call_next(request)` as the handoff
  point (Day 20's checkpoint/pause-resume idea, applied to middleware
  itself); a concrete worked example — request timing plus Day 15's
  `logging`-module structured-fields pattern reused verbatim, just moved
  from inside a handler to one middleware function covering every route;
  `BaseHTTPMiddleware` named as the class-based alternative, recognition-only
  (this course sticks to the decorator form); and the flagged gotcha, given
  its own full section 4: middleware sits **outside** Day 23's exception
  handlers in FastAPI's stack, so an exception with a registered
  `@app.exception_handler` never reaches middleware's own `try`/`except` as
  an exception at all — `call_next()` just returns a normal, finished
  response, and middleware must read `response.status_code` unconditionally
  to observe the real outcome rather than relying on catching it. Bridged
  from SQL per the baseline record: a database trigger firing on every
  table's `INSERT`/`UPDATE` without touching any single table's own
  definition, introduced before any Python in the top callout, not from a
  pandas or other "Python-adjacent" analogy.
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch/py24_probe/`, created under the repo root's shared `.scratch/`
  area and removed after use, not `/tmp` — `mkdir /tmp/...` was blocked
  outright by this sandbox, consistent with every prior day back through
  Day 3): two probe scripts built the exact section-4 shape and ran it
  through `TestClient` — confirmed a route raising an exception with a
  registered `@app.exception_handler` makes `call_next()` return normally
  with the handler's chosen status code (409 in the probe), with
  middleware's own `except Exception:` branch never firing at all; and
  separately confirmed a *truly* unhandled exception (no handler registered
  anywhere) really does propagate out of `call_next()` as a raised
  exception, which middleware's own `try`/`except` **does** catch — the
  precise, load-bearing distinction the lesson's gotcha section states.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-23 entry has flagged). Paced conservatively per that same assumption:
  one core mechanism (`@app.middleware("http")` + `call_next`) given the
  most weight, `BaseHTTPMiddleware` kept to a single recognition-only
  paragraph, and every new mechanism tied back explicitly to material
  already taught (Day 6's context-manager shape, Day 15's `logging` module,
  Day 20's `await` checkpoint, Day 23's exception handlers) rather than
  introduced cold.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (grep for `pandas|numpy|dataframe`, case-insensitive — zero hits in the
  practice file, exactly one hit in the lesson); one contrast sentence,
  naming that a pandas pipeline has no request/response cycle to wrap and
  would time a transform step with a bare `time.perf_counter()` call inline
  instead, without demonstrating any pandas API, placed once in its own
  callout after section 4 and matching the hard-rule section above.
  Practice file `practice/24_asgi_middleware.py` (4 checks: a timing
  middleware stamping `X-Process-Time-ms` via `call_next`, a
  structured-logging middleware appending one record per request to a
  shared list, that same gotcha confirmed directly — a route raising an
  exception with a registered handler is logged via `response.status_code`,
  never caught as an exception — and a second, guarded middleware whose own
  `try`/`except` around `call_next()` is what's actually needed to log
  anything at all for a route with no handler registered) needed no on-disk
  fixtures — every exercise runs the FastAPI app in-process via
  `TestClient`, same pattern as Days 16, 18, 19, 22, and 23. **One design
  bug was caught and fixed during verification**, the same failure class
  this file's own log has flagged on Days 8, 11, 20, and 21: the first
  draft's Exercise 4 assumed a *single* logging middleware would observe
  both the handled-exception case (409, logged via `response.status_code`)
  and the truly-unhandled case (500) by simply reading `response.status_code`
  after `call_next()` in both — actually running the *solved* copy in the
  scratch dir showed Ex 4 still printing ✗ even fully solved, because a
  truly unhandled exception makes `call_next()` raise rather than return, so
  a middleware with no `try`/`except` never runs its post-`call_next()` line
  at all for that request and logs nothing. Fixed by splitting into two
  middlewares with two separate log lists — Exercise 2's unguarded
  `log_requests` (only ever observes normal returns) and Exercise 3's
  guarded `log_even_unhandled` (a real `try`/`except` around `call_next()`,
  needed specifically for the no-handler-registered case) — confirmed
  correct by re-deriving the exact behavior from a standalone probe script
  before rewriting the exercise, not just patched until the check passed.
  After the fix, verified in a scratch dir (`.scratch/py24_verify/`, created
  under the repo root and removed after use): the shipped (unsolved) copy,
  run via `uv run --with fastapi --with httpx python3` both from the scratch
  copy and from its real `practice/` path with the documented command,
  printed four clean ✗ lines with no traceback each time (one pre-existing
  `StarletteDeprecationWarning` about `httpx`/`starlette` on every run,
  identical to every FastAPI practice file since Day 16, not a new issue);
  a separately solved copy (each TODO filled in directly) printed four ✓ and
  the "All green" tally.
  Glossary: added a Day 24 section to `reference/glossary.html` (`call_next`,
  `BaseHTTPMiddleware`) after confirming via grep that `middleware` itself
  was already a Day 22 glossary entry — reused today via plain `<code>` in
  prose with no second `<dfn>`, matching Day 23's own precedent for reusing
  `exception handler`/`ASGI` without re-defining them. Both new terms got
  matching `<dfn>` markup at first use in the lesson body (confirmed by
  counting `<dfn data-en` occurrences, 2 total, matching the two glossary
  rows one-for-one).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for all five questions (Q1
  12/10/10, Q2 11/9/10, Q3 10/10/11, Q4 6/10/9, Q5 8/11/11) — each went
  through several rewrite-and-recount rounds, iterated against the script's
  actual output rather than trusted by eye per every prior day's flagged
  difficulty here, until every option matched (all five questions landed at
  10/10/10 exactly), then a final script run against the real shipped file
  confirmed every one before shipping. Registered in `assets/nav.js` with
  `date: "2026-08-21"`.
  **DB access:** per this run's explicit instructions, the Postgres progress
  DB read paths (`psql`/`bin/query-progress`) were treated as unreachable
  from the start and attempted once as instructed — blocked by this
  sandbox's permission-approval gate with no user present, the same failure
  mode logged on every day since Day 8 — not retried, and this run paced
  entirely from on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record) per this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 24 --lesson
  0024-asgi-middleware.html --detail '{"by":"headless-agent"}'` was run once
  after shipping and **succeeded**: `recorded: python/lesson_generated
  day=24 lesson=0024-asgi-middleware.html` — consistent with every
  write-path attempt since Day 9/10, the read paths remaining the only
  consistently blocked side of DB access in this sandbox.
  **Next-day note:** with middleware now built out, the only Phase 2b
  spine item still recognition-level-only is the ASGI-server "deployable
  shape" — `uvicorn`/`gunicorn` startup, env-based config, worker counts —
  a natural Day 25 candidate, already named in today's lesson's own closing
  line. `RESOURCES.md`'s "Gaps" section (no Python interview-prep source, no
  FastAPI project-layout reference) remains open as of this session too.
- 2026-08-22 — **Day 25 generated** (`lessons/0025-deploying-with-uvicorn.html`),
  the eighteenth Phase 2 lesson and **the last named item of PLAN.md's Phase
  2b spine**, generated by an automated headless daily-generation run.
  Idempotency: confirmed before writing anything that no
  `python/lessons/0025-*.html` file existed and no `2026-08-22` entry existed
  anywhere in this file or `assets/nav.js` — highest existing lesson on disk
  was `0024-…` dated 2026-08-21, so generation proceeded as Day 25, not a
  re-run.
  Topic: the ASGI-server "deployable shape" — `uvicorn` startup,
  `--reload` vs. `--workers`, and env-based deploy config — the piece Day 24's
  own next-day note had already named as the only Phase 2b spine item left
  recognition-level-only after Day 24 built out middleware. Taught: what
  `uvicorn app:app --host … --port …` actually does (a real ASGI server
  binding a real socket and calling the same `app` callable `TestClient` has
  called in-process every lesson since Day 16); `--reload` (one process,
  auto-restart on file change, dev-only) versus `--workers N` (N independent
  processes for real concurrent load) as mutually exclusive by design — more
  worker processes, not more `await`, is what actually lets requests run on
  separate CPU cores, a direct callback to Day 20's event-loop material; the
  `(2 × cpu_count) + 1` worker-count starting point, confirmed against this
  sandbox's own `os.cpu_count()` (4 → 9); and reading deploy config (host,
  port, workers, reload) from the environment via Day 17's
  `pydantic_settings.BaseSettings`, unchanged, closing with a minimal
  `uvicorn.run(...)` launch script wired behind Day 9's
  `if __name__ == "__main__":` guard, made load-bearing for the first time
  all course (the file stays importable without starting a server). Bridged
  from SQL per the baseline record: a connection pool sized once via a
  setting rather than hardcoded per client, introduced before any Python in
  the top callout, not from a pandas or other "Python-adjacent" analogy.
  Version/behavior confirmed before writing the lesson, in a scratch dir
  (`.scratch/py25_probe/`, created under the repo root and removed after use,
  not `/tmp`, per every prior day's precedent): `uv run --with fastapi --with
  httpx --with uvicorn python3 …` reported `fastapi 0.141.1` / `uvicorn
  0.52.4` / `httpx 0.28.1`; `python3 -m uvicorn --help` confirmed
  `--host`/`--port`/`--workers`/`--reload` are real CLI flags and that
  `--workers` is documented as "Not valid with --reload"; a probe script
  confirmed `pydantic_settings.BaseSettings` coerces `PORT=9000`/`WORKERS=4`/
  `RELOAD=true` from `os.environ` into a real `int`/`int`/`bool` exactly like
  Day 17's request-body coercion; a third probe confirmed the
  `(2 * cpu_count) + 1` formula's actual output on this sandbox.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-24 entry has flagged). Paced conservatively per that same assumption:
  one core distinction (`--reload` vs. `--workers`) given the most weight,
  no `gunicorn`, Docker, or reverse-proxy material pulled in beyond what
  PLAN.md's own spine line ("a deployable shape") names, and every new
  mechanism tied back explicitly to material already taught (Day 9's import
  guard, Day 17's `BaseSettings`, Day 20's event loop) rather than
  introduced cold.
  No-pandas rule: zero pandas/NumPy API in the lesson body or practice file
  (grep for `pandas|numpy|dataframe`, case-insensitive — zero hits in the
  practice file, exactly one hit in the lesson); one contrast sentence,
  stating plainly that a pandas pipeline has no "deployable shape" question
  at all — no port, no worker count, nothing waiting to accept a next
  request — since it starts, runs, and exits rather than serving requests,
  placed once in its own callout after section 4 and matching the hard-rule
  section above.
  Practice file `practice/25_deploying_with_uvicorn.py` (3 exercises across
  6 checks: a `DeploySettings(BaseSettings)` with four defaulted fields, that
  same class re-read after setting `PORT`/`WORKERS`/`RELOAD` in `os.environ`,
  a `recommended_workers()` implementing the `(2 * cpu_count) + 1` formula,
  and an `is_valid_launch()` function encoding section 2's core gotcha —
  `reload=True` together with a `--workers` flag is invalid, either alone is
  fine) needed no on-disk fixtures and no real socket bind — every check
  works against in-memory settings objects and `os.environ`, matching Day
  14/17's precedent of skipping `tempfile` scaffolding when nothing touches
  disk. `_ex1_env_override()` sets and then `del`s three environment
  variables inside a `try/finally` so a mid-check failure can't leak env-var
  state into a later check. Verified in a scratch dir
  (`.scratch/py25_verify/`, created under the repo root and removed after
  use): the shipped (unsolved) copy, run via `uv run --with fastapi --with
  httpx --with pydantic-settings python3` both from the scratch copy and
  from its real `practice/` path with the documented command, printed six
  clean ✗ lines with no traceback each time (the unsolved `class
  DeploySettings(BaseSettings): ...` body is a bare `...` statement inside an
  otherwise-valid class, not an eagerly-evaluated base-class expression like
  Day 17's original bug, so it imports cleanly and simply has no fields,
  failing every check's attribute/comparison rather than crashing); a
  separately solved copy printed six ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 25 section to `reference/glossary.html` (`--reload`,
  `--workers`) after confirming via grep that `BaseSettings` already had a
  Day 17 row (reused today via plain `<code>` in prose, no second `<dfn>` or
  duplicate row, matching Day 24's own precedent for reusing `middleware`
  unchanged) and that `ASGI server` already had a Day 22 row (reused today
  via one `<dfn>` pointing at the existing term, no new row). Both new terms
  also got matching `<dfn>` markup at first use in the lesson body (confirmed
  by counting `<dfn data-en` occurrences: 3 total — `ASGI server` reused,
  `--reload` new, `--workers` new — 2 of which map to the 2 new Day 25 rows).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for all five questions (Q1
  8/7/8, Q2 10/11/9, Q3 9/7/8, Q4 10/11/11, Q5 12/8/8) — each went through
  several rewrite-and-recount rounds, re-running the script after every edit
  rather than trusting a manual count, until every option matched (Q1-Q4
  landed at 10/10/10, Q5 at 9/9/9), then a final script run against the real
  shipped file confirmed every one before shipping. Registered in
  `assets/nav.js` with `date: "2026-08-22"`.
  **DB access:** per this run's explicit instructions, the Postgres progress
  DB read paths (`psql`/`bin/query-progress`) were treated as unreachable
  from the start and not attempted this run, consistent with the
  documented block on every day since Day 8; this run paced entirely from
  on-disk state (this file's own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record) per
  this run's fallback instructions.
  `bin/record-progress python lesson_generated --lesson
  0025-deploying-with-uvicorn.html --detail '{"by":"headless-run"}'` was
  attempted once after shipping, per this run's instructions — see its own
  output for whether it recorded successfully.
  **This completes every named item of PLAN.md's Phase 2b spine.** Per
  PLAN.md's own closing line ("Revisit this plan when Phase 2a ends — the
  backend depth should be driven by what work and interviews actually
  demand by then" — now applicable to Phase 2b's completion instead), the
  natural next step is to revisit `PLAN.md` itself to decide Phase 3's
  direction, since the spine as written has no further named items; a
  reasonable Day 26 candidate in the meantime is filling `RESOURCES.md`'s
  still-open "Gaps" (Python interview prep, a FastAPI project-layout
  reference) or a consolidation/capstone lesson wiring Phases 2a+2b
  together, mirroring Day 7's Phase 1 capstone.
- 2026-08-24 — **Day 27 generated** (`lessons/0027-itertools.html`), the
  twentieth Phase 2 lesson, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0027-*.html` (or higher-numbered) file existed and no
  `2026-08-24` entry existed anywhere in this file or `assets/nav.js` —
  highest existing lesson on disk was `0026-…` dated 2026-08-23, so
  generation proceeded as Day 27, not a re-run.
  `bin/query-progress` was attempted once as instructed and immediately
  required approval with no user present, the same block documented on
  every day since Day 8 except the inconsistent successes on Days 5, 9, and
  10 — not retried; this run paced entirely from on-disk state (this file's
  own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record).
  Topic: per Day 26's own closing note, both of `PLAN.md`'s named Phase 2
  spines (2a and 2b) are fully covered, and Day 26 itself was already the
  synthesis/capstone move for the FastAPI material — so re-covering that
  ground with a second capstone would be padding, not a gap. Followed the
  same methodology `backend/NOTES.md` documents for its own post-spine
  rounds (its Lesson 20/26 entries: re-scan MISSION.md/PLAN.md/RESOURCES.md
  for a genuine still-open item before inventing anything, and prefer a
  named gap over a guessed Phase 3 direction). `RESOURCES.md`'s own "Gaps"
  section names two candidates (Python interview prep, a FastAPI
  project-layout reference) but neither is a single teachable mechanism —
  interview prep has no chosen source at all to ground a lesson in per this
  course's own "cite one primary source" rule, and project layout/`APIRouter`
  was already taught on Day 19 ("structuring an app beyond one file"), so
  writing it again would re-teach rather than fill a gap. Grepped instead for
  every stdlib module `MISSION.md`'s own success criteria and `RESOURCES.md`
  name by title: `itertools` is named explicitly in both — `RESOURCES.md`
  calls `itertools` and `collections` "the two stdlib modules that replace
  most hand-written data-munging loops," and `MISSION.md`'s success list
  names "`collections` (`defaultdict`, `Counter`), and `itertools`" side by
  side — but `collections` got its own full lesson on Day 3 while
  `itertools` never did; confirmed via grep that `itertools` appears in
  exactly one sentence across every lesson (Day 5's own closing line: "The
  itertools docs are the natural next stop… its recipes section is
  lesson-grade on its own"), named as a pointer forward and never actually
  taught — a genuine, twice-named, still-open gap, not an invented topic.
  Squarely language/stdlib-level, not a data-analysis library, so no scope
  ambiguity despite `itertools` living right next to pandas-adjacent
  vocabulary in `data/`'s own world.
  Taught: `itertools` as a module of ready-made generator functions
  replacing the handful of iterable-combining loop shapes that come up
  constantly, framed as the direct sequel to Day 5's hand-written generators
  ("one call does the job, lazily, exactly like a hand-written generator
  would"); `chain(*iterables)` as streaming several sources in one pass
  without a `+`-built copy, extended to Day 6's file objects
  (`chain(open("jan.csv"), open("feb.csv"))`); `groupby(iterable, key=...)`
  as a narrower, sorted-input-only alternative to Day 3's `defaultdict`
  grouping, reusing Day 4's exact `key=` argument shape, with its own section
  4 gotcha given real weight: it merges only *consecutive* matching items and
  never sorts first, so unsorted input silently produces extra groups instead
  of merging correctly (demonstrated concretely — 3 groups from data that
  looks like it should produce 2); `islice(iterable, stop)` as the
  generator-safe equivalent of Day 2's `seq[:n]` slicing, needed because a
  generator has no index to slice by; and `product(*iterables)` as the
  nested-for-loop-replacing every-combination function, bridged to a SQL
  `CROSS JOIN`. Bridged from SQL per the baseline record: `chain` framed as
  `UNION ALL` and `groupby` framed as a `GROUP BY` that (unlike SQL's own)
  never sorts for you, both in the opening callout before any Python.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-26 entry has flagged). Paced conservatively per that same assumption:
  four functions taught (`chain`, `groupby`, `islice`, `product`), each tied
  back explicitly to a named prior day (Days 2/3/4/5/6) rather than
  introduced cold, matching this course's usual per-lesson mechanism budget.
  No-pandas rule: zero pandas/NumPy/DataFrame hits in the practice file
  (grepped case-insensitively — zero hits, stdlib-only `itertools` import);
  exactly one hit in the lesson — one contrast sentence/callout (titled
  "Where pandas goes from here") naming `pd.concat()` as `chain`'s pandas
  equivalent and `df.groupby()` as `itertools.groupby`'s, stating only that
  pandas's versions sort/hash automatically and work on unsorted input
  unlike the stdlib versions taught here, without demonstrating any pandas
  API, placed once after section 4 and matching the hard-rule section above.
  Practice file `practice/27_itertools.py` (5 exercises: `chain` over two
  raw-line lists, `groupby`-and-sum over pre-sorted rows, counting `groupby`
  groups on deliberately unsorted rows to see the 3-vs-2 gotcha directly,
  `islice` pulling four values off a truly infinite generator, and `product`
  over two small lists) needed no on-disk fixtures — every exercise runs
  against small in-memory lists and one infinite generator, no file I/O.
  Verified in a scratch dir (`.scratch_py27_verify/`, created under the repo
  root and removed after use, per every prior day's `/tmp`-is-out-of-bounds
  precedent): the shipped (unsolved) copy, run via plain `uv run python3`
  (no `--with` needed — stdlib only) both from the scratch copy and from its
  real `practice/` path with the documented command, printed five clean ✗
  lines with no traceback each time (every unsolved `...` assignment or bare
  `...` statement leaves its target name unbound or `Ellipsis`, so each
  `check()`'s own `try/except` catches the resulting `NameError`/comparison
  mismatch cleanly); a separately solved copy (every TODO filled in
  directly) printed five ✓ and the "All green" tally. No bugs found during
  verification — both passes succeeded on the first attempt. One wording fix
  made during authoring, not a functional bug: an early draft of the "Try
  it" paragraph said "first three values" while the practice file's Exercise
  4 actually pulls four (`islice(counter(), 4)`) and the lesson's own worked
  example pulls five (`islice(counter(), 5)`) — the paragraph was reworded to
  say "first four," matching the practice file it actually describes; the
  lesson body's own worked example intentionally keeps the number 5 to avoid
  implying the exact practice-file count, consistent with how other lessons'
  worked examples use different literal numbers than their own practice
  file's exercises.
  Glossary: added a Day 27 section to `reference/glossary.html`
  (`itertools`, `chain`, `groupby`, `islice`, `product`) after confirming via
  grep that none of the five collided with any Day 1-26 entry (Day 3's
  `key` and Day 4's `key= (sorting)` entries were the only near-miss risk
  checked given this course's documented near-collision history, and neither
  string appears among today's five new terms). All five also got matching
  `<dfn>` markup at first use in the lesson body (confirmed by counting
  `<dfn data-en` occurrences: 8 total — `iterable`, `generator`, and `lazy
  evaluation` reused from Day 1/5 via plain `<dfn>` pointing at their
  existing definitions with no new row, plus the 5 new terms, one-for-one
  against the 5 new glossary rows).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line) run from a
  scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for four of five questions (Q1
  11/10/10, Q2 11/10/12, Q3 12/12/12 — already matching, Q4 11/11/9, Q5
  11/12/8) — each mismatched question went through one to three
  rewrite-and-recount rounds, re-running the script after every edit rather
  than trusting a manual count (a hyphenated word like "brand-new" or
  "single" counting as one token by `.split()`, not two, caused at least one
  overshoot per question exactly like prior days' flagged difficulty here),
  until every option matched (Q1 11/11/11, Q2 11/11/11, Q3 12/12/12 untouched,
  Q4 11/11/11, Q5 11/11/11), then a final script run against the real shipped
  file confirmed every one before shipping. Registered in `assets/nav.js`
  with `date: "2026-08-24"`.
  **DB access:** per this run's explicit instructions, `bin/query-progress`
  was attempted once and required approval with no user present — not
  retried, consistent with the documented block on every day since Day 8
  except the inconsistent Day 5/9/10 successes; this run paced entirely from
  on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record) per this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 27 --lesson
  0027-itertools.html --detail '{"by":"github-actions"}'` was attempted once
  after shipping and **required approval**, the same write-path block this
  file has not previously logged (every prior day's write-path attempt since
  Day 9/10 had succeeded) — not retried, logged here as a new observation for
  future runs to watch for rather than assumed to be the old read-path block
  recurring on the write path.
  **Next-day note:** with `itertools` now taught, `RESOURCES.md`'s "Gaps"
  section (Python interview prep, a FastAPI project-layout reference beyond
  the official docs) remains the most concrete still-open item, though
  interview prep still has no chosen source to ground a lesson in per this
  course's "cite one primary source" rule — Day 28 should either find and
  adopt such a source, or re-scan `MISSION.md`/`PLAN.md` once more for
  another named-but-untaught mechanism before falling back to an unnamed
  Phase 3 direction.

- 2026-08-25 — **Day 28 generated** (`lessons/0028-unpacking.html`), a
  Phase 3-adjacent stdlib-gap pick, generated by an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0028-*.html` (or higher-numbered) file existed and no
  `2026-08-25` entry existed anywhere in this file or `assets/nav.js` —
  highest existing lesson on disk was `0027-itertools.html` dated
  2026-08-24, so generation proceeded as Day 28, not a re-run.
  `bin/query-progress` was attempted once as instructed and immediately
  required approval with no user present, the same block documented on
  every day since Day 8 except the inconsistent successes on Days 5, 9, and
  10 — not retried; this run paced entirely from on-disk state (this file's
  own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record).
  Topic: pre-chosen and verified genuinely open before writing anything —
  grepped every prior lesson for "unpack" and found it named twice, never
  delivered. Day 2's slicing section (`0002-comprehensions-and-slicing.html`,
  line 77) wrote `header, *rows = [...]` with the comment "preview only —
  unpacking is Day 4"; Day 3's dict/grouping section
  (`0003-dict-set-and-grouping.html`, lines 30 and 95) said, twice, that
  `zip(names, ages)` "unpacks each (key, value) pair" and that "unpacking it
  fully is Day 4." Day 4 shipped as functions/`key=`/`lambda`
  (`0004-functions-args-and-key.html`) instead — confirmed via grep that the
  string "unpack" appears zero times anywhere in that file. `MISSION.md`'s
  own success-criteria list ("Reach for the idiom instead of the loop:
  comprehensions, unpacking, `sorted(key=…)`, `dict`/`set` … `collections`
  … and `itertools`") names six items; the other five each already have a
  lesson (Days 2, 4, 3, 3, and 27 respectively) — unpacking was the one
  remaining gap on that exact checklist, a twice-promised, never-delivered
  topic rather than an invented one.
  Taught: two-name tuple unpacking as the general mechanism behind
  something already in constant use since Day 3 (`for name, age in
  zip(...)` silently unpacks each pair every iteration — called out
  explicitly, "you've been doing this since Day 3"); `for`-loop unpacking
  generalized to `.items()` pairs; star-unpacking (`*rest`) delivering on
  Day 2's exact deferred `header, *rows` example, with an explicit
  side-by-side against Day 4's `def f(*args)` — same star, same "collect the
  rest" idea, one position over (function definition vs. assignment target);
  the no-temp swap idiom (`a, b = b, a`), explained via the same
  right-side-builds-first-as-one-tuple rule; and unpacking a function's
  returned tuple directly at the call site, via a small `min_max(values)`
  helper written for this lesson (no existing Day 1/7 function returned a
  tuple to reuse, so the parallel example was authored fresh, in the same
  self-contained style Day 4's `discount()` uses). Bridged from SQL per the
  baseline record: `city, amount, date = cursor.fetchone()` framed as the
  same "several names, one assignment" move, in the opening callout before
  any Python.
  Learning records: still only the Day 1 baseline record
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-27 entry has flagged). Paced conservatively per that same assumption:
  four mechanisms taught (plain unpacking, star-unpacking, the swap idiom,
  return-value unpacking), each tied back explicitly to a named prior day
  (Days 2/3/4) rather than introduced cold, matching this course's usual
  per-lesson mechanism budget.
  No-pandas rule: zero pandas/NumPy/DataFrame hits in the practice file
  (grepped case-insensitively — zero hits, no imports needed at all, every
  exercise is pure language mechanics); exactly one hit in the lesson — one
  contrast sentence/callout (titled "Where pandas goes from here") naming
  `df.shape` unpacked as `n_rows, n_cols = df.shape` as the pandas-world
  echo of today's mechanism, without demonstrating any pandas API, placed
  once after section 4 and matching the hard-rule section above.
  Practice file `practice/28_unpacking.py` (5 exercises: basic two-name
  tuple unpack, star-unpack a header off a small CSV-shaped list, the
  no-temp swap idiom on two arguments, summing scores via unpacking a `for`
  loop over `(name, score)` pairs, and unpacking `min_max()`'s returned
  tuple directly at the call site) needed no on-disk fixtures — every
  exercise runs against small in-memory literals. One design correction made
  during authoring, caught by verification rather than assumed safe: the
  first draft used bare `x, y = ...` / `header, *rows = ...` /
  `first, second = ...` assignments as the unsolved placeholders directly at
  module level — running the unsolved file raised an *unhandled*
  `TypeError: cannot unpack non-iterable ellipsis object` at import time
  (confirmed by actually running it), crashing before `check()`'s own
  try/except ever got a chance to catch it, which would have printed a raw
  traceback instead of this course's required five clean ✗ lines. Fixed by
  wrapping every exercise's unpacking inside its own small function
  (`unpack_point()`, `split_header()`, `swap(a, b)`, `total_score()`,
  `lowest_and_highest()`) with a bare `...` statement as its unsolved body,
  so the unsolved function returns `None` instead of raising at import time,
  and each `check()` lambda calls the function and compares its return value
  — the mismatch/`None` result is what the `try/except` inside `check()` was
  actually designed to catch. Verified in a scratch dir
  (`.scratch_py28_verify/`, created under the repo root and removed after
  use, per every prior day's `/tmp`-is-out-of-bounds precedent): the shipped
  (unsolved) copy, run via plain `uv run python3` (no `--with` needed — no
  imports at all), both from the scratch copy and from its real `practice/`
  path with the documented command, printed five clean ✗ lines with no
  traceback each time after the fix; a separately solved copy (every
  function body filled in directly) printed five ✓ and the "All green"
  tally. The ellipsis-at-module-level bug above was caught precisely because
  this course's convention is to actually run the unsolved file and read its
  output rather than assume a bare `...` is always safe — consistent with
  this file's own repeatedly flagged "Ellipsis placeholder must not silently
  produce a false checkmark" gotcha, extended here to "must not silently
  produce an unhandled crash" either.
  Glossary: added a Day 28 section to `reference/glossary.html`
  (`unpacking`, `star-unpacking (*rest)`, `swap idiom`) after grepping first
  to confirm none of the three collided with any Day 1-27 entry — the only
  near-miss risk checked given this course's documented near-collision
  history (Day 3's `key` vs. Day 4's `key= (sorting)`) was `*args`/`**kwargs`
  language reused from Day 4's `wrapper` glossary entry, and neither
  "unpacking," "star-unpacking," nor "swap idiom" appears among any existing
  row. All three also got matching `<dfn>` markup at first use in the lesson
  body (confirmed by counting `<dfn data-en` occurrences: 3 total, one-for-one
  against the 3 new glossary rows).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (splitting the quiz block into its five question `<div>`s on the opening
  tag and counting `.split()` words per `<button class="opt">` line) run
  from a scratch dir via `uv run python3`, per this course's established
  convention. Mismatched on the first draft for three of five questions (Q1
  10/10/10 — already matching, Q2 10/10/9, Q3 9/9/9 — already matching, Q4
  11/10/11, Q5 11/10/10) — each mismatched question went through one
  rewrite-and-recount round, re-running the script after every edit rather
  than trusting a manual count, until every option matched (Q1 10/10/10, Q2
  10/10/10, Q3 9/9/9, Q4 11/11/11, Q5 11/11/11), then a final script run
  against the real shipped file confirmed every one before shipping.
  Registered in `assets/nav.js` with `date: "2026-08-25"`.
  **DB access:** per this run's explicit instructions, `bin/query-progress`
  was attempted once and required approval with no user present — not
  retried, consistent with the documented block on every day since Day 8
  except the inconsistent Day 5/9/10 successes; this run paced entirely from
  on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record) per this run's fallback instructions.
  `bin/record-progress python lesson_generated --day 28 --lesson
  0028-unpacking.html --detail '{"by":"github-actions"}'` was attempted once
  after shipping and **succeeded** (contrast with Day 27's write-path block,
  logged here as a new observation — the write path is not consistently
  blocked the same way the read path is), consistent with the documented
  observation logged the same way on prior successful days).
  **Next-day note:** with `MISSION.md`'s full idiom checklist now covered
  (comprehensions, unpacking, `sorted(key=…)`, `dict`/`set`, `collections`,
  `itertools`), `RESOURCES.md`'s "Gaps" section (Python interview prep, a
  FastAPI project-layout reference beyond the official docs) remains the
  most concrete still-open item, though interview prep still has no chosen
  source to ground a lesson in per this course's "cite one primary source"
  rule — Day 29 should either find and adopt such a source, or re-scan
  `MISSION.md`/`PLAN.md` once more for another named-but-untaught mechanism
  before falling back to an unnamed Phase 3 direction.
- 2026-08-26 — **Day 29 generated**
  (`lessons/0029-writing-context-managers.html`), an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0029-*.html` (or higher-numbered) file existed and no
  `2026-08-26` entry existed anywhere in this file or `assets/nav.js` —
  highest existing lesson on disk was `0028-unpacking.html` dated
  2026-08-25, so generation proceeded as Day 29, not a re-run.
  **DB access:** per this run's explicit instructions, `LEARNING_DB_URL`
  reads were skipped entirely (hard-blocked in this sandbox, already
  confirmed prior to this session) — paced entirely from on-disk state
  (this file's own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record, no
  completion/quiz record for any day 2-28).
  Topic selection: Day 28's own next-day note offered two paths — find and
  adopt a genuine primary source for Python interview prep, or re-scan
  `MISSION.md`/`PLAN.md` for another named-but-untaught mechanism before
  falling back to an unnamed Phase 3 direction. The first path was
  attempted genuinely, not skipped: `WebSearch`/`WebFetch` were invoked
  directly and via a dedicated research subagent to find a real, citable
  interview-prep source, matching the quality bar of `RESOURCES.md`'s
  existing entries (official docs or a named, credible author/site, never
  an SEO listicle). Both tools returned a hard permission denial
  ("Claude requested permissions to use WebSearch, but you haven't granted
  it yet") at the top level and inside the subagent alike — no live web
  access was available this run, so that path was abandoned rather than
  risk shipping a fabricated or stale-memory URL as a cited "primary
  source," which would violate this course's own citation rule worse than
  not adding one yet.
  Fell through to the second path: re-grepped every lesson body (`0001`
  through `0028`) for named-but-undelivered mechanisms from
  `MISSION.md`/`PLAN.md` and found one concrete, textually-grounded gap —
  Day 6's own lesson prose (`lessons/0006-files-formats-and-with.html`,
  section 4) explicitly says "You won't write `__enter__`/`__exit__`
  yourself yet — that's a later lesson on writing your own classes," a
  promise no lesson since had delivered on (grepped
  `__enter__|__exit__|contextmanager` across all of `python/lessons/`;
  every hit besides Day 6 itself was an incidental "always runs" callback
  — Day 8's `finally`, Day 11's fixture teardown — never the mechanism
  itself). This is the same "twice-promised, never-delivered" shape Day
  28's own unpacking pick used, not an invented topic — grounded in this
  course's own text, language-level (the object-model protocol behind
  `with`, not a library), and backed by `RESOURCES.md`'s already-cited
  Data model reference (`docs.python.org/3/reference/datamodel.html`),
  which formally documents `__enter__`/`__exit__`. Also confirmed via grep
  that `@property`, `@classmethod`/`@staticmethod` as their own mechanism,
  `enum.Enum`, and `functools.lru_cache`/`reduce`/`partial` are likewise
  untaught, but none of those is named explicitly anywhere in
  `MISSION.md`/`PLAN.md` the way context managers were named (twice) and
  unpacking was (twice) — picking one of those instead would have been
  "inventing a topic with no textual basis," which this run's instructions
  explicitly forbid, so context managers was the only defensible pick.
  Topic: writing a context manager — both the class form (`__enter__`/
  `__exit__` on a plain class) and the `contextlib.contextmanager`
  generator-based shortcut. Taught: the `with` desugaring recap from Day 6
  section 4, now completed rather than left as recognition-only; a
  `Timer` class implementing both dunder methods, with the single most
  emphasized rule being `__exit__`'s return-value contract — a truthy
  return suppresses an in-flight exception, `False`/`None` lets it
  propagate, and a context manager that swallows everything by accident is
  a bug, not a feature; `contextlib.contextmanager` as Day 5's `yield`
  mechanism reused to skip the class boilerplate, with the
  before-`yield`/after-`yield` split mapped explicitly onto
  `__enter__`/`__exit__` and the teardown code's `finally` requirement tied
  back to Day 6's original handle-leak motivation; and a `transaction(log)`
  example (BEGIN/COMMIT/ROLLBACK) wiring in Day 8's narrow-catch-and-
  re-raise habit inside a generator instead of a plain function. Bridged
  from SQL per the baseline record: a transaction block (`BEGIN`/`COMMIT`/
  `ROLLBACK`, one guaranteed outcome) introduced before any Python in the
  top callout, not from a pandas or other "Python-adjacent" analogy — the
  same transaction shape also became section 4's worked example, not just
  the opening bridge.
  Learning records: still only the Day 1 baseline
  (`learning-records/0001-baseline-reads-python-writes-little.md`) — no
  completion/quiz record for any later day was found (same gap every Day
  8-28 entry has flagged). Paced conservatively per that same assumption:
  two forms taught (class-based, generator-based), each tied back to
  already-taught material (Day 5 `yield`, Day 6 `with`/`__enter__`/
  `__exit__`, Day 8 `try`/`except`/`raise`, Day 11 fixture teardown) rather
  than introduced as unrelated new ground, and no additional contextlib
  helpers (`ExitStack`, `suppress`, `closing`, `nullcontext`) pulled in
  beyond the two named forms and the one deliberate-suppression exercise.
  No-pandas rule: zero pandas/NumPy/DataFrame hits in the practice file
  (grepped case-insensitively — zero hits, standard library only, only
  `contextlib.contextmanager` imported); exactly one hit in the lesson —
  one contrast sentence/callout (titled "Where pandas goes from here")
  naming `pd.option_context(...)` as itself a context manager, without
  demonstrating any pandas API, placed once after section 4/the interview
  callout and labeled in prose as the only such sentence, matching the
  hard-rule section above.
  Practice file `practice/29_writing_context_managers.py` (7 checks across
  5 exercises: a class-based `LoggingCM` logging enter/exit in order,
  confirming `__exit__` still runs when the `with`-block raises, a
  `@contextmanager`-based generator equivalent, the `transaction()`
  commit/rollback pattern in both the success and failure paths, and a
  `Suppress(exc_type)` class whose `__exit__` deliberately suppresses only
  a matching exception type) needed no on-disk fixtures — every exercise
  runs against small in-memory logs and exceptions. Followed this course's
  now-standard defensive pattern against the Ellipsis-at-module-level bug
  family flagged repeatedly since Days 11/12/17/28: `LoggingCM`'s class
  line and `Suppress`'s class line are both left fully definable (concrete
  base classes, no bare `...` anywhere in a class header or decorator
  position), with every unsolved `...` placeholder living strictly inside a
  method or function body instead, so an unsolved `logging_cm`/
  `transaction` function simply returns `None` (undecorated in effect)
  rather than crashing at import/decoration time. Verified in a scratch dir
  (`.scratch_py29_verify/`, created under the repo root and removed after
  use, per every prior day's `/tmp`-is-out-of-bounds precedent): the
  shipped (unsolved) copy, run via plain `uv run python3` (no `--with`
  needed), both from the scratch copy and from its real `practice/` path
  with the documented command, printed seven clean ✗/✓ lines with no
  traceback each time — six ✗ and, correctly, one ✓ (Ex 5b passes even
  unsolved, since an unsolved `Suppress.__exit__` returns `None`/falsy,
  which correctly lets the non-matching `ValueError` propagate — confirmed
  to be the exercise's intended distinguishing behavior against Ex 5a, not
  a bug); a separately solved copy (every `...` filled in directly in the
  scratch copy) printed all seven ✓ and the "All green" tally. No bugs
  found during verification — both passes succeeded on the first attempt,
  and no unhandled traceback appeared at any point.
  Glossary: added a Day 29 section to `reference/glossary.html`
  (`contextlib.contextmanager`, `exception suppression`) after confirming
  via grep that neither term collided with any Day 1-28 entry — deliberately
  did **not** re-glossary `__enter__`/`__exit__`/`context manager`/`with
  statement`, all already defined under Day 6, and reused those existing
  terms as plain `<code>` in today's prose instead, per this course's own
  no-duplicate-glossary-row convention. The 2 new `<dfn data-en` tags in
  the lesson body match the 2 new glossary rows exactly (confirmed by
  count).
  Quiz: 5 questions. First draft had one markup slip caught during
  verification — Q4's opening `<div class="q" data-why="...">` had a stray
  line break landing the closing `>` on its own line, valid HTML but
  inconsistent with every other question in this and every prior lesson,
  fixed to a single-line tag to match convention. Word counts were checked
  with a small Python script (regex-splitting the quiz block into its five
  question `<div>`s and counting `.split()` words per `<button class="opt">`
  line, run from a scratch dir via `uv run python3`) and mismatched on the
  first draft for three of five questions (Q1 7/9/7, Q3 10/11/8, Q4 9/8/10)
  — Q2 and Q5 were already equal on the first draft (9/9/9 and 10/10/10).
  Each mismatched question went through one to two rewrite-and-recount
  rounds, re-running the script after every edit rather than trusting a
  manual count, until every option matched (Q1 9/9/9, Q3 10/10/10, Q4
  9/9/9), then — per this run's explicit instruction to re-verify with a
  second independent method after any rewrite — a second, differently
  written script (document-order `<button class="opt">` extraction grouped
  in threes, instead of the first script's per-question regex split) was
  run against the final file and independently confirmed all 15 options
  (5 questions × 3 options) land on their target counts (9/9/9, 9/9/9,
  10/10/10, 9/9/9, 10/10/10) before shipping. Registered in `assets/nav.js`
  with `date: "2026-08-26"`.
  `bin/record-progress python lesson_generated --day 29 --lesson
  0029-writing-context-managers.html --detail '{"by":"github-actions"}'`
  was run once after shipping and **succeeded**: `recorded:
  python/lesson_generated day=29 lesson=0029-writing-context-managers.html`.
  **Next-day note:** `RESOURCES.md`'s "Gaps" section (Python interview
  prep, a FastAPI project-layout reference beyond the official docs) is
  now the clearest remaining lead, but both require genuine live web
  research to resolve responsibly — this run confirmed `WebSearch`/
  `WebFetch` are denied by a permission gate in this sandbox (not merely
  rate-limited or flaky), a more specific finding than prior days' vaguer
  "DB access blocked" notes, and about a different pair of tools than any
  prior day tested. Day 30 should retry web access first (permissions may
  be granted differently in a future run); if still blocked, a further
  `MISSION.md`/`PLAN.md` re-scan may need to look at less obviously-named
  candidates — `MISSION.md` alludes to "Python's object model" broadly but
  does not name `@property`/operator-overloading/`__repr__`/`__eq__` as
  explicitly as it named unpacking or (via Day 6's own deferral) context
  managers, so picking one of those next would need a clearer textual
  hook than this run found for them — or fall back to an unnamed Phase 3
  direction. Still no `lesson_completed`/quiz/kata outcome record exists
  for ANY day after 29 rounds — no reported weak spot to target.
- 2026-08-27 — **Day 30 generated**
  (`lessons/0030-object-model-dunder-and-property.html`), an automated
  headless daily-generation run. Idempotency: confirmed before writing
  anything that no `python/lessons/0030-*.html` (or higher-numbered) file
  existed and no `2026-08-27` entry existed anywhere in this file or
  `assets/nav.js` — highest existing lesson on disk was
  `0029-writing-context-managers.html` dated 2026-08-26, so generation
  proceeded as Day 30, not a re-run.
  Topic selection: Day 29's own next-day note named the candidate directly
  — Python's object model: operator overloading, `__repr__`/`__eq__`/
  `__lt__`, and `@property`/data descriptors — and flagged that
  `MISSION.md` names "Python's object model" broadly (success criterion:
  "Explain Python's object model out loud... why `b = a` aliases, why a
  mutable default argument is a trap") without naming these specific dunder
  methods as explicitly as it named unpacking or context managers. Re-read
  `MISSION.md` directly this run to confirm the fit is real rather than
  assumed: the object-model thread is present, and `__repr__`/`__eq__` were
  already name-dropped in passing back on Day 7 ("comparing two instances
  with `==` checks identity, not field values, unless you write `__repr__`
  and `__eq__` by hand") and Day 17, always as something `@dataclass`/
  pydantic generate automatically, never taught as a mechanism to write by
  hand — a real, textually-grounded gap, not an invented one. Confirmed via
  grep across all of `python/` for
  `__repr__|__eq__|__lt__|@property|operator overload|dunder|__str__|__ne__|__gt__|__le__|__ge__`
  before committing: every lesson-body hit (Day 7, Day 17) was passing
  mention of dataclass/pydantic auto-generation, and every NOTES.md hit was
  prior-day planning prose (Day 28's `Path`/`/`-operator aside, Day 29's
  own next-day note) — no lesson ever taught writing `__repr__`, `__eq__`,
  `__lt__`, an operator-overload dunder, or `@property` by hand. Topic
  confirmed clear.
  Web-lookup attempt: per this run's instructions, tried once rather than
  assuming the prior run's block still holds — `WebFetch` against
  `docs.python.org/3/reference/datamodel.html#special-method-names`
  **succeeded** this run (a change from Day 29's hard permission denial on
  both `WebSearch` and `WebFetch`), returning confirmation of the rich-
  comparison method table (`__lt__`/`__le__`/`__eq__`/`__ne__`/`__gt__`/
  `__ge__`), the `__repr__` "valid Python expression" convention, and the
  `NotImplemented`-vs-`False` convention for unrelated-type comparisons —
  all used directly in section 3's prose and the interview callout. Did not
  add a new `RESOURCES.md` entry since the URL fetched is the same Data
  model reference already cited there for Day 1 and Day 29; cited it again
  for Day 30 instead, per the existing entry's own "any 'why does it behave
  like that' question" scope.
  Taught: section 1 shows the problem live (a plain class's ugly `__repr__`
  default and identity-based `==`/broken `<`); section 2 `__repr__` (tied
  back to Day 7's dataclass auto-generation, now explained rather than
  taken on faith); section 3 `__eq__`/`__lt__` with the `isinstance` guard
  and `NotImplemented` (not `NotImplementedError`) convention, plus the
  payoff that `sorted()` needs no `key=` once `__lt__` exists, closing the
  loop back to Day 4's `key=` lesson; section 4 operator overloading via
  `__add__` on a `Vector`, with a one-line caution against overloading an
  operator for a meaning that doesn't obviously fit; section 5 `@property`
  plus a paired `@x.setter`, tied to Day 8's `raise` for validation and
  explicitly compared to Day 17's pydantic validators ("the plain-Python
  version of that same instinct, scoped to one derived attribute"). Bridged
  from SQL per the baseline record: a table's column order/`ORDER BY` not
  happening by accident, introduced before any Python in the top callout,
  not from a pandas analogy.
  No-pandas rule: zero pandas/NumPy API calls anywhere in the practice
  file (grepped case-insensitively — zero hits, no imports beyond the
  standard library, which today's practice file doesn't even need to
  import anything from); exactly one hit in the lesson — one contrast
  sentence/callout (titled "Where pandas/NumPy go from here") naming
  `DataFrame.__eq__` returning an elementwise boolean mask as the same
  dunder mechanism at bigger scale, without demonstrating any pandas API,
  placed once after section 5/the interview callout, matching the hard-rule
  section above.
  Practice file `practice/30_object_model_dunder_and_property.py` (8 checks
  across 5 exercises: `Point.__repr__`, `Version.__eq__`/`__lt__` plus
  sorting a list of `Version`s with plain `sorted()` and no `key=`,
  `Version == <int>` falling back to `False` via `NotImplemented` instead
  of raising, `Vector.__add__` operator overloading, and a `Temperature`
  class with a `@property`/`@x.setter` pair that converts C↔F and validates
  against absolute zero) needed no on-disk fixtures. Followed this course's
  standard defensive pattern against the Ellipsis-at-module-level bug
  family: every class line stays fully definable (concrete base classes,
  no bare `...` in a class header or decorator position), with unsolved
  `...` living strictly inside method bodies. One real bug caught during
  verification, not just markup: Ex 5b's original scenario started
  `Temperature(0)` and set `.fahrenheit = 32`, expecting `.celsius == 0`
  afterward — but an *unsolved* no-op setter also leaves `.celsius` at its
  untouched initial value `0`, so the check passed ✓ even completely
  unsolved, a false-positive matching the same failure family Day 29's log
  flagged for Ex 5b there (coincidentally also a 5b). Fixed by starting
  from `Temperature(100)` instead, so an unsolved no-op setter leaves
  `.celsius` at `100` — correctly ✗ — while a solved setter still correctly
  converts to `0`. Verified in a scratch dir (`.scratch_py30_verify/`,
  created under the repo root and removed after use): the shipped
  (unsolved) copy printed 8 clean ✗ lines with no traceback, both from the
  scratch copy and from its real `practice/` path with the documented
  command; a separately solved copy (every `...` filled in directly in the
  scratch copy) printed all 8 ✓ and the "All green" tally. No other bugs
  found.
  Glossary: added a Day 30 section to `reference/glossary.html` (`dunder
  method`, `operator overloading`, `@property`) after confirming via grep
  that none collided with any Day 1-29 entry — deliberately did **not**
  re-glossary `__repr__`/`__eq__`/`__lt__` themselves as separate rows,
  since they're explained inline via `<code>` and the new `dunder method`/
  `operator overloading` entries cover the general mechanism, matching this
  course's no-duplicate-glossary-row convention. The 3 new `<dfn data-en`
  tags in the lesson body match the 3 new glossary rows exactly (confirmed
  by count).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line, run from a
  scratch dir via `uv run python3`) and mismatched on the first draft for
  four of five questions (Q1 8/9/9, Q3 9/10/10, Q4 11/7/11, Q5 9/10/10) —
  only Q2 was already equal (10/10/10). Each mismatched question went
  through one to two rewrite-and-recount rounds — Q4's second option needed
  two separate word insertions across two rounds before landing on 11 — re-
  running the script after every edit, until every option matched (Q1
  9/9/9, Q3 10/10/10, Q4 11/11/11, Q5 10/10/10). Re-verified with a second,
  independently-written script (document-order `<button class="opt">`
  extraction via regex across the whole document, ignoring the per-question
  `<div>` wrapper entirely, then grouped in threes) run against the final
  file — independently confirmed all 15 options (5 questions × 3 options)
  land on their target counts (9/9/9, 10/10/10, 10/10/10, 11/11/11,
  10/10/10) before shipping. Registered in `assets/nav.js` with
  `date: "2026-08-27"`.
  `bin/record-progress python lesson_generated --day 30 --lesson
  0030-object-model-dunder-and-property.html --detail
  '{"by":"github-actions"}'` was run once after shipping and **succeeded**:
  `recorded: python/lesson_generated day=30
  lesson=0030-object-model-dunder-and-property.html`. DB reads remain
  blocked: `bin/query-progress python` was tried once this run (per the
  one-attempt convention) and failed immediately with a generic "requires
  approval" gate, no user present to grant it — identical to every prior
  round, and notably still blocked even though `WebFetch` access was
  granted this run, confirming the two gates are independent.
  **Next-day note:** the object-model thread opened today (dunder methods,
  `@property`) is now taught through the single-attribute case; `__hash__`
  and its mutability interaction with `__eq__` (an object defining `__eq__`
  should not also define a mutable `__hash__`, straight from today's fetched
  Data model page) is the clearest immediate follow-on if Day 31 continues
  the same thread, alongside `@classmethod`/`@staticmethod` (named but
  deliberately deferred in Day 29's own log) as an alternative next pick.
  With today's `WebFetch` success, Day 31 should also retry the interview-
  prep source search flagged unresolved since Day 28 — worth attempting
  again now that at least one web tool responded, even though `WebSearch`
  itself was not re-tested this run. Still no `lesson_completed`/quiz/kata
  outcome record exists for any day — no reported weak spot to target.
- 2026-08-28 — **Day 31 generated**
  (`lessons/0031-hash-eq-and-mutability.html`), an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  `assets/nav.js` had no `n: 31` entry and no `date: "2026-08-28"` entry
  anywhere, and no `python/lessons/0031-*.html` file existed on disk —
  highest existing lesson was `0030-object-model-dunder-and-property.html`
  dated 2026-08-27, so generation proceeded as Day 31, not a re-run.
  Topic selection: Day 30's own next-day note named two live candidates —
  `__hash__`'s mutability interaction with `__eq__`, or `@classmethod`/
  `@staticmethod` (deferred since Day 29) — and explicitly asked this run to
  prefer the former as the more natural direct continuation unless research
  turned up a strong reason otherwise. Picked `__hash__`/`__eq__`: it
  continues the exact dunder-method thread Day 30 just opened (same
  mechanism family, same `Money`-style worked example reusable across both
  lessons), closes a real gap Day 3 left open (dict keys/set elements
  "must be immutable (hashable)" was stated back then with zero mechanism
  given), and Day 30's own practice file already named `__hash__` in its
  "Go deeper" primary-source blurb as one of the dunders "left untaught
  here" — a stronger textual hook than `@classmethod`/`@staticmethod` had.
  `@classmethod`/`@staticmethod` remains a legitimate open thread for a
  future day but was not picked today.
  Web-lookup: per Day 30's success and this run's own instructions, used
  `WebFetch` against
  `docs.python.org/3/reference/datamodel.html#object.__hash__` before
  writing anything — succeeded, returning the exact claims used directly in
  the lesson: "the only required property is that objects which compare
  equal have the same hash value," "a class that overrides `__eq__()` and
  does not define `__hash__()` will have its `__hash__()` implicitly set to
  `None`," and "if a class defines mutable objects and implements an
  `__eq__()` method, it should not implement `__hash__()`" — all three
  quoted close to verbatim in sections 1-3 and the interview callout, so no
  claim in the lesson rests on memory alone. Did not add a new
  `RESOURCES.md` entry since the URL is the same Data model reference
  already cited there and reused for Day 1/29/30; cited it again for Day 31
  instead. `WebSearch` (the still-unresolved `RESOURCES.md` "Gaps" —
  Python interview prep, FastAPI project-layout reference) was not
  re-attempted this run — today's session budget went to the `__hash__`
  research and verification instead; still open for a future day.
  Taught: section 1 what `__hash__` does mechanically (`hash(x)` calls
  `x.__hash__()`, picks a dict/set bucket, default is identity-based and
  stays in lockstep with the default `__eq__`, both from Day 30); section 2
  shows Day 30's own `Money.__eq__` example silently becoming unhashable
  the moment `__eq__` is defined, and states the implicit-`None` rule as
  Python's documented behavior, not an accident; section 3 the fix (a
  matching `__hash__` over the same field(s) `__eq__` compares) immediately
  followed by the mutability trap live on a `Tag` class whose `.label` is
  reassigned after being hashed into a `set`, showing `t in seen` return
  `False` for an object still physically present — closing with the
  documented guidance to leave mutable classes unhashable and the tie back
  to Day 7's `@dataclass(frozen=True)`, confirmed by direct execution this
  run (`hash()`/`==`/`FrozenInstanceError` all behaved as described) before
  writing it into the quiz. Bridged from SQL per the baseline record: a
  primary key that must stay put while used as a lookup/join key (`UPDATE
  orders SET id = ...` against a referenced row breaks every index),
  introduced before any Python in the top callout, not from a pandas
  analogy — the same "changing a value used as a key breaks the lookup
  structure" shape reused for the mutable-`__hash__` trap in section 3.
  No-pandas rule: zero pandas/NumPy/DataFrame hits in the practice file
  (grepped case-insensitively — zero hits; the file imports nothing at all,
  standard library needing no import for this lesson's content); exactly
  one hit in the lesson — one contrast sentence/callout (titled "Where
  pandas goes from here") naming a `DataFrame`'s own unhashability (mutable
  contents) and a `MultiIndex` level's use of hashable tuples, without
  demonstrating any pandas API, placed once after section 3/the interview
  callout, matching the hard-rule section above.
  Practice file `practice/31_hash_eq_and_mutability.py` (5 checks across 5
  exercises: a plain `PlainPoint` class hashable by default via identity,
  an `UnsafeMoney` class whose `__eq__` TODOs are completed and which stays
  correctly unhashable with no `__hash__` written, a `Money` class with a
  hand-written matching `__hash__`, confirming two equal `Money(500))`s
  share one dict slot, and a deliberately mutable `Tag` class demonstrating
  the wrong-bucket bug live after `.label` is reassigned post-insertion)
  needed no on-disk fixtures. Caught the same false-positive bug family
  flagged on Days 29/30 during drafting itself, before shipping: Exercise
  2's original check only called `hash(UnsafeMoney(500))` and never
  exercised the `__eq__` TODOs at all, so an unsolved `__eq__` (falling
  through to an implicit `None` return) would still correctly raise
  `TypeError` on `hash()` regardless of whether the TODOs were filled in —
  the TODO lines would have been decorative, producing an accidental ✓ with
  the fill-in untested. Fixed before shipping by having
  `run_unsafe_money_unhashable()` also evaluate and return
  `UnsafeMoney(500) == UnsafeMoney(500)` alongside the hashability check, so
  an unsolved `__eq__` now correctly fails Exercise 2 too (returns `None`
  instead of `True`). Exercise 1 has no TODO by design (a pure
  demonstration that a plain class is hashable by default) and is the one
  exercise expected to print ✓ even unsolved — confirmed intentional, not
  the same bug, since nothing in it is left for the learner to fill in.
  Followed this course's standard defensive pattern against the
  Ellipsis-at-module-level bug family: every class line and method
  signature stays fully definable, with unsolved `...` living strictly
  inside method bodies. Verified in a scratch dir (created under the repo
  root as `.scratch_py31_verify`/`.scratch_py31_final`/`.scratch_py31_qc`
  at different points this run, each removed immediately after use, per
  every prior day's `/tmp`-is-out-of-bounds precedent): the shipped
  (unsolved) copy printed exactly 1 ✓ (Exercise 1, by design) and 4 ✗ with
  no traceback, both from a scratch copy and from its real `practice/` path
  with the documented command; a separately solved copy (every `...` filled
  in directly in a scratch copy) printed all 5 ✓ and the "All green" tally.
  One real bug caught and fixed as described above; no other bugs found.
  Glossary: added a Day 31 section to `reference/glossary.html`
  (`implicit unhashable`) after confirming via grep that it collided with
  no Day 1-30 entry — deliberately did **not** re-glossary `dunder method`
  (Day 30), `hashable`/`key` (mentioned in passing under Day 3's existing
  `dict`/`key` rows), or `frozen=True`/`dataclass` (Day 7), reusing all of
  them as plain `<code>` in today's prose instead, matching this course's
  no-duplicate-glossary-row convention. The 1 new `<dfn data-en` tag in the
  lesson body matches the 1 new glossary row exactly (confirmed by count).
  Quiz: 5 questions (added a 5th after drafting only 4, once a headcount
  grep across all 31 lesson files showed every other lesson in the course
  has exactly 5 — the 5th question covers `@dataclass(frozen=True)`'s safe
  auto-generated `__hash__`, tying section 3's closing point back to Day 7).
  Word counts were checked with a small Python script (regex-splitting the
  quiz block into its question `<div>`s and counting `.split()` words per
  `<button class="opt">` line, run from a scratch dir via `uv run python3`)
  and mismatched on the first draft for all 4 originally-drafted questions
  (Q1 9/10/8, Q2 10/11/10, Q3 11/9/10, Q4 12/9/11); the added 5th question
  also mismatched on its own first draft (9/11/10). Each went through one
  to four rewrite-and-recount rounds — Q5 in particular needed four rounds,
  overshooting to 12/11/11 once before landing correctly — re-running the
  script after every edit, until every option matched (Q1 10/10/10, Q2
  11/11/11, Q3 11/11/11, Q4 12/12/12, Q5 11/11/11). Re-verified with a
  second, independently-written script (document-order `<button
  class="opt">` extraction via regex across the quiz block, ignoring the
  per-question `<div>` wrapper, then grouped in threes) run against the
  final file — independently confirmed all 15 options (5 questions × 3
  options) land on their target counts before shipping. Registered in
  `assets/nav.js` with `date: "2026-08-28"`.
  `bin/record-progress python lesson_generated --day 31 --lesson
  0031-hash-eq-and-mutability.html --detail '{"by":"github-actions"}'` was
  run once after shipping and **succeeded**: `recorded: python/lesson_generated
  day=31 lesson=0031-hash-eq-and-mutability.html`.
  **Next-day note:** `@classmethod`/`@staticmethod` (deferred again this
  run, now twice) is the clearest immediate candidate for Day 32 if the
  object-model/dunder thread has run its course — otherwise `RESOURCES.md`'s
  still-unresolved "Gaps" (Python interview prep, a FastAPI project-layout
  reference) is worth a dedicated `WebSearch` attempt given `WebFetch` has
  now succeeded on both Day 30 and Day 31. Still no `lesson_completed`/
  quiz/kata outcome record exists for any day — no reported weak spot to
  target.
- 2026-08-29 — **Day 32 generated**
  (`lessons/0032-classmethod-and-staticmethod.html`), an automated headless
  daily-generation run. Idempotency: confirmed before writing anything that
  no `python/lessons/0032-*.html` (or higher-numbered) file existed and no
  `n: 32`/`date: "2026-08-29"` entry existed anywhere in `assets/nav.js` —
  highest existing lesson on disk was `0031-hash-eq-and-mutability.html`
  dated 2026-08-28, so generation proceeded as Day 32, not a re-run.
  Topic selection: Day 31's own next-day note named `@classmethod`/
  `@staticmethod` directly as the clearest immediate candidate, deferred
  twice already (first named in Day 29's log, deferred again in Day 30's).
  Grepped all of `python/` for `classmethod|staticmethod` before committing:
  the only hits were pydantic-validator mentions (Day 17's lesson/practice,
  Day 26's capstone) and this file's own prior planning prose — neither
  decorator was ever taught as its own mechanism, confirming a real,
  textually-grounded gap. Picked over re-attempting `RESOURCES.md`'s "Gaps"
  (interview prep, FastAPI project-layout) since those still have no chosen
  primary source and this run's budget went to verifying the chosen topic
  instead; DB access (both `bin/query-progress` and direct
  `psql "$LEARNING_DB_URL"`) was not attempted this run per this run's own
  instructions (hard-blocked/gated every prior day since Day 8 except the
  Day 5/9/10 read-adjacent successes) — paced entirely from on-disk state
  (this file's own log, `python/lessons/`, `python/assets/nav.js`,
  `python/learning-records/` — still only the Day 1 baseline record, no
  completion/quiz record for any day 2-31).
  Taught: the three method shapes distinguished by first parameter — a
  plain instance method needing `self` (every method through Day 31);
  `@classmethod` receiving the class itself as `cls`, used as an alternative
  constructor (`Money.from_dollars("5.00")` beside plain `Money(cents=500)`),
  with the `cls(...)`-not-`Money(...)` convention explained via a subclass
  example so an inherited classmethod builds the subclass, not a hardcoded
  parent; and `@staticmethod`, needing neither `self` nor `cls`, framed as a
  plain function grouped inside a class purely for organization/lookup, with
  "delete `self` and see if the body still reads `self.anything`" as the
  concrete test for reaching for it. Tied `dict.fromkeys(...)` and
  `datetime.fromtimestamp(...)` in as already-familiar classmethod examples
  the learner has used without the label attached. Bridged from SQL per the
  baseline record: one `CREATE TABLE` shape but several real construction
  paths to a row (CSV import, form submission, copy-with-one-field-changed),
  introduced before any Python in the top callout, not from a pandas
  analogy.
  No-pandas rule: zero pandas/NumPy API calls anywhere in the practice file
  (grepped case-insensitively — zero hits, no imports at all needed); exactly
  one hit in the lesson — one contrast sentence/callout (titled "Where
  pandas goes from here") naming `pd.DataFrame.from_dict(...)` and
  `pd.DataFrame.from_records(...)` as classmethod alternative constructors
  at bigger scale, without demonstrating any pandas API, placed once after
  section 4/the interview callout, matching the hard-rule section above.
  Practice file `practice/32_classmethod_and_staticmethod.py` (4 exercises:
  completing `Money.from_dollars` as a `@classmethod` alternative
  constructor, completing `parse_amount()` to use the already-written
  `Money.is_valid_dollars` `@staticmethod` as a guard, confirming a
  `GiftCard(Money)` subclass's inherited `from_dollars` builds a `GiftCard`
  instance rather than a `Money` via the `cls(...)` convention, and a
  "classify three unlabeled method bodies" exercise reading commented-out
  code shapes to return which of instance/classmethod/staticmethod each
  needs) needed no on-disk fixtures. Followed this course's standard
  defensive pattern against the Ellipsis-at-module-level bug family flagged
  repeatedly since Days 11/12/17/28/29/30: every class/decorator line stays
  fully definable, with unsolved `...` living strictly inside method/function
  bodies, so an unsolved function returns `None` instead of raising at
  import/decoration time. Verified in a scratch dir
  (`.scratch_py32_verify/`, created under the repo root and removed after
  use, per every prior day's `/tmp`-is-out-of-bounds precedent — confirmed
  again this run when a bare `mkdir /tmp/...` was blocked outright): the
  shipped (unsolved) copy, run via plain `uv run python3` (no `--with`
  needed), both from a scratch copy and from its real `practice/` path with
  the documented command, printed four clean ✗ lines with no traceback each
  time; a separately solved copy (every `...`/TODO filled in directly in the
  scratch copy) printed all four ✓ and the "All green" tally. No bugs found
  during verification — both passes succeeded on the first attempt.
  Glossary: added a Day 32 section to `reference/glossary.html` (`method
  decorator`) after confirming via grep that the term collided with no Day
  1-31 entry — deliberately did **not** re-glossary `@classmethod`/
  `@staticmethod`/`cls` as separate rows, explaining them inline via
  `<code>` and folding the general mechanism into the one new `method
  decorator` entry, matching this course's no-duplicate-glossary-row
  convention (the same choice Day 30 made for `__repr__`/`__eq__`/`__lt__`
  and Day 31 for `hashable`/`key`). The 1 new `<dfn data-en` tag in the
  lesson body matches the 1 new glossary row exactly (confirmed by count).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (splitting the quiz block into its question `<div>`s via regex and
  counting `.split()` words per `<button class="opt">` line, run from a
  scratch dir via `uv run python3`) and mismatched on the first draft for
  all five questions (Q1 6/8/8, Q2 10/9/9, Q3 11/10/10, Q4 10/13/10, Q5
  8/9/8). Each mismatched question went through one rewrite-and-recount
  round, re-running the script after every edit, until every option matched
  (Q1 8/8/8, Q2 9/9/9, Q3 10/10/10, Q4 10/10/10, Q5 8/8/8) — Q3's first
  rewrite attempt undershot at 11 words and needed a second pass. Re-verified
  with a second, independently-written script (extracting every
  `<button class="opt">` in document order across the whole file, ignoring
  the per-question `<div>` wrapper, then grouped in threes) run against the
  final file — independently confirmed all 15 options (5 questions × 3
  options) land on their target counts before shipping. Registered in
  `assets/nav.js` with `date: "2026-08-29"`.
  **DB access:** per this run's confirmed-facts brief, both the
  `bin/query-progress` read path and direct `psql "$LEARNING_DB_URL"` were
  not attempted this run — documented as blocked on every prior day since
  Day 8 except the inconsistent Day 5/9/10 successes, so this run paced
  entirely from on-disk state (this file's own log, `python/lessons/`,
  `python/assets/nav.js`, `python/learning-records/` — still only the Day 1
  baseline record).
  `bin/record-progress python lesson_generated --day 32 --lesson
  0032-classmethod-and-staticmethod.html --detail '{"by":"headless"}'` was
  run once after shipping as a single standalone command, per this run's
  confirmed-working write-path convention.
  **Next-day note:** with `@classmethod`/`@staticmethod` now taught, the
  object-model/dunder thread opened on Day 30 (dunder methods, `@property`,
  `__hash__`) and extended through method shapes today has no further
  explicitly-named-but-untaught mechanism left in `MISSION.md`/`PLAN.md`
  that this run's grepping surfaced. Day 33 should re-scan
  `MISSION.md`/`PLAN.md`/`RESOURCES.md` fresh for a still-open, textually-
  grounded gap before falling back to an unnamed Phase 3 direction, and
  should retry `WebSearch` for `RESOURCES.md`'s still-unresolved "Gaps"
  (Python interview prep, a FastAPI project-layout reference) given
  `WebFetch` has now succeeded on Days 30 and 31. Still no
  `lesson_completed`/quiz/kata outcome record exists for any day — no
  reported weak spot to target.
- 2026-08-30 — **Day 33 generated** (`lessons/0033-enum.html`), an
  automated headless daily-generation run. Idempotency: confirmed before
  writing anything that no `python/lessons/0033-*.html` (or higher-numbered)
  file existed and no `n: 33`/`date: "2026-08-30"` entry existed anywhere in
  `assets/nav.js` — highest existing lesson on disk was
  `0032-classmethod-and-staticmethod.html` dated 2026-08-29, so generation
  proceeded as Day 33, not a re-run.
  Topic selection: per Day 32's own closing note, re-scanned
  `MISSION.md`/`PLAN.md`/`RESOURCES.md` fresh rather than assuming any prior
  round's gap analysis still held. Checked every named item on `PLAN.md`'s
  Phase 2 spine (2a: exceptions, modules/imports, environments/pyproject,
  pytest, decorators, pathlib, datetime/timezones, logging; 2b: FastAPI
  handlers, pydantic, request/response schemas, dependency injection,
  async/await, PostgreSQL, httpx testing) against `python/lessons/*.html` by
  filename and content grep — every single one is already taught (Days
  8-32), confirming the plan's explicit spine is now fully exhausted, not
  just the object-model/dunder thread Day 32 closed. Also grepped for
  mechanisms named in `MISSION.md`'s "Success looks like" section but never
  confirmed taught: `enum`/`Enum` came back with zero hits anywhere in
  `python/lessons/` or `python/practice/` (Day 17's pydantic/Day 16's FastAPI
  status-code lessons use plain ints and strings throughout, never
  `Enum`), while `match`/`__slots__`/`Protocol` also came back with zero
  hits but are not named anywhere in `MISSION.md`/`PLAN.md`, making `enum`
  the more textually-grounded pick of the four. Picked `enum.Enum`: it is a
  common, practically important stdlib mechanism for a closed set of named
  values (order/request status, priority levels), a real gap FastAPI
  path/query-parameter validation (Day 16) and pydantic fields (Day 17)
  both silently left open by using plain strings/ints throughout, and fits
  "rounding out the language" squarely. Did not re-attempt `RESOURCES.md`'s
  still-unresolved "Gaps" (Python interview prep, FastAPI project-layout
  reference) this run since `enum` is the more concretely-grounded pick
  with an obvious primary source already listed in this course's own docs
  citation pattern; those two gaps remain open for a future day. DB access
  (`bin/query-progress` and direct `psql "$LEARNING_DB_URL"`) was not
  attempted this run per this run's own instructions — paced entirely from
  on-disk state (this file's own log, `python/lessons/`, `python/assets/
  nav.js`, `python/learning-records/` — still only the Day 1 baseline
  record, no completion/quiz/kata outcome record for any day 2-32).
  Web-lookup: used `WebFetch` against `docs.python.org/3/library/enum.html`
  before writing anything — succeeded, returning class-syntax definition,
  `auto()`'s per-variant numbering behavior, member equality/identity
  (`Color.RED is Color.RED`), by-value/by-name lookup (`Color(1)` /
  `Color['RED']`), `IntEnum`/`StrEnum`, and documented guidance on when to
  reach for an enum over a plain constant — all used directly in sections
  2-3 of the lesson. Added a new `RESOURCES.md`-style citation to the
  lesson's "Go deeper" pointing at this same URL; did not edit
  `RESOURCES.md` itself (out of scope — read-only per this run's own
  instructions did not extend to it, and the existing "Knowledge — the
  language" section's docs-first citation pattern already covers adding new
  stdlib-doc links implicitly via each lesson's own "Go deeper").
  Taught: section 1 the problem live (a plain string/int status field
  accepting a typo like `"shiped"` silently, with nothing listing the valid
  set in one place); section 2 `enum.Enum` class-syntax definition,
  `.name`/`.value`, and the deliberate `Status.SHIPPED != "shipped"`
  inequality — a misspelled member raises `AttributeError` immediately
  instead of a silent wrong string; section 3 `auto()`, `list(Enum)`
  iteration in definition order (tied back to Day 5's iteration protocol),
  and the two lookup directions (`Status(2)` by value via call syntax,
  `Status["SHIPPED"]` by name via index syntax); section 4 replacing a
  string-based `if/elif` parameter-checking function with an `Enum`-typed
  one, bridged to Day 18's "type hints are the contract" idea and Day 16's
  FastAPI path/query parameters, which validate an `Enum` type hint
  automatically with a `422` for anything outside the set. Bridged from SQL
  per the baseline record: a `CHECK (status IN (...))` constraint or a
  small lookup table a column foreign-keys against, introduced before any
  Python in the top callout, not from a pandas analogy.
  No-pandas rule: zero pandas/NumPy/`pd.`/`np.` hits in the practice file
  (grepped case-insensitively — zero hits, only a plain `from enum import
  Enum, auto` stdlib import); exactly one hit in the lesson — one contrast
  sentence/callout (titled "Where pandas goes from here") naming a pandas
  `Categorical` column as the same closed-set-of-values idea at column
  scale, without demonstrating any pandas API, placed once after section
  4/the interview callout, matching the hard-rule section above.
  Practice file `practice/33_enum.py` (4 exercises: defining a `Status`
  `Enum` with explicit string values, writing `mark_shipped()` to confirm a
  real `Status.SHIPPED` member matches while the lookalike string
  `"shipped"` does not, an `auto()`-based `Priority` `Enum` confirming
  definition-order iteration via `list(Priority)`, and `lookup_both()`
  exercising both by-value call syntax and by-name index syntax) needed no
  on-disk fixtures. Followed this course's standard defensive pattern
  against the Ellipsis-at-module-level bug family: both `Enum` class bodies
  (`Status`, `Priority`) assign `...` directly as each member's placeholder
  value rather than leaving any line undefinable — confirmed this does not
  raise at class-definition time (`Enum` treats members sharing an equal
  value as aliases, not an error), with all other unsolved `...`/TODOs
  living strictly inside function bodies (`mark_shipped`, `lookup_both`).
  Verified in a scratch dir (`.scratch_py33_verify/`, created under the
  repo root and removed after use, per every prior day's `/tmp`-is-out-of-
  bounds precedent): the shipped (unsolved) copy, run via plain `uv run
  python3` (no `--with` needed), both from a scratch copy and from its real
  `practice/` path with the documented command, printed four clean ✗ lines
  with no traceback each time; a separately solved copy (every `...`/TODO
  filled in directly in the scratch copy) printed all four ✓ and the "All
  green" tally. No bugs found during verification — both passes succeeded
  on the first attempt; also spot-checked that all three `Status` members
  sharing the placeholder value `...` before being solved does not itself
  crash class definition, confirming the defensive pattern holds for `Enum`
  specifically, not just plain classes/functions as in prior days.
  Glossary: added a Day 33 section to `reference/glossary.html` (`enum`)
  after confirming via grep that the term collided with no Day 1-32 entry —
  deliberately did **not** re-glossary `auto()`, `.name`/`.value`,
  `IntEnum`/`StrEnum`, or the by-value/by-name lookup syntax as separate
  rows, explaining them inline via `<code>` and folding the general
  mechanism into the one new `enum` entry, matching this course's
  no-duplicate-glossary-row convention (the same choice Day 30 made for
  `__repr__`/`__eq__`/`__lt__`, Day 31 for `hashable`/`key`, and Day 32 for
  `@classmethod`/`@staticmethod`/`cls`). The 1 new `<dfn data-en` tag in the
  lesson body matches the 1 new glossary row exactly (confirmed by count).
  Quiz: 5 questions. Word counts were checked with a small Python script
  (regex-splitting the quiz block into its five question `<div>`s and
  counting `.split()` words per `<button class="opt">` line, run from a
  scratch dir via `uv run python3`) and mismatched on the first draft for
  all five questions (Q1 11/9/10, Q2 8/9/10, Q3 10/11/11, Q4 11/10/10, Q5
  10/11/11). Each mismatched question went through one to two
  rewrite-and-recount rounds — Q4 in particular overshot to 13/11/10 on its
  first rewrite attempt before a second pass landed all three options at
  11 — re-running the script after every edit, until every option matched
  (Q1 11/11/11, Q2 10/10/10, Q3 11/11/11, Q4 11/11/11, Q5 11/11/11).
  Re-verified with a second, independently-written script (document-order
  `<button class="opt">` extraction via regex across the whole file,
  ignoring the per-question `<div>` wrapper entirely, then grouped in
  threes) run against the final file — independently confirmed all 15
  options (5 questions × 3 options) land on their target counts before
  shipping. Registered in `assets/nav.js` with `date: "2026-08-30"`.
  **DB access:** per this run's own instructions, both the
  `bin/query-progress` read path and direct `psql "$LEARNING_DB_URL"` were
  not attempted this run — documented as blocked on every prior day since
  Day 8 except the inconsistent Day 5/9/10 successes, so this run paced
  entirely from on-disk state as described above under topic selection.
  `bin/record-progress python lesson_generated --day 33 --lesson
  0033-enum.html --detail '{"by":"headless"}'` was run once after shipping
  as a single standalone command and **succeeded**: `recorded:
  python/lesson_generated day=33 lesson=0033-enum.html`.
  **Next-day note:** with `PLAN.md`'s entire Phase 2 spine (2a and 2b) now
  fully taught and the object-model/dunder/method-shapes thread (Days
  30-32) closed, Day 34 has no single named-but-untaught mechanism left in
  `PLAN.md` itself — the plan's own text says "revisit this plan when
  Phase 2a ends," which has now happened, so Day 34 should treat this as
  entering an unnamed Phase 3 and lean on `RESOURCES.md`'s still-unresolved
  "Gaps" (Python interview prep, a FastAPI project-layout reference — both
  named since Day 28/25 respectively, still with no chosen primary source)
  as the most textually-grounded next targets, attempting a fresh
  `WebSearch` for each given `WebFetch` has now succeeded on Days 30-33.
  Other live candidates if those searches come up empty: `match`/case
  structural pattern matching (PEP 634, never mentioned anywhere in this
  course), `__slots__` (a real Day 1/7 follow-on for memory/attribute-typo
  tradeoffs), or a testing-focused retrieval day revisiting `pytest`
  fixtures/parametrize (Day 11) now that FastAPI/httpx testing exists too.
  Still no `lesson_completed`/quiz/kata outcome record exists for any
  day — no reported weak spot to target.

