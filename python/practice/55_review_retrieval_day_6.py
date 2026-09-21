# Practice 55 — review day 6: retrieval across six more lessons
# Run:  cd ~/learning/python && uv run python3 practice/55_review_retrieval_day_6.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 15, 28, 29,
# 35, 37, and 40. Replace each `...` (or the marked TODO body) and re-run
# until every check prints ✓. Try each from memory before reopening the old
# lesson.

import logging
from contextlib import ExitStack


# ---------------------------------------------------------------------------
# Exercise 1 (Day 15 — logging: %s-style formatting is lazy, f-strings are not)
# calls_made tracks how many times build_expensive_message() actually runs.
# log_lazy(logger, build_expensive_message) should call logger.debug() using
# %s-style formatting (message as the format string, the built value as a
# separate argument) so the expensive call is skipped entirely when the
# logger's level is above DEBUG.
def log_lazy(logger, build_expensive_message):
    # TODO: logger.debug("%s", build_expensive_message())
    #
    # WAIT - that still calls build_expensive_message() eagerly in Python,
    # since arguments are evaluated before the call happens. The real lazy
    # win needs isEnabledFor() checked first, exactly like logging does
    # internally before formatting a record:
    #     if logger.isEnabledFor(logging.DEBUG):
    #         logger.debug("%s", build_expensive_message())
    ...


# ---------------------------------------------------------------------------
# Exercise 2 (Day 28 — unpacking: *rest has no minimum count of its own)
# split_header(lines) should star-unpack lines into (header, rest), where
# header is the first element and rest is a list of everything else (empty
# list if lines has only one element).
def split_header(lines):
    # TODO: header, *rest = lines
    #       return header, rest
    ...


# ---------------------------------------------------------------------------
# Exercise 3 (Day 29 — context manager: no explicit return means falsy,
# so an exception still propagates)
# LoggingCM appends to `log` on enter and exit. Write __exit__ so it logs
# "exit" and then falls off the end with NO return statement at all
# (not even a bare `return`) — proving that omitting return, which
# implicitly gives None (falsy), still lets an exception raised inside
# the with block propagate normally instead of being suppressed.
class LoggingCM:
    def __init__(self, log):
        self.log = log

    def __enter__(self):
        self.log.append("enter")
        return self

    # TODO: def __exit__(self, exc_type, exc_value, tb):
    #           self.log.append("exit")
    #           (then nothing else — no return statement of any kind)


# ---------------------------------------------------------------------------
# Exercise 4 (Day 35 — __slots__: every class in the chain must opt in)
# Base declares __slots__ = ("a",). Child currently declares none of its
# own, which silently gives Child a real __dict__ back. Fix Child so it
# keeps the __slots__ guarantee too, adding only its own new field "b"
# (not "a", which already lives in Base's slots).
class Base:
    __slots__ = ("a",)


class Child(Base):
    # TODO: __slots__ = ("b",)
    pass


# ---------------------------------------------------------------------------
# Exercise 5 (Day 37 — descriptors: a data descriptor beats the instance
# __dict__, a non-data descriptor loses to it)
# DataDesc defines __get__ AND __set__ (data descriptor).
# NonDataDesc defines __get__ only (non-data descriptor).
# Both classes below assign one of each as a class attribute, then this
# exercise writes straight into the instance's own __dict__ under the same
# names and checks which one actually wins on read.
class DataDesc:
    def __get__(self, obj, objtype=None):
        return "from DataDesc.__get__"

    def __set__(self, obj, value):
        pass  # accepts writes, but reading always goes through __get__ above


class NonDataDesc:
    # TODO: def __get__(self, obj, objtype=None):
    #           return "from NonDataDesc.__get__"
    #
    # Define ONLY __get__ here — no __set__ at all, which is exactly what
    # makes this a NON-data descriptor, losing to the instance __dict__.
    ...


class Holder:
    data_attr = DataDesc()
    nondata_attr = NonDataDesc()


