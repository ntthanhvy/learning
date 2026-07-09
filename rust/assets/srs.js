// Daily practice engine: samples due questions from window.QUIZ_BANK using a
// Leitner spaced-repetition schedule, plus one kata. Progress in localStorage.
// Needs nav.js loaded first (window.COURSE) and quiz-bank.js (window.QUIZ_BANK).
// Include only on daily.html — it renders into #daily-quiz and #daily-kata.
(() => {
  const KEY = "rust-srs-v1";
  const INTERVALS = { 1: 1, 2: 2, 3: 4, 4: 8, 5: 16 }; // box -> days until next review
  const MAX_QUESTIONS = 8;

  const bank = window.QUIZ_BANK || [];
  const course = window.COURSE || { lessons: [], today: "" };
  const today = course.today;

  const unlockedDays = new Set(
    course.lessons.filter((l) => l.date <= today).map((l) => l.day)
  );

  const load = () => {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch { return {}; }
  };
  const save = (state) => localStorage.setItem(KEY, JSON.stringify(state));

  const addDays = (iso, n) => {
    const d = new Date(iso + "T12:00:00");
    d.setDate(d.getDate() + n);
    const pad = (x) => String(x).padStart(2, "0");
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  };

  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };

  const state = load();

  // Best-effort sync to the local progress helper (progress-sync, 127.0.0.1:8477
  // → Neon course_progress). Silent no-op when the helper isn't running or the
  // page is hosted remotely; localStorage stays the scheduling source of truth.
  const sync = (kind, day, detail) => {
    if (!/\/rust\//.test(location.pathname)) return;
    try {
      fetch("http://127.0.0.1:8477/record", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ course: "rust", kind, day, detail }),
        keepalive: true,
      }).catch(() => {});
    } catch { /* sync is optional */ }
  };

  // ---- pick today's questions: unlocked + (never seen OR due), weakest boxes first
  const questions = bank.filter((e) => !e.type && unlockedDays.has(e.day));
  const due = questions.filter((q) => {
    const s = state[q.id];
    return !s || s.due <= today;
  });
  due.sort((a, b) => ((state[a.id] || { box: 0 }).box) - ((state[b.id] || { box: 0 }).box));
  const session = shuffle(due.slice(0, MAX_QUESTIONS));

  // ---- render quiz
  const quizBox = document.getElementById("daily-quiz");
  let answered = 0, correct = 0;
  if (quizBox) {
    if (session.length === 0) {
      quizBox.innerHTML = questions.length === 0
        ? `<p class="srs-empty">The quiz bank is empty — it fills up as lessons unlock. Come back after Day 1.</p>`
        : `<p class="srs-empty">Nothing due today — every card is scheduled ahead. Come back tomorrow. ✅</p>`;
    } else {
      const scoreLine = document.createElement("p");
      scoreLine.className = "srs-score";
      scoreLine.textContent = `${session.length} question${session.length > 1 ? "s" : ""} due today.`;

      session.forEach((q) => {
        const div = document.createElement("div");
        div.className = "q";
        const stem = document.createElement("p");
        stem.className = "stem";
        stem.innerHTML = q.stem;
        div.appendChild(stem);

        let done = false;
        shuffle(q.opts).forEach((o) => {
          const btn = document.createElement("button");
          btn.className = "opt";
          btn.innerHTML = o.t;
          if (o.ok) btn.dataset.ok = "1";
          btn.addEventListener("click", () => {
            if (done) return;
            done = true;
            answered++;
            const s = state[q.id] || { box: 0 };
            if (o.ok) {
              correct++;
              btn.classList.add("correct");
              s.box = Math.min((s.box || 0) + 1, 5);
            } else {
              btn.classList.add("wrong");
              div.querySelectorAll(".opt[data-ok]").forEach((b) => b.classList.add("correct"));
              s.box = 1;
            }
            s.due = addDays(today, INTERVALS[s.box]);
            state[q.id] = s;
            save(state);
            sync("quiz", q.day, { id: q.id, ok: !!o.ok, box: s.box, due: s.due });
            div.classList.add("answered");
            const why = document.createElement("p");
            why.className = "why";
            why.innerHTML = (o.ok ? "✅ " : "❌ ") + q.why +
              ` <span class="srs-next">(next review: ${s.due})</span>`;
            div.appendChild(why);
            if (answered === session.length) {
              scoreLine.textContent = `Done: ${correct}/${session.length} correct. ` +
                (correct === session.length ? "Perfect — gaps grow longer. 🎯" : "Missed cards return tomorrow.");
            }
          });
          div.appendChild(btn);
        });
        quizBox.appendChild(div);
      });
      quizBox.appendChild(scoreLine);
    }
  }

  // ---- kata of the day: undone first, then least recently done
  const kataBox = document.getElementById("daily-kata");
  if (kataBox) {
    const katas = bank.filter((e) => e.type === "kata" && unlockedDays.has(e.day));
    if (katas.length === 0) {
      kataBox.innerHTML = `<p class="srs-empty">No katas yet — one arrives with each lesson.</p>`;
    } else {
      katas.sort((a, b) => ((state[a.id] || {}).done || "0") < ((state[b.id] || {}).done || "0") ? -1 : 1);
      const k = katas[0];
      kataBox.innerHTML =
        `<h3>${k.title} <span class="srs-kata-day">(from Day ${k.day})</span></h3>` +
        `<div class="kata-task">${k.task}</div>` +
        `<details class="kata-solution"><summary>Show solution (try first!)</summary>${k.solution}</details>`;
      const btn = document.createElement("button");
      btn.className = "opt kata-done";
      btn.textContent = (state[k.id] || {}).done ? `Done before (${state[k.id].done}) — mark done again` : "Mark kata done";
      btn.addEventListener("click", () => {
        state[k.id] = { done: today };
        save(state);
        sync("kata", k.day, { id: k.id });
        btn.textContent = `Marked done today ✅`;
      });
      kataBox.appendChild(btn);
    }
  }
})();
