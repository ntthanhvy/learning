# Practice 21 — Talking to PostgreSQL from Python
# Run:  cd ~/learning/python && uv run python3 practice/21_talking_to_postgresql.py
#
# Standard library only today — no PostgreSQL server or --with needed. The
# exercises use sqlite3, which follows the identical DB-API shape as psycopg
# (connect() -> cursor() -> execute(sql, params) -> fetchone()/fetchall()),
# the one real difference being sqlite3's "?" placeholder vs psycopg's "%s".
# Everything about the *pattern* — placeholders over string-building, cursor
# lifecycle, yield-based setup/teardown — is the same code you'd write
# against a real PostgreSQL connection.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import sqlite3


def _fresh_db():
    """A throwaway in-memory database, seeded with one table. Not part of
    the exercises — just the fixture every exercise below runs against."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.executemany(
        "INSERT INTO users (id, name) VALUES (?, ?)",
        [(1, "alice"), (2, "bob"), (3, "carol")],
    )
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Exercise 1 — connect, run a parameterized SELECT, fetch one row.
# Given an open connection `conn` and a user_id, run
#   SELECT id, name FROM users WHERE id = ?
# with (user_id,) as the params tuple, and return the single row fetched
# with cur.fetchone() (a tuple like (1, "alice"), or None if no match).
def get_user_by_id(conn, user_id: int):
    cur = conn.cursor()
    ...                              # TODO: cur.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
    ...                              # TODO: return cur.fetchone()


# ---------------------------------------------------------------------------
# Exercise 2 — placeholders are immune to injection; string-building isn't.
# Write two functions taking (conn, name) and returning how many rows match.
#
# unsafe_count_by_name builds the query with an f-string (the wrong way,
# on purpose, to prove the point below) and returns len(cur.fetchall()).
#
# safe_count_by_name uses a "?" placeholder with (name,) as the params
# tuple and returns len(cur.fetchall()).
def unsafe_count_by_name(conn, name: str) -> int:
    cur = conn.cursor()
    ...                              # TODO: cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
    ...                              # TODO: return len(cur.fetchall())


def safe_count_by_name(conn, name: str) -> int:
    cur = conn.cursor()
    ...                              # TODO: cur.execute("SELECT * FROM users WHERE name = ?", (name,))
    ...                              # TODO: return len(cur.fetchall())


# ---------------------------------------------------------------------------
# Exercise 3 — a yield-based dependency: setup before, teardown after.
# Write get_db(log: list) as a generator function (uses yield, not return):
#   - before yield: call _fresh_db() to open a connection, append "open" to
#     log, then yield that connection
#   - after yield: append "close" to log, then close the connection
# (In a real FastAPI app this is exactly the shape of Lesson 21 section 3's
# get_db() dependency — here you drive it by hand with next()/StopIteration
# instead of FastAPI calling it for you.)
def get_db(log: list):
    ...                              # TODO: conn = _fresh_db()
    ...                              # TODO: log.append("open")
    ...                              # TODO: yield conn
    ...                              # TODO: log.append("close")
    ...                              # TODO: conn.close()


# ---------------------------------------------------------------------------
# Exercise 4 — fetchall() reads every remaining row.
# Given an open connection `conn`, run SELECT id, name FROM users ORDER BY id
# with no params, and return every row as a list of tuples via fetchall().
def list_all_users(conn):
    cur = conn.cursor()
    ...                              # TODO: cur.execute("SELECT id, name FROM users ORDER BY id")
    ...                              # TODO: return cur.fetchall()


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _drain(gen):
    """Advance a generator past its yield so its teardown code runs, the
    same way FastAPI drives a yield-based dependency to completion after
    a request finishes."""
    try:
        next(gen)
    except StopIteration:
        pass


def _ex3_setup():
    """Runs get_db() through one full open/use/close cycle and returns
    (log, users) so both Ex 3 checks can inspect the outcome without
    running the generator twice (it's single-use, like any generator).
    Wrapped in try/except: an unsolved get_db() (all `...` TODOs, no real
    `yield`) is a plain function returning None, not a generator, so
    next(gen) would raise TypeError — caught here so both Ex 3 checks fail
    with a clean ✗ instead of crashing the whole file before Ex 4 can run."""
    log = []
    try:
        gen = get_db(log)
        conn = next(gen)            # advances get_db() up to its yield
        users = list_all_users(conn)
        _drain(gen)                 # advances get_db() past its yield
        return log, users
    except Exception:
        return [], None


_db1 = _fresh_db()
_db2 = _fresh_db()
_db3 = _fresh_db()
_ex3_log, _ex3_users = _ex3_setup()

results = [
    check("Ex 1: get_user_by_id(1) returns alice's row",
          lambda: get_user_by_id(_db1, 1) == (1, "alice")),
    check("Ex 1b: get_user_by_id(999) returns None for no match",
          lambda: get_user_by_id(_db1, 999) is None),
    check("Ex 2: unsafe_count_by_name is vulnerable to an injection string",
          lambda: unsafe_count_by_name(_db2, "x' OR '1'='1") == 3),
    check("Ex 2b: safe_count_by_name is NOT fooled by the same string",
          lambda: safe_count_by_name(_db2, "x' OR '1'='1") == 0),
    check("Ex 2c: safe_count_by_name still finds a real match normally",
          lambda: safe_count_by_name(_db2, "bob") == 1),
    check("Ex 3: get_db yields an open, usable connection",
          lambda: _ex3_users == [(1, "alice"), (2, "bob"), (3, "carol")]),
    check("Ex 3b: get_db logs open before yield, close after being driven to the end",
          lambda: _ex3_log == ["open", "close"]),
    check("Ex 4: list_all_users returns every row via fetchall()",
          lambda: list_all_users(_db3) == [(1, "alice"), (2, "bob"), (3, "carol")]),
]

print("\nAll green — lesson 21 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
