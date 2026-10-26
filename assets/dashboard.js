// Progress dashboard for the landing page (/index.html).
// Reads window.COURSES (courses.js) and window.PROGRESS (progress.js, written each
// morning by bin/export-progress in CI). Nothing to edit here when courses change.
(() => {
  const box = document.getElementById("dashboard");
  const P = window.PROGRESS;
  if (!box || !P) return;

  const pad = (n) => String(n).padStart(2, "0");
  const iso = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const parse = (s) => new Date(s + "T12:00:00");
  const addDays = (d, n) => new Date(d.getFullYear(), d.getMonth(), d.getDate() + n, 12);
  const fmt = (s, opts = { day: "numeric", month: "short" }) => parse(s).toLocaleDateString("en-GB", opts);
  const esc = (s) => String(s).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[ch]);
  const today = iso(new Date());
  const titleOf = Object.fromEntries(window.COURSES.map((c) => [c.id, c.title]));

  // --- roll activity up by day and by course --------------------------------
  const byDay = {};
  const studied = {};
  let quiz = 0, quizOk = 0;
  for (const a of P.activity) {
    (byDay[a.date] ||= { events: 0, courses: [] }).events += a.events;
    byDay[a.date].courses.push(a);
    (studied[a.course] ||= new Set());
    a.lessons.forEach((l) => studied[a.course].add(l));
    quiz += a.quiz;
    quizOk += a.quiz_ok;
  }
  const days = Object.keys(byDay).sort();

  let longest = 0, run = 0, prev = null;
  for (const d of days) {
    run = prev && iso(addDays(parse(prev), 1)) === d ? run + 1 : 1;
    longest = Math.max(longest, run);
    prev = d;
  }
  // Current streak: consecutive days ending today (or yesterday, before today's session).
  let current = 0;
  for (let d = byDay[today] ? parse(today) : addDays(parse(today), -1); byDay[iso(d)]; d = addDays(d, -1)) current++;

  const published = Object.values(P.courses).reduce((s, c) => s + c.lessons, 0);
  const studiedTotal = Object.values(studied).reduce((s, set) => s + set.size, 0);
  const last = days[days.length - 1];

  // --- stat tiles ------------------------------------------------------------
  const tile = (value, label, sub) =>
    `<div class="stat"><div class="stat-value">${value}</div><div class="stat-label">${label}</div>` +
    (sub ? `<div class="stat-sub">${sub}</div>` : "") + `</div>`;
  const tiles =
    tile(studiedTotal, "lessons studied", `of ${published} published`) +
    tile(days.length, "days committed", last ? `last: ${fmt(last)}` : "none recorded yet") +
    tile(current, "day streak", `longest: ${longest} day${longest === 1 ? "" : "s"}`) +
    tile(quiz ? Math.round((100 * quizOk) / quiz) + "%" : "–", "quiz accuracy", `${quizOk} / ${quiz} answers`);

  // --- calendar heatmap: one column per week, Mon→Sun ------------------------
  const starts = window.COURSES.map((c) => c.start).sort();
  const first = parse(starts[0]);
  const gridStart = addDays(first, -((first.getDay() + 6) % 7)); // back to Monday
  const level = (n) => (!n ? 0 : n < 3 ? 1 : n < 6 ? 2 : n < 10 ? 3 : 4);
  let cells = "", months = "", lastMonth = -1, col = 0;
  for (let wk = gridStart; iso(wk) <= today; wk = addDays(wk, 7), col++) {
    if (wk.getMonth() !== lastMonth) {
      months += `<span style="grid-column:${col + 1}">${wk.toLocaleDateString("en-GB", { month: "short" })}</span>`;
      lastMonth = wk.getMonth();
    }
    for (let i = 0; i < 7; i++) {
      const d = iso(addDays(wk, i));
      if (d > today) break;
      const day = byDay[d];
      const tip = day
        ? `<b>${fmt(d, { weekday: "short", day: "numeric", month: "short" })}</b> · ${day.events} activit${day.events === 1 ? "y" : "ies"}<br>` +
          day.courses.map((a) => `${esc(titleOf[a.course] || a.course)}: ${a.quiz ? `${a.quiz_ok}/${a.quiz} quiz` : `${a.events} done`}`).join("<br>")
        : `<b>${fmt(d, { weekday: "short", day: "numeric", month: "short" })}</b> · no study recorded`;
      cells += `<i class="cell l${level(day && day.events)}" style="grid-column:${col + 1};grid-row:${i + 1}" data-tip="${esc(tip)}"></i>`;
    }
  }
  const heat =
    `<div class="heat-scroll"><div class="heat">` +
    `<div class="heat-months" style="grid-template-columns:repeat(${col},var(--cell))">${months}</div>` +
    `<div class="heat-days"><span>Mon</span><span></span><span>Wed</span><span></span><span>Fri</span><span></span><span></span></div>` +
    `<div class="heat-grid" style="grid-template-columns:repeat(${col},var(--cell))">${cells}</div>` +
    `</div></div>` +
    `<div class="heat-legend">Less <i class="cell l0"></i><i class="cell l1"></i><i class="cell l2"></i><i class="cell l3"></i><i class="cell l4"></i> More</div>`;

  // --- per-course bars: published track, studied fill -------------------------
  const max = Math.max(...Object.values(P.courses).map((c) => c.lessons));
  const rows = window.COURSES.filter((c) => P.courses[c.id]).map((c) => {
    const n = P.courses[c.id].lessons, s = studied[c.id] ? studied[c.id].size : 0;
    const tip = `<b>${esc(c.title)}</b><br>${n} lessons published · ${s} studied` +
      (P.courses[c.id].latest ? `<br>latest lesson ${fmt(P.courses[c.id].latest)}` : "");
    return `<tr data-tip="${esc(tip)}">` +
      `<th scope="row"><img class="course-icon" src="assets/icons/${c.id}.svg" alt="">${esc(c.title)}</th>` +
      `<td class="bar-cell"><div class="bar" style="width:${(100 * n) / max}%">` +
      `<div class="bar-fill" style="width:${n ? (100 * s) / n : 0}%"></div></div></td>` +
      `<td class="num">${s} <span>/ ${n}</span></td></tr>`;
  }).join("");

  box.innerHTML =
    `<div class="stats">${tiles}</div>` +
    `<h3>Days committed</h3>${heat}` +
    `<h3>Lessons by course <span class="key"><i class="key-pub"></i>published <i class="key-std"></i>studied</span></h3>` +
    `<table class="course-bars"><thead><tr><th>Course</th><th></th><th class="num">Studied / published</th></tr></thead><tbody>${rows}</tbody></table>` +
    `<p class="dash-note">“Studied” counts lessons with a quiz, kata or completion recorded in a teacher session. Updated ${fmt(P.generated.slice(0, 10))} with the 06:00 lesson run.</p>`;

  // --- one shared tooltip for cells and rows ---------------------------------
  const tipEl = document.createElement("div");
  tipEl.className = "dash-tip";
  document.body.appendChild(tipEl);
  box.addEventListener("mouseover", (e) => {
    const t = e.target.closest("[data-tip]");
    if (!t) return void (tipEl.style.opacity = 0);
    tipEl.innerHTML = t.dataset.tip;
    tipEl.style.opacity = 1;
  });
  box.addEventListener("mousemove", (e) => {
    const x = Math.min(e.clientX + 14, window.innerWidth - tipEl.offsetWidth - 8);
    tipEl.style.transform = `translate(${x}px, ${e.clientY + 16}px)`;
  });
  box.addEventListener("mouseleave", () => (tipEl.style.opacity = 0));
})();
