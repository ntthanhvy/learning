// Course navigation + date-based unlocking. Single source of truth for the schedule.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Lessons unlock on their date (local time); references and daily practice are always open.
// When a new lesson or reference sheet is authored, register it here.
// Exposes window.COURSE = { lessons, today } for srs.js.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";

  const LESSONS = [
    { day: 1, date: "2026-07-08", title: "Cargo & the shape of Rust",
      file: "lessons/0001-cargo-and-the-shape-of-rust.html" },
    { day: 2, date: "2026-07-09", title: "Ownership & borrowing",
      file: "lessons/0002-ownership-and-borrowing.html" },
    { day: 3, date: "2026-07-10", title: "Option, Result & errors",
      file: "lessons/0003-option-result-and-errors.html" },
    { day: 4, date: "2026-07-11", title: "Traits, generics & iterators",
      file: "lessons/0004-traits-generics-iterators.html" },
    { day: 5, date: "2026-07-12", title: "Collections, modules & serde",
      file: "lessons/0005-collections-modules-serde.html" },
    { day: 6, date: "2026-07-13", title: "Async & tokio",
      file: "lessons/0006-async-and-tokio.html" },
    { day: 7, date: "2026-07-14", title: "Capstone: an axum service",
      file: "lessons/0007-axum-capstone.html" },
  ];

  const REFS = [
    { short: "Glossary", title: "Glossary — terms in software context (EN ↔ VN)",
      file: "reference/glossary.html" },
    { short: "Daily", title: "Daily practice — quiz + kata",
      file: "daily.html" },
  ];

  const pad = (n) => String(n).padStart(2, "0");
  const now = new Date();
  const today = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;
  const unlocked = (l) => l.date <= today;
  const fmt = (iso) =>
    new Date(iso + "T12:00:00").toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" });
  const here = (file) => location.pathname.endsWith("/" + file.split("/").pop());

  window.COURSE = { lessons: LESSONS, today };

  // ---- top bar, injected on every page ----
  const nav = document.createElement("nav");
  nav.className = "course-nav";

  const home = document.createElement("a");
  home.className = "nav-home";
  home.href = ROOT + "index.html";
  home.textContent = "Rust Intensive";
  nav.appendChild(home);

  const days = document.createElement("span");
  days.className = "nav-days";
  LESSONS.forEach((l) => {
    let chip;
    if (unlocked(l)) {
      chip = document.createElement("a");
      chip.href = ROOT + l.file;
      chip.title = "Day " + l.day + ": " + l.title;
      if (here(l.file) || (l.extras || []).some((e) => here(e.file))) chip.classList.add("current");
    } else {
      chip = document.createElement("span");
      chip.classList.add("locked");
      chip.title = "Day " + l.day + ": " + l.title + " — unlocks " + fmt(l.date);
    }
    chip.classList.add("day-chip");
    chip.textContent = l.day;
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
