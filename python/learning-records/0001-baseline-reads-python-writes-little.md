# Baseline: reads simple Python, writes almost none

Established 2026-07-29 at course creation, from the user directly rather than
inferred: *"basic, can read and understand simple python. need extreme
enhancement in everything else."*

This is a **reading/writing asymmetry**, and it is the single most important
fact for planning lessons. Following someone else's Python — a pandas lesson in
`data/`, a snippet in a PR — works. Producing Python from an empty file does
not. Recognition is intact; recall is not.

## Implications

- **Never mistake comprehension for capability.** A lesson the user reads and
  agrees with has taught nothing durable. Every lesson needs a retrieval step
  where they write code from memory — the practice file is not optional
  decoration, it is where the learning happens.
- **Nothing is assumed free.** Comprehensions, `lambda`, `*args`, `key=`,
  generators, decorators, and type hints are all *new*, even though the user
  has certainly seen them in `data/` lessons and at work. Seen ≠ owned. Each
  gets an explicit lesson before it appears unexplained in a sample.
- Before Day 2, samples use plain `for` loops deliberately, even where a
  comprehension would be idiomatic. Teaching the idiom is Day 2's whole job;
  using it on Day 1 would spend a win that hasn't been earned.
- **Bridge from SQL, not from Python.** SQL is genuinely strong. "This is
  `GROUP BY` done by hand with a dict" lands; "this is like a list
  comprehension" does not, yet.
- Watch Days 2 and 5 (comprehensions, generators) for the first real
  difficulty spike — they are where syntax stops being linear and starts being
  compositional. If the practice files there go badly, slow down and add a
  consolidation lesson rather than pressing on to the capstone.

## To verify

The "reads simple Python" half is self-reported and untested. Day 1's practice
file doubles as a probe: it asks for tiny edits to working code, so a stumble
there means the baseline is optimistic and Phase 1's pace needs revisiting
before Day 3. Revise this record either way once Day 1's practice comes back.
