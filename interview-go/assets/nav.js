// Course navigation for the Go Interview Screening Kit.
// Unlike the intensives, nothing here is date-locked — you may need the whole
// kit the day an interview lands on your calendar. Register new parts here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";
  // Course icon as the tab favicon (icons are shared, in /assets/icons/).
  document.head.insertAdjacentHTML("beforeend", `<link rel="icon" href="${ROOT}../assets/icons/interview-go.svg">`);

  const LESSONS = [
    { day: 1, title: "Go fundamentals",
      file: "lessons/0001-go-fundamentals.html" },
    { day: 2, title: "Concurrency — the core differentiator",
      file: "lessons/0002-concurrency.html" },
    { day: 3, title: "Backend & API design",
      file: "lessons/0003-backend-api-design.html" },
    { day: 4, title: "Data & infrastructure",
      file: "lessons/0004-data-infrastructure.html" },
    { day: 5, title: "Testing & tooling",
      file: "lessons/0005-testing-tooling.html" },
    { day: 6, title: "Calibration, red flags & running the screen",
      file: "lessons/0006-running-the-screen.html" },
  ];

  const REFS = [
    { short: "Scorecard", title: "Printable screening scorecard (1–5 rubric)",
      file: "reference/scorecard.html" },
  ];

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
  toggle.innerHTML = '<span aria-hidden="true">☰</span> Parts';
  nav.appendChild(toggle);

  const home = document.createElement("a");
  home.className = "nav-home";
  home.href = ROOT + "index.html";
  home.textContent = "Go Screening Kit";
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
  drawer.setAttribute("aria-label", "Parts");
  drawer.innerHTML =
    `<div class="drawer-head"><a class="drawer-title" href="${ROOT}index.html">Go Screening Kit</a>` +
    `<button type="button" class="drawer-close" aria-label="Close part list">×</button></div>` +
    `<input class="drawer-filter" type="search" placeholder="Filter by number or title…" aria-label="Filter parts">`;
  const list = document.createElement("ol");
  list.className = "drawer-list";
  LESSONS.forEach((l) => {
    const item = document.createElement("a");
    item.href = ROOT + l.file;
    if (here(l.file)) { item.classList.add("current"); item.setAttribute("aria-current", "page"); }
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

  // ---- course home: part list (always open) ----
  const idx = document.getElementById("course-index");
  if (idx) {
    LESSONS.forEach((l) => {
      const row = document.createElement("div");
      row.className = "idx-day unlocked";
      row.innerHTML =
        `<span class="idx-num">Part ${l.day}</span>` +
        `<span class="idx-body"><a href="${ROOT + l.file}">${l.title}</a></span>` +
        `<span class="idx-status">always open</span>`;
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
