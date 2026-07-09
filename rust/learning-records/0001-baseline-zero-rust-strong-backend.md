# Baseline: zero Rust, experienced backend dev, mid-Go-intensive

User has never written Rust. Strong general backend background; currently one week into a
parallel Go intensive (~/learning/go) — Day 1 (interfaces, embedding) completed with
working code. This shapes everything: teach Rust *by contrast with Go*, not from a blank
slate, and keep daily load at ~60–90 min since both courses share the same 2–3 h/day.

**Evidence:** User's own statement ("I know nothing of rust"); Go course learning records.

**Implications:** Skip nothing in Rust (it's from zero) but compress via Go contrasts —
enums vs Go's lack of them, Result vs error values, traits vs interfaces, ownership vs GC.
Go LR-0004 flagged a blurry pointer/memory model: ownership (Day 2) must draw the
stack/heap picture explicitly rather than assume it. Go LR-0003: practice must be
file-level concrete. Vietnamese gloss-popup rules apply from lesson one.
