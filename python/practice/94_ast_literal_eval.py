# Practice 94 — ast.literal_eval: parsing Python literals safely
# Run:  cd ~/learning/python && uv run python3 practice/94_ast_literal_eval.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import ast


# ---------------------------------------------------------------------------
# Exercise 1 — parse a literal safely.
# Given a string that is valid Python literal syntax (a list, dict, tuple,
# number, string, bool, or None — possibly nested), return the parsed
# Python value using ast.literal_eval(). Never use eval().
def parse_literal(text):
    # TODO: return ast.literal_eval(text)
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — reject disallowed-but-parseable text safely.
# Given a string, try to parse it with ast.literal_eval(). If parsing
# succeeds, return the parsed value. If it raises ValueError (valid syntax,
# but not a literal — e.g. a function call or a bare name) or SyntaxError
# (not valid Python syntax at all — e.g. an unclosed bracket), catch both
# and return the string "rejected" instead of letting the exception escape.
def parse_or_reject(text):
    # TODO: try:
    #           return ast.literal_eval(text)
    #       except (ValueError, SyntaxError):
    #           return "rejected"
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — tell the two rejection reasons apart.
# Given a string that ast.literal_eval() will refuse, return the name of
# the exception type it actually raises: the string "ValueError" if the
# text is valid syntax but not a literal (e.g. a function call, a bare
# name, or an arithmetic expression), or the string "SyntaxError" if the
# text is not valid Python syntax at all (e.g. an unclosed bracket).
# Do not hard-code which input produces which answer — let literal_eval's
# own exception tell you.
def rejection_reason(text):
    # TODO: try:
    #           ast.literal_eval(text)
    #           return None
    #       except ValueError:
    #           return "ValueError"
    #       except SyntaxError:
    #           return "SyntaxError"
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
    result = parse_literal("{'name': 'Ada', 'nums': [1, 2, 3], 'active': True}")
    return result == {"name": "Ada", "nums": [1, 2, 3], "active": True}


def _ex2():
    good = parse_or_reject("(1, 2, 'x')")
    bad_call = parse_or_reject("__import__('os').system('echo hi')")
    bad_syntax = parse_or_reject("[1, 2,")
    return good == (1, 2, "x") and bad_call == "rejected" and bad_syntax == "rejected"


def _ex3():
    a = rejection_reason("some_name")
    b = rejection_reason("[1, 2,")
    c = rejection_reason("1 + 2")
    return a == "ValueError" and b == "SyntaxError" and c == "ValueError"


results = [
    check("Ex 1: parse_literal() returns the parsed nested value", _ex1),
    check("Ex 2: parse_or_reject() parses good input, rejects bad input", _ex2),
    check("Ex 3: rejection_reason() tells ValueError apart from SyntaxError", _ex3),
]
print("\nAll green — lesson 94 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
