// Course registry for the landing page (/index.html).
// ADD NEW COURSES HERE — one entry renders one card; nothing else to touch.
// Fields: id (accent color key), title, desc, start/end (ISO, end omitted =
// open-ended), links [{label, href}] — first link is the primary button.
window.COURSES = [
  {
    id: "go",
    accent: "#00728f",
    title: "Go Intensive",
    desc: "Backend depth without frameworks: interfaces, errors, concurrency, the HTTP server — plus PostgreSQL modeling and queries. One week, one growing project.",
    start: "2026-07-07",
    end: "2026-07-13",
    days: 7,
    links: [
      { label: "Open course", href: "go/index.html" },
      { label: "Glossary", href: "go/reference/glossary.html" },
    ],
  },
  {
    id: "rust",
    accent: "#a53d00",
    title: "Rust Intensive",
    desc: "From zero to an axum HTTP service in a week: ownership, enums + match, Result, traits, async. Then an open-ended daily quiz + kata to make it stick.",
    start: "2026-07-08",
    end: "2026-07-14",
    days: 7,
    after: { label: "Daily practice continues", href: "rust/daily.html" },
    links: [
      { label: "Open course", href: "rust/index.html" },
      { label: "Daily practice", href: "rust/daily.html" },
      { label: "Glossary", href: "rust/reference/glossary.html" },
    ],
  },
  {
    id: "backend",
    accent: "#a86a2d",
    title: "Backend Foundations",
    desc: "The backend mindset for a frontend-heavy dev: schema design, API contracts, runtime reasoning, auth — one ~20-minute concept lesson every morning, open-ended.",
    start: "2026-07-07",
    links: [
      { label: "Open course", href: "backend/index.html" },
      { label: "Glossary", href: "backend/reference/glossary.html" },
    ],
  },
  {
    id: "interview-go",
    accent: "#1f6e43",
    title: "Go Interview Screening Kit",
    desc: "The other side of the table: 20 screening questions for a 3–4 yr Go backend candidate, each with answer guidelines, red flags, follow-up probes, and a printable 1–5 scorecard. Nothing date-locked.",
    start: "2026-07-16",
    end: "2026-07-16",
    days: 1,
    after: { label: "Ready whenever an interview lands", href: "interview-go/index.html" },
    links: [
      { label: "Open kit", href: "interview-go/index.html" },
      { label: "Scorecard", href: "interview-go/reference/scorecard.html" },
    ],
  },
  {
    id: "data",
    accent: "#5a3d99",
    title: "Data Wrangling",
    desc: "pandas + NumPy for ETL/ELT interviews: tables-not-loops thinking, cleaning, groupby, joins, reshaping — taught through SQL you already know. Light daily lessons now, main track after the intensives.",
    start: "2026-07-09",
    links: [
      { label: "Open course", href: "data/index.html" },
      { label: "Glossary", href: "data/reference/glossary.html" },
    ],
  },
];

(() => {
  const box = document.getElementById("course-list");
  if (!box) return;

  const pad = (n) => String(n).padStart(2, "0");
  const now = new Date();
  const today = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;
  const fmt = (iso) =>
    new Date(iso + "T12:00:00").toLocaleDateString("en-GB", { day: "numeric", month: "short" });
  const dayNumber = (start) =>
    Math.floor((new Date(today + "T12:00:00") - new Date(start + "T12:00:00")) / 86400000) + 1;

  const status = (c) => {
    if (today < c.start) return `starts ${fmt(c.start)}`;
    if (!c.end) return `open-ended · lesson ${dayNumber(c.start)} arrives each morning`;
    if (today > c.end) return c.after ? c.after.label.toLowerCase() : "completed";
    return `Day ${dayNumber(c.start)} of ${c.days} · today's lesson is open`;
  };

  window.COURSES.forEach((c) => {
    const card = document.createElement("div");
    card.className = "course-card";
    card.style.borderTopColor = c.accent;
    const active = today >= c.start && (!c.end || today <= c.end);
    card.innerHTML =
      `<h2 style="color:${c.accent}">${c.title}</h2>` +
      `<p class="course-status">${active ? "● " : ""}${status(c)}</p>` +
      `<p class="course-desc">${c.desc}</p>` +
      `<p class="course-links">` +
      c.links
        .map((l, i) => `<a class="${i === 0 ? "primary" : ""}" href="${l.href}">${l.label}</a>`)
        .join(" ") +
      `</p>`;
    box.appendChild(card);
  });
})();
