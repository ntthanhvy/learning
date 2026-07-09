# One-Week Go + Data Intensive — 2026-07-07 → 2026-07-13

Grounded in [MISSION.md](./MISSION.md): backend services + job hunting, 2–3 h/day, already writes Go, comfortable with SQL and wants depth. **Revised 2026-07-07** to integrate data modeling & queries (PostgreSQL) into the original week.

**Running project:** *linkshort* — a URL-shortener HTTP service, stdlib + pgx only. By Sunday: a tested, Postgres-backed service with graceful shutdown, a defensible schema, and `EXPLAIN`-verified queries — a complete interview walkthrough.

**Daily shape (2–3 h):** ~30 min lesson → ~60–90 min project/exercise work → ~15 min recall quiz from *previous* days (spaced retrieval).

**What got squeezed:** the dedicated generics/iterators day. Generics are now taught in context on Day 6 (`pgx.CollectRows[T]`, generic scan helpers) and iterators via range-over-func row streaming — real usage beats a toy LRU cache anyway.

---

## Day 1 — Mon Jul 7 · Interfaces & composition ✅ (lesson delivered)
Implicit satisfaction, small consumer-defined interfaces, embedding, "accept interfaces, return structs."
**Project:** scaffold linkshort; `Store` interface + `MemStore`.
**Primary source:** [Effective Go — Interfaces](https://go.dev/doc/effective_go#interfaces_and_types)

## Day 2 — Tue Jul 8 · Errors as values
Wrapping with `%w`, `errors.Is`/`As`, sentinel vs typed errors, when to panic (almost never).
**Project:** error taxonomy for the store (`ErrNotFound`, validation) surfaced as correct HTTP statuses — this taxonomy must survive the Postgres swap on Day 5.
**Primary source:** [Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors)

## Day 3 — Wed Jul 9 · Goroutines, channels, select
Goroutines vs threads, channel directions, buffered vs unbuffered, `select`, closing semantics, race detector.
**Project:** background click-counter fed by a channel; run tests with `-race`.
**Primary source:** [Rob Pike — Concurrency Is Not Parallelism](https://go.dev/blog/waza-talk)

## Day 4 — Thu Jul 10 · context, sync & the HTTP server
`context.Context` cancellation & timeouts (which Days 5–6 need for every query), `sync` primitives, `errgroup`, goroutine-leak avoidance. Plus the server essentials pulled forward from old Day 6: 1.22 ServeMux patterns (`GET /{code}`), middleware as decorators, graceful shutdown via `signal.NotifyContext`.
**Project:** full HTTP surface (create, redirect, stats) on `MemStore`, with timeouts, logging middleware, graceful shutdown.
**Primary sources:** [Go Blog — Context](https://go.dev/blog/context) · [Routing Enhancements for Go 1.22](https://go.dev/blog/routing-enhancements)

## Day 5 — Fri Jul 11 · Data modeling in PostgreSQL 🗄️
Schema design as invariant design: normalization judgment calls, constraints (`UNIQUE`, `CHECK`, FKs) as the first line of correctness, choosing keys, index fundamentals (B-tree, composite, partial), migrations as versioned artifacts.
**Project:** design the linkshort schema (`links`, `clicks`), defend each constraint; use a hosted Postgres ([Neon](https://neon.tech) free tier — no Docker needed locally); write migrations; implement `PostgresStore` satisfying `Store` — Day 1's interface pays off.
**Primary source:** [PostgreSQL docs — DDL & Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

## Day 6 — Sat Jul 12 · Queries from Go (+ generics in the wild) 🗄️
pgx query patterns, `pgx.CollectRows[T]` (generics doing real work), range-over-func for streaming rows, transactions & isolation levels, keyset vs offset pagination, N+1 avoidance, reading `EXPLAIN ANALYZE`, verifying an index earns its keep.
**Project:** click-stats aggregate query with keyset pagination; wrap create-with-collision-retry in a transaction; `EXPLAIN` the redirect hot path and fix it with the right index.
**Primary sources:** [pgx docs](https://pkg.go.dev/github.com/jackc/pgx/v5) · [Use The Index, Luke](https://use-the-index-luke.com/)

## Day 7 — Sun Jul 13 · Testing, tooling & capstone
Table-driven tests, subtests, `httptest`, integration tests against real Postgres (a dedicated Neon branch — instant, free database copies stand in for testcontainers), benchmarks, `go vet`/`go fix` modernizers, pprof taste. Capstone: full test pass on linkshort; mock-interview self-review covering both the Go and the data story.
**Primary source:** [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests)

---

## Spacing & retention
- Each lesson opens with 3 recall questions from earlier days (retrieval practice), interleaving Go and SQL topics from Day 5 on.
- Reference sheets accumulate in [./reference/](./reference/) — review the pile, not the lessons.
- After Day 7: schedule two spaced reviews (Jul 20, Aug 3) using the reference sheets and the linkshort codebase.
