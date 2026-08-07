# Practice 10 — Environments & pyproject.toml
# Run:  cd ~/learning/python && uv run python3 practice/10_environments_and_pyproject.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.
#
# Today's topic is a project-metadata FILE, not a library API, so this file
# writes its own small pyproject.toml-shaped fixture into a temp folder at
# startup (same "write my own fixtures" approach Day 6/9's practice files
# used), then reads it back with the standard library's own `tomllib` parser
# — no third-party TOML package needed.

import tempfile
import tomllib
from pathlib import Path

# ---------------------------------------------------------------------------
# Fixture setup — don't edit. Writes a minimal pyproject.toml to a temp file
# and parses it once with tomllib, so every exercise below works with real
# parsed data instead of a hand-built dict.
_tmp = Path(tempfile.mkdtemp(prefix="py10_"))
_pyproject = _tmp / "pyproject.toml"
_pyproject.write_text(
    '[project]\n'
    'name = "sales-pipeline"\n'
    'version = "0.1.0"\n'
    'requires-python = ">=3.12"\n'
    'dependencies = [\n'
    '    "httpx>=0.27",\n'
    '    "pydantic>=2.0",\n'
    ']\n'
    '\n'
    '[dependency-groups]\n'
    'dev = ["pytest>=8.0"]\n'
)

with open(_pyproject, "rb") as _f:
    PYPROJECT = tomllib.load(_f)


# ---------------------------------------------------------------------------
# Exercise 1 — read the project's own name back out of the parsed TOML.
# PYPROJECT is already parsed above (a nested dict, same shape as JSON).
# Return the value at PYPROJECT["project"]["name"].
def project_name():
    ...                              # TODO: return PYPROJECT["project"]["name"]


# ---------------------------------------------------------------------------
# Exercise 2 — pull the runtime dependencies list out of the parsed data.
# Return PYPROJECT["project"]["dependencies"] — a list of constraint strings
# like "httpx>=0.27".
def runtime_dependencies():
    ...                              # TODO: return PYPROJECT["project"]["dependencies"]


# ---------------------------------------------------------------------------
# Exercise 3 — split a constraint string into (package_name, constraint).
# split_constraint("httpx>=0.27") -> ("httpx", ">=0.27")
# The package name is everything before the first occurrence of "<", ">",
# "=", or "!"; the constraint is everything from that point on.
def split_constraint(text):
    ...                              # TODO:
    # for i, ch in enumerate(text):
    #     if ch in "<>=!":
    #         return text[:i], text[i:]
    # return text, ""


# ---------------------------------------------------------------------------
# Exercise 4 — tell a runtime dependency from a dev-only one.
# Return True if package_name appears anywhere in PYPROJECT's runtime
# "dependencies" list (compare against the name part only, ignoring any
# version constraint — reuse split_constraint), False otherwise.
def is_runtime_dependency(package_name):
    ...                              # TODO:
    # return any(split_constraint(dep)[0] == package_name
    #            for dep in runtime_dependencies())


# ---------------------------------------------------------------------------
# Exercise 5 — does an installed version satisfy a ">=" constraint?
# satisfies(installed, constraint) takes two dotted version strings like
# "0.29" and ">=0.27", and returns True if installed meets the constraint.
# Only ">=" needs handling here. Compare version parts as integer tuples,
# e.g. "0.29" -> (0, 29) — that way (0, 9) < (0, 10) compares correctly,
# unlike a plain string compare where "0.9" > "0.10" lexically.
def satisfies(installed, constraint):
    ...                              # TODO:
    # assert constraint.startswith(">=")
    # required = tuple(int(p) for p in constraint[2:].split("."))
    # have = tuple(int(p) for p in installed.split("."))
    # return have >= required


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
    check("Ex 1: project_name() reads the name back out of pyproject.toml",
          lambda: project_name() == "sales-pipeline"),
    check("Ex 2: runtime_dependencies() returns the dependencies list",
          lambda: runtime_dependencies() == ["httpx>=0.27", "pydantic>=2.0"]),
    check("Ex 3: split_constraint() splits name from version constraint",
          lambda: split_constraint("httpx>=0.27") == ("httpx", ">=0.27")
                  and split_constraint("pydantic") == ("pydantic", "")),
    check("Ex 4: is_runtime_dependency() tells runtime deps from dev-only ones",
          lambda: is_runtime_dependency("httpx") is True
                  and is_runtime_dependency("pytest") is False),
    check("Ex 5: satisfies() checks a >= version constraint correctly",
          lambda: satisfies("0.29", ">=0.27") is True
                  and satisfies("0.9", ">=0.10") is False
                  and satisfies("0.10", ">=0.9") is True),
]

print("\nAll green — lesson 10 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")


if __name__ == "__main__":
    pass  # the check() calls above already ran at import time (module-level);
          # this guard just follows the pattern every practice file uses.
