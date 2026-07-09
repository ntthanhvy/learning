# Mission: Rust from Zero — the Gist, for Backend Work

## Why
Starting from zero Rust, grasp in one week the core of the language and the specific features that make Rust compelling for backend services — ownership & borrowing, enums + exhaustive `match`, `Result`-based errors, traits, and the async backend stack (tokio + axum + serde). This complements the parallel Go intensive: same backend goals (work + job hunting), second language for breadth. After the week, a short daily practice test (quiz + tiny kata) keeps the language from fading.

## Success looks like
- Read idiomatic Rust and explain what the compiler is complaining about — fix borrow-checker errors independently using its messages.
- Explain ownership, moves, borrows (`&` / `&mut`), and why Rust needs no garbage collector, in an interview setting.
- Use `Option`/`Result` + `?` and `match` as reflexes — no null checks, no exceptions.
- Build a small HTTP service (the linkshort domain again, mirroring the Go project) with axum, tokio, and serde.
- Articulate Rust's backend pitch: memory safety without GC, fearless concurrency, exhaustive enums, zero-cost abstractions.
- Pass the daily quiz + kata in ~15 minutes without looking things up.

## Constraints
- One week: 2026-07-08 → 2026-07-14, **in parallel with the Go week** — Rust gets ~60–90 min/day, so lessons must be lean.
- Complete beginner in Rust; experienced backend developer; one week into a Go intensive (use Go contrasts deliberately).
- Language rule (same as Go course): jargon gets click-popup glosses — English software-context first, then dev-style Vietnamese. No inline translation.
- After the week: daily quiz + tiny kata, open-ended until told to stop, drawn from a growing quiz bank.

## Out of scope
- `unsafe`, writing macros, FFI/CGo-equivalents, embedded, WASM.
- Lifetimes beyond the basics (elision, `'static`) — enough to read errors, not to design APIs around.
- Frameworks other than axum; async internals (`Pin`, executors, manual `Future` impls).
- Databases from Rust (sqlx) — the Go course owns the data layer this week; revisit later if wanted.
