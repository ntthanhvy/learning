# Gap: pointer syntax and composite-literal construction are blurry

User asked for a revision of variable declaration forms and type construction — specifically `*` and the `&T{}` construct. Their Go reading fluency has gaps at the fundamentals level despite overall "writes Go" experience; likely they've used these forms by pattern-matching without a firm model of pointer-vs-value semantics.

**Evidence:** Requested refresher 2026-07-07 after the Day 1 scaffold used `*MemStore`, `&MemStore{}`, pointer receivers, and `var _ Store = (*MemStore)(nil)`. Further refines [[0001-prior-knowledge-baseline]] and [[0003-practice-granularity-calibration]].

**Implications:** Delivered lesson 0002 (vars/pointers refresher) + glossary Basics section. Future lessons must not assume fluency in: pointer receivers, value-copy semantics, make vs new, nil-map behavior. These matter again at Day 3 (sharing state across goroutines is pointer semantics + a mutex) and Day 6 (pgx scanning into &struct fields) — open both with a recall question on pointer semantics. Watch for similar pattern-matched-but-not-modeled gaps (likely candidates: slices vs arrays, string/byte handling).
