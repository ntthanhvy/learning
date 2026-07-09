# Mission: Backend Foundations for a Frontend-Heavy Fullstack Dev

## Why
Titled fullstack, but day-to-day work is frontend-heavy, so the backend mindset never formed: given a feature, I can build the UI but can't confidently design the schema, the API, or the service behind it. This course builds that mindset — the terminology, concepts, and design instincts — so I can own backend work at my job end-to-end, grounded in the stack I actually touch: Go + PostgreSQL.

## Success looks like
- Take a feature request and design the data model for it: entities, relationships, constraints, and a migration plan — and explain the trade-offs.
- Design an API for that feature: resource naming, verbs, status codes, pagination, error contract, idempotency — and defend it in review.
- Reason about what happens at runtime: transactions, N+1 queries, caching, background jobs, connection pools — and spot these problems in existing code.
- Hold a conversation about auth (sessions vs JWT), security basics (OWASP top risks), and production operations (logging, monitoring) without switching to frontend framing.
- Read backend PRs at work and give substantive review comments, not just style nits.

## Constraints
- Runs **in parallel** with the Go week (Jul 7–13) and Rust week (Jul 8–14) intensives: light touch, ~20 min/day — one short concept lesson, terminology and mental models over heavy practice.
- After the intensives end (~Jul 15), the pace can deepen; revisit this mission then.
- Ground examples in Go + PostgreSQL; don't duplicate the Go week's Days 5–6 data track (constraints, indexes, EXPLAIN, transactions in depth) — this course provides the conceptual frame around it.

## Out of scope
- NoSQL, sharding, replication, distributed systems beyond vocabulary level.
- Kubernetes/infra tooling; cloud-provider specifics.
- Frameworks and ORMs — concepts first; the Go week already covers stdlib + pgx practice.
