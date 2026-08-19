# Practice 23 — Error handling: custom exceptions, exception handlers & a
# consistent error shape
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/23_error_handling_and_exception_handlers.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Days 16-22.
#
# Today's exercises build a custom exception, an @app.exception_handler that
# turns it into a chosen response, and a RequestValidationError handler that
# reshapes pydantic's default 422 body — Lesson 23's two mechanisms, driven
# through TestClient exactly like every practice file since Day 16.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()

_stock = {"widget": 0, "gadget": 5}


# ---------------------------------------------------------------------------
# Exercise 1 — a custom exception, Day 8's shape.
# Define OutOfStock as a subclass of Exception whose __init__ takes an
# `item: str` and stores it as self.item — the exact InvalidSalesRow pattern
# from Day 8, just a new name and one field.
class OutOfStock(Exception):
    ...                              # TODO: def __init__(self, item: str):
    ...                              # TODO:     self.item = item


# ---------------------------------------------------------------------------
# Exercise 2 — an app-wide exception handler for OutOfStock.
# Register this function with @app.exception_handler(OutOfStock) (the
# decorator is already applied below) so it returns a JSONResponse with
# status_code=409 and content={"error": "out_of_stock", "item": exc.item}.
@app.exception_handler(OutOfStock)
def handle_out_of_stock(request: Request, exc: OutOfStock):
    ...                              # TODO: return JSONResponse(status_code=409, content={"error": "out_of_stock", "item": exc.item})


@app.post("/orders/{item}")
def place_order(item: str):
    if _stock.get(item, 0) <= 0:
        raise OutOfStock(item)
    _stock[item] -= 1
    return {"item": item, "remaining": _stock[item]}


class Signup(BaseModel):
    email: str
    age: int


# ---------------------------------------------------------------------------
# Exercise 3 — reshaping RequestValidationError's default body.
# Register this function with @app.exception_handler(RequestValidationError)
# (decorator already applied below) so it returns a JSONResponse with
# status_code=422 and content={"error": "validation_failed",
# "field": first["loc"][-1], "message": first["msg"]}, where `first` is
# exc.errors()[0] — the first failing field's error dict.
@app.exception_handler(RequestValidationError)
def handle_validation_error(request: Request, exc: RequestValidationError):
    first = exc.errors()[0]
    ...                              # TODO: return JSONResponse(status_code=422, content={"error": "validation_failed", "field": first["loc"][-1], "message": first["msg"]})


@app.post("/signup")
def signup(payload: Signup):
    return {"email": payload.email, "age": payload.age}


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


def _ex1_custom_exception_has_item():
    exc = OutOfStock("widget")
    return exc.item == "widget"


def _ex2_out_of_stock_returns_409_shape():
    response = _client.post("/orders/widget")
    body = response.json()
    return (
        response.status_code == 409
        and body == {"error": "out_of_stock", "item": "widget"}
    )


def _ex2_in_stock_still_works_normally():
    response = _client.post("/orders/gadget")
    return response.status_code == 200 and response.json()["item"] == "gadget"


def _ex3_validation_error_reshaped():
    response = _client.post("/signup", json={"email": "an@example.com", "age": "not-a-number"})
    body = response.json()
    return (
        response.status_code == 422
        and body.get("error") == "validation_failed"
        and body.get("field") == "age"
        and "message" in body
    )


results = [
    check("Ex 1: OutOfStock stores the item that ran out", _ex1_custom_exception_has_item),
    check("Ex 2: handle_out_of_stock returns 409 with the right shape", _ex2_out_of_stock_returns_409_shape),
    check("Ex 2: an in-stock order still succeeds normally", _ex2_in_stock_still_works_normally),
    check("Ex 3: handle_validation_error reshapes the default 422 body", _ex3_validation_error_reshaped),
]

print("\nAll green — lesson 23 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
