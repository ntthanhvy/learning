# Baseline: frontend-heavy fullstack, SQL-comfortable, backend mindset missing

User is a fullstack dev whose real work is frontend-heavy; they can build UIs against existing APIs but haven't formed the backend design mindset — schema design, API design, runtime reasoning are the gaps, not programming ability. SQL syntax and joins are comfortable (established in [[go-week 0002-sql-baseline]]). Go week (Jul 7–13) runs in parallel and will cover Postgres depth (constraints, indexes, EXPLAIN, transactions) on its Days 5–6.

**Implications:** Start from the mental-model layer, not syntax: request lifecycle, statelessness, "database is the state," entities-vs-UI-shapes. Bridge every backend concept from a frontend concept the user already owns. Keep lessons ~20 min while the intensives run; don't schedule practice-heavy data-modeling work before the Go week's data days land (Jul 11–12).
