# Data Wrangling (pandas & NumPy) Resources

## Knowledge

- [Book: _Python for Data Analysis_, 3rd ed. — Wes McKinney (open access)](https://wesmckinney.com/book/)
  Written by pandas' original author; the canonical text. Use for: any pandas/NumPy concept in depth — ch. 5 (pandas basics), ch. 7 (cleaning), ch. 8 (join/reshape), ch. 10 (groupby).
- [Docs: pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
  The official reference. Use for: authoritative behavior of any method; the "Merge, join, concatenate" and "Group by" pages are lesson-grade on their own.
- [Docs: Comparison with SQL — pandas](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)
  Official side-by-side SQL ↔ pandas translation. Use for: the fastest bridge from existing SQL knowledge to pandas idioms — this course's backbone.
- [Docs: NumPy fundamentals — broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
  Official explanation of broadcasting rules with diagrams. Use for: understanding why pandas arithmetic "just works" across shapes, and interview questions on it.
- [Article series: "Modern Pandas" — Tom Augspurger (pandas core dev)](https://tomaugspurger.net/posts/modern-1-intro/)
  Idiomatic-pandas series from a core developer. Use for: method chaining, avoiding SettingWithCopy traps, writing pipelines that read like pipelines.
- [Article: "ETL vs ELT" — dbt Labs](https://www.getdbt.com/blog/etl-vs-elt)
  Clear industry framing of the two pipeline shapes. Use for: interview vocabulary on where transformation lives and why the industry shifted to ELT.

## Practice (interview drills)

- [LeetCode: "Introduction to Pandas" study plan](https://leetcode.com/studyplan/introduction-to-pandas/)
  Free, short, auto-graded pandas exercises. Use for: timed retrieval practice once a topic has been covered in a lesson.
- [StrataScratch](https://www.stratascratch.com/)
  Real interview questions from data roles, solvable in pandas or SQL. Use for: realistic interview simulation in the final stretch before interviews.

## Wisdom (Communities)

- [r/dataengineering](https://www.reddit.com/r/dataengineering/)
  Active, well-moderated; frequent interview-experience and "what do DE interviews actually ask" threads. Use for: calibrating what real interviews test.
- [pandas GitHub Discussions](https://github.com/pandas-dev/pandas/discussions)
  Maintainers answer usage questions. Use for: "is this idiom right?" questions once past the basics.

## Gaps

- No curated source yet for *take-home assignment* norms (typical rubric for "clean this dataset" take-homes) — search when an actual interview process starts.
