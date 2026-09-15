# Plan: Data Pipelines — dbt, Kafka & Airflow

Two phases, same convention as `python/`. Phase 1 is date-locked with
pre-assigned filenames. Phase 2 is open-ended and sequential.

**The course builds one thing:** the learner's public repo
`food-delivery-pipeline`. Every lesson ends with a build step in that repo and
a verification command whose expected output is printed in the lesson. That
command is the feedback loop. CI cannot push to the learner's repo, so lessons
*instruct*; they never assume a step is already done.

## The domain (keep it consistent across every lesson)

A food-delivery platform with four raw entities. Use these names exactly:

| Raw table / topic | Grain | Arrives via |
|---|---|---|
| `raw.restaurants` | one row per restaurant (name, cuisine, city, commission_rate, updated_at) | batch CSV load |
| `raw.couriers` | one row per courier (vehicle, city, joined_at) | batch CSV load |
| `raw.orders` | one row per order (customer_id, restaurant_id, courier_id, subtotal, delivery_fee, placed_at) | batch CSV load |
| `order_events` topic → `raw.order_events` | one row per status change (event_id, order_id, status, occurred_at); status ∈ placed, accepted, picked_up, delivered, cancelled | Kafka |

The headline marts are `fct_orders`, `dim_restaurants`, `dim_couriers`, and
`mart_delivery_sla`: minutes from placed to delivered, and the share of
orders over 45 min per city per day.

Stack: Postgres 17 as the warehouse (`docker compose`), dbt-postgres,
`apache/kafka:4.3.1` single-node KRaft, a Python producer/consumer on
confluent-kafka, and Airflow 3.3.1.

## Phase 1 — Intensive week: one thin slice, end to end

Seven days, one lesson each, **date-locked**. The generator must use exactly
these filenames on exactly these dates and must not generate ahead of the date.
~30–45 min per day, most of it building.

| Day | Date | Lesson | File | Tangible win |
|-----|------|--------|------|--------------|
| 1 | 2026-09-15 | The pipeline map & the repo | `0001-pipeline-map-and-repo.html` | Public repo exists; `docker compose up` gives a Postgres with `raw.*` tables loaded from a generator script; can say where dbt, Kafka and Airflow each sit and why this is ELT |
| 2 | 2026-09-16 | dbt: sources, staging & `ref()` | `0002-dbt-sources-and-staging.html` | `dbt run` builds `stg_orders`, `stg_restaurants`, `stg_couriers` as views; can read the lineage graph |
| 3 | 2026-09-17 | dbt: tests catch bad data | `0003-dbt-tests.html` | `dbt build` fails on a planted bad row (orphan restaurant_id, negative subtotal), then passes after a fix; source freshness configured |
| 4 | 2026-09-18 | dbt: marts, facts, dimensions & incremental | `0004-dbt-marts-and-incremental.html` | `fct_orders` + `dim_restaurants` built; one model incremental with `unique_key`; can defend view vs table vs incremental |
| 5 | 2026-09-19 | Kafka: topics, partitions, keys & offsets | `0005-kafka-topics-partitions-offsets.html` | Kafka runs in compose; a Python producer writes `order_events` keyed by order_id; a consumer group's offsets inspected with the CLI; can explain why the key preserves per-order ordering |
| 6 | 2026-09-20 | Kafka → warehouse: at-least-once, landed safely | `0006-kafka-consumer-to-warehouse.html` | Consumer lands events into `raw.order_events` with `INSERT … ON CONFLICT (event_id) DO NOTHING`, committing offsets *after* the write; killing and restarting it creates no duplicates; `stg_order_events` + `mart_delivery_sla` built in dbt |
| 7 | 2026-09-21 | Airflow orchestrates the batch & ship it | `0007-airflow-orchestrates-dbt.html` | An Airflow 3 DAG runs load → `dbt build` daily with retries; a manual re-run is safe; README with architecture diagram and a "decisions" section pushed |

