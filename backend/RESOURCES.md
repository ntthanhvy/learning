# Backend Foundations Resources

## Knowledge

- [Repo: "What happens when…" — alex/what-happens-when](https://github.com/alex/what-happens-when)
  Community-maintained deep trace of a request from keystroke to response. Use for: the request lifecycle, what sits between browser and handler.
- [Docs: MDN HTTP Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP)
  Canonical reference for methods, status codes, headers, caching, CORS. Use for: any HTTP semantics question — this is the arbiter.
- [Docs: PostgreSQL Manual — Data Definition](https://www.postgresql.org/docs/current/ddl.html)
  The primary source for tables, constraints, defaults, schemas. Use for: schema design details; always beats blog posts.
- [Book/Site: _Use The Index, Luke_ — Markus Winand](https://use-the-index-luke.com)
  The standard free text on SQL indexing and query performance. Use for: index selection, why a query is slow, pagination done right.
- [Book: _Designing Data-Intensive Applications_ — Martin Kleppmann](https://dataintensive.net)
  The backend book. Use for: data models (ch. 2), storage engines (ch. 3), transactions (ch. 7). Read chapters as topics come up, not cover-to-cover.
- [Book/Site: _The Copenhagen Book_](https://thecopenhagenbook.com)
  Free, focused guide to auth implementation: sessions, tokens, OAuth, CSRF. Use for: the auth & security track.
- [Site: OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org)
  High-trust, maintained security checklists. Use for: input validation, SQL injection, session management, secrets.
- [Site: The Twelve-Factor App](https://12factor.net)
  Classic operational manifesto for services. Use for: config, logs, statelessness, deployment vocabulary.

## Wisdom (Communities)

- [Database Administrators Stack Exchange](https://dba.stackexchange.com)
  High-signal Q&A for schema and query design; strong PostgreSQL presence. Use for: schema-design critique with real reviewers.
- [r/ExperiencedDevs](https://reddit.com/r/ExperiencedDevs)
  Moderated, senior-leaning. Use for: "how do teams actually do X" questions — migrations, review culture, backend ownership.
- Work code review — the user's own backend PRs at work are the primary wisdom loop: apply each concept by reviewing or writing one real backend change.

## Gaps

- No vetted resource yet for API design specifically (REST semantics beyond MDN — resource modeling, versioning, error contracts). Candidates to evaluate when that track starts: Microsoft REST API Guidelines, Stripe's API as an exemplar.
