# Practice 60 — unittest.mock: faking the outside world in a test
# Run:  cd ~/learning/python && uv run python3 practice/60_unittest_mock.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from unittest.mock import Mock, patch


# ---------------------------------------------------------------------------
# Exercise 1 — build a Mock with a fixed return_value and inspect calls.
# Write make_fake_response(rate) -> Mock, a Mock whose .json() method
# (also a Mock, with its own return_value) returns {"rate": rate}.
def make_fake_response(rate):
    # TODO:
    # fake = Mock()
    # fake.json = Mock(return_value={"rate": rate})
    # return fake
    return None


# ---------------------------------------------------------------------------
# Exercise 2 — patch() a module-level function for one `with` block only.
# `billing.py`-style code under test, defined right here for the exercise:
def fetch_rate(currency):
    # Pretends to hit a network API — in real code this would be
    # `requests.get(...).json()["rate"]`. Here it calls this module's own
    # `_http_get` name so section 5's "patch the right path" lesson applies
    # to a name this file actually owns.
    return _http_get(currency).json()["rate"]


def _http_get(currency):
    raise RuntimeError(f"no real network call should ever happen in a test ({currency})")


def convert(amount, currency):
    return amount * fetch_rate(currency)


# Write patched_convert(amount, currency, rate) -> float that uses
# unittest.mock.patch to temporarily replace THIS MODULE's `_http_get` name
# (patch target: "__main__._http_get") with a Mock returning
# make_fake_response(rate), calls convert(amount, currency) inside the
# `with` block, and returns the result. _http_get must never actually run.
def patched_convert(amount, currency, rate):
    # TODO:
    # with patch("__main__._http_get", return_value=make_fake_response(rate)):
    #     return convert(amount, currency)
    return None


# ---------------------------------------------------------------------------
# Exercise 3 — after the `with` block ends, the original is restored.
# Write real_http_get_still_raises() -> bool, True if calling _http_get(...)
# OUTSIDE any patch block still raises RuntimeError (proving patch() didn't
# permanently replace it).
def real_http_get_still_raises():
    # TODO:
    # try:
    #     _http_get("eur")
    #     return False
    # except RuntimeError:
    #     return True
    return False


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex1():
    fake = make_fake_response(1.5)
    return fake is not None and fake.json() == {"rate": 1.5} and fake.json() == fake.json()


def _ex2():
    result = patched_convert(100, "eur", 1.1)
    return result is not None and abs(result - 110.0) < 1e-9


def _ex3():
    # Exercise 2 must not have permanently replaced _http_get.
    patched_convert(100, "eur", 1.1)  # run it once first, patched
    return real_http_get_still_raises()


results = [
    check("Ex 1: make_fake_response returns a Mock with a fixed .json()", _ex1),
    check("Ex 2: patched_convert mocks _http_get and computes the real product", _ex2),
    check("Ex 3: _http_get is restored to normal after the with block ends", _ex3),
]
print("\nAll green — lesson 60 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
