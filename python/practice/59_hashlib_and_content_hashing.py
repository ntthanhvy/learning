# Practice 59 — hashlib and content hashing
# Run:  cd ~/learning/python && uv run python3 practice/59_hashlib_and_content_hashing.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import hashlib
import os
import tempfile
from collections import defaultdict


# ---------------------------------------------------------------------------
# Exercise 1 — hash bytes and confirm determinism.
# Write hash_bytes(data: bytes) -> str returning the sha256 hex digest of data.
def hash_bytes(data):
    # TODO: return hashlib.sha256(data).hexdigest()
    return "TODO_hash_bytes"


# ---------------------------------------------------------------------------
# Exercise 2 — hash a file in chunks, matching a whole-file hash.
# Write hash_file(path, chunk_size=65536) -> str that reads the file in binary
# mode, feeds it to a sha256 object in chunks via .update(), and returns the
# hex digest. Must match hash_bytes() of the same content read in one shot.
def hash_file(path, chunk_size=65536):
    # TODO:
    # h = hashlib.sha256()
    # with open(path, "rb") as f:
    #     while chunk := f.read(chunk_size):
    #         h.update(chunk)
    # return h.hexdigest()
    return "TODO_hash_file"


# ---------------------------------------------------------------------------
# Exercise 3 — detect whether a file changed since a saved hash.
# Write file_changed(path, old_hash) -> bool that returns True if the file's
# current hash differs from old_hash, False if it's the same.
def file_changed(path, old_hash):
    # TODO: return hash_file(path) != old_hash
    return None


# ---------------------------------------------------------------------------
# Exercise 4 — group duplicate files by content hash.
# Write find_duplicates(paths) -> dict mapping hash -> list of paths, but
# ONLY including groups with 2 or more files (exact duplicates).
def find_duplicates(paths):
    # TODO:
    # by_hash = defaultdict(list)
    # for p in paths:
    #     by_hash[hash_file(p)].append(p)
    # return {h: ps for h, ps in by_hash.items() if len(ps) > 1}
    return {}


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
    a = hash_bytes(b"hello world")
    b = hash_bytes(b"hello world")
    c = hash_bytes(b"hello worle")
    return len(a) == 64 and a == b and a != c


def _ex2():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "sample.bin")
        data = b"x" * 200_000 + b"y" * 50_000  # bigger than one 65536 chunk
        with open(path, "wb") as f:
            f.write(data)
        return hash_file(path) == hash_bytes(data) and hash_file(path, chunk_size=17) == hash_bytes(data)


def _ex3():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "report.csv")
        with open(path, "w") as f:
            f.write("city,amount\nHanoi,120\n")
        old = hash_file(path)
        unchanged = file_changed(path, old) is False
        with open(path, "a") as f:
            f.write("Hue,80\n")
        changed = file_changed(path, old) is True
        return unchanged and changed


def _ex4():
    with tempfile.TemporaryDirectory() as d:
        paths = []
        contents = [b"same content", b"same content", b"different content", b"unique one"]
        for i, c in enumerate(contents):
            p = os.path.join(d, f"f{i}.bin")
            with open(p, "wb") as f:
                f.write(c)
            paths.append(p)
        dupes = find_duplicates(paths)
        if len(dupes) != 1:
            return False
        (group,) = dupes.values()
        return sorted(group) == sorted(paths[:2])


results = [
    check("Ex 1: hash_bytes is deterministic and sensitive to a byte change", _ex1),
    check("Ex 2: hash_file (chunked) matches hash_bytes of the same content", _ex2),
    check("Ex 3: file_changed detects an appended line but not a no-op", _ex3),
    check("Ex 4: find_duplicates groups exact-content duplicates only", _ex4),
]
print("\nAll green — lesson 59 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
