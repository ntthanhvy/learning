// Quiz component. Markup contract:
// <div class="quiz">
//   <div class="q" data-why="explanation shown after answering">
//     <p class="stem">Question?</p>
//     <button class="opt" data-ok>Right answer</button>
//     <button class="opt">Wrong answer</button>
//   </div>
// </div>
// Options are shuffled on load so position carries no signal.
//
// Answers are also synced (best-effort) to the local progress helper
// (progress-sync on 127.0.0.1:8477 → Neon course_progress). Fails silently
// when the helper isn't running or the page is hosted remotely — the page
// itself never holds credentials.
const QUIZ_COURSE = (location.pathname.match(/\/(go|rust|backend|data)\//) || [])[1];
function quizSync(q, ok) {
  if (!QUIZ_COURSE) return;
  const stem = ((q.querySelector(".stem") || {}).textContent || "").trim().slice(0, 80);
  try {
    fetch("http://127.0.0.1:8477/record", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        course: QUIZ_COURSE,
        kind: "quiz",
        lesson: location.pathname.split("/").pop(),
        detail: { stem, ok },
      }),
      keepalive: true,
    }).catch(() => {});
  } catch { /* sync is optional */ }
}

document.querySelectorAll(".quiz .q").forEach((q) => {
  const opts = Array.from(q.querySelectorAll("button.opt"));
  // shuffle in place
  opts
    .map((el) => ({ el, r: Math.random() }))
    .sort((a, b) => a.r - b.r)
    .forEach(({ el }) => q.appendChild(el));
  const why = document.createElement("p");
  why.className = "why";
  why.textContent = q.dataset.why || "";
  q.appendChild(why);
  opts.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (q.classList.contains("answered")) return;
      q.classList.add("answered");
      const ok = btn.hasAttribute("data-ok");
      btn.classList.add(ok ? "correct" : "wrong");
      if (!ok) {
        opts.find((b) => b.hasAttribute("data-ok")).classList.add("correct");
      }
      quizSync(q, ok);
    });
  });
});
