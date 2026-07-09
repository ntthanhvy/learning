# Calibration: practice steps need file-level concreteness

The Day 1 practice ("create package link", 6 terse bullets) was too compressed to follow — user asked whether the steps were vague or they lacked a skill. Diagnosis: the instructions assumed from-scratch project scaffolding experience (module init, package-per-directory layout, file naming, import paths); user's Go experience appears to be working inside existing codebases, not starting projects from zero.

**Evidence:** User reported being unable to follow the Day 1 scaffold instructions (2026-07-07). Refines [[0001-prior-knowledge-baseline]] — "already writes some Go" means code-level fluency, not project-level.

**Implications:** All future practice sections must spell out mechanics completely — exact commands, directory tree, one code block per file with imports, TODO markers only on the concept being taught (difficulty belongs in the learning target, not in incidental setup). Day 5's Postgres/migration setup especially needs this treatment. Also: verify every scaffold compiles before shipping the lesson.
