# Practice 24 — ASGI middleware: wrapping every request/response
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/24_asgi_middleware.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Days 16-23.
#
# Today's exercises build a timing middleware that stamps a response header,
# a structured-logging middleware that records one entry per request, and
# confirm Lesson 24's gotcha directly: a route whose exception has a
# registered @app.exception_handler never reaches middleware's own
# try/except as an exception at all — call_next() just returns a normal,
# finished response, and middleware must read response.status_code to see
# it. A route with NO handler registered is the opposite case: call_next()
# itself raises, so middleware needs a real try/except around it to log
# anything for that request at all.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

app = FastAPI()

log = []          # appended by Exercise 2's middleware
guarded_log = []  # appended by Exercise 3's middleware (separate, so each
                   # exercise's check can look at only its own middleware)


# ---------------------------------------------------------------------------
# Exercise 1 — a timing middleware using call_next.
# Fill in the two TODO lines: await call_next(request) to run the rest of
# the app and get the real response back, then stamp the elapsed time (in
# whole milliseconds, as a string) onto response.headers["X-Process-Time-ms"].
@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    start = time.perf_counter()
    response = ...                  # TODO: await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    ...                              # TODO: response.headers["X-Process-Time-ms"] = str(round(duration_ms))
    return response


# ---------------------------------------------------------------------------
# Exercise 2 — a structured-logging middleware appending to `log`.
# Fill in the TODO: after call_next() returns, append a dict to `log` with
# keys "method", "path", "status_code" — read from request.method,
# request.url.path, and response.status_code respectively.
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    ...                              # TODO: log.append({"method": request.method, "path": request.url.path, "status_code": response.status_code})
    return response


# ---------------------------------------------------------------------------
# Exercise 3 — a guarded middleware that also logs the truly-unhandled case.
# call_next() itself RAISES when a route's exception has no registered
# @app.exception_handler — so unlike Exercise 2, this middleware needs a
# real try/except around call_next() to log anything for that request.
# Fill in the TODO: inside the except block, append {"path": ..., "status_code": 500}
# to `guarded_log`, then re-raise (so FastAPI's own default 500 handling
# still runs and the client still gets a real 500 response).
@app.middleware("http")
async def log_even_unhandled(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception:
        ...                          # TODO: guarded_log.append({"path": request.url.path, "status_code": 500}); raise
    else:
        return response


class OutOfStock(Exception):
    def __init__(self, item: str):
        self.item = item


@app.exception_handler(OutOfStock)
def handle_out_of_stock(request: Request, exc: OutOfStock):
    return JSONResponse(status_code=409, content={"error": "out_of_stock", "item": exc.item})


@app.get("/ok")
def ok():
    return {"hello": "world"}


@app.get("/handled-failure")
def handled_failure():
    raise OutOfStock("widget")


@app.get("/unhandled-failure")
def unhandled_failure():
    raise ValueError("nobody registered a handler for this")


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


_client = TestClient(app, raise_server_exceptions=False)


def _ex1_timing_header_present():
    response = _client.get("/ok")
    header = response.headers.get("x-process-time-ms")
    return response.status_code == 200 and header is not None and float(header) >= 0


def _ex2_log_records_status_code_for_ok_route():
    log.clear()
    _client.get("/ok")
    return len(log) == 1 and log[0]["path"] == "/ok" and log[0]["status_code"] == 200


def _ex3_handled_exception_logged_via_status_code_not_exception():
    # The gotcha: OutOfStock has a registered exception_handler, so
    # call_next() returns a normal 409 response - middleware never sees an
    # exception to catch, only a finished response to read the status from.
    log.clear()
    response = _client.get("/handled-failure")
    return (
        response.status_code == 409
        and len(log) == 1
        and log[0]["status_code"] == 409
    )


def _ex4_truly_unhandled_exception_needs_try_except_to_be_logged():
    # No handler is registered for ValueError, so call_next() itself raises -
    # only a middleware with a real try/except (Exercise 3's guarded_log)
    # can log anything for this request at all; FastAPI's own default
    # handling still turns the response the client sees into a real 500.
    guarded_log.clear()
    response = _client.get("/unhandled-failure")
    return (
        response.status_code == 500
        and len(guarded_log) == 1
        and guarded_log[0]["status_code"] == 500
    )


results = [
    check("Ex 1: timing middleware stamps X-Process-Time-ms", _ex1_timing_header_present),
    check("Ex 2: logging middleware records method/path/status_code", _ex2_log_records_status_code_for_ok_route),
    check("Ex 3: a handled exception is logged via response.status_code, not caught as an exception", _ex3_handled_exception_logged_via_status_code_not_exception),
    check("Ex 3: a truly unhandled exception needs try/except to be logged at all", _ex4_truly_unhandled_exception_needs_try_except_to_be_logged),
]

print("\nAll green — lesson 24 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
