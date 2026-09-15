// Term-gloss popups. Markup contract:
//   <dfn data-en="English, software-context explanation" data-vn="Vietnamese aid">term</dfn>
// Click/tap or Enter toggles; Escape or clicking elsewhere closes. English shows first.
(() => {
  const terms = Array.from(document.querySelectorAll("dfn[data-en]"));
  const closeAll = () => terms.forEach((t) => {
    t.classList.remove("open");
    t.setAttribute("aria-expanded", "false");
  });
  terms.forEach((t) => {
    t.tabIndex = 0;
    t.setAttribute("role", "button");
    t.setAttribute("aria-expanded", "false");
    const pop = document.createElement("span");
    pop.className = "gloss-pop";
    const en = document.createElement("span");
    en.className = "pop-en";
    en.textContent = t.dataset.en;
    pop.appendChild(en);
    if (t.dataset.vn) {
      const vn = document.createElement("span");
      vn.className = "pop-vn";
      vn.textContent = t.dataset.vn;
      pop.appendChild(vn);
    }
    pop.addEventListener("click", (e) => e.stopPropagation());
    t.appendChild(pop);
    t.addEventListener("click", (e) => {
      e.stopPropagation();
      const wasOpen = t.classList.contains("open");
      closeAll();
      if (!wasOpen) {
        // flip the popup leftwards if it would overflow the right edge
        t.classList.toggle("pop-right",
          t.getBoundingClientRect().left + 24 * 16 > window.innerWidth - 16);
        t.classList.add("open");
        t.setAttribute("aria-expanded", "true");
      }
    });
    t.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t.click(); }
      if (e.key === "Escape") closeAll();
    });
  });
  document.addEventListener("click", closeAll);
})();
