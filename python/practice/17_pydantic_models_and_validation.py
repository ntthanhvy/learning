# Practice 17 — pydantic models: validation, coercion & settings
# Run:  cd ~/learning/python && uv run --with pydantic --with pydantic-settings python3 practice/17_pydantic_models_and_validation.py
#
# Needs pydantic + pydantic-settings — installed one-off via --with, no
# pyproject.toml changes, same one-off pattern as Day 16's fastapi/httpx.
# No fastapi/httpx needed today since nothing here runs a route.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import os

from pydantic import BaseModel, ValidationError, field_validator


# ---------------------------------------------------------------------------
# Exercise 1 — a BaseModel with coercion.
# Define a pydantic model named Item with fields:
#   name: str
#   price: float
#   qty: int = 1
class Item:                             # TODO: subclass pydantic's BaseModel (class Item(BaseModel):)
    ...                                  # TODO: name: str
    ...                                  # TODO: price: float
    ...                                  # TODO: qty: int = 1


# ---------------------------------------------------------------------------
# Exercise 2 — catching a ValidationError.
# Given a dict of constructor kwargs for Item, try to build an Item from it.
# Return True if construction succeeds, False if it raises ValidationError.
def item_is_valid(kwargs):
    ...                                  # TODO:
    # try:
    #     Item(**kwargs)
    #     return True
    # except ValidationError:
    #     return False


# ---------------------------------------------------------------------------
# Exercise 3 — a field_validator that rejects bad input.
# Define a pydantic model named SignUp with fields username: str, age: int,
# and a @field_validator("username") @classmethod method that raises
# ValueError("username must not contain spaces") if the value contains a
# space, otherwise returns the value lower-cased.
class SignUp(BaseModel):
    username: str
    age: int

    ...                                  # TODO: add @field_validator("username") above the method below
    ...                                  # TODO: add @classmethod above the method below
    def username_no_spaces(cls, v):
        ...                              # TODO:
        # if " " in v:
        #     raise ValueError("username must not contain spaces")
        # return v.lower()


# ---------------------------------------------------------------------------
# Exercise 4 — reading a BaseSettings value from the environment.
# Define a pydantic_settings.BaseSettings subclass named Settings with
# fields app_name: str = "myapp" and debug: bool = False, so that
# Settings() picks up APP_NAME / DEBUG from os.environ when they're set.
from pydantic_settings import BaseSettings  # noqa: E402  (import kept near its exercise, matching this file's per-exercise style)


class Settings:                          # TODO: subclass pydantic_settings' BaseSettings (class Settings(BaseSettings):)
    ...                                  # TODO: app_name: str = "myapp"
    ...                                  # TODO: debug: bool = False


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_coerces_and_defaults():
    item = Item(name="pen", price="12.5", qty="3")
    return (
        item.name == "pen"
        and item.price == 12.5 and isinstance(item.price, float)
        and item.qty == 3 and isinstance(item.qty, int)
        and Item(name="pen", price=1.0).qty == 1
    )


def _ex3_rejects_and_normalizes():
    try:
        SignUp(username="Anh Tuan", age=20)
        rejected = False
    except ValidationError:
        rejected = True
    normalized = SignUp(username="AnhTuan", age=20).username == "anhtuan"
    return rejected and normalized


def _ex4_settings_reads_environment():
    os.environ["APP_NAME"] = "demo-app"
    os.environ["DEBUG"] = "true"
    try:
        s = Settings()
        return s.app_name == "demo-app" and s.debug is True
    finally:
        del os.environ["APP_NAME"]
        del os.environ["DEBUG"]


results = [
    check("Ex 1: Item coerces string input and applies its default",
          _ex1_coerces_and_defaults),
    check("Ex 2: item_is_valid() tells good kwargs from bad ones",
          lambda: item_is_valid({"name": "pen", "price": "12.5"}) is True
          and item_is_valid({"name": "pen", "price": "not-a-number"}) is False),
    check("Ex 3: SignUp's field_validator rejects spaces and lower-cases good input",
          _ex3_rejects_and_normalizes),
    check("Ex 4: Settings() reads APP_NAME / DEBUG from the environment",
          _ex4_settings_reads_environment),
]

print("\nAll green — lesson 17 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
