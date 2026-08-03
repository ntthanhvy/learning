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
