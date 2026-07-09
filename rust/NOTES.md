# Teaching notes — Rust workspace

Standing rules carried over from the Go course (~/learning/go/NOTES.md), all confirmed
by the user there; they apply here identically.

## Language (critical)
- Jargon terms get click-popups: `<dfn data-en="..." data-vn="...">term</dfn>` + gloss.js.
  English **software-context explanation first**, then Vietnamese in dev-community mixed
  style ("giữ nguyên" where devs keep the English word). Textbook translations are out.
- **No inline translating** in sentence flow — popups only.
- New terms go into reference/glossary.html the same day they first appear.

## Lessons
- nav.js is the single source of truth for the schedule. Lessons unlock on their date —
  do NOT create, open, or link a future lesson before its day. Reference material and
  daily.html are always visible.
- Pre-assigned filenames: see PLAN.md. Register each lesson in assets/nav.js when authored.
- LEAN lessons (~60–90 min): this week runs parallel with the Go intensive. One concept
  cluster per day, cut everything optional.
- Use Go contrasts deliberately: "in Go you wrote X — Rust does Y because Z". The user is
  mid-Go-week; contrast is cheap transfer. (Go Day-1 linkshort code is the shared anchor.)
- Practice = full file-level walkthrough: exact commands, directory tree, complete given
  files, TODOs only on the concept being taught. Compile-verify every scaffold in the
  scratchpad (`cargo check && cargo test && cargo clippy`) before shipping.
- "Done when" is always three commands green: `cargo check` (or build), `cargo test`,
  `cargo run`. Keep it prominent — the testing habit isn't formed yet (Go LR-0005).

## Quizzes & the bank
- Quiz options: equal word count per option, no formatting clues; quiz.js shuffles.
- Every lesson ALSO ships its questions into assets/quiz-bank.js (day-tagged, stable ids
  like "d1-01") plus one kata entry (type:"kata", with hidden solution). The daily
  practice page samples from this bank — a lesson without bank entries is unfinished.
- Daily practice: daily.html + assets/srs.js (Leitner boxes, localStorage key
  "rust-srs-v1"). Starts Tue Jul 15, open-ended until the user says stop. During the week
  it doubles as review of unlocked days only.

## Publishing online
- User wants the quiz library "saved online". Plan: push this workspace to GitHub and
  serve via GitHub Pages (static, free for public repos). Instructions in README.md.
  Do NOT create the repo or push without the user asking — their call on public/private.
- Quiz progress lives in localStorage → per-browser. Fine for one learner; noted in README.

## Progress tracking (Neon DB, added 2026-07-08)
- Learning progress persists in a Neon Postgres table `course_progress` shared by all
  three courses (go/rust/backend). Connection string lives ONLY in
  `~/.config/learning/db.env` (env var `LEARNING_DB_URL`, chmod 600) — never in any
  workspace file, never committed.
- Record events with `~/learning/bin/record-progress <course> <kind> [--day N]
  [--lesson FILE] [--detail '{...}']`; kinds: lesson_generated, lesson_completed, quiz,
  kata, review, note. Record a lesson_completed row (with outcome + gaps in detail)
  every time the user reports finishing a day's practice.
- Nightly generation (launchd job `com.ntthanhvy.daily-lessons`, 06:00, script
  `~/learning/generate-daily-lessons.sh`, prompt `~/learning/daily-lessons-prompt.md`)
  reads the last 20 progress rows per course and shapes recall questions and pacing
  from recorded gaps and scores.

## Learner profile shortcuts
- Zero Rust. One week into Go. Pointer/memory model was blurry in Go (Go LR-0004) —
  ownership lessons need explicit memory diagrams, don't assume the stack/heap picture.
- Practice instructions must be file-level concrete (Go LR-0003) — terse steps failed.
- Browser → DB sync: quiz.js and srs.js POST answers (best-effort, silent-fail) to the
  local helper `progress-sync` (Go server, ~/learning/bin/progress-sync, 127.0.0.1:8477),
  which holds the DB creds and inserts into course_progress. Pages stay credential-free
  and publishable. Helper persisted by launchd `com.ntthanhvy.progress-sync`.
- 2026-07-10 (Day 3 generation): DB unreachable from the headless generator run, so
  pacing was decided from learning-records + project file state alone. `linkshort-rs/src/main.rs`
  still showed Day 1's found/loop `Get` arm with no `print_link` extraction and no
  `.clone()`-triggered-E0382/E0502 experiments — Day 2's practice looks unstarted or
  unfinished. Day 3 was written to open gently and work directly on the actual current
  file (not the post-Day-2 state PLAN.md assumes), noting both possible starting points
  in the practice steps. If Day 2's practice does get done later, verify it still lines
  up with Day 3's `find_link` refactor.
