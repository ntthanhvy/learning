// Course navigation. Single source of truth for the lesson & reference lists.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Phase 1 (Days 1-7) is date-locked to the filenames pre-assigned in PLAN.md;
// from 2026-08-05 the course is open-ended — register each new lesson here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";

  const LESSONS = [
    { n: 1, date: "2026-07-29", title: "Names, objects & mutability",
      file: "lessons/0001-names-objects-and-mutability.html" },
    { n: 2, date: "2026-07-30", title: "Comprehensions & slicing: retiring the loop",
      file: "lessons/0002-comprehensions-and-slicing.html" },
    { n: 3, date: "2026-07-31", title: "dict & set: grouping without pandas",
      file: "lessons/0003-dict-set-and-grouping.html" },
    { n: 4, date: "2026-08-01", title: "Functions that pull their weight",
      file: "lessons/0004-functions-args-and-key.html" },
    { n: 5, date: "2026-08-02", title: "Iterators & generators: lazy pipelines",
      file: "lessons/0005-iterators-and-generators.html" },
    { n: 6, date: "2026-08-03", title: "Files, formats & context managers",
      file: "lessons/0006-files-formats-and-with.html" },
    { n: 7, date: "2026-08-04", title: "Dataclasses, typing & an ETL capstone",
      file: "lessons/0007-dataclasses-typing-capstone.html" },
    { n: 8, date: "2026-08-05", title: "Exceptions: catching failure on purpose",
      file: "lessons/0008-exceptions.html" },
    { n: 9, date: "2026-08-06", title: "Modules, packages & imports",
      file: "lessons/0009-modules-imports-and-layout.html" },
    { n: 10, date: "2026-08-07", title: "Environments & pyproject.toml",
      file: "lessons/0010-environments-and-pyproject.html" },
    { n: 11, date: "2026-08-08", title: "Testing with pytest",
      file: "lessons/0011-testing-with-pytest.html" },
    { n: 12, date: "2026-08-09", title: "Decorators",
      file: "lessons/0012-decorators.html" },
    { n: 13, date: "2026-08-10", title: "pathlib",
      file: "lessons/0013-pathlib.html" },
    { n: 14, date: "2026-08-11", title: "datetime & timezones",
      file: "lessons/0014-datetime-and-timezones.html" },
    { n: 15, date: "2026-08-12", title: "logging",
      file: "lessons/0015-logging.html" },
    { n: 16, date: "2026-08-13", title: "FastAPI handlers, path/query params & status codes",
      file: "lessons/0016-fastapi-handlers-and-status-codes.html" },
    { n: 17, date: "2026-08-14", title: "pydantic models: validation, coercion & settings",
      file: "lessons/0017-pydantic-models-and-validation.html" },
    { n: 18, date: "2026-08-15", title: "Request/response schemas: the type hints ARE the contract",
      file: "lessons/0018-request-response-schemas.html" },
    { n: 19, date: "2026-08-16", title: "Dependency injection with Depends() & structuring an app",
      file: "lessons/0019-dependency-injection-and-app-structure.html" },
    { n: 20, date: "2026-08-17", title: "async/await: what it buys, when it doesn't, and blocking-call traps",
      file: "lessons/0020-async-await-and-blocking-calls.html" },
    { n: 21, date: "2026-08-18", title: "Talking to PostgreSQL from Python",
      file: "lessons/0021-talking-to-postgresql.html" },
    { n: 22, date: "2026-08-19", title: "Testing endpoints with httpx",
      file: "lessons/0022-testing-with-httpx.html" },
    { n: 23, date: "2026-08-20", title: "Error handling: custom exceptions, exception handlers & a consistent error shape",
      file: "lessons/0023-error-handling-and-exception-handlers.html" },
    { n: 24, date: "2026-08-21", title: "ASGI middleware: wrapping every request/response",
      file: "lessons/0024-asgi-middleware.html" },
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
  home.textContent = "Python Intensive";
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
