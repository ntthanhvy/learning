# Day 1 practice: embedding and delegation demonstrated; zero-value trap surfaced

User completed the linkshort scaffold same-day: MemStore, LoggingStore with correct embedding + log-then-delegate Save, compile-time satisfaction check in place, vet-clean, runs. Went beyond instructions (added URL to the log attrs; chose *LoggingStore constructor return). Two gaps at review: (1) `Get` returned `s.links[code], nil` — missing-key case silently returns zero-value Link instead of ErrNotFound, i.e. the nil-map/zero-value concept from lesson 0002 hasn't transferred to the comma-ok idiom yet; (2) step 6 (fake-store test) not attempted.

**Evidence:** Code review of ~/learning/go/project/linkshort, 2026-07-07 evening.

**Implications:** Day 1 concepts (embedding, promotion, delegation, consumer-defined interface) — demonstrated, solid floor. Day 2 (errors) must open with the Get bug as its motivating example: the comma-ok lookup and ErrNotFound return ARE the first exercise. Verify the fix and the fake test landed before teaching wrapping/errors.Is. Testing habit not yet formed — keep "done when: three commands green" prominent in every practice.
