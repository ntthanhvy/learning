# Working Notes

## User preferences
- **Language:** first language is Vietnamese; learned some CS concepts in Vietnamese. English jargon (e.g. "delegate") creates comprehension gaps. EVERY lesson must: (1) mark each new jargon term as `<dfn data-en="software-context English explanation" data-vn="dev-style Vietnamese">term</dfn>` and include `../assets/gloss.js` — this renders a click popup, English first, Vietnamese second; (2) NO inline translations in sentence flow — user explicitly asked to drop them (2026-07-07); popups only; (3) add new terms to reference/glossary.html (columns: Term / In software / Tiếng Việt dev-style — mixed EN–VN as devs actually speak, not textbook translation; many terms are "giữ nguyên"); (4) prefer plain words when the jargon isn't the thing being taught. User can ask questions in Vietnamese anytime.
- Already writes working Go — do NOT re-teach syntax basics; teach depth, idiom, and "why."
- 2–3 hours/day available, one-week intensive (2026-07-07 → 2026-07-13).
- Motivation is dual: backend services at work + job hunting. Lessons should flag interview-relevant angles explicitly.
- Workspace deliberately placed at ~/learning/go (user chose dedicated dir over home).

## Course design decisions
- **Site navigation (2026-07-07):** index.html is the course home; assets/nav.js is the single source of truth for the schedule and injects a sticky nav bar on every page. Date-based unlocking: lesson chips are locked 🔒 until their date (user explicitly wants lessons inaccessible before their day — do NOT open or link future lessons early). References/glossary always open. Maintenance: every new HTML page must include `<script src="../assets/nav.js"></script>`; new reference sheets get registered in nav.js REFS. Pre-assigned lesson filenames (already in nav.js LESSONS): 0003-errors-as-values, 0004-goroutines-channels-select, 0005-context-sync-http-server, 0006-data-modeling-postgres, 0007-queries-from-go, 0008-testing-tooling-capstone — use these exact names when generating each day's lesson.
- Practice sections: full file-level walkthroughs (exact commands, tree diagram, one code block per file with imports given, TODOs only on the taught concept). Terse bullets don't work — see learning-records/0003. Compile-check every scaffold in the scratchpad before shipping a lesson.
- User cannot run Docker locally → course database is a hosted Neon free-tier Postgres (connection string in env var `LINKSHORT_DB_URL`, never committed). Day 7 testing approach adjusted: integration tests hit a dedicated Neon branch instead of testcontainers.
- 2026-07-07 revision: data modeling + queries (PostgreSQL) squeezed into the 7 days at user request. Old Day 5 (generics) and Day 6 (net/http) merged/redistributed: server essentials moved into Day 4; Days 5–6 are now the data track; generics taught in context via pgx generics on Day 6. User is comfortable with SQL — skip syntax, teach depth (constraints, indexes, EXPLAIN, transactions).
- Running project across the week: **"linkshort"** — a URL-shortener HTTP service built with stdlib only. Each day's feature work exercises that day's topic. Lives at ~/learning/go/project/linkshort (user creates it Day 1).
- Go version context: Go 1.26 is current (Feb 2026). Highlight modern features: 1.22 ServeMux routing, 1.23 range-over-func iterators, 1.26 generics self-reference & `go fix` modernizers.
- Plan lives in PLAN.md; lessons are generated one per day so each stays in the zone of proximal development based on the previous day's learning records.

## Progress tracking (Neon DB, added 2026-07-08)
- Learning progress persists in Neon Postgres, table `course_progress`, shared by all
  three courses (go/rust/backend). Connection string ONLY in `~/.config/learning/db.env`
  (`LEARNING_DB_URL`, chmod 600) — never in a workspace file, never committed. (This is
  a separate concern from LINKSHORT_DB_URL, the Day 5 practice database — though both
  may point at the same Neon project.)
