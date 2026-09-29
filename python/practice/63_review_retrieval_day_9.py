# Practice 63 — review day 9: retrieval across four more lessons
# Run:  cd ~/learning/python && uv run python3 practice/63_review_retrieval_day_9.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 57, 59, 60,
# and 62. Replace each `...` (or the marked TODO body) and re-run until every
# check prints ✓. Try each from memory before reopening the old lesson.

import hashlib
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from unittest.mock import Mock, patch


# ---------------------------------------------------------------------------
# Exercise 1 (Day 57 — field(default_factory=list) gives every instance its
# own independent list, instead of every instance sharing one list built once)
@dataclass
class Cart:
    # TODO: items: list = field(default_factory=list)
    items: list = None


# ---------------------------------------------------------------------------
# Exercise 2 (Day 59 — hashing a file in chunks via .update() must match
# hashing the same bytes in one call; update() is cumulative, not a replace)
def hash_bytes_in_chunks(data, chunk_size):
    h = hashlib.sha256()
    for i in range(0, len(data), chunk_size):
        # TODO: h.update(data[i:i + chunk_size])
        ...
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Exercise 3 (Day 60 — patch()'s target string names where a name is looked
# up, not where it was defined; a module that does `from mod import name`
# holds its own separate local copy that a patch on the original never
# touches)
# `billing` below is a tiny stand-in module (a SimpleNamespace-like object)
# that has already imported `get` directly, the way `from requests import
# get` would. fetch_rate() calls billing.get(...) directly.
class _Billing:
    def get(self, url):  # pretend "real" network call
        raise RuntimeError("real network call — should never run in a test")


billing = _Billing()


def fetch_rate(url):
    return billing.get(url)


def patch_the_wrong_path():
    """Patch a path that does NOT affect billing.get, then call fetch_rate.
    Return the Mock object used, after calling fetch_rate inside the patch
    (fetch_rate will raise — that's expected and fine, this demonstrates the
    mock never actually got used)."""
    fake = Mock(return_value={"rate": 1.1})
    # TODO: with patch("os.path.exists", fake):  # names something real but irrelevant
    #           try:
    #               fetch_rate("https://example.com")
    #           except RuntimeError:
    #               pass
    ...
    return fake


def patch_the_right_path():
    """Patch billing's own `get` name (the one fetch_rate actually calls),
    call fetch_rate, and return its result."""
    fake = Mock(return_value={"rate": 1.1})
    # TODO: with patch.object(billing, "get", fake):
    #           return fetch_rate("https://example.com")
    ...


# ---------------------------------------------------------------------------
# Exercise 4 (Day 62 — shutil.copytree() refuses to run if the destination
# already exists, to protect against a destination-path typo silently
# merging into and corrupting an existing directory)
def copy_tree_safely(src_dir, dst_dir):
    """Call shutil.copytree(src_dir, dst_dir) and return True if it raised
    FileExistsError (because dst_dir already existed), False if it did not
    raise at all."""
    # TODO: try:
    #           shutil.copytree(src_dir, dst_dir)
    #           return False
    #       except FileExistsError:
    #           return True
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


def _ex1_two_carts_do_not_share_one_list():
    c1 = Cart()
    c2 = Cart()
    c1.items.append("apple")
    return c1.items == ["apple"] and c2.items == []


def _ex2_chunked_matches_whole():
    data = b"x" * 200_000 + b"the quick brown fox" + b"y" * 50_000
    whole = hashlib.sha256(data).hexdigest()
    chunked = hash_bytes_in_chunks(data, 65536)
    return whole == chunked


def _ex3_wrong_path_never_actually_used():
    fake = patch_the_wrong_path()
    return fake.called is False


def _ex3_right_path_gets_used():
    result = patch_the_right_path()
    return result == {"rate": 1.1}


def _ex4_raises_when_destination_exists():
    with tempfile.TemporaryDirectory() as d:
        src_dir = Path(d) / "src"
        src_dir.mkdir()
        (src_dir / "a.txt").write_text("a")
        dst_dir = Path(d) / "dst"
        dst_dir.mkdir()  # destination already exists on purpose
        return copy_tree_safely(src_dir, dst_dir) is True


results = [
    check("Ex 1: field(default_factory=list) gives each Cart its own list",
          _ex1_two_carts_do_not_share_one_list),
    check("Ex 2: hashing in chunks via .update() matches hashing in one call",
          _ex2_chunked_matches_whole),
    check("Ex 3: patching the wrong path never actually redirects the real call",
          _ex3_wrong_path_never_actually_used),
    check("Ex 3: patching the right path redirects the call to the fake",
          _ex3_right_path_gets_used),
    check("Ex 4: copytree() raises FileExistsError when the destination already exists",
          _ex4_raises_when_destination_exists),
]

print("\nAll green — lesson 63 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
