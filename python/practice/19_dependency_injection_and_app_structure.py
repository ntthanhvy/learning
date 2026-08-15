# Practice 19 — Dependency injection with Depends() & structuring an app
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/19_dependency_injection_and_app_structure.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Days 16-18.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

calls = []


# ---------------------------------------------------------------------------
# Exercise 1 — a shared dependency, reused by two routes.
# Write a plain function get_query_params(limit: int = 10) that returns
# {"limit": limit}. Then register two GET routes, "/items" and "/users",
# each taking a parameter `params: dict = Depends(get_query_params)` and
# returning {"received": params}.
def get_query_params(limit: int = 10):
    ...                              # TODO: return {"limit": limit}


@app.get("/items")
def list_items(params: dict = ...):     # TODO: params: dict = Depends(get_query_params)
    ...                                  # TODO: return {"received": params}


@app.get("/users")
def list_users(params: dict = ...):     # TODO: params: dict = Depends(get_query_params)
    ...                                  # TODO: return {"received": params}


# ---------------------------------------------------------------------------
# Exercise 2 — a dependency that gates a request with HTTPException.
# Write require_token(x_token: str = Header(...)) that raises
# HTTPException(status_code=401, detail="bad token") if x_token != "secret",
# and otherwise returns x_token. Register GET "/secure" taking
# `token: str = Depends(require_token)` and returning {"token": token}.
def require_token(x_token: str = Header(...)):
    ...                              # TODO: if x_token != "secret": raise HTTPException(status_code=401, detail="bad token")
    ...                              # TODO: return x_token


@app.get("/secure")
def secure_route(token: str = ...):     # TODO: token: str = Depends(require_token)
    ...                                  # TODO: return {"token": token}


# ---------------------------------------------------------------------------
# Exercise 3 — a sub-dependency chain, called once per request.
# Write get_db() that appends "get_db" to the module-level `calls` list and
# returns {"conn": "fake-db"}. Write get_current_user(db: dict =
# Depends(get_db)) that appends "get_current_user" to `calls` and returns
# {"user": "alice", "db": db}. Register GET "/whoami" taking
# `user: dict = Depends(get_current_user)` and returning `user`.
def get_db():
    ...                              # TODO: calls.append("get_db"); return {"conn": "fake-db"}


def get_current_user(db: dict = ...):   # TODO: db: dict = Depends(get_db)
    ...                                  # TODO: calls.append("get_current_user")
    ...                                  # TODO: return {"user": "alice", "db": db}


@app.get("/whoami")
def whoami(user: dict = ...):           # TODO: user: dict = Depends(get_current_user)
    ...                                  # TODO: return user


# ---------------------------------------------------------------------------
# Exercise 4 — an APIRouter with a prefix, attached via include_router().
# Build an APIRouter named `router` with prefix="/products". Give it one
# GET route at "/{product_id}" returning {"product_id": product_id}
# (product_id: int). Then attach it to `app` with app.include_router(router).
router = APIRouter(prefix="/products")     # TODO: keep this prefix as-is


@router.get("/{product_id}")               # TODO: fix the path if you changed it
def get_product(product_id: int):
    ...                              # TODO: return {"product_id": product_id}


...                                  # TODO: app.include_router(router)


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
    check("Ex 1: shared dependency answers /items with default limit",
          lambda: _client.get("/items").json() == {"received": {"limit": 10}}),
    check("Ex 1b: same shared dependency reused on a different route",
          lambda: _client.get("/users?limit=3").json() == {"received": {"limit": 3}}),
    check("Ex 2: correct token reaches the handler",
          lambda: (lambda r: r.status_code == 200 and r.json() == {"token": "secret"})(
              _client.get("/secure", headers={"x-token": "secret"}))),
    check("Ex 2b: wrong token is blocked with 401, handler never runs",
          lambda: _client.get("/secure", headers={"x-token": "nope"}).status_code == 401),
    check("Ex 3: sub-dependency chain resolves and returns the final shape",
          lambda: _client.get("/whoami").json() == {"user": "alice", "db": {"conn": "fake-db"}}),
    check("Ex 3b: get_db runs exactly once per request in the chain",
          lambda: (calls.clear(), _client.get("/whoami"), calls.count("get_db"))[-1] == 1),
    check("Ex 4: APIRouter route reachable under its own prefix",
          lambda: _client.get("/products/7").json() == {"product_id": 7}),
]

print("\nAll green — lesson 19 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
