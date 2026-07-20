# Working Notes

## User preferences (carried over from ~/learning/backend/NOTES.md, 2026-07-09)
- **Language:** first language is Vietnamese. EVERY lesson must: (1) mark each new jargon term as `<dfn data-en="software-context English explanation" data-vn="dev-style Vietnamese">term</dfn>` and include `../assets/gloss.js`; (2) NO inline translations in sentence flow — popups only; (3) add new terms to reference/glossary.html (columns: Term / Tiếng Việt dev-style / In software — mixed EN–VN as devs actually speak; many terms are "giữ nguyên"); (4) prefer plain words when the jargon isn't the thing being taught. User can ask questions in Vietnamese anytime.
- Frontend-heavy fullstack dev, **strong SQL** (work + Go week Days 5–6). The fastest route into the zone of proximal development here is the **SQL bridge**: teach every pandas operation as "you already know this in SQL; here is the pandas spelling and where the mental model differs."
- Python level: working but basic (assumption — see learning-records/0001). Gloss Python idioms (comprehensions, lambdas, unpacking) when lessons use them.

## Course design decisions (2026-07-09)
- **Purpose is interview-readiness** (see MISSION.md). Every lesson should include an `.interview` callout box (styled by course.css): how this topic gets asked in interviews and how to answer out loud. This course's lessons are both *do* (write the code) and *say* (explain the why).
- **Pacing:** light ~20 min/day while Go (→Jul 13) / Rust (→Jul 14) weeks run; from ~Jul 15 this becomes a main track and can deepen. Day 1 = 2026-07-09.
- **Assets forked from the backend course** (course.css with violet accent `#5a3d99` / dark `#b39ddb`; gloss.js verbatim; quiz.js with the course-regex extended to `data`; nav.js retitled, no date-locking — open-ended like backend).
- **Practice runs via uv, no venv:** Python 3.14 is present but pandas is NOT installed system-wide. All practice files run with `uv run --with pandas python3 practice/<file>.py`. Practice files live in `./practice/`, are self-checking (asserts + ✓/✗ output) so the feedback loop is immediate, and are referenced from their lesson.
- **Site navigation:** same pattern as backend — every HTML page includes `<script src="../assets/nav.js"></script>` (end of body); every new lesson/reference must be registered in `assets/nav.js` LESSONS/REFS. Course is registered on the landing page in `~/learning/assets/courses.js`.
- **Progress DB:** course id is `data`. The `course_progress_course_check` constraint in Neon was widened on 2026-07-09 to `('go','rust','backend','data')`. Record events with `~/learning/bin/record-progress data <kind> ...`; same idempotency rule as backend for the 06:00 job (skip if a `lesson_generated` row for course=data exists today, or a lesson was added to nav.js today).
- **Daily generation:** registered as course 4 in `~/learning/daily-lessons-prompt.md` (06:00 launchd job `com.ntthanhvy.daily-lessons`).
- **Curriculum spine (front-loaded by interview frequency):** 1) tables-not-loops / vectorization + SQL bridge → 2) load & inspect real files (dtypes, index) → 3) missing data & cleaning → 4) groupby split–apply–combine → 5) merge/join → 6) reshape (pivot/melt) → 7) rank/cumulative/window-ish → 8) method chaining & pipeline shape (ETL framing) → then timed drills (LeetCode pandas / StrataScratch) with review lessons targeting recorded weak spots. Adjust order freely based on learning records.
- 2026-07-11 generation (Lesson 3): Neon DB and shell commands needing interactive
  approval (psql, `uv run`, `bin/record-progress`) were unavailable in this headless
  run — no user present to approve in a sandboxed agent session. No learning record
  exists yet beyond the baseline, so Lesson 3 was generated conservatively from
  Lesson 2's own teaser ("missing data & cleaning... just fill with 0 is usually
  wrong") plus its file state, not a reported outcome. Practice file
  `03_missing_data_cleaning.py` was hand-verified against the fixture's known values
  (median of the 5 non-null amounts = 99.9, one NaT row = order_id 4) but could NOT
  actually be executed with `uv run --with pandas` this round — run it once and
  confirm the ✓/✗ output before trusting it blindly. `lesson_generated` could not be
  recorded; do it manually once DB access is back.
