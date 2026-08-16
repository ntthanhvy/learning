# Practice 20 — async/await: what it buys, when it doesn't, and blocking-call traps
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx python3 practice/20_async_await_and_blocking_calls.py
#
# Needs fastapi + httpx — installed one-off via --with, same as Days 16-19.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import asyncio
import time

import httpx
from fastapi import FastAPI

app = FastAPI()


# ---------------------------------------------------------------------------
# Exercise 1 — a real async route that yields control.
# Write an async def route at GET "/async-sleep" that awaits
# asyncio.sleep(0.05) and then returns {"ok": True}.
@app.get("/async-sleep")
async def async_sleep():
    ...                              # TODO: await asyncio.sleep(0.05)
    ...                              # TODO: return {"ok": True}


# ---------------------------------------------------------------------------
# Exercise 2 — the blocking-call trap, on purpose.
# Write an async def route at GET "/async-trap" that calls time.sleep(0.05)
# — a BLOCKING call, no await — and then returns {"ok": True}. This is
# deliberately the wrong way to do it, so the checks below can measure the
# difference against Exercise 1.
@app.get("/async-trap")
async def async_trap():
    ...                              # TODO: time.sleep(0.05)  (no await - that's the point)
    ...                              # TODO: return {"ok": True}


# ---------------------------------------------------------------------------
# Exercise 3 — asyncio.gather() runs coroutines concurrently.
# Write an async def function fetch_all(n: int) that builds a list of n
# coroutines, each calling square(i) for i in range(n) (square() is given
# below), and awaits them all at once with asyncio.gather(*coros), returning
# the list of results.
async def square(i: int) -> int:
    await asyncio.sleep(0.03)
    return i * i


async def fetch_all(n: int) -> list[int]:
    ...                              # TODO: coros = [square(i) for i in range(n)]
    ...                              # TODO: return await asyncio.gather(*coros)


# ---------------------------------------------------------------------------
# Exercise 4 — awaiting one at a time instead, for comparison.
# Write an async def function fetch_one_by_one(n: int) that calls and awaits
# square(i) for i in range(n) sequentially (a plain for loop with await
# inside it, no gather), collecting results into a list and returning it.
async def fetch_one_by_one(n: int) -> list[int]:
    ...                              # TODO: results = []
    ...                              # TODO: for i in range(n): results.append(await square(i))
    ...                              # TODO: return results


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


async def _time_n_concurrent_requests(path: str, n: int) -> float:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        t0 = time.perf_counter()
        responses = await asyncio.gather(*[ac.get(path) for _ in range(n)])
        elapsed = time.perf_counter() - t0
        for r in responses:
            if r.status_code != 200 or r.json() != {"ok": True}:
                raise AssertionError(f"bad response from {path}: {r.status_code} {r.text}")
        return elapsed


def _run(coro):
    return asyncio.run(coro)


results = [
    check("Ex 1: /async-sleep answers correctly",
          lambda: _run(_time_n_concurrent_requests("/async-sleep", 1)) is not None),
    check("Ex 1b: 5 concurrent /async-sleep requests overlap (well under 5x0.05s)",
          lambda: _run(_time_n_concurrent_requests("/async-sleep", 5)) < 0.2),
    check("Ex 2: /async-trap answers correctly",
          lambda: _run(_time_n_concurrent_requests("/async-trap", 1)) is not None),
    check("Ex 2b: 5 concurrent /async-trap requests serialize (close to 5x0.05s)",
          lambda: _run(_time_n_concurrent_requests("/async-trap", 5)) > 0.2),
    check("Ex 3: fetch_all(4) returns squares via gather",
          lambda: _run(fetch_all(4)) == [0, 1, 4, 9]),
    check("Ex 3b: fetch_all(4) is correct AND runs concurrently (well under 4x0.03s)",
          lambda: (lambda t0, res: res == [0, 1, 4, 9] and (time.perf_counter() - t0) < 0.08)(
              time.perf_counter(), _run(fetch_all(4)))),
    check("Ex 4: fetch_one_by_one(4) returns the same squares",
          lambda: _run(fetch_one_by_one(4)) == [0, 1, 4, 9]),
    check("Ex 4b: fetch_one_by_one(4) is slower than fetch_all(4) (serialized, ~4x0.03s)",
          lambda: (lambda t0: (_run(fetch_one_by_one(4)), time.perf_counter() - t0)[-1])(time.perf_counter()) > 0.1),
]

print("\nAll green — lesson 20 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
