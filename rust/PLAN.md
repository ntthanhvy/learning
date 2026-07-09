# Rust Week — Plan (2026-07-08 → 2026-07-14, parallel with Go week)

Budget: ~60–90 min/day (Go intensive runs at the same time). Lessons are lean:
one concept cluster, one practice block on the running project, one quiz.

Running project: **linkshort-rs** (`~/learning/rust/project/linkshort-rs`) — the same
URL-shortener domain as the Go course, on purpose: same problem, contrasting language,
maximum transfer. Ends the week as an axum HTTP service.

| Day | Date | Lesson | Core of the day |
|----|------|--------|-----------------|
| 1 | Tue Jul 8 | Cargo & the shape of Rust | cargo new/run/check; `let`/`mut`/shadowing; expressions vs statements; structs; **enums with data + exhaustive `match`** |
| 2 | Wed Jul 9 | Ownership & borrowing | moves, clones, `&`/`&mut`, slices, `String` vs `&str` — THE Rust feature |
| 3 | Thu Jul 10 | Option, Result & errors | `Option`/`Result`, `?`, matching patterns; thiserror/anyhow orientation |
| 4 | Fri Jul 11 | Traits, generics & iterators | `impl`, derive, trait bounds vs `dyn`; closures + iterator adapters |
| 5 | Sat Jul 12 | Collections, modules & serde | `Vec`/`HashMap`, module system, crates; JSON with serde derive |
| 6 | Sun Jul 13 | Async & tokio | async/await, tasks, `.await` points; threads + Send/Sync in one sketch |
| 7 | Mon Jul 14 | Capstone: axum service | linkshort-rs as HTTP service: routing, extractors, state, tests, clippy |

## After the week — daily practice (from Tue Jul 15, open-ended)

One page: `daily.html`. ~15 min/day:
- **Quiz**: up to 8 questions sampled from the quiz bank (`assets/quiz-bank.js`) by a
  Leitner spaced-repetition schedule (`assets/srs.js`, progress in localStorage) —
  wrong answers come back sooner, mastered ones stretch out to 16-day gaps.
- **Kata**: one tiny compile-it-yourself exercise with a hidden solution.

The bank grows: every lesson ships its questions + one kata into quiz-bank.js.
Runs until the user says stop.

## Pre-assigned lesson filenames (register in assets/nav.js when authored)
- lessons/0001-cargo-and-the-shape-of-rust.html
- lessons/0002-ownership-and-borrowing.html
- lessons/0003-option-result-and-errors.html
- lessons/0004-traits-generics-iterators.html
- lessons/0005-collections-modules-serde.html
- lessons/0006-async-and-tokio.html
- lessons/0007-axum-capstone.html
