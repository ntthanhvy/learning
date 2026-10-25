# Practice 88 — collections.ChainMap: layered lookups without merging
# Run:  cd ~/learning/python && uv run python3 practice/88_chainmap_layered_lookups.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

from collections import ChainMap


# ---------------------------------------------------------------------------
# Exercise 1 — build a layered settings lookup.
# Given three dicts (highest priority first: cli, then user, then defaults),
# return a ChainMap that searches cli first, then user, then defaults.
def build_settings(cli, user, defaults):
    # TODO: return ChainMap(cli, user, defaults)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — writes only touch the first layer.
# Given an existing ChainMap `settings`, set the key "size" to "XL" on it
# directly (through the ChainMap, not through one of its .maps), then
# return settings.maps[0] — the first underlying dict — so the caller can
# confirm the write landed there and nowhere else.
def write_and_show_first_layer(settings):
    # TODO: settings["size"] = "XL"
    #       return settings.maps[0]
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — a temporary override with new_child().
# Given an existing ChainMap `settings` and a dict `overrides`, return a
# NEW ChainMap with `overrides` as its highest-priority layer in front of
# `settings`'s own layers, without modifying `settings` itself.
def with_override(settings, overrides):
    # TODO: return settings.new_child(overrides)
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


def _ex1():
    cli = {}
    user = {"size": "L"}
    defaults = {"color": "blue", "size": "M"}
    settings = build_settings(cli, user, defaults)
    return (
        isinstance(settings, ChainMap)
        and settings["size"] == "L"
        and settings["color"] == "blue"
        and list(settings.maps) == [cli, user, defaults]
    )


def _ex2():
    cli = {}
    user = {"size": "L"}
    defaults = {"color": "blue", "size": "M"}
    settings = ChainMap(cli, user, defaults)
    first_layer = write_and_show_first_layer(settings)
    return (
        settings["size"] == "XL"
        and first_layer == {"size": "XL"}
        and cli == {"size": "XL"}
        and user == {"size": "L"}
        and defaults == {"color": "blue", "size": "M"}
    )


def _ex3():
    cli = {}
    user = {"size": "L"}
    defaults = {"color": "blue", "size": "M"}
    settings = ChainMap(cli, user, defaults)
    scoped = with_override(settings, {"size": "S"})
    return (
        scoped is not settings
        and scoped["size"] == "S"
        and settings["size"] == "L"
        and scoped["color"] == "blue"
    )


results = [
    check("Ex 1: build_settings() chains cli, then user, then defaults", _ex1),
    check("Ex 2: writing through the ChainMap only changes the first layer", _ex2),
    check("Ex 3: new_child() overrides without touching the original", _ex3),
]
print("\nAll green — lesson 88 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
