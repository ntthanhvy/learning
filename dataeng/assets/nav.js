// Course navigation. Single source of truth for the lesson & reference lists.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Phase 1 (Days 1-7) is date-locked to the filenames pre-assigned in PLAN.md;
// from 2026-09-22 the course is open-ended — register each new lesson here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";

  const LESSONS = [
    // Phase 1 — date-locked, filenames pre-assigned in PLAN.md. Register each
    // lesson here on its day, never ahead of it. Example shape:
    // { n: 1, date: "2026-09-15", title: "…", file: "lessons/0001-….html" },
    { n: 1, date: "2026-09-15", title: "The pipeline map & the repo", file: "lessons/0001-pipeline-map-and-repo.html" },
    { n: 2, date: "2026-09-16", title: "dbt: sources, staging & ref()", file: "lessons/0002-dbt-sources-and-staging.html" },
    { n: 3, date: "2026-09-17", title: "dbt: tests catch bad data", file: "lessons/0003-dbt-tests.html" },
    { n: 4, date: "2026-09-18", title: "dbt: marts, facts, dimensions & incremental", file: "lessons/0004-dbt-marts-and-incremental.html" },
    { n: 5, date: "2026-09-19", title: "Kafka: topics, partitions, keys & offsets", file: "lessons/0005-kafka-topics-partitions-offsets.html" },
    { n: 6, date: "2026-09-20", title: "Kafka → warehouse: at-least-once, landed safely", file: "lessons/0006-kafka-consumer-to-warehouse.html" },
    { n: 7, date: "2026-09-21", title: "Airflow orchestrates the batch & ship it", file: "lessons/0007-airflow-orchestrates-dbt.html" },
    // Phase 2 — open-ended, sequential from here. Register each new lesson on
    // the day it's generated.
    { n: 8, date: "2026-09-22", title: "dbt: the intermediate layer", file: "lessons/0008-dbt-intermediate-layer.html" },
    { n: 9, date: "2026-09-23", title: "dbt snapshots: SCD Type 2 for commission_rate", file: "lessons/0009-dbt-snapshots-scd2.html" },
    { n: 10, date: "2026-09-24", title: "dbt: Jinja, macros & var()", file: "lessons/0010-dbt-jinja-and-macros.html" },
    { n: 11, date: "2026-09-25", title: "dbt packages: dbt_utils and when to write a test instead", file: "lessons/0011-dbt-utils-and-packages.html" },
    { n: 12, date: "2026-09-26", title: "dbt unit tests vs. data tests", file: "lessons/0012-dbt-unit-tests.html" },
    { n: 13, date: "2026-09-27", title: "dbt incremental strategies in depth", file: "lessons/0013-dbt-incremental-strategies.html" },
    { n: 14, date: "2026-09-28", title: "dbt docs, exposures & model contracts", file: "lessons/0014-dbt-docs-exposures-contracts.html" },
    { n: 15, date: "2026-09-29", title: "dbt in CI: GitHub Actions, state:modified+, deferral", file: "lessons/0015-dbt-in-ci.html" },
    { n: 16, date: "2026-09-30", title: "Kafka delivery semantics & the idempotent producer", file: "lessons/0016-kafka-delivery-semantics.html" },
    { n: 17, date: "2026-10-02", title: "Schema evolution: why JSON-without-a-schema bites", file: "lessons/0017-kafka-schema-evolution.html" },
    { n: 18, date: "2026-10-03", title: "Retention vs log compaction, and consumer lag", file: "lessons/0018-kafka-retention-compaction-and-consumer-lag.html" },
    { n: 19, date: "2026-10-04", title: "Airflow: logical date, data interval & safe backfills", file: "lessons/0019-airflow-logical-date-and-backfills.html" },
    { n: 20, date: "2026-10-05", title: "Airflow TaskFlow API, and why XCom is not a data transport", file: "lessons/0020-airflow-taskflow-and-xcom.html" },
    { n: 21, date: "2026-10-06", title: "Airflow Assets: data-aware scheduling", file: "lessons/0021-airflow-assets.html" },
    { n: 22, date: "2026-10-07", title: "Airflow Connections, Variables & never hard-coding credentials", file: "lessons/0022-airflow-connections-and-variables.html" },
    { n: 23, date: "2026-10-08", title: "Kafka Connect and CDC with Debezium", file: "lessons/0023-kafka-connect-and-cdc-with-debezium.html" },
    { n: 24, date: "2026-10-09", title: "Cosmos: dbt models as individual Airflow tasks", file: "lessons/0024-airflow-cosmos-dbt-as-tasks.html" },
    { n: 25, date: "2026-10-10", title: "Airflow sensors, deferrable operators & deadline alerts", file: "lessons/0025-airflow-sensors-deferrable-sla.html" },
    { n: 26, date: "2026-10-11", title: "One-command demo: make demo, and a README that reads in 2 minutes", file: "lessons/0026-portfolio-one-command-demo.html" },
    { n: 27, date: "2026-10-12", title: "The data-quality story: what is tested where, and why", file: "lessons/0027-data-quality-story.html" },
    { n: 28, date: "2026-10-13", title: "What breaks at 100×: partitions, incremental models & warehouse choice", file: "lessons/0028-what-breaks-at-100x.html" },
    { n: 29, date: "2026-10-14", title: "A mock design-review walkthrough of the repo", file: "lessons/0029-design-review-walkthrough.html" },
    { n: 30, date: "2026-10-15", title: "Stream processing vs. \"land it and let dbt do it\"", file: "lessons/0030-stream-processing-vs-land-and-let-dbt.html" },
    { n: 31, date: "2026-10-16", title: "dbt environments: dev/CI/prod targets & generate_schema_name", file: "lessons/0031-dbt-environments-and-schema-naming.html" },
    { n: 32, date: "2026-10-17", title: "dbt test severity (warn/error) & store_failures", file: "lessons/0032-dbt-test-severity-and-store-failures.html" },
    { n: 33, date: "2026-10-18", title: "dbt seeds vs. sources", file: "lessons/0033-dbt-seeds-vs-sources.html" },
    { n: 34, date: "2026-10-19", title: "Kafka consumer group rebalancing", file: "lessons/0034-kafka-consumer-group-rebalancing.html" },
  ];

  const REFS = [
    { short: "Glossary", title: "Glossary — terms in software context (EN ↔ VN)",
      file: "reference/glossary.html" },
  ];

  const fmt = (iso) =>
    new Date(iso + "T12:00:00").toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" });
  const here = (file) => location.pathname.endsWith("/" + file.split("/").pop());

  // ---- top bar, injected on every page ----
  // Only the course name, a lessons toggle and the reference links. The full
  // lesson list lives in a slide-out drawer so it never crowds the content.
  const nav = document.createElement("nav");
  nav.className = "course-nav";

  const toggle = document.createElement("button");
  toggle.type = "button";
  toggle.className = "nav-toggle";
  toggle.setAttribute("aria-controls", "lesson-drawer");
  toggle.setAttribute("aria-expanded", "false");
  toggle.innerHTML = '<span aria-hidden="true">☰</span> Lessons';
  nav.appendChild(toggle);

  const home = document.createElement("a");
  home.className = "nav-home";
  home.href = ROOT + "index.html";
  home.textContent = "Data Pipelines";
  nav.appendChild(home);

  const right = document.createElement("span");
  right.className = "nav-right";
  REFS.forEach((r) => {
    const a = document.createElement("a");
    a.href = ROOT + r.file;
    a.textContent = r.short;
    a.title = r.title;
    if (here(r.file)) a.classList.add("current-ref");
    right.appendChild(a);
  });
  nav.appendChild(right);
  document.body.prepend(nav);

  // ---- lesson drawer (toggled from the top bar; Esc or backdrop closes) ----
  const drawer = document.createElement("aside");
  drawer.id = "lesson-drawer";
  drawer.className = "lesson-drawer";
  drawer.setAttribute("aria-label", "Lessons");
  drawer.innerHTML =
    `<div class="drawer-head"><a class="drawer-title" href="${ROOT}index.html">Data Pipelines</a>` +
    `<button type="button" class="drawer-close" aria-label="Close lesson list">×</button></div>` +
    `<input class="drawer-filter" type="search" placeholder="Filter by number or title…" aria-label="Filter lessons">`;
  const list = document.createElement("ol");
  list.className = "drawer-list";
  LESSONS.forEach((l) => {
    const item = document.createElement("a");
    item.href = ROOT + l.file;
    if (here(l.file)) { item.classList.add("current"); item.setAttribute("aria-current", "page"); }
    const num = document.createElement("span");
    num.className = "dl-num";
    num.textContent = l.n;
    const title = document.createElement("span");
    title.className = "dl-title";
    title.textContent = l.title;
    item.append(num, title);
    const li = document.createElement("li");
    li.dataset.search = (l.n + " " + l.title).toLowerCase();
    li.appendChild(item);
    list.appendChild(li);
  });
  drawer.appendChild(list);
  const scrim = document.createElement("div");
  scrim.className = "drawer-scrim";
  document.body.append(drawer, scrim);

  const filter = drawer.querySelector(".drawer-filter");
  filter.addEventListener("input", () => {
    const q = filter.value.trim().toLowerCase();
    list.querySelectorAll("li").forEach((li) => { li.hidden = !!q && !li.dataset.search.includes(q); });
  });
  const setOpen = (on) => {
    document.documentElement.classList.toggle("drawer-open", on);
    toggle.setAttribute("aria-expanded", String(on));
    if (on) {
      const cur = list.querySelector(".current");
      if (cur) cur.scrollIntoView({ block: "center" });
      // Skip auto-focus on touch screens so the keyboard doesn't pop up.
      if (matchMedia("(hover: hover)").matches) filter.focus({ preventScroll: true });
    } else if (drawer.contains(document.activeElement)) {
      toggle.focus();
    }
  };
  toggle.addEventListener("click", () => setOpen(!document.documentElement.classList.contains("drawer-open")));
  drawer.querySelector(".drawer-close").addEventListener("click", () => setOpen(false));
  scrim.addEventListener("click", () => setOpen(false));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && document.documentElement.classList.contains("drawer-open")) setOpen(false);
  });

  // ---- course home: lesson list ----
  const idx = document.getElementById("course-index");
  if (idx) {
    LESSONS.forEach((l) => {
      const row = document.createElement("div");
      row.className = "idx-day unlocked";
      row.innerHTML =
        `<span class="idx-num">Lesson ${l.n}</span>` +
        `<span class="idx-body"><a href="${ROOT + l.file}">${l.title}</a></span>` +
        `<span class="idx-status">${fmt(l.date)}</span>`;
      idx.appendChild(row);
    });
  }

  // ---- course home: references ----
  const refBox = document.getElementById("course-refs");
  if (refBox) {
    REFS.forEach((r) => {
      const row = document.createElement("div");
      row.className = "idx-day unlocked";
      row.innerHTML =
        `<span class="idx-num">Ref</span>` +
        `<span class="idx-body"><a href="${ROOT + r.file}">${r.title}</a></span>` +
        `<span class="idx-status">always open</span>`;
      refBox.appendChild(row);
    });
  }
})();

