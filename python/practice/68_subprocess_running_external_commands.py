# Practice 68 — subprocess: running another program from Python
# Run:  cd ~/learning/python && uv run python3 practice/68_subprocess_running_external_commands.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import subprocess
import sys


# ---------------------------------------------------------------------------
# Exercise 1 — run a command as a list of arguments and capture its stdout
# as text. Write run_echo(words) that runs the external command
# [sys.executable, "-c", "import sys; print(' '.join(sys.argv[1:]))"] plus
# each item of `words` appended as its own extra argument, with
# capture_output=True and text=True, and returns the captured stdout with
# any trailing newline stripped.
# (Using sys.executable instead of "python3" keeps this portable — it's
# whatever Python interpreter is currently running this file.)
def run_echo(words):
    # TODO: result = subprocess.run(
    #           [sys.executable, "-c", "import sys; print(' '.join(sys.argv[1:]))"] + list(words),
    #           capture_output=True, text=True,
    #       )
    #       return result.stdout.rstrip("\n")
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — check=True raising CalledProcessError on a nonzero exit, vs.
# reading returncode by hand. Write exits_with_code(code) that runs
# [sys.executable, "-c", f"import sys; sys.exit({code})"] with check=True
# inside a try/except subprocess.CalledProcessError, and returns:
#   - 0 if the command succeeded (no exception)
#   - the exception's .returncode if CalledProcessError was raised
def exits_with_code(code):
    # TODO: try:
    #           subprocess.run([sys.executable, "-c", f"import sys; sys.exit({code})"], check=True)
    #           return 0
    #       except subprocess.CalledProcessError as e:
    #           return e.returncode
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — stdout and stderr captured separately. Write
# split_stdout_stderr() that runs
# [sys.executable, "-c", "import sys; print('out-line'); print('err-line', file=sys.stderr)"]
# with capture_output=True and text=True, and returns a tuple
# (stdout_stripped, stderr_stripped) — each with any trailing newline
# stripped.
def split_stdout_stderr():
    # TODO: result = subprocess.run(
    #           [sys.executable, "-c",
    #            "import sys; print('out-line'); print('err-line', file=sys.stderr)"],
    #           capture_output=True, text=True,
    #       )
    #       return (result.stdout.rstrip("\n"), result.stderr.rstrip("\n"))
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
    return run_echo(["hello", "world"]) == "hello world"


def _ex2():
    return exits_with_code(0) == 0 and exits_with_code(7) == 7


def _ex3():
    return split_stdout_stderr() == ("out-line", "err-line")


results = [
    check("Ex 1: subprocess.run() with a list of args captures stdout as text", _ex1),
    check("Ex 2: check=True raises CalledProcessError with the right returncode", _ex2),
    check("Ex 3: stdout and stderr come back as two separate captured streams", _ex3),
]
print("\nAll green — lesson 68 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
