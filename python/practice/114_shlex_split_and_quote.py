# Practice 114 — shlex: splitting and quoting shell-style strings
# Run:  cd ~/learning/python && uv run python3 practice/114_shlex_split_and_quote.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

import shlex


# ---------------------------------------------------------------------------
# Exercise 1 — turn one command-line-shaped string into the list form
# Day 68's subprocess.run() wants. Write to_argv(command_line) that uses
# shlex.split() to split command_line into a list of strings, respecting
# quotes (a quoted substring with spaces inside stays one list element).
def to_argv(command_line):
    # TODO: return shlex.split(command_line)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — make one value safe to drop into a shell command string.
# Write safe_for_shell(value) that uses shlex.quote() to return `value`
# wrapped/escaped so a shell would treat it as exactly one argument no
# matter what characters it contains.
def safe_for_shell(value):
    # TODO: return shlex.quote(value)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — round-trip: build one shell-safe command string from a
# program name plus a list of raw argument values (which might contain
# spaces or shell-special characters). Write build_command(argv) that uses
# shlex.join() to join every element of argv into one string where each
# argument is safely quoted, in order.
def build_command(argv):
    # TODO: return shlex.join(argv)
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
    return to_argv('cp "my file.txt" /tmp/backup --verbose') == [
        "cp", "my file.txt", "/tmp/backup", "--verbose",
    ]


def _ex2():
    # A value with no special characters comes back unchanged; a value
    # with a space or a shell metacharacter comes back quoted.
    plain = safe_for_shell("hello")
    spaced = safe_for_shell("my file.txt")
    dangerous = safe_for_shell("a; rm -rf /")
    return (
        plain == "hello"
        and spaced == "'my file.txt'"
        and dangerous == "'a; rm -rf /'"
    )


def _ex3():
    built = build_command(["cp", "my file.txt", "/tmp/backup"])
    # The built string, re-split, must reproduce the original argv exactly —
    # that's what makes join() the inverse of split().
    return built == "cp 'my file.txt' /tmp/backup" and shlex.split(built) == [
        "cp", "my file.txt", "/tmp/backup",
    ]


results = [
    check("Ex 1: shlex.split() turns a command-line string into an argv list", _ex1),
    check("Ex 2: shlex.quote() only adds quoting when a value actually needs it", _ex2),
    check("Ex 3: shlex.join() builds a string that splits back to the same argv", _ex3),
]
print("\nAll green — lesson 114 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