# ---------------------------------------------------------------------------
# Exercise 6 (Day 40 — ExitStack: a runtime-built list of resources, closed
# in reverse order)
# close_all_reversed(log, names) should use ExitStack to "open" a runtime
# list of LogResource stand-ins (one per name) via stack.enter_context(),
# then let them all close automatically in reverse order when the with
# block ends.
class LogResource:
    def __init__(self, log, name):
        self.log = log
        self.name = name

    def __enter__(self):
        self.log.append(f"open {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.log.append(f"close {self.name}")
        return False


def close_all_reversed(log, names):
    # TODO:
    #     with ExitStack() as stack:
    #         for name in names:
    #             stack.enter_context(LogResource(log, name))
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


def _ex1_below_threshold_skips_the_expensive_call():
    logger = logging.getLogger("ex1_quiet")
    logger.setLevel(logging.WARNING)  # DEBUG calls should be filtered out
    calls_made = []

    def build_expensive_message():
        calls_made.append(1)
        return "expensive"

    log_lazy(logger, build_expensive_message)
    return len(calls_made) == 0


def _ex1_above_threshold_makes_the_call():
    logger = logging.getLogger("ex1_loud")
    logger.setLevel(logging.DEBUG)
    calls_made = []

    def build_expensive_message():
        calls_made.append(1)
        return "expensive"

    log_lazy(logger, build_expensive_message)
    return len(calls_made) == 1


def _ex2_multi_element():
    return split_header(["id,name", "1,An", "2,Binh"]) == ("id,name", ["1,An", "2,Binh"])


def _ex2_single_element():
    return split_header(["only-row"]) == ("only-row", [])


def _ex3_exit_runs_and_exception_still_propagates():
    log = []
    raised = False
    try:
        with LoggingCM(log):
            log.append("inside")
            raise ValueError("boom")
    except ValueError:
        raised = True
    return raised and log == ["enter", "inside", "exit"]


def _ex4_child_keeps_slots_guarantee():
    c = Child()
    c.a = 1
    c.b = 2
    try:
        c.z = 3
        return False  # should have raised AttributeError
    except AttributeError:
        return c.a == 1 and c.b == 2 and not hasattr(c, "__dict__")


def _ex5_data_descriptor_wins_over_instance_dict():
    h = Holder()
    h.__dict__["data_attr"] = "instance value"  # deliberately shadow it
    return h.data_attr == "from DataDesc.__get__"


def _ex5_nondata_descriptor_get_works_unshadowed():
    h = Holder()
    return h.nondata_attr == "from NonDataDesc.__get__"


def _ex5_nondata_descriptor_loses_to_instance_dict():
    h = Holder()
    h.__dict__["nondata_attr"] = "instance value"  # deliberately shadow it
    return h.nondata_attr == "instance value"


def _ex6_closes_in_reverse_order():
    log = []
    close_all_reversed(log, ["a", "b", "c"])
    return log == [
        "open a", "open b", "open c",
        "close c", "close b", "close a",
    ]


results = [
    check("Ex 1: log_lazy skips the expensive call below threshold, makes it above",
          lambda: _ex1_below_threshold_skips_the_expensive_call() and _ex1_above_threshold_makes_the_call()),
    check("Ex 2: split_header star-unpacks correctly, even with just one element",
          lambda: _ex2_multi_element() and _ex2_single_element()),
    check("Ex 3: __exit__ with no return still lets a raised exception propagate",
          _ex3_exit_runs_and_exception_still_propagates),
    check("Ex 4: Child keeps the __slots__ guarantee after declaring its own",
          _ex4_child_keeps_slots_guarantee),
    check("Ex 5: a data descriptor wins over the instance dict, a non-data one loses",
          lambda: _ex5_data_descriptor_wins_over_instance_dict()
          and _ex5_nondata_descriptor_get_works_unshadowed()
          and _ex5_nondata_descriptor_loses_to_instance_dict()),
    check("Ex 6: ExitStack closes a runtime-built resource list in reverse order",
          _ex6_closes_in_reverse_order),
]

print("\nAll green — lesson 55 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
