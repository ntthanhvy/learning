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
  ];

  const REFS = [
    { short: "Glossary", title: "Glossary — terms in software context (EN ↔ VN)",
      file: "reference/glossary.html" },
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
