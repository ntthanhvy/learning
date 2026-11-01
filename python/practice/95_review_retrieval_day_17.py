# Practice 95 — review day 17: retrieval across Days 92-94
# Run:  cd ~/learning/python && uv run python3 practice/95_review_retrieval_day_17.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 92, 93, and 94.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import ast
import sqlite3
import weakref


class Node:
    def __init__(self, name):
        self.name = name


# ---------------------------------------------------------------------------
# Exercise 1 (Day 92 — weakref: a plain weak reference that returns None
# once the object is collected, and a WeakValueDictionary cache that cleans
# up on its own)
def watch(obj):
    """Return a weakref.ref() pointing at obj."""
    # TODO: return weakref.ref(obj)
    pass


def make_cache():
    """Return a fresh weakref.WeakValueDictionary()."""
    # TODO: return weakref.WeakValueDictionary()
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 93 — sqlite3: a parameterized query that treats an
# injection-shaped string as plain data, never as SQL syntax)
def find_user_by_name(con, name):
    """Query the "users" table for a row whose name column equals `name`,
    using a ? placeholder (never an f-string). Return the matching row's
    name via fetchone(), or None if there is no match."""
    # TODO: cur = con.cursor()
    #       cur.execute("SELECT name FROM users WHERE name = ?", (name,))
    #       row = cur.fetchone()
    #       return row[0] if row else None
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 94 — ast.literal_eval: tell a parseable-but-disallowed
# expression apart from text that isn't valid Python syntax at all)
def classify(text):
    """Try ast.literal_eval(text). Return "ok" if it succeeds, "ValueError"
    if it raises ValueError (valid syntax, not a literal), or "SyntaxError"
    if it raises SyntaxError (not valid syntax at all)."""
    # TODO: try:
    #           ast.literal_eval(text)
    #           return "ok"
    #       except ValueError:
    #           return "ValueError"
    #       except SyntaxError:
    #           return "SyntaxError"
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
    obj = Node("alive")
    ref = watch(obj)
    if ref is None or ref() is not obj:
        return False
    del obj
    if ref() is not None:
        return False  # should be collected -- nothing strong points at it anymore

    cache = make_cache()
    if cache is None:
        return False
    held = Node("cached")
    cache["k"] = held
    if len(cache) != 1 or cache["k"] is not held:
        return False
    del held
    return len(cache) == 0  # entry vanished on its own, no explicit del cache["k"]


def _ex2():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE users (name TEXT)")
    con.execute("INSERT INTO users (name) VALUES (?)", ("Ada",))
    con.commit()

    found = find_user_by_name(con, "Ada")
    injected = find_user_by_name(con, "Ada' OR '1'='1")
    return found == "Ada" and injected is None  # injection string matched nothing


def _ex3():
    a = classify("[1, 2, 3]")
    b = classify("1 + 2")
    c = classify("[1, 2,")
    return a == "ok" and b == "ValueError" and c == "SyntaxError"


results = [
    check("Ex 1 (Day 92): weakref returns None once collected; WeakValueDictionary self-cleans", _ex1),
    check("Ex 2 (Day 93): parameterized query treats an injection string as plain data", _ex2),
    check("Ex 3 (Day 94): literal_eval tells ValueError apart from SyntaxError", _ex3),
]

print("\nAll green — lesson 95 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