Why this order: batch before stream, because dbt on static tables uses the
learner's strongest skill (SQL) and gives a working warehouse by Day 4. Kafka
then *feeds* that warehouse rather than being learned in a vacuum. Airflow comes
last because orchestration only means something once there are steps to
orchestrate. The learner has already edited DAGs, so Day 7 can move faster.

Generator notes for Phase 1:
- **Day 1 must not overrun.** Repo + compose + raw load is the whole win. The
  data generator script should be given in full: it is scaffolding, not the
  lesson. Seed it deterministically and plant a few bad rows on purpose, so
  Day 3's tests have something real to catch.
- **Day 5 memory:** Kafka's JVM plus Postgres fit comfortably in 16 GB. Tell the
  learner to give colima enough memory (`colima start --memory 6`, or check
  current settings) before debugging anything else.
- **Day 7 Airflow:** prefer the lightest setup that runs Airflow 3.3.1 next to
  the existing compose stack. Verify against the official Quick Start and
  docker-compose how-to *before* writing, because the official compose file is
  documented as a heavy, non-production reference. Running dbt through
  `BashOperator` is fine for Day 7. Cosmos is a Phase 2 upgrade, not a
  prerequisite.

## Phase 2 — Open-ended: depth where the mission says depth

Starts **2026-09-22**, sequential numbering from `0008-…`, no date-locking,
~20 min/day. Ordering is a spine, not a schedule: adapt it to the learning
records. Roughly 50% dbt, 20% Kafka, 20% Airflow, 10% portfolio and interview.

**2a. dbt in depth**
- Layering conventions: staging → intermediate → marts, naming, one-source-per-staging-model (dbt's "How we structure our dbt projects")
- Snapshots: SCD type 2 for restaurant `commission_rate` changes; `dbt_valid_from`/`dbt_valid_to`; joining a fact to the version valid at order time
- Jinja & macros: DRY SQL, `{{ var() }}`, `{{ target }}`, when a macro makes a project *worse*
- Packages: `dbt_utils` (surrogate keys, `generate_series`), and when to write a test instead of importing one
- Unit tests (dbt ≥ 1.8) vs data tests: testing *logic* with fixed inputs vs testing *data*
- Incremental strategies in depth: `merge`/`delete+insert` on Postgres, late-arriving events, `--full-refresh`
- Docs, exposures, model contracts & versions: dbt as an API for downstream consumers
- dbt in CI: GitHub Actions with a Postgres service container, `dbt build --select state:modified+`, deferral

**2b. Kafka, concept-first**
- Delivery semantics: at-most / at-least / exactly-once; idempotent producer; what "exactly-once" does and doesn't promise end to end
- Schema evolution: why JSON-without-a-schema bites, and what a Schema Registry and Avro/Protobuf buy (one hands-on change, the rest vocabulary)
- Retention vs log compaction; consumer lag as the key health metric
- Kafka Connect and CDC with Debezium: the alternative to a hand-written consumer (concept plus a diagram)
- When stream processing (Kafka Streams, Flink) is warranted vs "land it and let dbt do it": vocabulary only

**2c. Airflow, working depth**
- Logical date / data interval, catchup and backfills, and idempotent tasks that make backfills safe
- TaskFlow API, and why XCom is not a data transport
- Assets (data-aware scheduling): trigger the dbt DAG when `raw.order_events` is updated instead of by clock
- Connections, variables and secrets; never hard-code credentials in a DAG
- Cosmos: dbt models as individual Airflow tasks, and the trade-off vs one `dbt build` task
- Sensors vs deferrable operators; retries, SLAs/deadlines and alerting

**2d. Portfolio & interview**
- One-command demo (`make demo`), a README that reads in 2 minutes, and an architecture diagram
- A data-quality story: what is tested where (Kafka consumer, dbt tests, source freshness), and why
- "What breaks at 100×?": partitions, incremental models, warehouse choice
- A mock design-review walkthrough of the repo, recorded as a learning record

Revisit this plan at the end of 2a, when the dbt depth versus Kafka/Airflow
split should be re-checked against what the learner actually wants to show.
