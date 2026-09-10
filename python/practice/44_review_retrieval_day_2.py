# Practice 44 — review day 2: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/44_review_retrieval_day_2.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 16-38.
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓. Try each from memory before reopening the old lesson.
#
# Exercises 1 and 2 test the same *rules* Days 16/19 taught, in plain
# Python — a dict stands in for a request's path/query params, and a list
# stands in for a call-count tracker — rather than running a real FastAPI
# app, so this file stays standard-library-only.

import re
from enum import Enum, auto


# ---------------------------------------------------------------------------
# Exercise 1 (Day 16 — FastAPI handlers: path vs query params)
# Given a route URL template like "/users/{user_id}" and a dict of the
# names actually supplied on the incoming call, return a tuple of two sets:
# (path_param_names, query_param_names) using Day 16's own rule — a name is
# a path param exactly when it appears inside {} in the url_template.
def classify_params(url_template, supplied_names):
    # TODO: path params are the {name} segments found in url_template;
    #       query params are every name in supplied_names NOT in that set.
    #       e.g. classify_params("/users/{user_id}", {"user_id", "limit"})
    #       -> ({"user_id"}, {"limit"})
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 19 — dependency injection: shared dependency runs once)
# Simulate resolving a sub-dependency chain for ONE request: get_db() feeds
# get_current_user(), and both are needed by the "handler". Track how many
# times get_db actually ran by appending to `call_log` each time it runs.
# Must call get_db exactly once for the whole request, then reuse its
# result for get_current_user — not call get_db a second time.
def resolve_request(call_log):
    def get_db():
        call_log.append("get_db")
        return {"conn": "fake-db"}

    def get_current_user(db):
        return {"user": "alice", "db": db}

    # TODO: db = get_db(); return get_current_user(db)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 30 — dunder methods: __eq__ falls back to identity)
# Money has NO __eq__ defined at all. Return whether two separately
# constructed Money instances with the same amount compare equal with ==.
# (The point: without __eq__, == falls back to identity, per Day 30/Day 1.)
class Money:
    def __init__(self, cents):
        self.cents = cents


def same_amount_equal_without_eq(cents):
    m1 = Money(cents)
    m2 = Money(cents)
    # TODO: return m1 == m2  (will be False — identity fallback, not a bug)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 (Day 33 — Enum: a member is never equal to its bare value)
class Status(Enum):
    PENDING = auto()
    SHIPPED = auto()
    CANCELLED = auto()


def status_equals_plain_string(member, text):
    # TODO: return member == text  (an Enum member is never == a bare str)
    ...


# ---------------------------------------------------------------------------
# Exercise 5 (Day 34 — match/case: a failing guard skips to the next case)
# Return "small" if n < 10, "big-even" if n is even (and >= 10), else
# "big-odd" — written with match/case and a guard clause, per Day 34.
def classify_number(n):
    # TODO:
    #     match n:
    #         case x if x < 10:
    #             return "small"
    #         case x if x % 2 == 0:
    #             return "big-even"
    #         case _:
    #             return "big-odd"
    ...


# ---------------------------------------------------------------------------
# Exercise 6 (Day 38 — re.search vs re.match)
# re.match only anchors at index 0; re.search scans the whole string.
# Return a (match_result, search_result) tuple of booleans: whether each
# function finds pattern `r"super"` in `"insuperable"`.
def match_vs_search():
    # TODO: return (re.match(r"super", "insuperable") is not None,
    #               re.search(r"super", "insuperable") is not None)
    ...


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


def _ex2_single_call_and_correct_result():
    call_log = []
    result = resolve_request(call_log)
    return call_log == ["get_db"] and result == {
        "user": "alice",
        "db": {"conn": "fake-db"},
    }


results = [
    check("Ex 1: classify_params splits path vs query params by Day 16's rule",
          lambda: classify_params("/users/{user_id}", {"user_id", "limit"})
          == ({"user_id"}, {"limit"})),
    check("Ex 1b: classify_params with no query params returns an empty query set",
          lambda: classify_params("/ping", set()) == (set(), set())),
    check("Ex 2: resolve_request calls get_db exactly once and returns the chained result",
          _ex2_single_call_and_correct_result),
    check("Ex 3: Money with no __eq__ falls back to identity (separate instances are unequal)",
          lambda: same_amount_equal_without_eq(500) is False),
    check("Ex 4: an Enum member is never == its own bare string/name",
          lambda: status_equals_plain_string(Status.SHIPPED, "SHIPPED") is False),
    check("Ex 5: classify_number(3) is 'small'",
          lambda: classify_number(3) == "small"),
    check("Ex 5b: classify_number(10) is 'big-even' and classify_number(11) is 'big-odd'",
          lambda: classify_number(10) == "big-even" and classify_number(11) == "big-odd"),
    check("Ex 6: re.match fails but re.search succeeds on 'insuperable'",
          lambda: match_vs_search() == (False, True)),
]
print("\nAll green — lesson 44 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
