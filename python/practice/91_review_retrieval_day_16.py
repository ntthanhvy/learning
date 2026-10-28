# Practice 91 — review day 16: retrieval across Days 88-90
# Run:  cd ~/learning/python && uv run python3 practice/91_review_retrieval_day_16.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 88, 89, and 90.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import hashlib
import hmac
from collections import ChainMap
from graphlib import CycleError, TopologicalSorter


# ---------------------------------------------------------------------------
# Exercise 1 (Day 88 — ChainMap: layer CLI/user/default settings without
# merging them, and confirm a write only ever lands in the first layer)
def build_settings(cli_flags, user_config, defaults):
    """Return a ChainMap searching cli_flags first, then user_config, then
    defaults — the same priority order as COALESCE(cli, user, default)."""
    # TODO: return ChainMap(cli_flags, user_config, defaults)
    pass


def override_size(settings, new_size):
    """Assign new_size to settings["size"] (through the ChainMap itself,
    not through any one layer directly), then return settings["size"]."""
    # TODO: settings["size"] = new_size
    #       return settings["size"]
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 89 — hmac: compute a keyed tag, confirm a different key
# changes it, and confirm a naive concatenated hash does not match it)
def sign(key, msg):
    """Return the hex digest of an hmac-sha256 tag over msg, keyed by key.
    Both key and msg are bytes."""
    # TODO: return hmac.new(key, msg, hashlib.sha256).hexdigest()
    pass


def naive_concat_hash(key, msg):
    """Return the hex digest of hashlib.sha256(key + msg) -- the tempting
    but wrong shortcut hmac is NOT equivalent to."""
    # TODO: return hashlib.sha256(key + msg).hexdigest()
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 90 — graphlib: read a valid order off a dependency dict,
# and detect a cycle instead of letting a hand-written order drift silently)
def build_order(graph):
    """graph maps each node to a list of its own predecessors (same
    direction as TopologicalSorter's own dict-constructor shortcut).
    Return list(TopologicalSorter(graph).static_order())."""
    # TODO: return list(TopologicalSorter(graph).static_order())
    pass


def has_cycle(graph):
    """Return True if calling build_order(graph) raises CycleError,
    False if it returns normally."""
    # TODO: try:
    #           build_order(graph)
    #           return False
    #       except CycleError:
    #           return True
    pass


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
    defaults = {"color": "blue", "size": "M"}
    user_config = {"size": "L"}
    cli_flags = {}
    settings = build_settings(cli_flags, user_config, defaults)
    if settings is None or settings["size"] != "L" or settings["color"] != "blue":
        return False
    new_size = override_size(settings, "XL")
    return (
        new_size == "XL"
        and cli_flags == {"size": "XL"}
        and user_config == {"size": "L"}  # untouched -- write hit the first layer only
    )


def _ex2():
    key = b"shared-secret-key"
    other_key = b"different-key"
    msg = b'{"order_id": 42}'
    tag = sign(key, msg)
    if not isinstance(tag, str) or sign(key, msg) != tag:
        return False  # same inputs must reproduce the same tag
    if sign(other_key, msg) == tag:
        return False  # a different key must change the tag
    return naive_concat_hash(key, msg) != tag  # not the same construction


def _ex3():
    order = build_order({"a": [], "b": ["a"], "c": ["a", "b"]})
    if order != ["a", "b", "c"]:
        return False
    no_cycle = has_cycle({"a": [], "b": ["a"]})
    yes_cycle = has_cycle({"x": ["y"], "y": ["x"]})
    return no_cycle is False and yes_cycle is True


results = [
    check("Ex 1 (Day 88): ChainMap layers settings, write hits first layer only", _ex1),
    check("Ex 2 (Day 89): hmac tag is key-sensitive and not a naive concat hash", _ex2),
    check("Ex 3 (Day 90): static_order() orders a graph, CycleError on a loop", _ex3),
]

print("\nAll green — lesson 91 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