- 2026-07-12 generation (Lesson 4): direct `psql "$LEARNING_DB_URL" ...` and reading
  `~/.config/learning/db.env` were both blocked in this headless run (shell-variable
  expansion and out-of-workspace file reads disallowed for this session) — still no
  learning record beyond the baseline, so Lesson 4 continues the conservative
  pattern from the curriculum spine (groupby, per Lesson 3's own teaser) rather than
  a reported outcome. `uv run --with pandas` access WAS available this round though:
  `practice/04_groupby_split_apply_combine.py` was actually executed — confirmed it
  prints all ✗ with the shipped `...` placeholders, then all ✓ once solved, against
  the real `orders_raw.csv` fixture (An 162.0/3 orders, Binh 215.5/2, Chi 99.9/1).
  `bin/record-progress` also worked (sources the DB env internally) — `lesson_generated`
  was recorded for the first time since Lesson 1's baseline.
- 2026-07-13 generation (Lesson 5): DB access (`psql`, `bin/record-progress`) and
  `uv run --with pandas` were all blocked in this headless run (each requires
  interactive approval; no user present) — still no learning record beyond the
  baseline, so Lesson 5 continues the conservative pattern from the curriculum
  spine (merge/join, per Lesson 4's own teaser) rather than a reported outcome.
  New fixture added: `practice/data/customers.csv` (An/Binh/Danh + region),
  deliberately mismatched against `orders_raw.csv`'s customers (An/Binh/Chi) so
  the practice exercises have a real "customer with no orders" (Danh) and a real
  "order with no customer record" (Chi, order_id 4) to find via
  `indicator=True`/`_merge`. Hand-traced against both CSVs: inner join = 5 rows
  (Chi's order excluded), `never_ordered == ["Danh"]`, `orphan_order_ids == [4]` —
  but `practice/05_merge_and_join.py` could NOT actually be executed with
  `uv run --with pandas` this round. Run it once and confirm the ✓/✗ output
  before trusting it blindly; `lesson_generated` could not be recorded either,
  do it manually once DB access is back.
- 2026-07-14 generation (Lesson 6): direct `psql "$LEARNING_DB_URL" ...` reads
  were still blocked in this headless run (shell-variable expansion of that
  specific name is disallowed for this session), so no `course_progress` rows
  could be read — still no learning record beyond the baseline, so Lesson 6
  continues the conservative pattern from the curriculum spine (reshape,
  pivot/melt, per Lesson 5's own teaser) rather than a reported outcome.
  `uv run --with pandas` and `bin/record-progress` BOTH worked this round
  (invoked directly, not through a wrapper script) — `practice/06_reshape_pivot_melt.py`
  was actually executed in a scratch copy (`.scratch/`, deleted after): the
  shipped (unsolved) version printed all ✗, and a solved version (pivot_table
  then melt on the pre-cleaned 4-row slice of `orders_raw.csv`) printed all ✓
  before the unsolved file was copied into `practice/`. `lesson_generated` was
  recorded successfully.
- 2026-07-15 generation (Lesson 7): per MISSION.md this course "becomes a main
  track" from today, but with still no `lesson_completed` record beyond the
  Lesson 1 baseline, there's no reported outcome to size a bigger lesson
  against — so this round keeps the established ~20 min/day format and the
  curriculum spine's next topic (rank & cumulative operations, per Lesson 6's
  own teaser) rather than unilaterally deepening pace with no user in the
  loop; revisit pace in an interactive session. `uv run --with pandas` and
  `bin/record-progress` both worked this round (invoked directly): the shipped
  (unsolved) `practice/07_rank_cumulative.py` was executed in a scratch dir
  and printed all ✗ against the real `orders_raw.csv` fixture, then a solved
  version (groupby+rank with method="first", groupby+cumsum after sort_values
  by date) printed all ✓ before the unsolved file was copied into `practice/`.
  `lesson_generated` was recorded successfully. Direct `psql "$LEARNING_DB_URL"
  ...` was still blocked (shell-variable expansion of that name disallowed for
  this sandboxed session), so no `course_progress` rows could be read.
- 2026-07-16 generation (Lesson 8): direct `psql "$LEARNING_DB_URL" ...` reads
  were still blocked in this headless run (referencing that exact variable
  name in a typed command is disallowed for this sandboxed session), so no
  `course_progress` rows could be read — still no learning record beyond the
  Lesson 1 baseline, so Lesson 8 continues the conservative pattern from the
  curriculum spine (method chaining & pipeline shape, per Lesson 7's own
  teaser) rather than a reported outcome. `uv run --with pandas` and
  `bin/record-progress` both worked this round (invoked directly): the shipped
  (unsolved) `practice/08_method_chaining_pipeline.py` was executed in a
  scratch dir and printed all ✗ against the real `orders_raw.csv` fixture
  (4 clean rows after dropping order_id 3/4, same slice as Lessons 6–7), then
  a solved version (chain + `.pipe()` reproducing Lesson 7's rank-1-per-customer
  result) printed all ✓ before the unsolved file was copied into `practice/`.
  `lesson_generated` was recorded successfully.
- 2026-07-17 generation (Lesson 9): direct `psql "$LEARNING_DB_URL" ...` reads
  and an ad-hoc read-only query script were both blocked in this headless run
  (same two distinct blocks as the backend course hit today — a hard
  content-level block on expanding that exact variable name, and a generic
  approval gate on running a novel script with no user present) — no
  `course_progress` rows could be read, still no learning record beyond the
  Lesson 1 baseline. The 8-lesson curriculum spine (see "Curriculum spine"
  above) finished with Lesson 8, and Lesson 8's own teaser already named the
  next phase — timed drills — so Lesson 9 starts that phase rather than
  inventing a new spine topic: three short interview-shaped problems (Nth-
  highest-per-group, merge-then-aggregate, and a named anti-join) recombining
  Lessons 4/5/7/8's patterns on the existing fixtures. `uv run --with pandas`
  and `bin/record-progress` (an existing, already-committed repo script) both
  worked when invoked directly this round — the shipped (unsolved)
  `practice/09_timed_drills.py` was executed in a scratch dir and printed all
  ✗, then a hand-written solved version printed all ✓ against the real
  `orders_raw.csv`/`customers.csv` fixtures, before the unsolved file was
  copied into `practice/`; `lesson_generated` was recorded successfully.
- 2026-07-18 generation (Lesson 10): direct `psql "$LEARNING_DB_URL" ...`
  reads were blocked in this headless run (network/credential commands need
  interactive approval; no user present) — still no `course_progress` rows
  readable, no learning record beyond the Lesson 1 baseline. Lesson 9's own
  teaser promised "a review pass shaped by however today's drills actually
  go," but with no drill-outcome signal available, guessing which pattern
  came back shakiest isn't possible — so Lesson 10 keeps building the drill
  library instead: three patterns not yet covered anywhere in Lessons 1–9
  (checked the glossary for existing terms first) — `value_counts()`, the
  `.str` accessor, and `nlargest()` contrasted against Lesson 9's per-group
  `rank()` pattern. `uv run --with pandas` worked directly this round: the
  shipped (unsolved) `practice/10_value_counts_str_nlargest.py` was executed
  in place and printed all ✗, then a solved version was executed in a
  scratch dir (`.scratch/data-lesson10/solved.py`, not shipped) against the
  real `orders_raw.csv`/`customers.csv` fixtures and printed all ✓ (An/Binh
  both value_counts to 2 clean orders each; North+South match `.str.contains
  ("th")`, West doesn't; nlargest(2) is Binh/180.0 then An/120.0, no ties).
  `bin/record-progress` also worked when invoked directly — `lesson_generated`
  was recorded for day 10.
- 2026-07-19 generation (Lesson 11): direct `psql "$LEARNING_DB_URL" ...`
  reads were blocked in this headless run (shell-variable expansion of that
  exact command is disallowed for this sandboxed session) — still no
  `course_progress` rows readable, no learning record beyond the Lesson 1
  baseline. Lesson 10's own teaser already named the next fresh pattern —
  `duplicated`/`drop_duplicates` and `pct_change` — so Lesson 11 ships exactly
  that (checked the glossary first, confirmed neither term existed yet)
  rather than guessing which drill came back shakiest with no signal to go
  on. Since `orders_raw.csv`/`customers.csv` have no real duplicate rows and
  editing the shared fixtures would risk earlier lessons' hand-traced values,
  Drills 1-2 use a small inline "double-submitted export" DataFrame built
  directly in the practice file instead of a new CSV; Drill 3 returns to the
  real `orders_raw.csv` clean slice for `pct_change()`. `uv run --with
  pandas` worked directly this round: the shipped (unsolved)
  `practice/11_duplicates_and_pct_change.py` was executed in a scratch dir
  (`.scratch/data-lesson11/`, deleted after) and printed all ✗ (had to wrap
  the Drill 3 two-line placeholder in try/except first — an unassigned
  `ordered = ...` followed by `ordered["col"] = ...` raised a TypeError on
  the Ellipsis before any checks could run, unlike the single-line
  placeholders elsewhere), then a solved version printed all ✓ against the
  real fixtures (An 120.0→42.0 = -0.65 pct_change, Binh 35.5→180.0 = 4.07,
  each customer's first order NaN; duplicated() flags rows 2 & 4 as repeats
  of row 0, drop_duplicates() leaves 3 rows keeping each first occurrence)
  before the unsolved file was copied into `practice/`. `bin/record-progress`
  also worked when invoked directly this round — `lesson_generated` was
  recorded for day 11.
- 2026-07-20 generation (Lesson 12, headless 06:00 run): direct `psql
  "$LEARNING_DB_URL" ...` reads and any shell-variable expansion of that name
  were blocked outright by this session's sandbox as an out-of-workspace
  credential read (working directory restricted to the repo root, not merely
  "needs interactive approval") — still no learning record beyond the Lesson 1
  baseline, so no drill-outcome signal to redirect pacing. Lesson 11's own
  teaser named the fallback explicitly ("otherwise, one more fresh pattern —
  apply() with a custom function, or cut()/binning"), and both were still
  absent from the glossary, so Lesson 12 ships both together on purpose: `apply
  (axis=1)` as the honest per-row escape hatch (building a formatted label from
  3 columns — a shape with no vectorized shortcut) paired against `pd.cut()`
  as the vectorized tool for the specific case people reach for `apply()` for
  wrongly (numeric binning). `uv run --with pandas` worked directly this
  round: the shipped (unsolved) `practice/12_apply_and_cut.py` was executed in
  a scratch dir (`.scratch/data-lesson12/`) and printed all ✗ (the `pd.cut`
  call needed a `try/except` around it, same reason as Lesson 11's Drill 3 —
  calling `pd.cut(bins=..., labels=...)` with literal `Ellipsis` arguments
  raises immediately, before the check functions can run), then a solved
  version printed all ✓ against the real `orders_raw.csv`/`customers.csv`
  clean 4-row slice (An/120.0/North→High, Binh/35.5/South→Low,
  Binh/180.0/South→High, An/42.0/North→Mid — bins=[0,40,100,200] chosen
  deliberately so all three labels appear at least once) before the unsolved
  file was copied into `practice/`. `bin/record-progress` also worked when
  invoked directly this round (from the repo root — an earlier `cd` into the
  scratch dir during the `uv run` step persisted across the session's shell
  state and had to be un-done first) — `lesson_generated` was recorded for
  day 12. Added `apply()` and `pd.cut()` to the glossary and registered
  Lesson 12 in nav.js. The `.scratch/data-lesson12/` directory could not be
  removed this round (an `rm -rf` on it was flagged as a workspace-directory
  removal requiring explicit approval unavailable in this headless session,
  unlike a plain flagless `cp` of individual files, which worked fine) — it's
  harmless leftover scratch state, same as the pre-existing `data-lesson7/8/9`
  and `backend-lesson11` directories already in `.scratch/`; a future
  interactive session can clean these up.
- 2026-07-21 generation (Lesson 13, headless run): direct `psql
  "$LEARNING_DB_URL" ...` reads were unreachable in this headless session
  (no interactive DB access available) — still no `course_progress` rows
  readable and no `lesson_completed`/quiz/kata outcome record beyond the
  Lesson 1 baseline, so no reported weak spot to target. Lesson 12's own
  teaser named the fallback explicitly ("otherwise one more fresh pattern —
  melt revisited, or a window-function-style rolling calculation"), so
  Lesson 13 takes that branch: `.rolling()` and `.expanding()`, the two
  members of Lesson 7's "window operations" family that were only ever
  linked out to (the pandas Window Operations user guide) and never
  actually taught — confirmed via grep that neither `.rolling(` nor
  `.expanding(` appears anywhere in `data/lessons/*.html` before today.
  Bridged from Lesson 7's `cumsum()`/`rank()`, contrasted rolling's
  fixed-size sliding window against expanding's ever-growing one
  (`expanding().sum()` == `cumsum()`), and mapped both to SQL's
  `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW` / `ROWS BETWEEN UNBOUNDED
  PRECEDING AND CURRENT ROW` frames. `uv run --with pandas` worked directly
  this round: the shipped (unsolved) `practice/13_rolling_and_expanding.py`
  was executed in a scratch dir (`.scratch/data-lesson13/`, deleted after —
  a plain `rm -rf` on it worked fine this round, unlike Lesson 12's) and
  printed all ✗, then a separate solved copy (`solved.py`, not shipped)
  printed all ✓ against the real `orders_raw.csv` clean 4-row slice: An's
  rolling(2) mean NaN then 81.0 (120.0, 42.0), Binh's NaN then 107.75
  (35.5, 180.0); An's expanding mean 120.0 then 81.0, Binh's 35.5 then
  107.75, both with no leading NaN — all hand-computed values matched
  before the unsolved file was left in place. `bin/record-progress` also
  worked when invoked directly this round — `lesson_generated` was recorded
  for day 13. Added `rolling window` and `expanding window` to the
  glossary and registered Lesson 13 in nav.js. Quiz options were rewritten
  once to equalize word counts per question (this course's convention) —
  double-checked with `wc -w` per option, not just eyeballed.
