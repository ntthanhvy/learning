# Practice 58 — review day 7: retrieval across the six backend lessons
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx --with pydantic-settings python3 practice/58_review_retrieval_day_7.py
# Needs fastapi, httpx, and pydantic-settings — installed one-off via --with,
# same as every Day 16-26 practice file.
#
# No new syntax here — every mechanism below was taught in Days 18, 21, 22,
# 23, 25, and 26. Replace each `...` (or the marked TODO body) and re-run
# until every check prints ✓. Try each from memory before reopening the old
# lesson.

import os
import sqlite3

from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel
from pydantic_settings import BaseSettings


# ---------------------------------------------------------------------------
# Exercise 1 (Day 18 — response_model filters a field the handler returned
# but the response model doesn't declare)
# ItemOut should declare only id, name, and price — NOT secret_cost, even
# though the handler below returns a dict that includes it.
class ItemIn(BaseModel):
    name: str
    price: float


class ItemOut(BaseModel):
    # TODO: id: int
    #       name: str
    #       price: float
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 21 — a %s/? placeholder is immune to an injection string
# an f-string is not; uses sqlite3's DB-API, same shape as psycopg)
# safe_lookup(conn, name) should run a parameterized SELECT using a
# placeholder (sqlite3 uses "?", psycopg uses "%s" — same idea) so that an
# injection-style name value matches nothing, unlike a pasted-in f-string.
def safe_lookup(conn, name):
    # TODO: cur = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    #       return cur.fetchall()
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 22 — a test_*-shaped function driving TestClient in-process)
# test_get_widget_returns_200 should call client.get("/widgets/1") and
# assert both the status code (200) and the JSON body
# ({"id": 1, "label": "widget"}) — Day 11's assert-based shape, aimed at a
# route instead of a plain function.
_review_app = FastAPI()


@_review_app.get("/widgets/{widget_id}")
def get_widget(widget_id: int):
    return {"id": widget_id, "label": "widget"}


_review_client = TestClient(_review_app)


def test_get_widget_returns_200():
    # TODO: response = _review_client.get("/widgets/1")
    #       assert response.status_code == 200
    #       assert response.json() == {"id": 1, "label": "widget"}
    #       return True   # <- reached only if both asserts above passed
    ...
    return False  # unsolved default: makes Ex 3 print an honest ✗, not a
                  # vacuous ✓ from an empty, assertion-free function body


# ---------------------------------------------------------------------------
# Exercise 4 (Day 23 — one app-wide exception handler instead of a repeated
# if/raise in every route)
# OutOfStock carries the item name. handle_out_of_stock should return a
# JSONResponse with status_code=409 and
# content={"error": "out_of_stock", "item": exc.item}.
# IMPORTANT: this handler must be registered on _stock_app BEFORE any
# request is made through its TestClient — starlette builds and caches its
# exception-handling stack on first use, so registering it late is a bug,
# not a style choice (this bit an earlier draft of Day 55's own review).
_stock_app = FastAPI()
_stock = {"widget": 0, "gadget": 5}


class OutOfStock(Exception):
    def __init__(self, item: str):
        self.item = item


@_stock_app.exception_handler(OutOfStock)
def handle_out_of_stock(request, exc: OutOfStock):
    # TODO: return JSONResponse(status_code=409, content={"error": "out_of_stock", "item": exc.item})
    ...


@_stock_app.post("/orders/{item}")
def place_order(item: str):
    if _stock.get(item, 0) <= 0:
        raise OutOfStock(item)
    _stock[item] -= 1
    return {"item": item, "remaining": _stock[item]}


_stock_client = TestClient(_stock_app)


# ---------------------------------------------------------------------------
# Exercise 5 (Day 25 — BaseSettings coerces PORT/WORKERS from the
# environment into real int fields, keeping unset fields at their default)
class DeploySettings(BaseSettings):
    # TODO: host: str = "127.0.0.1"
    #       port: int = 8000
    #       workers: int = 1
    ...


# ---------------------------------------------------------------------------
# Exercise 6 (Day 26 — a tiny two-route service: create, then read-or-404,
# composed from Days 17-20 and 23's already-taught pieces, same shape as
# the capstone)
_task_app = FastAPI()
_TASKS: dict[int, dict] = {}
_next_task_id = 1


