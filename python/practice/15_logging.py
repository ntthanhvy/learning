# Practice 15 — logging
# Run:  cd ~/learning/python && uv run python3 practice/15_logging.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import io
import logging


# ---------------------------------------------------------------------------
# Exercise 1 — build a logger with a handler and formatter attached.
# Given a logging.StreamHandler `handler` already pointed at an in-memory
# stream, and a format string `fmt_string`, create a logging.Formatter from
# fmt_string, attach it to handler with .setFormatter(), attach handler to a
# logger named "practice15" via logging.getLogger("practice15"), and return
# that logger. Do NOT call logging.basicConfig() here.
def build_logger(handler, fmt_string):
    ...                              # TODO:
    # formatter = logging.Formatter(fmt_string)
    # handler.setFormatter(formatter)
    # logger = logging.getLogger("practice15")
    # logger.addHandler(handler)
    # return logger


# ---------------------------------------------------------------------------
# Exercise 2 — filter records by level.
# Given a logger `logger` and a level (e.g. logging.WARNING), set the
# logger's level with .setLevel(level) and return the logger.
def set_logger_level(logger, level):
    ...                              # TODO:
    # logger.setLevel(level)
    # return logger


# ---------------------------------------------------------------------------
# Exercise 3 — read back a formatted record's text.
# Given a logger `logger` already wired to a StreamHandler writing into a
# io.StringIO `stream`, and a message string `message`, log `message` at INFO
# level with logger.info(message), then return everything written to the
# stream so far via stream.getvalue().
def log_and_read(logger, stream, message):
    ...                              # TODO:
    # logger.info(message)
    # return stream.getvalue()


# ---------------------------------------------------------------------------
# Exercise 4 — log a caught ValueError with a traceback attached.
# Given a logger `logger`, try converting `text` to an int with int(text).
# If it raises ValueError, log an error with logger.error(...) passing
# exc_info=True so the traceback is attached, then return None. If it
# succeeds, return the parsed int.
def safe_int(logger, text):
    ...                              # TODO:
    # try:
    #     return int(text)
    # except ValueError:
    #     logger.error("could not parse %r as an int", text, exc_info=True)
    #     return None


# ---------------------------------------------------------------------------
# Exercise 5 — a below-threshold call produces no record at all.
# Given a logger `logger` whose level has already been set to logging.ERROR,
# call logger.info(message) (below the threshold), then return whatever was
# written to `stream` so far via stream.getvalue() — it should be empty,
# since INFO does not clear an ERROR-level logger's filter.
def log_below_threshold(logger, stream, message):
    ...                              # TODO:
    # logger.info(message)
    # return stream.getvalue()


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _fresh_logger(name, level=logging.INFO):
    # Each check gets its own uniquely-named logger + stream so earlier
    # exercises' handlers never leak into a later one's check.
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.setLevel(level)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    return logger, stream, handler


results = [
    check("Ex 1: build_logger() attaches a formatter and handler, returns the logger",
          lambda: (lambda h=logging.StreamHandler(io.StringIO()):
                    build_logger(h, "%(levelname)s: %(message)s").name == "practice15"
                    and h.formatter is not None)()),
    check("Ex 2: set_logger_level() sets the logger's level and returns it",
          lambda: (lambda lg=logging.getLogger("practice15_lvl"):
                    set_logger_level(lg, logging.WARNING).level == logging.WARNING)()),
    check("Ex 3: log_and_read() logs a message and returns the formatted text",
          lambda: (lambda: (
              lambda lg, stream, _h: "hello world" in log_and_read(lg, stream, "hello world")
              and "INFO" in log_and_read(lg, stream, "hello world")
          )(*_fresh_logger("practice15_read")))()),
    check("Ex 4: safe_int() logs a traceback on ValueError and returns None; parses valid ints",
          lambda: (lambda: (
              lambda lg, stream, _h: (
                  safe_int(lg, "42") == 42
                  and safe_int(lg, "nope") is None
                  and "Traceback" in stream.getvalue()
              )
          )(*_fresh_logger("practice15_safeint")))()),
    check("Ex 5: log_below_threshold() produces no output when below the logger's level",
          lambda: (lambda: (
              lambda lg, stream, _h: log_below_threshold(lg, stream, "quiet") == ""
          )(*_fresh_logger("practice15_thresh", level=logging.ERROR)))()),
]

print("\nAll green — lesson 15 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
