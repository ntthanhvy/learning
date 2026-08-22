# Practice 26 — Capstone: a small FastAPI + pydantic task service
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/26_fastapi_capstone.py
#
# Needs fastapi and httpx, installed one-off via --with, same as every
# FastAPI practice file since Day 16. No real uvicorn server binds a socket
# here — everything runs in-process through TestClient, same discipline as
# Days 16, 18, 19, 22, 23, and 24.
#
# Today wires together nearly every Phase 2b lesson into one small service:
# Day 16 (handlers + status codes), Day 17 (pydantic validation), Day 18
# (response_model), Day 19 (Depends), Day 20 (async/await), Day 22 (testing
# via TestClient), and Day 23 (a custom exception + exception handler).
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import asyncio

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel, field_validator

app = FastAPI()

_DB: dict[int, dict] = {}
_NEXT_ID = 1


# ---------------------------------------------------------------------------
# Exercise 1 — TaskIn: the request-body pydantic model.
# Fields: title (str, required), done (bool, default False).
# Add a @field_validator("title") that raises ValueError if the stripped
# title is empty — Day 17's custom-validator shape.
class TaskIn(BaseModel):
    ...  # TODO: title: str, done: bool = False, plus the validator


# ---------------------------------------------------------------------------
# Exercise 2 — TaskOut: the response-body pydantic model, Day 18's
# response_model idea. Fields: id (int), title (str), done (bool).
class TaskOut(BaseModel):
    ...  # TODO


# ---------------------------------------------------------------------------
# Exercise 3 — a custom exception + its exception handler (Day 23's shape).
class TaskNotFound(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id


@app.exception_handler(TaskNotFound)
async def task_not_found_handler(request, exc: TaskNotFound):
    # TODO: return a JSONResponse, status_code=404, content=
    #   {"error": "task_not_found", "id": exc.task_id}
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — a dependency (Day 19's Depends() shape) that looks a task up
# by id and raises TaskNotFound if it's missing, otherwise returns the dict.
def get_task_or_404(task_id: int) -> dict:
    ...  # TODO


# ---------------------------------------------------------------------------
# Routes — don't edit below this line except where a TODO says so.
@app.post("/tasks", response_model=TaskOut, status_code=201)
async def create_task(task: TaskIn):
    global _NEXT_ID
    await asyncio.sleep(0)  # Day 20: a real async checkpoint, however small
    record = {"id": _NEXT_ID, "title": task.title, "done": task.done}
    _DB[_NEXT_ID] = record
    _NEXT_ID += 1
    return record


@app.get("/tasks/{task_id}", response_model=TaskOut)
async def read_task(task: dict = Depends(get_task_or_404)):
    return task


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


client = TestClient(app)


def _ex1_and_2_create_task_shape():
    r = client.post("/tasks", json={"title": "write lesson"})
    body = r.json()
    return (
        r.status_code == 201
        and body["title"] == "write lesson"
        and body["done"] is False
        and isinstance(body["id"], int)
    )


def _ex1_blank_title_rejected():
    r = client.post("/tasks", json={"title": "   "})
    return r.status_code == 422


def _ex4_read_back_created_task():
    created = client.post("/tasks", json={"title": "read me back"}).json()
    r = client.get(f"/tasks/{created['id']}")
    return r.status_code == 200 and r.json() == created


def _ex3_and_4_missing_task_is_404_with_shape():
    r = client.get("/tasks/999999")
    return r.status_code == 404 and r.json() == {"error": "task_not_found", "id": 999999}


results = [
    check("Ex 1/2: POST /tasks returns 201 with the right TaskOut shape", _ex1_and_2_create_task_shape),
    check("Ex 1: a blank title is rejected with 422", _ex1_blank_title_rejected),
    check("Ex 4: GET /tasks/{id} reads back a just-created task", _ex4_read_back_created_task),
    check("Ex 3/4: a missing task returns the custom 404 shape", _ex3_and_4_missing_task_is_404_with_shape),
]

print("\nAll green — capstone done, Phase 2b fully wired together!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
