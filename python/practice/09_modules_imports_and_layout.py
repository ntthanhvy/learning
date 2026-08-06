# Practice 9 — Modules, packages & imports
# Run:  cd ~/learning/python && uv run python3 practice/09_modules_imports_and_layout.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# This lesson is about *multiple files* importing each other, which is hard
# to demo from one script honestly. So this file builds a tiny throwaway
# project (a module + a package) on disk in a temp folder at startup, the
# same "write my own fixtures" approach Day 6's practice file used for its
# CSV/JSON files — then your TODOs import real code from those real files.
# Nothing here needs `practice/` itself to contain extra files.

import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Fixture setup — don't edit. Builds:
#   <tmp>/helpers.py                a lone module
#   <tmp>/mypkg/__init__.py         a package
#   <tmp>/mypkg/parsing.py          a module inside that package
_tmp = Path(tempfile.mkdtemp(prefix="py09_"))

(_tmp / "helpers.py").write_text(
    'def shout(text):\n'
    '    return text.upper() + "!"\n'
    '\n'
    'if __name__ == "__main__":\n'
    '    print(shout("running directly"))\n'
)

_pkg = _tmp / "mypkg"
_pkg.mkdir()
(_pkg / "__init__.py").write_text("")
(_pkg / "parsing.py").write_text(
    'def safe_int(text):\n'
    '    try:\n'
    '        return int(text)\n'
    '    except ValueError:\n'
    '        return None\n'
)

sys.path.insert(0, str(_tmp))  # so `import helpers` / `import mypkg` find them


# ---------------------------------------------------------------------------
# Exercise 1 — import a name from a sibling module.
# The fixture above wrote helpers.py with a function shout(text) that
# upper-cases text and appends "!". Import shout directly (the
# `from helpers import shout` form) and call it here.
def call_shout(text):
    ...                              # TODO:
    # from helpers import shout
    # return shout(text)


# ---------------------------------------------------------------------------
# Exercise 2 — import a whole module and use the module-prefix form.
# Same helpers.py. This time use `import helpers` (not `from ... import`)
# and call it as helpers.shout(text).
def call_shout_prefixed(text):
    ...                              # TODO:
    # import helpers
    # return helpers.shout(text)


# ---------------------------------------------------------------------------
# Exercise 3 — read __name__ to tell "run directly" from "imported".
# Return the CURRENT file's own __name__ value (just the built-in variable,
# no import needed) — when this whole practice file is run directly with
# `uv run python3 practice/09_modules_imports_and_layout.py`, what is it?
def current_name():
    ...                              # TODO: return __name__


# ---------------------------------------------------------------------------
# Exercise 4 — import a function from a package (a folder with __init__.py).
# The fixture above wrote mypkg/parsing.py with safe_int(text), inside a
# real package (mypkg/__init__.py exists). Import safe_int from mypkg.parsing
# and call it here.
def call_safe_int(text):
    ...                              # TODO:
    # from mypkg.parsing import safe_int
    # return safe_int(text)


# ---------------------------------------------------------------------------
# Exercise 5 — importing a module runs it once; a second import reuses the
# cached copy instead of re-running it.
# Add a module-level counter to helpers.py the first time it's imported here
# (simulate this WITHOUT editing the fixture: import helpers twice in a row
# and return how many entries are in sys.modules for the name "helpers" —
# it should never be more than 1, no matter how many times it's imported).
def import_count_stays_one():
    ...                              # TODO:
    # import helpers
    # import helpers
    # return list(sys.modules).count("helpers")


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: call_shout() imports shout directly and calls it",
          lambda: call_shout("hi") == "HI!"),
    check("Ex 2: call_shout_prefixed() imports the module and uses helpers.shout(...)",
          lambda: call_shout_prefixed("yo") == "YO!"),
    check("Ex 3: current_name() returns this file's own __name__",
          lambda: current_name() == __name__),
    check("Ex 4: call_safe_int() imports safe_int from the mypkg package",
          lambda: call_safe_int("42") == 42 and call_safe_int("nope") is None),
    check("Ex 5: importing the same module twice only caches it once",
          lambda: import_count_stays_one() == 1),
]

print("\nAll green — lesson 9 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")


if __name__ == "__main__":
    pass  # the check() calls above already ran at import time (module-level);
          # this guard just demonstrates the pattern Exercise 3 asks about.
