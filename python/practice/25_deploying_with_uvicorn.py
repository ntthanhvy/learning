# Practice 25 — Deploying with uvicorn: workers, reload & env-based config
# Run:  cd ~/learning/python && uv run --with fastapi --with httpx --with pydantic-settings python3 practice/25_deploying_with_uvicorn.py
#
# Needs fastapi, httpx, and pydantic-settings — installed one-off via --with,
# same as Days 16-24. No real uvicorn server actually binds a socket here —
# everything is checkable in-process, same discipline as every FastAPI
# practice file since Day 16 (TestClient, never a real network call).
#
# Today's exercises: a DeploySettings(BaseSettings) reading host/port/workers/
# reload with sane defaults, confirming those fields really do get overridden
# from os.environ (Day 17's coercion, now aimed at deploy config), a
# recommended_workers() function implementing the "(2 * cpu_count) + 1"
# starting point from lesson section 2, and a check that --reload and
# --workers are never both true in one config at once (lesson section 2's
# core gotcha, made concrete instead of only stated in prose).
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import os

from pydantic_settings import BaseSettings


# ---------------------------------------------------------------------------
# Exercise 1 — DeploySettings with sane defaults.
# Define a BaseSettings subclass named DeploySettings with four fields:
#   host: str, default "127.0.0.1"
#   port: int, default 8000
#   workers: int, default 1
#   reload: bool, default False
# TODO: fill in the class body below.
class DeploySettings(BaseSettings):
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — recommended_workers().
# Implement the "(2 * cpu_count) + 1" starting point from lesson section 2.
# Use os.cpu_count(); if it returns None (rare, but documented), treat it as 1.
def recommended_workers() -> int:
    ...  # TODO: return (2 * (os.cpu_count() or 1)) + 1


# ---------------------------------------------------------------------------
# Exercise 3 — reload and workers should never both be requested together.
# Implement is_valid_launch(settings, workers_flag_set): given a DeploySettings
# instance and a bool for "was --workers passed on the command line", return
# False when settings.reload is True AND workers_flag_set is True (the
# combination uvicorn itself refuses), True otherwise.
def is_valid_launch(settings: "DeploySettings", workers_flag_set: bool) -> bool:
    ...  # TODO: return not (settings.reload and workers_flag_set)


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1_defaults():
    s = DeploySettings()
    return (
        s.host == "127.0.0.1"
        and s.port == 8000
        and s.workers == 1
        and s.reload is False
    )


def _ex1_env_override():
    os.environ["PORT"] = "9000"
    os.environ["WORKERS"] = "4"
    os.environ["RELOAD"] = "true"
    try:
        s = DeploySettings()
        return (
            s.port == 9000
            and isinstance(s.port, int)
            and s.workers == 4
            and s.reload is True
            and isinstance(s.reload, bool)
        )
    finally:
        del os.environ["PORT"]
        del os.environ["WORKERS"]
        del os.environ["RELOAD"]


def _ex2_recommended_workers():
    expected = (2 * (os.cpu_count() or 1)) + 1
    return recommended_workers() == expected


def _ex3_reload_and_workers_conflict_is_invalid():
    s = DeploySettings(reload=True)
    return is_valid_launch(s, workers_flag_set=True) is False


def _ex3_reload_alone_is_valid():
    s = DeploySettings(reload=True)
    return is_valid_launch(s, workers_flag_set=False) is True


def _ex3_workers_alone_is_valid():
    s = DeploySettings(reload=False)
    return is_valid_launch(s, workers_flag_set=True) is True


results = [
    check("Ex 1: DeploySettings has the four documented defaults", _ex1_defaults),
    check("Ex 1: DeploySettings reads PORT/WORKERS/RELOAD from the environment", _ex1_env_override),
    check("Ex 2: recommended_workers() implements (2 * cpu_count) + 1", _ex2_recommended_workers),
    check("Ex 3: reload=True with --workers requested is flagged invalid", _ex3_reload_and_workers_conflict_is_invalid),
    check("Ex 3: reload=True alone (no --workers) is valid", _ex3_reload_alone_is_valid),
    check("Ex 3: --workers alone (reload=False) is valid", _ex3_workers_alone_is_valid),
]

print("\nAll green — lesson 25 done!" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
