# Practice 39 — argparse: turning a script into a real command-line tool
# Run:  cd ~/learning/python && uv run python3 practice/39_argparse.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import argparse


# ---------------------------------------------------------------------------
# Exercise 1 — a positional argument plus a type=int optional with a default.
# Build and return an ArgumentParser with:
#   - a required positional argument named "infile"
#   - an optional "-n"/"--top" argument, type=int, default=5
def build_basic_parser():
    # TODO: parser = argparse.ArgumentParser()
    #       parser.add_argument("infile")
    #       parser.add_argument("-n", "--top", type=int, default=5)
    #       return parser
    ...


def run_basic_parser_checks():
    parser = build_basic_parser()
    with_top = parser.parse_args(["report.txt", "--top", "3"])
    without_top = parser.parse_args(["report.txt"])
    return (with_top.infile, with_top.top, without_top.top, type(without_top.top))


# ---------------------------------------------------------------------------
# Exercise 2 — a store_true flag.
# Add a "-v"/"--verbose" flag (action="store_true") to the given parser,
# then return it. Absent from the command line, it should default to False.
def add_verbose_flag(parser):
    # TODO: parser.add_argument("-v", "--verbose", action="store_true")
    #       return parser
    ...


def run_verbose_flag_checks():
    parser = add_verbose_flag(build_basic_parser())
    on = parser.parse_args(["report.txt", "-v"])
    off = parser.parse_args(["report.txt"])
    return (on.verbose, off.verbose)


# ---------------------------------------------------------------------------
# Exercise 3 — choices= restricting an optional argument's allowed values.
# Add a "--unit" option to the given parser: choices=["words", "lines"],
# default="words". Then return it.
def add_unit_choice(parser):
    # TODO: parser.add_argument("--unit", choices=["words", "lines"], default="words")
    #       return parser
    ...


def run_unit_choice_checks():
    parser = add_unit_choice(add_verbose_flag(build_basic_parser()))
    default_unit = parser.parse_args(["report.txt"]).unit
    explicit_unit = parser.parse_args(["report.txt", "--unit", "lines"]).unit
    try:
        parser.parse_args(["report.txt", "--unit", "bytes"])
        rejected_bad_choice = False
    except SystemExit:
        rejected_bad_choice = True
    return (default_unit, explicit_unit, rejected_bad_choice)


# ---------------------------------------------------------------------------
# Exercise 4 — bad input raises SystemExit, not a plain Exception.
# Write parses_cleanly(parser, argv) so it returns True if parser.parse_args(argv)
# succeeds, and False if it raises SystemExit (do NOT catch other exceptions —
# only SystemExit is the expected failure mode here).
def parses_cleanly(parser, argv):
    # TODO: try:
    #           parser.parse_args(argv)
    #           return True
    #       except SystemExit:
    #           return False
    ...


def run_parses_cleanly_checks():
    parser = add_unit_choice(add_verbose_flag(build_basic_parser()))
    good = parses_cleanly(parser, ["report.txt", "--top", "2"])
    bad_type = parses_cleanly(parser, ["report.txt", "--top", "notanum"])
    missing_positional = parses_cleanly(parser, [])
    return (good, bad_type, missing_positional)


# ---------------------------------------------------------------------------
# Checks — don't edit below this line.
def check(name, cond):
    try:
        ok = bool(cond())
    except Exception:
        ok = False
    print(("✓" if ok else "✗"), name)
    return ok


results = [
    check("Ex 1: positional + type=int optional with a default",
          lambda: run_basic_parser_checks() == ("report.txt", 3, 5, int)),
    check("Ex 2: store_true flag defaults False, True only when present",
          lambda: run_verbose_flag_checks() == (True, False)),
    check("Ex 3: choices= applies a default and rejects an out-of-list value",
          lambda: run_unit_choice_checks() == ("words", "lines", True)),
    check("Ex 4: bad input raises SystemExit, good input does not",
          lambda: run_parses_cleanly_checks() == (True, False, False)),
]
print("\nAll green — lesson 39 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
