# Practice 64 — zipfile: reading and writing zip archives
# Run:  cd ~/learning/python && uv run python3 practice/64_zipfile_reading_and_writing_archives.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import zipfile
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 — write several files into a new zip archive.
# Write make_archive(zip_path, files) where `files` is a dict mapping the
# internal archive name -> text content, e.g. {"report.csv": "a,b\n1,2\n"}.
# Create zip_path in write mode and add each entry with that exact name.
def make_archive(zip_path, files):
    # TODO: with zipfile.ZipFile(zip_path, "w") as zf:
    #           for name, content in files.items():
    #               zf.writestr(name, content)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — list an archive's members without extracting anything.
# Write list_members(zip_path) that returns a list of member names inside
# the archive, in whatever order namelist() gives them.
def list_members(zip_path):
    # TODO: with zipfile.ZipFile(zip_path) as zf: return zf.namelist()
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — read one member's bytes directly out of the archive.
# Write read_member(zip_path, name) that returns the text content of the
# named member, decoded as utf-8, without extracting the whole archive.
def read_member(zip_path, name):
    # TODO: with zipfile.ZipFile(zip_path) as zf:
    #           with zf.open(name) as f:
    #               return f.read().decode("utf-8")
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — extract everything to a directory.
# Write extract_all(zip_path, dest_dir) that extracts every member of the
# archive into dest_dir, preserving any nested folder structure.
def extract_all(zip_path, dest_dir):
    # TODO: with zipfile.ZipFile(zip_path) as zf: zf.extractall(dest_dir)
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
    with tempfile.TemporaryDirectory() as d:
        zip_path = Path(d) / "drop.zip"
        make_archive(zip_path, {
            "orders.csv": "id,amount\n1,10\n",
            "nested/readme.txt": "hello",
        })
        with zipfile.ZipFile(zip_path) as zf:
            names = set(zf.namelist())
            return names == {"orders.csv", "nested/readme.txt"}


def _ex2():
    with tempfile.TemporaryDirectory() as d:
        zip_path = Path(d) / "drop.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("a.txt", "aaa")
            zf.writestr("b.txt", "bbb")
        return sorted(list_members(zip_path)) == ["a.txt", "b.txt"]


def _ex3():
    with tempfile.TemporaryDirectory() as d:
        zip_path = Path(d) / "drop.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("orders.csv", "id,amount\n1,10\n")
            zf.writestr("customers.csv", "id,name\n1,Mai\n")
        return read_member(zip_path, "orders.csv") == "id,amount\n1,10\n"


def _ex4():
    with tempfile.TemporaryDirectory() as d:
        zip_path = Path(d) / "drop.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("top.txt", "top")
            zf.writestr("sub/inner.txt", "inner")
        dest = Path(d) / "extracted"
        extract_all(zip_path, dest)
        return (
            (dest / "top.txt").read_text() == "top"
            and (dest / "sub" / "inner.txt").read_text() == "inner"
        )


results = [
    check("Ex 1: make_archive writes multiple named entries into a zip", _ex1),
    check("Ex 2: list_members lists names without extracting anything", _ex2),
    check("Ex 3: read_member reads one member's bytes directly", _ex3),
    check("Ex 4: extract_all extracts everything, nested folders included", _ex4),
]
print("\nAll green — lesson 64 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
