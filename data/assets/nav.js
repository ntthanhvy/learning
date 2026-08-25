// Course navigation. Single source of truth for the lesson & reference lists.
// Include on every page: <script src="../assets/nav.js"></script> (end of body).
// Like the backend course, there is no date-locking: this course is open-ended
// and lessons are generated one at a time — register each new lesson/reference here.
(() => {
  const ROOT = /\/(lessons|reference)\//.test(location.pathname) ? "../" : "";

  const LESSONS = [
    { n: 1, date: "2026-07-09", title: "Think in tables, not loops",
      file: "lessons/0001-think-in-tables-not-loops.html" },
    { n: 2, date: "2026-07-10", title: "Load & inspect real files",
      file: "lessons/0002-load-and-inspect.html" },
    { n: 3, date: "2026-07-11", title: "Missing data & cleaning",
      file: "lessons/0003-missing-data-and-cleaning.html" },
    { n: 4, date: "2026-07-12", title: "GroupBy: split, apply, combine",
      file: "lessons/0004-groupby-split-apply-combine.html" },
    { n: 5, date: "2026-07-13", title: "Merge & join",
      file: "lessons/0005-merge-and-join.html" },
    { n: 6, date: "2026-07-14", title: "Reshape: pivot & melt",
      file: "lessons/0006-reshape-pivot-and-melt.html" },
    { n: 7, date: "2026-07-15", title: "Rank & cumulative operations",
      file: "lessons/0007-rank-and-cumulative-operations.html" },
    { n: 8, date: "2026-07-16", title: "Method chaining & pipeline shape",
      file: "lessons/0008-method-chaining-pipeline-shape.html" },
    { n: 9, date: "2026-07-17", title: "Timed drills",
      file: "lessons/0009-timed-drills.html" },
    { n: 10, date: "2026-07-18", title: "Timed drills, round 2: value_counts, .str & nlargest",
      file: "lessons/0010-value-counts-str-and-nlargest.html" },
    { n: 11, date: "2026-07-19", title: "Timed drills, round 3: duplicates & pct_change",
      file: "lessons/0011-duplicates-and-pct-change.html" },
    { n: 12, date: "2026-07-20", title: "Timed drills, round 4: apply() & binning with cut()",
      file: "lessons/0012-apply-and-binning.html" },
    { n: 13, date: "2026-07-21", title: "Timed drills, round 5: rolling & expanding windows",
      file: "lessons/0013-rolling-and-expanding-windows.html" },
    { n: 14, date: "2026-07-22", title: "Melt revisited: multiple metrics at once",
      file: "lessons/0014-multi-metric-melt.html" },
    { n: 15, date: "2026-07-23", title: "Unstack: pulling a row-index level back into columns",
      file: "lessons/0015-unstack.html" },
    { n: 16, date: "2026-07-24", title: "Transform: broadcasting a group value back to every row",
      file: "lessons/0016-transform-group-relative-values.html" },
    { n: 17, date: "2026-07-25", title: "crosstab(): frequency tables done right",
      file: "lessons/0017-crosstab.html" },
    { n: 18, date: "2026-07-26", title: "qcut(): binning by rank, not by value",
      file: "lessons/0018-qcut.html" },
    { n: 19, date: "2026-07-27", title: "nunique() and explode(): counting distinct, and un-nesting lists",
      file: "lessons/0019-nunique-and-explode.html" },
    { n: 20, date: "2026-07-28", title: "idxmax() and idxmin(): WHICH row, not just the value",
      file: "lessons/0020-idxmax-and-idxmin.html" },
    { n: 21, date: "2026-07-29", title: "pd.concat(): stacking DataFrames",
      file: "lessons/0021-concat-stacking-dataframes.html" },
    { n: 22, date: "2026-07-30", title: "query(): WHERE, spelled as a string",
      file: "lessons/0022-query-method.html" },
    { n: 23, date: "2026-07-31", title: "shift(): LAG/LEAD, spelled in pandas",
      file: "lessons/0023-shift-lag-lead.html" },
    { n: 24, date: "2026-08-01", title: "np.where() and np.select(): vectorized if/else",
      file: "lessons/0024-np-where-and-np-select.html" },
    { n: 25, date: "2026-08-02", title: "select_dtypes() and the category dtype",
      file: "lessons/0025-select-dtypes-and-category.html" },
    { n: 26, date: "2026-08-03", title: "SettingWithCopy and .copy(): views vs copies",
      file: "lessons/0026-settingwithcopy-and-copy.html" },
    { n: 27, date: "2026-08-04", title: ".map(): recoding a Series value-by-value",
      file: "lessons/0027-map-value-mapping.html" },
    { n: 28, date: "2026-08-05", title: "pd.wide_to_long(): melting several metrics at once",
      file: "lessons/0028-wide-to-long.html" },
    { n: 29, date: "2026-08-06", title: "isin(): filtering against a list of values",
      file: "lessons/0029-isin.html" },
    { n: 30, date: "2026-08-07", title: "Broadcasting: why pandas arithmetic \"just works\"",
      file: "lessons/0030-broadcasting.html" },
    { n: 31, date: "2026-08-08", title: "sort_values() and reset_index() edge cases",
      file: "lessons/0031-sort-values-and-reset-index.html" },
    { n: 32, date: "2026-08-09", title: "The .dt accessor: pulling parts out of a datetime column",
      file: "lessons/0032-dt-accessor-datetime-columns.html" },
    { n: 33, date: "2026-08-10", title: "set_index(): making a real column the row label",
      file: "lessons/0033-set-index.html" },
    { n: 34, date: "2026-08-11", title: "pd.get_dummies(): one-hot encoding a category column",
      file: "lessons/0034-get-dummies-one-hot-encoding.html" },
    { n: 35, date: "2026-08-12", title: "clip(): capping values into a min/max range",
      file: "lessons/0035-clip-bounding-values.html" },
    { n: 36, date: "2026-08-13", title: "between(): a readable range filter",
      file: "lessons/0036-between-range-filtering.html" },
    { n: 37, date: "2026-08-14", title: "combine_first(): filling gaps in one Series from another",
      file: "lessons/0037-combine-first.html" },
    { n: 38, date: "2026-08-15", title: "resample(): bucketing a datetime index into fixed periods",
      file: "lessons/0038-resample.html" },
    { n: 39, date: "2026-08-16", title: "stack(): pulling columns down into the row index",
      file: "lessons/0039-stack.html" },
    { n: 40, date: "2026-08-17", title: "groupby().filter(): keeping whole groups, not rows",
      file: "lessons/0040-groupby-filter.html" },
    { n: 41, date: "2026-08-18", title: "astype(): converting a column's dtype on purpose",
      file: "lessons/0041-astype.html" },
    { n: 42, date: "2026-08-19", title: "str.extract(): pulling structured pieces out of text",
      file: "lessons/0042-str-extract.html" },
    { n: 43, date: "2026-08-20", title: "str.extractall(): every match, not just the first",
      file: "lessons/0043-str-extractall.html" },
    { n: 44, date: "2026-08-21", title: "pivot_table() vs .pivot(), and margins=True",
      file: "lessons/0044-pivot-table-and-margins.html" },
    { n: 45, date: "2026-08-22", title: "ffill() and bfill(): carrying a value across a gap",
      file: "lessons/0045-ffill-and-bfill.html" },
    { n: 46, date: "2026-08-23", title: ".at[] and .iat[]: fast single-scalar access",
      file: "lessons/0046-at-and-iat.html" },
    { n: 47, date: "2026-08-24", title: "reindex(): forcing a chosen label set",
      file: "lessons/0047-reindex.html" },
    { n: 48, date: "2026-08-25", title: "cumcount(): a running position within each group",
      file: "lessons/0048-cumcount.html" },
    { n: 49, date: "2026-08-26", title: "describe(): the fast summary-stats sanity check",
      file: "lessons/0049-describe.html" },
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
  home.textContent = "Data Wrangling";
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
