# Practice 74 — uuid & configparser
# Run:  cd ~/learning/python && uv run python3 practice/74_uuid_and_configparser.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

import configparser
import tempfile
import uuid
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 — generate two independent uuid4() values and confirm they
# never collide. Write two_uuids() that returns a tuple (a, b) of two
# DIFFERENT uuid.UUID objects, each from its own uuid.uuid4() call.
def two_uuids():
    # TODO: a = uuid.uuid4()
    #       b = uuid.uuid4()
    #       return (a, b)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — round-trip a UUID through str() and back. Write
# roundtrip_uuid() that creates one uuid.uuid4(), converts it to a string
# with str(...), rebuilds a UUID from that string with uuid.UUID(...), and
# returns a tuple (original, rebuilt) of the two UUID objects.
def roundtrip_uuid():
    # TODO: original = uuid.uuid4()
    #       rebuilt = uuid.UUID(str(original))
    #       return (original, rebuilt)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — write a ConfigParser section to a file, then read back a
# typed int with getint(). Write write_and_read_port(path) that:
#   - builds a configparser.ConfigParser()
#   - sets config["database"] = {"host": "localhost", "port": "5432"}
#   - writes it to the given path (a string or Path) by opening it "w"
#     and calling config.write(f)
#   - builds a FRESH ConfigParser, reads the file back with config.read(path)
#   - returns config.getint("database", "port") as an int
def write_and_read_port(path):
    # TODO: config = configparser.ConfigParser()
    #       config["database"] = {"host": "localhost", "port": "5432"}
    #       with open(path, "w") as f:
    #           config.write(f)
    #       reader = configparser.ConfigParser()
    #       reader.read(path)
    #       return reader.getint("database", "port")
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — read back a typed bool with getboolean(), accepting a
# non-True/False spelling. Write write_and_read_debug(path) that:
#   - builds a configparser.ConfigParser()
#   - sets config["app"] = {"debug": "yes"}   (note: "yes", not "True")
#   - writes it to the given path the same way as Exercise 3
#   - reads it back with a fresh ConfigParser
#   - returns reader.getboolean("app", "debug") as a bool
def write_and_read_debug(path):
    # TODO: config = configparser.ConfigParser()
    #       config["app"] = {"debug": "yes"}
    #       with open(path, "w") as f:
    #           config.write(f)
    #       reader = configparser.ConfigParser()
    #       reader.read(path)
    #       return reader.getboolean("app", "debug")
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
    result = two_uuids()
    if result is None:
        return False
    a, b = result
    return isinstance(a, uuid.UUID) and isinstance(b, uuid.UUID) and a != b


def _ex2():
    result = roundtrip_uuid()
    if result is None:
        return False
    original, rebuilt = result
    return (
        isinstance(original, uuid.UUID)
        and isinstance(rebuilt, uuid.UUID)
        and original == rebuilt
        and str(original) == str(rebuilt)
    )


def _ex3():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "settings.ini"
        port = write_and_read_port(path)
        return port == 5432 and isinstance(port, int)


def _ex4():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "settings.ini"
        debug = write_and_read_debug(path)
        return debug is True


results = [
    check("Ex 1: two independent uuid.uuid4() calls never collide", _ex1),
    check("Ex 2: a UUID round-trips through str() and uuid.UUID(...)", _ex2),
    check("Ex 3: ConfigParser writes a file, getint() reads 5432 back as int", _ex3),
    check("Ex 4: getboolean() reads 'yes' back as the bool True", _ex4),
]
print("\nAll green — lesson 74 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
