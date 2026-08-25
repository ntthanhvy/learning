# Practice 29 — Writing your own context manager
# Run:  cd ~/learning/python && uv run python3 practice/29_writing_context_managers.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from contextlib import contextmanager

# ---------------------------------------------------------------------------
# Exercise 1 — a class-based context manager.
# Complete LoggingCM so that:
#   - __enter__ appends "enter" to self.log and returns self
#   - __exit__ appends "exit" to self.log and returns False (never suppress)
# Note: the class itself must stay definable even before you fill in the
# methods, so the TODO bodies live inside the methods, not the class line.
class LoggingCM:
    def __init__(self):
        self.log = []

    def __enter__(self):
        ...                       # TODO: self.log.append("enter"); return self

    def __exit__(self, exc_type, exc_value, tb):
        ...                       # TODO: self.log.append("exit"); return False


def run_logging_cm():
    cm = LoggingCM()
    with cm:
        pass
    return cm.log


# ---------------------------------------------------------------------------
# Exercise 2 — __exit__ still runs when the block raises.
# Using the same LoggingCM, run a with-block that raises a ValueError inside
# it, catch that ValueError around the with statement, and return cm.log
# afterward — it should show __exit__ ran ("exit" is in the list) even
# though the block never finished normally.
def run_logging_cm_with_exception():
    cm = LoggingCM()

    def _raise():
        raise ValueError("boom")

    try:
        with cm:
            _raise()
    except ValueError:
        pass
    return cm.log


# ---------------------------------------------------------------------------
# Exercise 3 — the @contextmanager generator shortcut.
# Write `logging_cm()` as a generator-based context manager (decorated with
# @contextmanager) that appends "enter" to `log` before yield and "exit"
# to `log` after yield, inside a try/finally so exit still happens on error.
# It should yield nothing meaningful (bare `yield` is fine).
def logging_cm(log):
    ...                           # TODO: @contextmanager generator — see docstring above


def run_generator_cm():
    log = []
    with logging_cm(log):
        pass
    return log


# ---------------------------------------------------------------------------
# Exercise 4 — transaction-style commit/rollback.
# Write `transaction(log)` as a generator-based context manager that:
#   - appends "BEGIN" to log before yield
#   - appends "COMMIT" to log right after yield IF the block didn't raise
#   - appends "ROLLBACK" to log and re-raises if the block DID raise
def transaction(log):
    ...                           # TODO: @contextmanager generator — see docstring above


def run_transaction_commit():
    log = []
    with transaction(log):
        log.append("INSERT")
    return log


def run_transaction_rollback():
    log = []
    try:
        with transaction(log):
            log.append("INSERT")
            raise RuntimeError("db error")
    except RuntimeError:
        pass
    return log


# ---------------------------------------------------------------------------
# Exercise 5 — deliberate exception suppression.
# Write a class Suppress(exc_type) whose __exit__ returns True (suppressing
# the exception) only when the raised exception is an instance of the
# exc_type it was constructed with, and False otherwise (letting anything
# else propagate normally).
class Suppress:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        ...                       # TODO: return exc_type is not None and issubclass(exc_type, self.exc_type)


def run_suppress_matching():
    with Suppress(KeyError):
        raise KeyError("missing")
    return "reached here — KeyError was suppressed"


def run_suppress_nonmatching():
    try:
        with Suppress(KeyError):
            raise ValueError("not a KeyError")
        return "should not reach here"
    except ValueError:
        return "ValueError propagated — not suppressed"


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
    check("Ex 1: LoggingCM's __enter__/__exit__ both log in order",
          lambda: run_logging_cm() == ["enter", "exit"]),
    check("Ex 2: __exit__ still runs even when the with-block raises",
          lambda: run_logging_cm_with_exception() == ["enter", "exit"]),
    check("Ex 3: logging_cm() is a working @contextmanager generator",
          lambda: run_generator_cm() == ["enter", "exit"]),
    check("Ex 4a: transaction() commits when the block doesn't raise",
          lambda: run_transaction_commit() == ["BEGIN", "INSERT", "COMMIT"]),
    check("Ex 4b: transaction() rolls back and re-raises when the block does",
          lambda: run_transaction_rollback() == ["BEGIN", "INSERT", "ROLLBACK"]),
    check("Ex 5a: Suppress(KeyError) swallows a matching KeyError",
          lambda: run_suppress_matching() == "reached here — KeyError was suppressed"),
    check("Ex 5b: Suppress(KeyError) lets a non-matching exception propagate",
          lambda: run_suppress_nonmatching() == "ValueError propagated — not suppressed"),
]
print("\nAll green — lesson 29 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
