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