- Record events: `~/learning/bin/record-progress go <kind> [--day N] [--lesson FILE]
  [--detail '{...}']` — kinds: lesson_generated, lesson_completed, quiz, kata, review,
  note. Record lesson_completed (outcome + gaps in detail) whenever the user reports
  finishing a day.
- Nightly generation: launchd `com.ntthanhvy.daily-lessons` at 06:00 runs
  `~/learning/generate-daily-lessons.sh` (prompt: `~/learning/daily-lessons-prompt.md`),
  which reads recent progress rows per course before authoring.
- 2026-07-11 (Day 5 generation): the Neon progress DB and all shell tool access
  requiring interactive approval were unavailable in this headless run (sandboxed
  agent session, no user present to approve) — pacing was decided from
  learning-records + project file state alone, and `lesson_generated` could not be
  recorded via `bin/record-progress`; record it manually once DB access is back.
  `project/linkshort` on disk showed Day 2 done (LoggingStore, %w-wrapped `resolve`,
  comma-ok `Get` fix all present) but no `checker.go`/`race_test.go` (Day 3) or
  `server.go`/`middleware.go` (Day 4) — those two days' practice looks unstarted.
  Day 5 was written to not depend on either: `PostgresStore` only extends the
  `link` package and swaps one line in `main`'s existing CLI wiring, not the Day 4
  HTTP surface. Also couldn't run `go vet`/`go build` in a scratch dir to
  compile-check the lesson's Go/pgx code (same approval restriction) — the
  scaffold was written carefully against known-correct pgx v5 API but is unverified
  by a compiler this round; verify it compiles before/while doing the practice.
- 2026-07-12 (Day 6 generation): direct `psql "$LEARNING_DB_URL" ...` and reading
  `~/.config/learning/db.env` were both blocked in this headless run (shell-variable
  expansion and out-of-workspace file reads are disallowed for this session), so no
  prior-progress SELECT was possible — paced from learning-records + project file
  state alone, same as 2026-07-11. `bin/record-progress`, however, *did* work (it
  sources the DB env internally rather than the caller expanding it), so Day 6's
  `lesson_generated` event was recorded successfully. `project/linkshort` still had
  no `postgres.go` on disk (Day 5 practice looks unstarted, no completion record
  either) — Day 6's lesson opens with a "Step 0" that hands over a complete, working
  copy of Day 5's `postgres.go` so today doesn't block on it. Unlike 2026-07-11, `go
  vet`/`go build` access WAS available this round — the full `link/postgres.go`,
  `link/queries.go`, and `main.go` scaffold was compile-checked clean in a scratch
  dir (confirmed pgx v5's `RowToStructByName` matches columns to struct fields
  case-insensitively, underscores stripped, by reading its source directly) before
  shipping.
- 2026-07-13 (Day 7 generation, capstone): DB access (`psql`, `bin/record-progress`)
  and the `go`/`cargo`/`uv` toolchains were all blocked in this headless run (each
  requires interactive approval; no user present) — paced from learning-records +
  project file state alone, same limitation as 2026-07-11/12; `lesson_generated`
  could not be recorded, record it manually once access is back. `project/linkshort`
  on disk still only shows Day 1–2 (`link/` package: `link.go`, `memstore.go`,
  `logging.go`, `store_test.go`); Days 3–6 (goroutines, HTTP server, Postgres store,
  queries) look unstarted in the actual project even though each day's lesson
  handed over working code. Day 7's Step 0 therefore hands over Day 4's server
  files (`middleware.go`, `server.go`, both TODOs filled in) and Day 5–6's
  `postgres.go` again, plus a **new** `main.go` that's the first place the HTTP
  server and the Postgres store are wired together in one file. `go vet`/`go build`
  were not available this round to compile-check the new `main.go`, `server_test.go`,
  `postgres_integration_test.go`, or `bench_test.go` — they're written carefully
  against the exact, previously-shipped and already-referenced code from Days 4–6,
  but are unverified by a compiler this round; verify with `go vet ./...` before/while
  doing the Day 7 practice.
