# Go Resources

## Knowledge

- [Effective Go](https://go.dev/doc/effective_go)
  The canonical idiom guide from the Go team. Use for: interfaces, embedding, concurrency conventions, naming.
- [Go Code Review Comments (Go wiki)](https://go.dev/wiki/CodeReviewComments)
  The Go team's list of common review feedback. Use for: settling "is this idiomatic?" questions quickly.
- [Go by Example](https://gobyexample.com)
  Annotated runnable examples of every language feature. Use for: quick syntax refreshers on any topic.
- [The Go Blog](https://go.dev/blog)
  Primary source for feature deep-dives. Key posts: [Errors are values](https://go.dev/blog/errors-are-values), [Working with Errors](https://go.dev/blog/go1.13-errors), [Go Concurrency Patterns](https://go.dev/blog/pipelines), [Context](https://go.dev/blog/context), [Range over function types](https://go.dev/blog/range-functions), [Routing enhancements (1.22 ServeMux)](https://go.dev/blog/routing-enhancements).
- [Go 1.26 Release Notes](https://go.dev/doc/go1.26)
  What's current as of Feb 2026 (Green Tea GC default, generics self-reference, `go fix` modernizers). Use for: staying current in interviews.
- [Learn Go with Tests — Chris James](https://quii.gitbook.io/learn-go-with-tests)
  TDD-driven Go fundamentals, free. Use for: testing idioms, table-driven tests, mocking with interfaces.
- [100 Go Mistakes and How to Avoid Them — Teiva Harsanyi](https://100go.co)
  Free companion site to the book. Use for: common pitfalls (slices, goroutine leaks, defer, interfaces) — high interview signal.
- [Rob Pike: "Concurrency Is Not Parallelism" (talk)](https://go.dev/blog/waza-talk)
  The mental model for Go concurrency. Use for: Day 3 grounding.
- [pkg.go.dev standard library docs](https://pkg.go.dev/std)
  Primary reference for `net/http`, `encoding/json`, `context`, `sync`, `errors`.

### Data modeling & queries

- [PostgreSQL official documentation](https://www.postgresql.org/docs/current/)
  Primary source for everything Postgres. Key chapters: [DDL & constraints](https://www.postgresql.org/docs/current/ddl.html), [indexes](https://www.postgresql.org/docs/current/indexes.html), [transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html), [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).
- [Use The Index, Luke — Markus Winand](https://use-the-index-luke.com/)
  The best free text on SQL indexing and query performance, written for developers. Use for: Day 6 index/EXPLAIN work, pagination (his keyset-pagination argument is canonical).
- [pgx — PostgreSQL driver for Go](https://pkg.go.dev/github.com/jackc/pgx/v5)
  The de-facto Postgres driver; `CollectRows`/`RowToStructByName` showcase generics in production. Use for: all query-from-Go patterns.
- [Go tutorial — Accessing a relational database](https://go.dev/doc/tutorial/database-access)
  Official `database/sql` walkthrough. Use for: understanding the stdlib layer pgx sits beside.
- [sqlc](https://docs.sqlc.dev/)
  Generates type-safe Go from SQL. Not used in the course project, but common in job listings — worth a skim before interviews.
- [Neon — serverless Postgres](https://neon.tech) ([docs](https://neon.com/docs))
  The course database (free tier; no local Docker available). Use for: main DB + a separate branch for Day 7 integration tests.

## Wisdom (Communities)

- [Gophers Slack](https://invite.slack.golangbridge.org/)
  The largest Go community (~100k members); #newbies and #jobs channels. Use for: code critique, job-hunt advice.
- [r/golang](https://reddit.com/r/golang)
  Active, well-moderated. Use for: ecosystem questions, "how do people do X in production."
- [Go Forum](https://forum.golangbridge.org/)
  Slower-paced official-adjacent forum. Use for: longer-form design questions.

## Gaps

- No curated Go interview-question bank vetted yet — evaluate one before Day 7.
