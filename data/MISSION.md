# Mission: Data Wrangling with pandas & NumPy — Interview-Ready

## Why
Preparing to interview for a position that requires data-processing skills (ETL/ELT pipelines). The goal is to quickly grasp the *methodology* behind common data processing and data wrangling — the thinking patterns, not encyclopedic API coverage — so that in an interview I can solve a wrangling task hands-on and talk through pipeline design with confidence.

## Success looks like
- Given a messy CSV or table in an interview, narrate and write the standard wrangling path: load → inspect → clean (dtypes, missing values, duplicates) → transform → aggregate → output.
- Solve the classic pandas interview tasks without Python loops: filter/select, groupby (split–apply–combine), merge/join, reshape (pivot/melt), rank & cumulative ops.
- Explain the *why* out loud: vectorization vs loops, when to use pandas vs SQL vs Spark/Polars, ETL vs ELT and where each transform belongs.
- Read NumPy-flavored code (broadcasting, dtype, NaN behavior) and predict its output.
- Complete timed practice problems (LeetCode pandas track, StrataScratch mediums) comfortably.

## Constraints
- Runs **in parallel** with the Go week (through Jul 13), Rust week (through Jul 14), and Backend Foundations: light touch, ~20 min/day, one lesson per day. From ~Jul 15 this can become a main track — revisit pace then.
- Strong SQL (joins, aggregation, window basics): teach pandas **through SQL equivalence**; never re-teach SQL concepts.
- Python: working but basic — gloss Python idioms (comprehensions, lambdas, unpacking) as they appear; don't assume fluency.
- No system-wide pandas install: practice runs via `uv run --with pandas` (uv is installed).
- Interview date not yet fixed — front-load the highest-frequency interview topics first.

## Out of scope
- Spark / Dask / Polars beyond vocabulary-level comparison ("when would you outgrow pandas?").
- Machine learning, statistics, and visualization libraries.
- Orchestration tooling (Airflow, Dagster) beyond vocabulary — the mission is the wrangling methodology itself.
- Deep NumPy (linear algebra, C-level internals) — only what pandas fluency requires.
