# Baseline: SQL strong, pipeline tools read-about, Airflow lightly used

Established 2026-09-14 at course creation, from the user directly. Asked about
prior exposure, the user reported **heard of / read about** dbt, Kafka and
Airflow, and **used Airflow a bit**. Asked which one had been hands-on, it was
Airflow: reading or editing an existing DAG, never building one from scratch.

Other courses in this workspace establish the rest (see their MISSION.md files).
Strong SQL and PostgreSQL. Python written from a blank file only since
`python/` (48 lessons deep as of today, including FastAPI). Backend concepts
such as idempotency, transactions and connection pools from `backend/` (71
lessons). pandas-based ETL/ELT interview prep from `data/`.

## Implications

- **dbt will feel familiar fast.** A dbt model is a `SELECT`, so don't spend
  lesson time on the SQL. Spend it on what dbt adds: `ref()`/`source()` and the
  DAG, materializations, tests, and project layering. Days 2–4 can move quickly.
- **Kafka is the real difficulty spike (Days 5–6).** It is the first truly new
  mental model: an append-only log with partitions and offsets, not a queue and
  not a table. Bridge from things already owned. A partition is ordered like an
  `ORDER BY` on insertion, and a consumer offset is a bookmark, like keyset
  pagination's cursor. At-least-once plus an idempotent write is the backend
  course's idempotency-key idea applied to a pipeline. If Day 5's quiz or build
  step goes badly, add a consolidation lesson before Day 6.
- **Airflow exposure may be 2.x-era.** "Edited a DAG" could mean old import
  paths and pre-3.0 concepts (`execution_date`, SubDAGs, datasets rather than
  assets). Day 7 should check what carries over and what changed in Airflow 3,
  not assume a blank slate or current knowledge.
- **Recognition ≠ recall** (the same asymmetry `python/`'s baseline record
  found). Having read about these tools means the vocabulary will feel
  familiar before it is usable. Every lesson's build step and quiz is where the
  learning happens.

## To verify

The Airflow depth is self-reported and untested. On Day 7, open with a short
diagnostic (read a small DAG and predict its task order and schedule) and
revise this record with what it shows.
