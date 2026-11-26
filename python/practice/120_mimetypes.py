# Practice 120 — mimetypes: guessing a file's type from its name
# Run:  cd ~/learning/python && uv run python3 practice/120_mimetypes.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import mimetypes


# ---------------------------------------------------------------------------
# Exercise 1 — separate recognized filenames from unrecognized ones.
# Write split_known(filenames) that returns a tuple (known, unknown) of two
# dicts: `known` maps each filename whose mimetypes.guess_type() found a
# type (not None) to that type string; `unknown` maps each filename whose
# guess_type() returned None for the type to None.
def split_known(filenames):
    # TODO: for each name in filenames, call mimetypes.guess_type(name),
    # take the first tuple item as the type, and put name -> type into
    # `known` if the type is not None, else into `unknown`.
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — read off a file's compression encoding.
# Write compression_of(filename) that returns the second item of
# mimetypes.guess_type(filename) — the encoding ("gzip", "compress", etc.),
# or None if the file isn't flagged as compressed.
def compression_of(filename):
    # TODO: return mimetypes.guess_type(filename)[1]
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — register a new extension and confirm the lookup picks it up.
# Write register_and_check(mime_type, extension, filename) that calls
# mimetypes.add_type(mime_type, extension) and then returns the `type` item
# of mimetypes.guess_type(filename) for the given filename.
def register_and_check(mime_type, extension, filename):
    # TODO: call mimetypes.add_type(mime_type, extension), then return
    # mimetypes.guess_type(filename)[0]
    pass


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    known, unknown = split_known(["report.csv", "photo.jpg", "noextension", "page.html"])
    return (
        known == {"report.csv": "text/csv", "photo.jpg": "image/jpeg", "page.html": "text/html"}
        and unknown == {"noextension": None}
    )


def _ex2():
    return (
        compression_of("archive.tar.gz") == "gzip"
        and compression_of("notes.txt") is None
    )


def _ex3():
    before = mimetypes.guess_type("thing.myappext")[0]
    after = register_and_check("application/x-myappext", ".myappext", "thing.myappext")
    return before is None and after == "application/x-myappext"


results = [
    check("Ex 1: split_known separates recognized from unrecognized names", _ex1),
    check("Ex 2: compression_of reads the encoding tuple item", _ex2),
    check("Ex 3: register_and_check registers then confirms a new extension", _ex3),
]
print("\nAll green — lesson 120 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
