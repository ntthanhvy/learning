# Practice 22 — Testing endpoints with httpx
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/22_testing_with_httpx.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Days 16-20.
#
# Today's exercises are written as plain functions taking a TestClient and
# asserting inside, the exact test_*-shaped code Lesson 22 teaches — this
# file's own check() wrapper (same one every practice file since Day 8 has
# used) just drives them and reports ✓/✗ instead of a real pytest run, so
# no separate `pytest` command is needed to see the result.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

_users = {1: "an", 2: "binh"}


class ProductNotFound(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id


@app.exception_handler(ProductNotFound)
def _product_not_found_handler(request, exc: ProductNotFound):
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=404,
        content={"detail": f"no product with id {exc.product_id}"},
    )


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in _users:
        raise HTTPException(status_code=404, detail="user not found")
    return {"user_id": user_id, "name": _users[user_id]}


@app.post("/users")
def create_user(name: str):
    new_id = max(_users) + 1
    _users[new_id] = name
    return {"user_id": new_id, "name": name}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id != 1:
        raise ProductNotFound(product_id)
    return {"product_id": 1, "name": "widget"}


# ---------------------------------------------------------------------------
# Exercise 1 — status code AND JSON body, both checked together.
# Given a TestClient `client`, GET "/users/1" and return True only if the
# response's status_code is 200 AND its parsed JSON body equals
# {"user_id": 1, "name": "an"}.
def test_get_user_ok(client) -> bool:
    response = client.get("/users/1")
    ...                              # TODO: return response.status_code == 200 and response.json() == {"user_id": 1, "name": "an"}


# ---------------------------------------------------------------------------
# Exercise 2 — a 404 error path.
# Given a TestClient `client`, GET "/users/999" (a missing user) and return
# True only if the response's status_code is 404.
def test_get_missing_user_404(client) -> bool:
    ...                              # TODO: return client.get("/users/999").status_code == 404


# ---------------------------------------------------------------------------
# Exercise 3 — POST with a query param, checking the new record's shape.
# Given a TestClient `client`, POST "/users" with params={"name": "chi"} and
# return True only if the response's status_code is 200 (the route above
# never set status_code=201, so it defaults to 200) AND
# response.json()["name"] == "chi" AND "user_id" in response.json().
def test_create_user_shape(client) -> bool:
    response = client.post("/users", params={"name": "chi"})
    ...                              # TODO:
    # body = response.json()
    # return (response.status_code == 200 and body["name"] == "chi"
    #         and "user_id" in body)


# ---------------------------------------------------------------------------
# Exercise 4 — a custom exception handler still returns through TestClient.
# Given a TestClient `client`, GET "/products/999" (triggers ProductNotFound,
# caught by the @app.exception_handler(ProductNotFound) above) and return
# True only if status_code == 404 AND "999" appears in
# response.json()["detail"].
def test_product_not_found_handler(client) -> bool:
    ...                              # TODO: response = client.get("/products/999")
    ...                              # TODO: return response.status_code == 404 and "999" in response.json()["detail"]


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
    check("Ex 1: test_get_user_ok checks status AND body together",
          lambda: test_get_user_ok(_client) is True),
    check("Ex 2: test_get_missing_user_404 catches the 404 path",
          lambda: test_get_missing_user_404(_client) is True),
    check("Ex 3: test_create_user_shape checks the new record's shape",
          lambda: test_create_user_shape(_client) is True),
    check("Ex 4: test_product_not_found_handler exercises the custom handler",
          lambda: test_product_not_found_handler(_client) is True),
]

print("\nAll green — lesson 22 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
