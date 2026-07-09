# Baseline: comfortable with SQL, wants depth

User self-reports SQL comfort — joins and schema basics are fine; the gap is depth: indexes, query performance, transactions, and deliberate data modeling. Chose PostgreSQL as the course database and opted to squeeze the data track into the original 7 days rather than extend.

**Evidence:** Stated during mission-revision interview 2026-07-07.

**Implications:** Days 5–6 skip SQL syntax and basic joins entirely; start at constraints-as-invariants, index selection, EXPLAIN, and transaction semantics. The dedicated generics day was sacrificed — generics must be taught in context on Day 6 (pgx.CollectRows) and reinforced in Day 7 recall. Cross-link: [[MISSION.md]] updated same day.