// ---- copy button on code blocks ----
// Every <pre> gets a "Copy" button (top-right). Wrapping in a div keeps the
// button pinned while the <pre> scrolls horizontally, and keeps the button
// text out of the copied/selected content. Styles live in course.css.
(() => {
  const copyText = (text) => {
    if (navigator.clipboard && navigator.clipboard.writeText)
      return navigator.clipboard.writeText(text);
    return new Promise((resolve, reject) => {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.style.cssText = "position:fixed;opacity:0";
      document.body.appendChild(ta);
      ta.select();
      const ok = document.execCommand("copy");
      ta.remove();
      ok ? resolve() : reject(new Error("copy failed"));
    });
  };

  document.querySelectorAll("pre").forEach((pre) => {
    const wrap = document.createElement("div");
    wrap.className = "code-wrap";
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "copy-btn";
    btn.textContent = "Copy";
    btn.setAttribute("aria-label", "Copy code to clipboard");
    btn.addEventListener("click", () => {
      const code = pre.querySelector("code");
      copyText((code || pre).textContent.replace(/\n$/, "")).then(() => {
        btn.textContent = "Copied!";
        btn.classList.add("copied");
        setTimeout(() => {
          btn.textContent = "Copy";
          btn.classList.remove("copied");
        }, 1500);
      }).catch(() => { btn.textContent = "Press ⌘C"; });
    });
    wrap.appendChild(btn);
  });
})();
