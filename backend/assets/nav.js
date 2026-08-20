// Course navigation. Single source of truth for the lesson & reference lists.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Unlike the Go course, there is no date-locking: this course is open-ended and
// lessons are generated one at a time — register each new lesson/reference here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";

  const LESSONS = [
    { n: 1, date: "2026-07-07", title: "What happens after fetch()?",
      file: "lessons/0001-what-happens-after-fetch.html" },
    { n: 2, date: "2026-07-08", title: "Tables are not JSON",
      file: "lessons/0002-tables-are-not-json.html" },
    { n: 3, date: "2026-07-09", title: "The API contract",
      file: "lessons/0003-the-api-contract.html" },
    { n: 4, date: "2026-07-10", title: "Who are you?",
      file: "lessons/0004-who-are-you.html" },
    { n: 5, date: "2026-07-11", title: "Should I add an index?",
      file: "lessons/0005-should-i-add-an-index.html" },
    { n: 6, date: "2026-07-12", title: "What actually happens inside a transaction",
      file: "lessons/0006-what-actually-happens-in-a-transaction.html" },
    { n: 7, date: "2026-07-13", title: "What a 500 should (and shouldn't) tell the client",
      file: "lessons/0007-what-a-500-should-tell-the-client.html" },
    { n: 8, date: "2026-07-14", title: "Why two instances break your \"stateless\" server",
      file: "lessons/0008-two-instances-break-your-server.html" },
    { n: 9, date: "2026-07-15", title: "Where caching belongs",
      file: "lessons/0009-where-caching-belongs.html" },
    { n: 10, date: "2026-07-16", title: "Background jobs",
      file: "lessons/0010-background-jobs.html" },
    { n: 11, date: "2026-07-17", title: "Rate limiting & backpressure",
      file: "lessons/0011-rate-limiting-and-backpressure.html" },
    { n: 12, date: "2026-07-18", title: "Authorization: what are you allowed to do?",
      file: "lessons/0012-authorization-what-are-you-allowed-to-do.html" },
    { n: 13, date: "2026-07-19", title: "Logging & monitoring: how you find out something's wrong",
      file: "lessons/0013-logging-and-monitoring.html" },
    { n: 14, date: "2026-07-20", title: "Reading a backend PR: substance over style",
      file: "lessons/0014-reading-a-backend-pr.html" },
    { n: 15, date: "2026-07-21", title: "Pagination: offset vs. cursor",
      file: "lessons/0015-pagination-offset-vs-cursor.html" },
    { n: 16, date: "2026-07-22", title: "API versioning: what changes safely, what doesn't",
      file: "lessons/0016-api-versioning.html" },
    { n: 17, date: "2026-07-23", title: "SQL injection & input validation",
      file: "lessons/0017-sql-injection-and-input-validation.html" },
    { n: 18, date: "2026-07-24", title: "Connection pool sizing & exhaustion",
      file: "lessons/0018-connection-pool-sizing-and-exhaustion.html" },
    { n: 19, date: "2026-07-25", title: "Schema migrations: evolving a table without breaking anything",
      file: "lessons/0019-schema-migrations.html" },
    { n: 20, date: "2026-07-26", title: "Synthesis: reviewing one small feature end-to-end",
      file: "lessons/0020-synthesis-mark-order-urgent.html" },
    { n: 21, date: "2026-07-27", title: "Configuration: what belongs in code, what belongs in the environment",
      file: "lessons/0021-configuration-env-vs-code.html" },
    { n: 22, date: "2026-07-28", title: "CSRF: the other half of cookie auth",
      file: "lessons/0022-csrf-the-other-half-of-cookie-auth.html" },
    { n: 23, date: "2026-07-29", title: "Mass assignment & overexposure",
      file: "lessons/0023-mass-assignment-and-overexposure.html" },
    { n: 24, date: "2026-07-30", title: "SSRF: server-side request forgery",
      file: "lessons/0024-ssrf-server-side-request-forgery.html" },
    { n: 25, date: "2026-07-30", title: "Concurrency is not parallelism, and a goroutine is not a thread",
      file: "lessons/0025-concurrency-parallelism-threads-coroutines.html" },
    { n: 26, date: "2026-07-31", title: "Idempotency keys: making POST safe to retry",
      file: "lessons/0026-idempotency-keys-safe-retries.html" },
    { n: 27, date: "2026-08-01", title: "Graceful shutdown: what happens the instant before a process dies",
      file: "lessons/0027-graceful-shutdown.html" },
    { n: 28, date: "2026-08-02", title: "Circuit breaker: stop calling what's already down",
      file: "lessons/0028-circuit-breaker.html" },
    { n: 29, date: "2026-08-03", title: "The outbox pattern: making a DB write and an event atomic",
      file: "lessons/0029-outbox-pattern.html" },
    { n: 30, date: "2026-08-04", title: "Webhook signature verification: trusting a request from outside",
      file: "lessons/0030-webhook-signature-verification.html" },
    { n: 31, date: "2026-08-05", title: "Service-to-service auth: when the caller isn't a person",
      file: "lessons/0031-service-to-service-auth.html" },
    { n: 32, date: "2026-08-06", title: "Retries: exponential backoff and jitter",
      file: "lessons/0032-retries-exponential-backoff-and-jitter.html" },
    { n: 33, date: "2026-08-07", title: "Optimistic locking: the version-column alternative to FOR UPDATE",
      file: "lessons/0033-optimistic-locking-version-columns.html" },
    { n: 34, date: "2026-08-08", title: "Soft delete: keeping the row, hiding the record",
      file: "lessons/0034-soft-delete.html" },
    { n: 35, date: "2026-08-09", title: "Upsert: INSERT ... ON CONFLICT",
      file: "lessons/0035-upsert-insert-on-conflict.html" },
    { n: 36, date: "2026-08-10", title: "The N+1 query problem",
      file: "lessons/0036-n-plus-one-queries.html" },
    { n: 37, date: "2026-08-11", title: "Transaction isolation levels",
      file: "lessons/0037-transaction-isolation-levels.html" },
    { n: 38, date: "2026-08-12", title: "Foreign key referential actions: what happens to the children",
      file: "lessons/0038-foreign-key-referential-actions.html" },
    { n: 39, date: "2026-08-13", title: "MVCC: how Postgres actually does isolation",
      file: "lessons/0039-mvcc-how-postgres-does-isolation.html" },
    { n: 40, date: "2026-08-14", title: "Deadlocks: when two transactions wait on each other forever",
      file: "lessons/0040-deadlocks.html" },
    { n: 41, date: "2026-08-15", title: "context.Context: the cancellation signal riding along with every request",
      file: "lessons/0041-context-cancellation-and-deadlines.html" },
    { n: 42, date: "2026-08-16", title: "Interfaces and the driver abstraction",
      file: "lessons/0042-interfaces-and-the-driver-abstraction.html" },
    { n: 43, date: "2026-08-17", title: "Database views and materialized views",
      file: "lessons/0043-database-views-and-materialized-views.html" },
    { n: 44, date: "2026-08-18", title: "JSONB: when one column is allowed to be a schema of its own",
      file: "lessons/0044-jsonb-semi-structured-columns.html" },
    { n: 45, date: "2026-08-19", title: "Unit vs. integration tests: where the line actually is",
      file: "lessons/0045-unit-vs-integration-tests.html" },
    { n: 46, date: "2026-08-20", title: "Audit logging: recording what happened, not just what's true now",
      file: "lessons/0046-audit-logging-recording-what-happened.html" },
    { n: 47, date: "2026-08-21", title: "Health checks: why checking the DB in the wrong one causes cascading restarts",
      file: "lessons/0047-health-checks-cascading-restarts.html" },
  ];

  const REFS = [
    { short: "Glossary", title: "Glossary — terms in software context (EN ↔ VN)",
      file: "reference/glossary.html" },
    { short: "Concurrency", title: "Concurrency vocabulary & decision rules — thread vs coroutine, I/O- vs CPU-bound",
      file: "reference/concurrency-vocabulary.html" },
  ];

  const fmt = (iso) =>
    new Date(iso + "T12:00:00").toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" });
  const here = (file) => location.pathname.endsWith("/" + file.split("/").pop());

  // ---- top bar, injected on every page ----
  const nav = document.createElement("nav");
  nav.className = "course-nav";

  const home = document.createElement("a");
  home.className = "nav-home";
  home.href = ROOT + "index.html";
  home.textContent = "Backend Foundations";
  nav.appendChild(home);

  const days = document.createElement("span");
  days.className = "nav-days";
  LESSONS.forEach((l) => {
    const chip = document.createElement("a");
    chip.href = ROOT + l.file;
    chip.title = "Lesson " + l.n + ": " + l.title;
    if (here(l.file)) chip.classList.add("current");
    chip.classList.add("day-chip");
    chip.textContent = l.n;
    days.appendChild(chip);
  });
  nav.appendChild(days);

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
