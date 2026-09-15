# Mission: Data Pipelines — dbt, Kafka & Airflow, Shipped as a Portfolio

## Why
The other courses taught the parts: wrangling in `data/`, the language in `python/`, backend design in `backend/`. None of them produced a working pipeline anyone can see. This course builds one, a **food-delivery data platform** in a public GitHub repo. Order events stream through Kafka, land in a Postgres warehouse, get modelled by dbt into tested marts, and run on an Airflow schedule. The repo is the proof: something to link on a CV and walk an interviewer through, decision by decision.

## Success looks like
- A public repo (`food-delivery-pipeline`) where `docker compose up` plus one documented command runs the pipeline end to end on a laptop.
- **dbt, in depth:** build sources → staging → intermediate → marts from a blank project. Write generic, singular and unit tests. Choose view, table or incremental and defend the choice. Track slowly-changing restaurant data with snapshots.
- **Kafka, working level:** explain topics, partitions, keys, offsets and consumer groups. Produce and consume order events from Python. Explain why the landing step is at-least-once and how an idempotent write makes that safe.
- **Airflow, working level:** write an Airflow 3 DAG that orchestrates the batch side (`dbt build` after raw data lands), with retries and safe re-runs. Explain the logical date, catchup and backfills out loud.
- Walk through the repo's architecture diagram in a 10-minute interview-style explanation: why ELT, why this split between stream and batch, where data quality is enforced, and what would change at 100× volume.

## Constraints
- **Depth is deliberately uneven.** dbt goes deep, because strong SQL makes it the highest-leverage tool. Kafka and Airflow go as deep as the portfolio needs to run, with the rest at concept level.
- **Prior exposure:** has *heard of / read about* all three. Has *used Airflow a bit* (read or edited an existing DAG, never built one from scratch). Kafka and dbt are hands-on new. Strong SQL and PostgreSQL. Python and FastAPI from `python/`. Backend idempotency and transaction concepts from `backend/`.
- **Pacing:** a 7-day date-locked intensive, 2026-09-15 → 2026-09-21, then open-ended. It runs alongside `backend/`, `data/` and `python/`, so each day is one build step (~30–45 min in the intensive, ~20 min after).
- **Environment:** macOS, 16 GB RAM, Docker via colima, `uv` for Python. Everything runs locally with no cloud account and no paid services.
- Pinned versions (checked on PyPI and Docker Hub, 2026-09-14): dbt-core 1.12.4 + dbt-postgres 1.11.0, `apache/kafka:4.3.1` (KRaft, no ZooKeeper), confluent-kafka 2.15.1, apache-airflow 3.3.1.

## Out of scope
- **pandas and NumPy** belong to `data/`, the Python language to `python/`, and API/schema design to `backend/`. Use them as bridges and never re-teach them.
- Spark, Flink and Kafka Streams beyond vocabulary: "when would you reach for stream processing?"
- Cloud warehouses (Snowflake, BigQuery, Redshift) and dbt Cloud/Fusion beyond a one-line contrast. The warehouse here is Postgres.
- Kubernetes, Terraform and managed Kafka/Airflow (MSK, Confluent Cloud, MWAA, Astro).
- Running Kafka in production: multi-broker tuning, security/ACLs, capacity planning.
