# Python Intensive — Resources

Ground every lesson in these. Prefer the official docs for behavior, the named
authors for *why*. Cite inline; each lesson recommends exactly one primary source.

## Knowledge — the language

- [Docs: The Python Tutorial](https://docs.python.org/3/tutorial/)
  The official guided introduction. Use for: the canonical spelling of any core-language feature; ch. 4–5 (control flow, data structures) back the whole intensive week.
- [Docs: The Python Language Reference — Data model](https://docs.python.org/3/reference/datamodel.html)
  Authoritative on objects, identity, and special methods. Use for: Day 1's names-vs-objects claims, and any "why does it behave like that" question.
- [Article: "Facts and Myths about Python names and values" — Ned Batchelder](https://nedbatchelder.com/text/names.html)
  The clearest explanation anywhere of assignment, aliasing, and mutability, with diagrams. Use for: Day 1 — this is the primary source for the object model.
- [Book: _Fluent Python_, 2nd ed. — Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
  The standard text on idiomatic Python. Use for: depth on the data model, sequences, iterators/generators, and dataclasses. (Paid — the docs cover the same ground for this course's purposes.)
- [Docs: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
  Official guide to `sorted()`, `key=`, and stability. Use for: Day 4 — the shortest path to sorting fluency.
- [Docs: `itertools`](https://docs.python.org/3/library/itertools.html) · [`collections`](https://docs.python.org/3/library/collections.html) · [`operator`](https://docs.python.org/3/library/operator.html)
  The stdlib modules that replace most hand-written data-munging loops and lambdas. Use for: Days 3, 5, 53, and 56; the `itertools` recipes section is lesson-grade on its own, and `operator`'s "Mapping Operators to Functions" table covers every arithmetic/comparison spelling Day 56 only samples two of.
- [Talk/course: "Generators: The Final Frontier" — David Beazley](https://www.dabeaz.com/generators/)
  Deep, practical treatment of generators as data-pipeline building blocks. Use for: Day 5's lazy-pipeline framing.
- [Blog: Trey Hunner](https://treyhunner.com/blog/archives/)
  Careful, beginner-aware writing on comprehensions, unpacking, and looping idioms. Use for: Day 2 — good at explaining *when not to* use a comprehension.
- [Docs: `dataclasses`](https://docs.python.org/3/library/dataclasses.html) · [`typing`](https://docs.python.org/3/library/typing.html)
  Use for: Day 7 — structuring records and reading annotated signatures; also Day 57 — `field()`'s `default_factory`/`repr`/`compare` keywords and `frozen=True`, the two escape hatches Day 7 deferred.
- [Docs: `abc`](https://docs.python.org/3/library/abc.html)
  Use for: Day 50 — abstract base classes, `@abstractmethod`, and how they differ from Day 41's structural `Protocol`.
- [Docs: `heapq`](https://docs.python.org/3/library/heapq.html) · [`bisect`](https://docs.python.org/3/library/bisect.html)
  Use for: Day 51 — priority queues and binary search over a plain Python list, without a full re-sort on every change.
- [Docs: `hashlib`](https://docs.python.org/3/library/hashlib.html)
  Use for: Day 59 — content hashing for change detection and de-duplication, chunked file hashing via `.update()`, and why a fast general-purpose digest like `sha256` is the wrong tool for password storage (`pbkdf2_hmac()` or a dedicated library instead).
- [Docs: `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
  Use for: Day 60 — `Mock`/`patch()` for faking network calls, dates, and other side effects in a test; the "Where to patch" section is the primary source for the "patched the wrong path" failure mode Day 60 spends a whole section on. Standard library, unlike `pytest` itself.
- [Docs: `shutil`](https://docs.python.org/3/library/shutil.html)
  Use for: Day 62 — copying/moving a file or a whole directory tree, `copytree()`'s destination-must-not-exist safety rule, `rmtree()`'s unrecoverable-deletion risk, and `disk_usage()`.
- [Docs: `zipfile`](https://docs.python.org/3/library/zipfile.html)
  Use for: Day 64 — reading and writing zip archives: `namelist()`/`open()` for inspecting or reading a member without extracting the rest, `extractall()`, `write()`/`writestr()` with `arcname` control, and the path-traversal risk of extracting an untrusted archive.
- [Docs: `tempfile`](https://docs.python.org/3/library/tempfile.html)
  Use for: Day 65 — `TemporaryDirectory()` and `NamedTemporaryFile()` as self-cleaning scratch space for pipeline staging, collision-proof unique naming, and the `delete=False` escape hatch for code that needs to reopen a temp file by path.
- [Docs: `csv`](https://docs.python.org/3/library/csv.html)
  Use for: Day 6 — `csv.reader`/`csv.DictReader` for the read side; Day 66 — `csv.writer`/`csv.DictWriter`, `fieldnames=`, the `newline=""` rule for avoiding doubled line endings, and `extrasaction=`/`restval=` for mismatched dict keys.
- [Docs: `json`](https://docs.python.org/3/library/json.html)
  Use for: Day 6 — `json.load`/`json.dump` for the file-based round trip; Day 76 — `dumps()`/`loads()` for working with JSON as an in-memory string, `indent=`/`sort_keys=` for human-readable output, and `default=` for serializing a type (`dataclass`, `datetime`) `json` doesn't know natively, the `cls=` full-encoder option being the natural next step beyond it.
- [Docs: `subprocess`](https://docs.python.org/3/library/subprocess.html)
  Use for: Day 68 — `subprocess.run()`, the list-of-arguments form vs. the injection risk of `shell=True`, `returncode`/`check=True`, and separating captured `stdout` from `stderr`.
- [Docs: `statistics`](https://docs.python.org/3/library/statistics.html)
  Use for: Day 69 — `mean()`/`median()`/`mode()`/`stdev()`/`variance()` on a plain list or iterable, and why each answers a different "typical value" or "spread" question.
- [Docs: `decimal`](https://docs.python.org/3/library/decimal.html)
  Use for: Day 70 — `Decimal` for exact base-10 arithmetic, the float-construction trap (`Decimal(0.1)` vs. `Decimal("0.1")`), and `quantize()` with an explicit rounding mode for rounding money to cents.
- [Docs: `pickle`](https://docs.python.org/3/library/pickle.html)
  Use for: Day 72 — `dumps()`/`loads()`/`dump()`/`load()` for serializing arbitrary Python objects (including `dataclass` instances `json` can't hold), the `"wb"`/`"rb"` binary-mode rule, and the documented warning against unpickling data from an untrusted source.
- [Docs: `concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html)
  Use for: Day 73 — `ThreadPoolExecutor`'s `submit()`/`map()` and `Future.result()` for running I/O-bound calls concurrently, the GIL's I/O-release behavior that makes threading help here but not for CPU-bound work, and `ProcessPoolExecutor`/`as_completed()` as the named-but-undemonstrated next steps.
- [Docs: `uuid`](https://docs.python.org/3/library/uuid.html) · [`configparser`](https://docs.python.org/3/library/configparser.html)
  Use for: Day 74 — `uuid.uuid4()` for coordination-free unique identifiers and why it's preferred over `uuid1()`; `configparser.ConfigParser` for reading/writing INI-style config files, its string-only raw values, and the typed `getint()`/`getfloat()`/`getboolean()` readers.
- [Docs: `secrets`](https://docs.python.org/3/library/secrets.html)
  Use for: Day 77 — `token_hex()`/`token_urlsafe()` for cryptographically secure tokens (vs. Day 54's `random`, never safe for this), `secrets.choice()` for picking from a fixed alphabet securely, and `compare_digest()` for timing-safe comparison of a secret against untrusted input; the "Recipes and best practices" section is the primary source for the timing-attack claim.
- [Docs: `pprint`](https://docs.python.org/3/library/pprint.html)
  Use for: Day 78 — `pprint()`/`pformat()` for readable multi-line output on any nested Python object (not only JSON-shaped data, unlike Day 76's `json.dumps(indent=)`), `sort_dicts=` for alphabetical vs. insertion key order, and `width=`/`depth=` for layout control.
- [Docs: `difflib`](https://docs.python.org/3/library/difflib.html)
  Use for: Day 80 — `unified_diff()` for a `git diff`-shaped line-by-line comparison, `SequenceMatcher.ratio()` for a 0.0-1.0 similarity score instead of a rendered diff, and `get_close_matches()` for ranking known candidates against one input word (a "did you mean…?" suggestion).
- [Docs: `io`](https://docs.python.org/3/library/io.html)
  Use for: Day 81 — `StringIO`/`BytesIO` as in-memory, file-like objects for code that expects an open file (`csv`, `json`), `.getvalue()` for reading back everything written, and `.seek(0)` for rewinding before a read.
- [Docs: `base64`](https://docs.python.org/3/library/base64.html)
  Use for: Day 82 — `b64encode()`/`b64decode()` for carrying arbitrary bytes through a text-only format (JSON, a log line), `urlsafe_b64encode()`/`urlsafe_b64decode()` for the URL-safe `-`/`_` alphabet variant, and why encoding is not encryption.
- [Docs: `traceback`](https://docs.python.org/3/library/traceback.html)
  Use for: Day 84 — `format_exc()`/`print_exc()` for capturing or writing out the same report an uncaught exception would print, from inside a running `except` block; `print_exc()`'s `file=` redirect; and how Day 15's `logging` `exc_info=True` calls this module internally.
- [Docs: `warnings`](https://docs.python.org/3/library/warnings.html)
  Use for: Day 85 — `warn()` for a non-fatal "probably wrong, keep going" signal distinct from `raise` and from Day 15's `logging.warning()`; `catch_warnings(record=True)`/`simplefilter("always")` for asserting a warning fired in a test; and `filterwarnings("error", ...)` for escalating a warning category into a real exception.
- [Docs: `inspect`](https://docs.python.org/3/library/inspect.html)
  Use for: Day 86 — `signature()`/`Signature`/`Parameter` for reading a function's parameter names, defaults, and kinds as data instead of text; `bind()`/`apply_defaults()` for matching real arguments against a signature without calling the function, the mechanism behind Day 19's `Depends()`; and the `is*` predicate family (`isfunction`, `isclass`, `isbuiltin`) for telling apart what kind of object something actually is.
- [Docs: `hmac`](https://docs.python.org/3/library/hmac.html)
  Use for: Day 89 — `hmac.new(key, msg, digestmod)` for keyed message authentication, `digestmod` being a required argument unlike `hashlib`'s own named functions, confirming `hashlib.sha256(key + msg)` is not the same as a real HMAC tag, and bridging to Day 59's chunked `.update()` and Day 77's `compare_digest()` for safe verification.
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
  Use for: naming and layout conventions, so written code looks like the ecosystem's.

## Knowledge — backend (Phase 2b)

- [Docs: FastAPI](https://fastapi.tiangolo.com/)
  Unusually good official tutorial — genuinely teaches the concepts, not just the API. Use for: the whole backend phase; the "Tutorial - User Guide" is the spine.
- [Docs: pydantic](https://docs.pydantic.dev/latest/)
  Use for: validation, coercion rules, custom validators, and settings management.
- [Docs: pytest](https://docs.pytest.org/en/stable/)
  Use for: Phase 2a testing lessons; fixtures and `parametrize` especially.
- [Docs: uv — Astral](https://docs.astral.sh/uv/)
  The environment/dependency tool this course already uses to run practice files. Use for: the environments lesson.

## Practice

- [Exercism — Python track](https://exercism.org/tracks/python)
  Free, mentored, idiom-focused exercises. Use for: retrieval practice after a lesson; its feedback targets idiomatic style, which suits this course's goal.
- [Advent of Code](https://adventofcode.com/)
  Parsing-heavy puzzles solvable with the stdlib alone. Use for: realistic "messy input → structured records" drills, especially after Days 5–6.
- [Real Python — Python Interview Questions and Answers](https://realpython.com/python-interview-questions/)
  Groups questions by the same fundamentals this course already teaches (data model, comprehensions, generators, decorators). Use for: Day 47's four-part answer-shape drill and general interview prep — closes the interview-prep Gap noted below since Day 1.

## Wisdom — communities

- [r/learnpython](https://www.reddit.com/r/learnpython/)
  High-volume, beginner-friendly, fast answers. Use for: "is this idiomatic?" questions while the fundamentals are still settling.
- [Python Discord](https://www.pythondiscord.com/)
  Large, well-moderated, with live help channels. Use for: real-time unblocking and code review from practitioners.

## Gaps

- ~~No source chosen yet for **Python-specific interview prep**~~ — closed Day 47 (2026-09-13): Real Python's interview-questions guide, added to Practice above.
- No canonical free text for FastAPI *architecture* beyond one file — the official docs stop at structure basics. Day 19 already teaches and cites `bigger-applications` directly for `APIRouter`/`include_router()`, so this is now closer to a citation nicety than an unmet learner need; still open if a dedicated project-layout reference surfaces.
