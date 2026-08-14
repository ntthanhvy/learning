# Practice 18 — Request/response schemas: the type hints ARE the contract
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/18_request_response_schemas.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Day 16. No
# pydantic-settings needed today since nothing here reads the environment.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()

_items = {}
_next_id = 1


# ---------------------------------------------------------------------------
# Exercise 1 — a request-body model.
# Define a pydantic model named ItemIn with fields:
#   name: str
#   price: float
class ItemIn:                           # TODO: subclass pydantic's BaseModel (class ItemIn(BaseModel):)
    ...                                  # TODO: name: str
    ...                                  # TODO: price: float


# ---------------------------------------------------------------------------
# Exercise 2 — a POST handler that takes ItemIn as its request body.
# Register a POST route at "/items" (decorate with @app.post("/items"))
# whose handler takes one parameter `item: ItemIn`, assigns it the next id
# (a module-level counter starting at 1), stores it in _items, and returns
# {"id": new_id, "name": item.name, "price": item.price}.
...                                  # TODO: add @app.post("/items") above the def below
def create_item(item: ItemIn):
    ...                              # TODO:
    # global _next_id
    # new_id = _next_id
    # _next_id += 1
    # _items[new_id] = item
    # return {"id": new_id, "name": item.name, "price": item.price}


# ---------------------------------------------------------------------------
# Exercise 3 — a response model narrower than what the handler returns.
# Define a pydantic model named ItemOut with fields:
#   id: int
#   name: str
class ItemOut:                          # TODO: subclass pydantic's BaseModel (class ItemOut(BaseModel):)
    ...                                  # TODO: id: int
    ...                                  # TODO: name: str


# ---------------------------------------------------------------------------
# Exercise 4 — wire ItemOut up as a route's response_model.
# Register a POST route at "/items/summary", with response_model=ItemOut and
# status_code=201, whose handler takes item: ItemIn and returns
# {"id": 99, "name": item.name, "price": item.price} — note "price" isn't
# a field on ItemOut, so it must not appear in the actual JSON response.
...                                  # TODO: add @app.post("/items/summary", response_model=ItemOut, status_code=201) above the def below
def create_item_summary(item: ItemIn):
    ...                              # TODO: return {"id": 99, "name": item.name, "price": item.price}


# ---------------------------------------------------------------------------
# Exercise 5 — call both routes through TestClient and read the results.
# Given a TestClient `client` already built from `app`, POST `body` (a dict)
# as JSON to "/items" and return the parsed response JSON.
def post_item(client, body):
    ...                              # TODO: return client.post("/items", json=body).json()


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
    check("Ex 1: ItemIn is a BaseModel with name/price fields",
          lambda: ItemIn(name="pen", price="12.5").price == 12.5
          and isinstance(ItemIn(name="pen", price="12.5").price, float)),
    check("Ex 2: POST /items reads a JSON body into ItemIn and stores it",
          lambda: post_item(_client, {"name": "pen", "price": "12.5"})
          == {"id": 1, "name": "pen", "price": 12.5}),
    check("Ex 2b: POST /items with a missing field returns 422, no crash",
          lambda: _client.post("/items", json={"name": "pen"}).status_code == 422),
    check("Ex 3: ItemOut is a BaseModel with id/name fields only",
          lambda: ItemOut(id=1, name="pen").name == "pen"
          and not hasattr(ItemOut(id=1, name="pen"), "price")),
    check("Ex 4: POST /items/summary returns 201 and drops the price field",
          lambda: (lambda r: r.status_code == 201
                    and r.json() == {"id": 99, "name": "pen"})(
              _client.post("/items/summary", json={"name": "pen", "price": "3.0"}))),
    check("Ex 5: post_item() returns the parsed JSON response body",
          lambda: post_item(_client, {"name": "cup", "price": "4.0"})["name"] == "cup"),
]

print("\nAll green — lesson 18 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
