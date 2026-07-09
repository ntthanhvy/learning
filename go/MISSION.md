# Mission: Go for Backend Work & Job Hunting

## Why
Sharpen existing Go skills to a level where I can confidently build backend services at work and pass Go-focused job interviews. The goal is not "learning Go from scratch" — it's mastering the features that make Go distinctive (concurrency, interfaces, error handling, the stdlib) well enough to use and explain them under pressure. Backend services live on databases, so the mission includes the data layer: modeling schemas well and writing performant queries from Go against PostgreSQL.

## Success looks like
- Build a small, production-shaped HTTP service in Go (routing, JSON, context, graceful shutdown) without reaching for a framework.
- Explain and demonstrate goroutines, channels, `select`, and `context` cancellation in an interview whiteboard setting.
- Use interfaces idiomatically: small interfaces, implicit satisfaction, "accept interfaces, return structs."
- Write table-driven tests and use the race detector as a reflex, not an afterthought.
- Know what's modern (Go 1.22–1.26): stdlib routing, range-over-func iterators, generics improvements.
- Design a normalized PostgreSQL schema with the right constraints and indexes, and defend the choices.
- Write queries from Go (pgx) with transactions, pagination, and `EXPLAIN`-verified performance.

## Constraints
- One week intensive: 2026-07-07 → 2026-07-13, 2–3 hours/day.
- Already writes working Go — skip syntax basics, focus on depth and idiom.

## Out of scope
- Frameworks (Gin, Echo, Fiber) — stdlib first; frameworks are easy to pick up later.
- Kubernetes/infra tooling, CGo, assembly, runtime internals beyond what interviews need.
- ORMs (GORM/ent) and NoSQL — raw SQL + pgx first; distributed-data topics (sharding, replication) beyond interview talking points.
