# Practice 93 — sqlite3: a real database with no server to run
# Run:  cd ~/learning/python && uv run python3 practice/93_sqlite3_embedded_database.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import sqlite3


# ---------------------------------------------------------------------------
# Exercise 1 — create a table and insert with a parameterized query.
# Given an open sqlite3 connection `con`, a name, and an age:
#   1. Create a table "users" with columns id (INTEGER PRIMARY KEY),
#      name (TEXT), age (INTEGER) — if it doesn't already exist.
#   2. Insert one row (name, age) using a ? placeholder for each value
#      (never an f-string pasted into the SQL text).
#   3. Commit the transaction.
# Return nothing; the caller queries the table afterward.
def create_and_insert(con, name, age):
    # TODO: cur = con.cursor()
    #       cur.execute(
    #           "CREATE TABLE IF NOT EXISTS users "
    #           "(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    #       )
    #       cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    #       con.commit()
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — read a row back by column name.
# Given an open connection `con` already holding a "users" table and a
# name to look up, return the matching row as a sqlite3.Row (so the
# caller can read row["name"] and row["age"]) — not a plain tuple.
# Remember: row_factory must be set on the connection before the cursor
# that runs the SELECT is created.
def fetch_row_by_name(con, name):
    # TODO: con.row_factory = sqlite3.Row
    #       cur = con.cursor()
    #       cur.execute("SELECT id, name, age FROM users WHERE name = ?", (name,))
    #       return cur.fetchone()
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — catch the constraint violation, don't prevent it.
# Given an open connection `con` holding a table "tags" with a UNIQUE
# column "label", and a label that is already present in the table,
# attempt to insert that same label again. Catch sqlite3.IntegrityError
# specifically (never a bare except) and return the string message from
# the exception. Do not pre-check whether the label exists — let SQLite's
# own constraint raise it.
def insert_duplicate_label(con, label):
    # TODO: cur = con.cursor()
    #       try:
    #           cur.execute("INSERT INTO tags (label) VALUES (?)", (label,))
    #           con.commit()
    #           return None
    #       except sqlite3.IntegrityError as e:
    #           return str(e)
    ...


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
    con = sqlite3.connect(":memory:")
    create_and_insert(con, "Ada", 30)
    cur = con.cursor()
    cur.execute("SELECT name, age FROM users WHERE name = ?", ("Ada",))
    row = cur.fetchone()
    return row == ("Ada", 30)


def _ex2():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Grace", 40))
    con.commit()
    row = fetch_row_by_name(con, "Grace")
    if row is None or isinstance(row, tuple):
        return False
    return row["name"] == "Grace" and row["age"] == 40


def _ex3():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE tags (label TEXT UNIQUE)")
    cur.execute("INSERT INTO tags (label) VALUES (?)", ("urgent",))
    con.commit()
    message = insert_duplicate_label(con, "urgent")
    if not isinstance(message, str):
        return False
    cur.execute("SELECT COUNT(*) FROM tags")
    (count,) = cur.fetchone()
    return "UNIQUE" in message and count == 1


results = [
    check("Ex 1: create_and_insert() builds a table and inserts with ?", _ex1),
    check("Ex 2: fetch_row_by_name() returns a sqlite3.Row, lookup by name", _ex2),
    check("Ex 3: insert_duplicate_label() catches IntegrityError, returns its message", _ex3),
]
print("\nAll green — lesson 93 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
