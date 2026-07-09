# Baseline: strong SQL, basic Python, no prior pandas/NumPy

Starting point established at course creation (2026-07-09), inferred from the sibling courses' records rather than direct assessment. Strong SQL: joins, aggregation, and (from Go week Days 5–6) constraints/indexes/EXPLAIN — so SQL-equivalence is the teaching bridge and basic SQL must never be re-taught. Python is assumed working-but-basic and pandas/NumPy experience is assumed zero; **both assumptions need verification in Lesson 1's practice** — if the user breezes through or stumbles on Python syntax itself, revise this record and re-plan the curriculum spine in NOTES.md.

**Implications**
- Teach pandas operations as translations of SQL the user already knows (SELECT/WHERE/GROUP BY/JOIN → the pandas spelling), then highlight where the mental model genuinely differs (the index, mutation vs expression, NaN semantics).
- Gloss Python idioms (comprehensions, lambdas) as jargon — they are not yet free.
