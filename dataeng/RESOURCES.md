# Data Pipelines — Resources

Ground every lesson in these. For behaviour and syntax, the official docs win
over any blog post. Named authors are for the *why*. Cite inline, and have each
lesson recommend exactly one primary source. All links were checked on
2026-09-14. The Medium, O'Reilly and Reddit links block automated checks but
are real.

Versions pinned by this course (PyPI / Docker Hub, 2026-09-14): dbt-core
1.12.4, dbt-postgres 1.11.0, apache-airflow 3.3.1, `apache/kafka:4.3.1`,
confluent-kafka 2.15.1, astronomer-cosmos 1.15.1. dbt 2.0 is in release
candidates. **Do not teach 2.0-only features** until it is GA, and re-check
before Phase 2.

## Knowledge — the big picture

- [Book: _Fundamentals of Data Engineering_ — Joe Reis & Matt Housley (O'Reilly)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108295/)
  The lifecycle framing: generation → ingestion → storage → transformation → serving. Use for: Day 1's pipeline map and any "where does this tool belong" question. (Paid.)
- [Book: _Designing Data-Intensive Applications_ — Martin Kleppmann](https://dataintensive.net/)
  Ch. 10 (batch) and ch. 11 (stream processing) are the authoritative explanation of logs, partitions and delivery semantics. Use for: the *why* behind Kafka on Days 5–6 and Phase 2b. (Paid.)
- [Article: "Functional Data Engineering" — Maxime Beauchemin](https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a)
  By Airflow's creator: idempotent, re-runnable partitions as the core discipline. Use for: Day 7 and every backfill/idempotency lesson.
- [Kimball Group: Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
  Primary source for facts, dimensions, grain and slowly changing dimensions. Use for: Day 4 marts and Phase 2a snapshots.

## Knowledge — dbt (deep)

- [Docs: What is dbt?](https://docs.getdbt.com/docs/introduction)
  Official overview. Use for: Day 1's one-paragraph definition of dbt as the T in ELT.
- [Docs: Postgres setup (dbt-postgres)](https://docs.getdbt.com/docs/core/connect-data-platform/postgres-setup)
  `profiles.yml` fields for Postgres. Use for: Day 2 connection setup.
- [Docs: Sources](https://docs.getdbt.com/docs/build/sources) · [Materializations](https://docs.getdbt.com/docs/build/materializations) · [Seeds](https://docs.getdbt.com/docs/build/seeds)
  Use for: Day 2 (`source()`, `ref()`, view vs table), and when a seed is and isn't appropriate.
- [Docs: Data tests](https://docs.getdbt.com/docs/build/data-tests)
  Generic and singular tests, and `dbt build`. Use for: Day 3, the primary source.
- [Docs: Incremental models](https://docs.getdbt.com/docs/build/incremental-models)
  `is_incremental()`, `unique_key`, strategies. Use for: Day 4 and Phase 2a incremental depth.
- [Docs: Snapshots](https://docs.getdbt.com/docs/build/snapshots)
  SCD type 2 in dbt. Use for: Phase 2a.
- [Docs: Jinja and macros](https://docs.getdbt.com/docs/build/jinja-macros) · [var()](https://docs.getdbt.com/reference/dbt-jinja-functions/var) · [target](https://docs.getdbt.com/reference/dbt-jinja-functions/target)
  DRY SQL via reusable Jinja functions, project variables and the active-connection object. Use for: Day 10, the primary source.
- [Guide: How we structure our dbt projects — dbt Labs](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview)
  The community-standard staging → intermediate → marts layering and naming. Use for: Day 2's folder layout and every modelling lesson after it. This is the house style.
- [Courses: dbt Learn catalog](https://learn.getdbt.com/catalog)
  Free official video courses (dbt Fundamentals etc.). Use for: an optional second pass on Days 2–4 for a learner who prefers video.

## Knowledge — Kafka (working level)

- [Docs: Apache Kafka Quickstart](https://kafka.apache.org/quickstart/)
  Official single-node KRaft start with the Docker image and CLI tools. Use for: Day 5 setup. Kafka 4.x has no ZooKeeper, and tools use `--bootstrap-server`.
- [Docs: Apache Kafka Documentation — Design](https://kafka.apache.org/documentation/)
  Authoritative on the log, partitions, replication, and producer/consumer delivery semantics. Use for: Days 5–6 claims about ordering and offsets.
- [Image: `apache/kafka` on Docker Hub](https://hub.docker.com/r/apache/kafka)
  The official image and its env-var configuration. Use for: the compose service on Day 5.
- [Course: Kafka 101 — Confluent Developer](https://developer.confluent.io/courses/apache-kafka/events/)
  Short, clear videos on events, topics, partitions and consumer groups. Use for: Day 5's primary source for a first-timer. Skip the Confluent Cloud sign-up steps, since this course runs locally.
- [Docs: confluent-kafka Python client](https://docs.confluent.io/kafka-clients/python/current/overview.html)
  Producer/consumer API, delivery callbacks, manual commits. Use for: Days 5–6 code.
- [Book: _Kafka: The Definitive Guide_, 2nd ed. — Shapira, Palino, Sivaram, Petty](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)
  Deep reference, free download from Confluent (registration). Use for: Phase 2b delivery semantics, retention and compaction.

## Knowledge — Airflow (working level)

- [Docs: Airflow Quick Start](https://airflow.apache.org/docs/apache-airflow/stable/start.html) · [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
  Official local setups. Use for: Day 7. Read both before choosing, because the docker-compose file is a heavy reference setup.
- [Docs: Upgrading to Airflow 3](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html)
  What changed from 2.x. Use for: bridging the learner's earlier Airflow exposure, which may be 2.x-era, so imports and concepts that moved are flagged explicitly.
- [Docs: Core Concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html) · [TaskFlow tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
  DAGs, tasks, operators, scheduling, TaskFlow. Use for: Day 7 and Phase 2c.
- [Docs: Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
  Idempotent tasks, top-level code, testing DAGs. Use for: Day 7's "safe re-run" requirement.
- [Docs: Assets (data-aware scheduling)](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/assets.html)
  Use for: Phase 2c, triggering dbt when raw data lands.
- [Docs: Astronomer Cosmos](https://astronomer.github.io/astronomer-cosmos/) · [Astronomer: Orchestrate dbt Core with Airflow and Cosmos](https://www.astronomer.io/docs/learn/airflow-dbt)
  Running each dbt model as an Airflow task. Use for: Phase 2c. Some Astronomer pages still show Airflow 2 code, so check imports against the Airflow 3 docs.

## Knowledge — a reference build to compare against

- [Course: DataTalksClub Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
  Free, well-maintained, community-run: orchestration, analytics engineering with dbt, and streaming with Kafka. Use for: seeing another end-to-end build when stuck. Don't copy its project, because a taxi-data portfolio is overused. Its cloud (GCP) parts are out of scope.

## Wisdom (Communities)

- [dbt Community Slack](https://www.getdbt.com/community/join-the-community)
  Large, active and well-moderated, with `#advice-dbt-help` and `#advice-data-modeling`. Use for: modelling critique ("is this the right grain?"), incremental-model edge cases.
- [Apache Airflow Community (Slack + mailing lists)](https://airflow.apache.org/community/)
  Official community with maintainers present. Use for: DAG design questions and Airflow 3 migration gotchas.
- [Confluent Community Forum](https://forum.confluent.io/)
  Kafka Q&A, active since the old mailing lists quietened. Use for: consumer/producer config questions and delivery-semantics sanity checks.
- [DataTalksClub Slack](https://datatalks.club/slack.html)
  Learners and practitioners building exactly this kind of portfolio project. Use for: **portfolio review**. Post the repo when Phase 1 ships.
- [r/dataengineering](https://www.reddit.com/r/dataengineering/)
  Large and noisier, but good for career and portfolio feedback. Use for: "does this project read as hireable?" Sort by top, not new.

## Gaps

- No single high-trust source on **running Airflow 3 lightly next to an existing docker-compose stack** for local development. Day 7 must verify against the official docs at generation time rather than trusting a blog.
- No good primary source yet for **testing a Kafka consumer's idempotency** locally. Day 6 relies on the Kafka design docs plus Postgres `ON CONFLICT` docs, and should flag this.
