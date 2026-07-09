# Rust Resources

## Knowledge

- [The Rust Programming Language ("the Book")](https://doc.rust-lang.org/book/)
  The official book — the single most trusted Rust source. Use for: ownership (ch. 4), enums & match (ch. 6), error handling (ch. 9), traits (ch. 10). Primary source for most lessons.
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
  Official, runnable annotated examples. Use for: seeing any syntax in a compilable snippet fast.
- [Comprehensive Rust — Google](https://google.github.io/comprehensive-rust/)
  Google's fast-paced course for experienced developers — matches this course's "know backend, new to Rust" profile. Use for: a second explanation when the Book's pace feels slow.
- [Rustlings](https://github.com/rust-lang/rustlings)
  Official small fix-the-code exercises. Use for: extra reps on a concept; a source to adapt daily katas from.
- [Tokio tutorial](https://tokio.rs/tokio/tutorial)
  Official async runtime tutorial. Use for: Day 6 — async/await, tasks, why an executor exists.
- [axum documentation](https://docs.rs/axum/latest/axum/) and [axum examples](https://github.com/tokio-rs/axum/tree/main/examples)
  The de-facto standard Rust web framework (Tokio team; current stable 0.8). Use for: Day 7 capstone — routing, extractors, state.
- [serde documentation](https://serde.rs/)
  The standard (de)serialization framework. Use for: Day 5 — JSON in/out with derive.
- [Zero To Production in Rust — Luca Palmieri](https://www.zero2prod.com/)
  The reference book for production backend Rust. Use for: after the week, when going deeper than the capstone.
- [Rust std library docs](https://doc.rust-lang.org/std/)
  Use for: exact signatures of `Option`, `Result`, `Vec`, `HashMap`, iterator adapters.
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
  What "idiomatic" means in public API shape. Use for: capstone review, interview vocabulary.
- [Error handling crates: thiserror](https://docs.rs/thiserror/latest/thiserror/) / [anyhow](https://docs.rs/anyhow/latest/anyhow/)
  Community-standard error ergonomics. Use for: Day 3 — when to derive errors vs. bail with context.

## Wisdom (Communities)

- [users.rust-lang.org](https://users.rust-lang.org/)
  The official forum; famously welcoming to beginners. Use for: "is this idiomatic?" questions, borrow-checker fights.
- [r/rust](https://www.reddit.com/r/rust/)
  High-signal subreddit. Use for: ecosystem picks (crate X vs Y), what's current.
- [Rust Community Discord](https://discord.gg/rust-lang)
  Real-time help. Use for: quick unblocking during practice.

## Gaps

- No single trusted source found for "daily Rust quiz question banks" — we build our own (assets/quiz-bank.js), adapting exercise ideas from Rustlings and the Book's quizzes ([Brown University's interactive Book fork](https://rust-book.cs.brown.edu/) has built-in quizzes worth mining).
