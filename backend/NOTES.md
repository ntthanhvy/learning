# Working Notes

## User preferences (carried over from ~/learning/go/NOTES.md, 2026-07-07)
- **Language:** first language is Vietnamese. EVERY lesson must: (1) mark each new jargon term as `<dfn data-en="software-context English explanation" data-vn="dev-style Vietnamese">term</dfn>` and include `../assets/gloss.js`; (2) NO inline translations in sentence flow — popups only; (3) add new terms to reference/glossary.html (columns: Term / In software / Tiếng Việt dev-style — mixed EN–VN as devs actually speak; many terms are "giữ nguyên"); (4) prefer plain words when the jargon isn't the thing being taught. User can ask questions in Vietnamese anytime.
- Frontend-heavy fullstack dev — lessons should *bridge from frontend concepts* (state, props, rendering) to backend equivalents; that mapping is the fastest route into their zone of proximal development.
- Comfortable with SQL syntax and joins — never teach basic SQL.

## Course design decisions
- **Daily auto-generation (2026-07-08):** a launchd job (`com.ntthanhvy.daily-lessons`, plist in ~/Library/LaunchAgents) runs ~/learning/generate-daily-lessons.sh at 06:00 local, which runs headless `claude -p` with ~/learning/daily-lessons-prompt.md to generate the day's lesson for go/, rust/, and backend/ (idempotent — skips a course if today's lesson is already in its nav.js). Log: ~/learning/.daily-gen.log. If the Mac is asleep at 06:00 launchd fires on wake; if it was powered off, run the script manually.
- **Pacing (2026-07-07):** runs in parallel with Go week (Jul 7–13) and Rust week (Jul 8–14) as a *light touch* track: ~20 min/day, one concept lesson — terminology and mental models, no heavy practice until the intensives end (~Jul 15). Revisit pace and mission then.
- **Division of labor with Go week:** Go week Days 5–6 teach Postgres *practice* (constraints, indexes, EXPLAIN, transactions, pgx). This course teaches the *conceptual frame* (how to think about data modeling, API design, runtime behavior, auth/ops). Cross-link rather than duplicate.
- Examples in Go + PostgreSQL (user's work stack and Go-week stack).
- Assets forked from the Go course (course.css with copper accent instead of teal, gloss.js, quiz.js verbatim).
- **Site navigation (added 2026-07-08 at user request):** index.html is the course home; assets/nav.js injects the sticky nav bar and renders the home lists. Unlike the Go course there is NO date-locking — lessons are open-ended and generated on demand. Maintenance: every new HTML page must include `<script src="../assets/nav.js"></script>` (end of body), and every new lesson/reference must be registered in nav.js LESSONS/REFS.
- Four scope tracks chosen by user (2026-07-07): data modeling & schema design; API & service design; backend runtime concepts; auth/security/ops.
- **2026-07-08 generation note:** no learning record existed for Lesson 1's outcome (only the baseline record), so Lesson 2 ("Tables are not JSON", the topic Lesson 1's teaser promised) was generated conservatively — it opens by recalling Lesson 1's stateless/DB-is-the-state idea and takes one small step into entity thinking. If Lesson 1 went differently than assumed, adjust Lesson 3 accordingly.

## Progress tracking (Neon DB, added 2026-07-08, proposed in this course's session)
- Learning progress persists in Neon Postgres, table `course_progress` (courses:
  go/rust/backend). Connection string ONLY in `~/.config/learning/db.env`
  (`LEARNING_DB_URL`, chmod 600) — never in a workspace file, never committed.
- Record events: `~/learning/bin/record-progress backend <kind> [--day N]
  [--lesson FILE] [--detail '{...}']` — kinds: lesson_generated, lesson_completed,
  quiz, kata, review, note. Record lesson_completed (outcome + open questions in
  detail) whenever the user finishes a lesson, so any session can pick up the thread.
- The 06:00 launchd job generates one short concept lesson per day for this course
  too. Its nav.js has no dates, so the idempotency check is: skip if a
  `lesson_generated` row for course=backend exists with today's date, OR if a lesson
  was already added to nav.js LESSONS today (e.g. by an interactive session).
  Register every generated lesson in nav.js and record it with record-progress.
  Sessions SHOULD still read recent course_progress rows (all three courses) to know
  what the user studied elsewhere.