class TaskIn(BaseModel):
    title: str


class TaskOut(BaseModel):
    id: int
    title: str


class TaskNotFound(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id


@_task_app.exception_handler(TaskNotFound)
def task_not_found_handler(request, exc: TaskNotFound):
    return JSONResponse(status_code=404, content={"error": "task_not_found", "id": exc.task_id})


def get_task_or_404(task_id: int) -> dict:
    if task_id not in _TASKS:
        raise TaskNotFound(task_id)
    return _TASKS[task_id]


@_task_app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(task: TaskIn):
    # TODO: global _next_task_id
    #       record = {"id": _next_task_id, "title": task.title}
    #       _TASKS[_next_task_id] = record
    #       _next_task_id += 1
    #       return record
    ...


@_task_app.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task: dict = Depends(get_task_or_404)):
    # TODO: return task
    ...


_task_client = TestClient(_task_app)


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_response_model_filters_extra_field():
    app = FastAPI()

    @app.post("/items", response_model=ItemOut, status_code=201)
    def create_item(item: ItemIn):
        return {"id": 1, "name": item.name, "price": item.price, "secret_cost": 999}

    client = TestClient(app)
    r = client.post("/items", json={"name": "pen", "price": 12.5})
    return r.status_code == 201 and r.json() == {"id": 1, "name": "pen", "price": 12.5}


def _ex2_placeholder_blocks_injection_fstring_does_not():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice')")
    conn.execute("INSERT INTO users VALUES (2, 'bob')")
    conn.commit()
    injection = "nonexistent' OR '1'='1"
    danger = conn.execute(f"SELECT * FROM users WHERE name = '{injection}'").fetchall()
    safe = safe_lookup(conn, injection)
    return len(danger) == 2 and safe == []


def _ex3_testclient_in_process_test_passes():
    return test_get_widget_returns_200() is True


def _ex4_exception_handler_returns_409_shape():
    r = _stock_client.post("/orders/widget")
    return r.status_code == 409 and r.json() == {"error": "out_of_stock", "item": "widget"}


def _ex4_second_route_would_share_identical_shape():
    # Same handler, different item — proves it's not hardcoded to "widget".
    _stock["gadget"] = 0
    r = _stock_client.post("/orders/gadget")
    return r.status_code == 409 and r.json() == {"error": "out_of_stock", "item": "gadget"}


def _ex5_settings_default_when_unset():
    os.environ.pop("HOST", None)
    s = DeploySettings()
    return s.host == "127.0.0.1"


def _ex5_settings_coerce_from_environment():
    os.environ["PORT"] = "9000"
    os.environ["WORKERS"] = "4"
    s = DeploySettings()
    return s.port == 9000 and isinstance(s.port, int) and s.workers == 4


def _ex6_create_then_read_then_404():
    r_create = _task_client.post("/tasks", json={"title": "write lesson"})
    if r_create.status_code != 201:
        return False
    task_id = r_create.json()["id"]
    r_read = _task_client.get(f"/tasks/{task_id}")
    if r_read.status_code != 200 or r_read.json()["title"] != "write lesson":
        return False
    r_missing = _task_client.get("/tasks/999999")
    return r_missing.status_code == 404 and r_missing.json()["error"] == "task_not_found"


results = [
    check("Ex 1: response_model filters a field the handler returned but ItemOut doesn't declare",
          _ex1_response_model_filters_extra_field),
    check("Ex 2: a placeholder query is immune to injection, an f-string query is not",
          _ex2_placeholder_blocks_injection_fstring_does_not),
    check("Ex 3: a test_*-shaped function asserts status + body via in-process TestClient",
          _ex3_testclient_in_process_test_passes),
    check("Ex 4: one app-wide exception handler gives every raising route the same shape",
          lambda: _ex4_exception_handler_returns_409_shape() and _ex4_second_route_would_share_identical_shape()),
    check("Ex 5: BaseSettings keeps unset fields at default, coerces set ones from the environment",
          lambda: _ex5_settings_default_when_unset() and _ex5_settings_coerce_from_environment()),
    check("Ex 6: create -> read -> 404-on-missing, composed from already-taught pieces",
          _ex6_create_then_read_then_404),
]

print("\nAll green — lesson 58 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
