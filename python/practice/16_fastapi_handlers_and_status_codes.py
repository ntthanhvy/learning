# Practice 16 — FastAPI handlers, path/query params & status codes
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/16_fastapi_handlers_and_status_codes.py
#
# Needs fastapi + httpx — installed one-off via --with, no pyproject.toml
# changes. First practice file in this course that isn't standard-library
# only, matching Day 11's own one-off `pytest` exception.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

_users = {1: "an", 2: "binh"}


# ---------------------------------------------------------------------------
# Exercise 1 — a GET handler with a path parameter.
# Register a GET route at "/users/{user_id}" (decorate the function below
# with @app.get("/users/{user_id}")) whose handler takes user_id: int and
# returns {"user_id": user_id, "name": _users[user_id]}. Assume user_id is
# always present in _users for this exercise (Exercise 3 handles the
# missing case).
...                                  # TODO: add @app.get("/users/{user_id}") above the def below
def get_user(user_id: int):
    ...                              # TODO: return {"user_id": user_id, "name": _users[user_id]}


# ---------------------------------------------------------------------------
# Exercise 2 — a GET handler with a default-valued query parameter.
# Register a GET route at "/users" whose handler takes a query parameter
# `limit` (type int, default 10) and returns
# {"limit": limit, "user_ids": sorted(_users)[:limit]}.
...                                  # TODO: add @app.get("/users") above the def below
def list_users(limit: int = 10):
    ...                              # TODO: return {"limit": limit, "user_ids": sorted(_users)[:limit]}


# ---------------------------------------------------------------------------
# Exercise 3 — raise HTTPException(404) for a missing user.
# Register a GET route at "/users/{user_id}/strict" whose handler takes
# user_id: int. If user_id is not in _users, raise
# HTTPException(status_code=404, detail="user not found"). Otherwise return
# {"user_id": user_id, "name": _users[user_id]}, same shape as Exercise 1.
...                                  # TODO: add @app.get("/users/{user_id}/strict") above the def below
def get_user_strict(user_id: int):
    ...                              # TODO:
    # if user_id not in _users:
    #     raise HTTPException(status_code=404, detail="user not found")
    # return {"user_id": user_id, "name": _users[user_id]}


# ---------------------------------------------------------------------------
# Exercise 4 — a POST handler returning 201.
# Register a POST route at "/users" with status_code=201 (decorate with
# @app.post("/users", status_code=201)) whose handler takes name: str,
# assigns it the next id (max(_users) + 1), stores it in _users, and
# returns {"user_id": new_id, "name": name}.
...                                  # TODO: add @app.post("/users", status_code=201) above the def below
def create_user(name: str):
    ...                              # TODO:
    # new_id = max(_users) + 1
    # _users[new_id] = name
    # return {"user_id": new_id, "name": name}


# ---------------------------------------------------------------------------
# Exercise 5 — call all four routes through TestClient.
# Given a TestClient `client` already built from `app`, make a GET request
# to "/users/1" and return its parsed JSON body via client.get(path).json().
def get_user_response(client, user_id):
    ...                              # TODO: return client.get(f"/users/{user_id}").json()


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


_client = TestClient(app)

results = [
    check("Ex 1: GET /users/{user_id} returns the matching user",
          lambda: _client.get("/users/1").status_code == 200
          and _client.get("/users/1").json() == {"user_id": 1, "name": "an"}),
    check("Ex 2: GET /users honors the default and an explicit limit query param",
          lambda: _client.get("/users").json() == {"limit": 10, "user_ids": [1, 2]}
          and _client.get("/users?limit=1").json() == {"limit": 1, "user_ids": [1]}),
    check("Ex 3: GET /users/{user_id}/strict returns 404 for a missing user",
          lambda: _client.get("/users/1/strict").status_code == 200
          and _client.get("/users/999/strict").status_code == 404),
    check("Ex 4: POST /users creates a user and returns 201",
          lambda: (lambda r: r.status_code == 201
                    and r.json()["name"] == "chi"
                    and r.json()["user_id"] == 3)(_client.post("/users", params={"name": "chi"}))),
    check("Ex 5: get_user_response() reads a parsed JSON body back from TestClient",
          lambda: get_user_response(_client, 2) == {"user_id": 2, "name": "binh"}),
]

print("\nAll green — lesson 16 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
