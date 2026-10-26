// Course navigation + date-based unlocking. Single source of truth for the schedule.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Lessons unlock on their date (local time); references are always open.
// When a new lesson or reference sheet is authored, register it here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";
  // Course icon as the tab favicon (icons are shared, in /assets/icons/).
  document.head.insertAdjacentHTML("beforeend", `<link rel="icon" href="${ROOT}../assets/icons/go.svg">`);

  const LESSONS = [
    { day: 1, date: "2026-07-07", title: "Interfaces & composition",
      file: "lessons/0001-interfaces-and-composition.html",
      extras: [{ title: "Refresher: variables, pointers & the &T{} construct",
                 file: "lessons/0002-vars-pointers-refresher.html" }] },
    { day: 2, date: "2026-07-08", title: "Errors as values",
      file: "lessons/0003-errors-as-values.html" },
    { day: 3, date: "2026-07-09", title: "Goroutines, channels, select",
      file: "lessons/0004-goroutines-channels-select.html" },
    { day: 4, date: "2026-07-10", title: "context, sync & the HTTP server",
      file: "lessons/0005-context-sync-http-server.html" },
    { day: 5, date: "2026-07-11", title: "Data modeling in PostgreSQL",
      file: "lessons/0006-data-modeling-postgres.html" },
    { day: 6, date: "2026-07-12", title: "Queries from Go (+ generics in the wild)",
      file: "lessons/0007-queries-from-go.html" },
    { day: 7, date: "2026-07-13", title: "Testing, tooling & capstone",
      file: "lessons/0008-testing-tooling-capstone.html" },
    { day: 8, date: "2026-07-15", title: "Mutex & the memory model",
      file: "lessons/0009-mutex-and-the-memory-model.html" },
    { day: 9, date: "2026-07-16", title: "Worker pools & pipelines",
      file: "lessons/0010-worker-pools-and-pipelines.html" },
    { day: 10, date: "2026-07-17", title: "Context, cancellation & errgroup",
      file: "lessons/0011-context-cancellation-errgroup.html" },
    { day: 11, date: "2026-07-19", title: "Debugging concurrency",
      file: "lessons/0012-debugging-concurrency.html" },
    { day: 12, date: "2026-07-20", title: "The rest of sync",
      file: "lessons/0013-the-rest-of-sync.html" },
    { day: 13, date: "2026-07-20", title: "Concurrency capstone + interview drills",
      file: "lessons/0014-concurrency-capstone.html" },
  ];

  const REFS = [
    { short: "Glossary", title: "Glossary — terms in software context (EN ↔ VN)",
      file: "reference/glossary.html" },
    { short: "Interfaces", title: "Interfaces & composition cheat sheet",
      file: "reference/interfaces-cheatsheet.html" },
  ];

  const pad = (n) => String(n).padStart(2, "0");
  const now = new Date();
  const today = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;
  const unlocked = (l) => l.date <= today;
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
  toggle.innerHTML = '<span aria-hidden="true">☰</span> Days';
  nav.appendChild(toggle);

  const home = document.createElement("a");
  home.className = "nav-home";
  home.href = ROOT + "index.html";
  home.textContent = "Go Intensive";
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
  drawer.setAttribute("aria-label", "Days");
  drawer.innerHTML =
    `<div class="drawer-head"><a class="drawer-title" href="${ROOT}index.html">Go Intensive</a>` +
    `<button type="button" class="drawer-close" aria-label="Close day list">×</button></div>` +
    `<input class="drawer-filter" type="search" placeholder="Filter by number or title…" aria-label="Filter days">`;
  const list = document.createElement("ol");
  list.className = "drawer-list";
  LESSONS.forEach((l) => {
    let item;
    if (unlocked(l)) {
      item = document.createElement("a");
      item.href = ROOT + l.file;
      if (here(l.file) || (l.extras || []).some((e) => here(e.file))) {
        item.classList.add("current");
        item.setAttribute("aria-current", "page");
      }
    } else {
      item = document.createElement("span");
      item.className = "locked";
      item.title = "Unlocks " + fmt(l.date);
    }
    const num = document.createElement("span");
    num.className = "dl-num";
    num.textContent = l.day;
    const title = document.createElement("span");
    title.className = "dl-title";
    title.textContent = l.title;
    item.append(num, title);
    const li = document.createElement("li");
    li.dataset.search = (l.day + " " + l.title).toLowerCase();
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

  // ---- course home: lesson list with lock states ----
  const idx = document.getElementById("course-index");
  if (idx) {
    LESSONS.forEach((l) => {
      const row = document.createElement("div");
      row.className = "idx-day " + (unlocked(l) ? "unlocked" : "locked");
      if (unlocked(l)) {
        row.innerHTML =
          `<span class="idx-num">Day ${l.day}</span>` +
          `<span class="idx-body"><a href="${ROOT + l.file}">${l.title}</a>` +
          (l.extras || []).map((e) => `<a class="idx-extra" href="${ROOT + e.file}">↳ ${e.title}</a>`).join("") +
          `</span><span class="idx-status">${fmt(l.date)}</span>`;
      } else {
        row.innerHTML =
          `<span class="idx-num">Day ${l.day}</span>` +
          `<span class="idx-body">${l.title}</span>` +
          `<span class="idx-status">🔒 unlocks ${fmt(l.date)}</span>`;
      }
      idx.appendChild(row);
    });
  }

  // ---- course home: always-open references ----
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
