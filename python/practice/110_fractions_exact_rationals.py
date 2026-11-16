# Practice 110 — fractions: exact rational numbers, no float imprecision
# Run:  cd ~/learning/python && uv run python3 practice/110_fractions_exact_rationals.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

from fractions import Fraction


# ---------------------------------------------------------------------------
# Exercise 1 — build exact Fraction values from integer pairs and confirm
# their sum is exactly equal to a whole number, not a float near-miss.
# Write sum_of_thirds() that:
#   - builds three Fraction(1, 3) values
#   - returns their sum (a Fraction)
def sum_of_thirds():
    # TODO:
    # return Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — avoid the float-construction trap. Building a Fraction from a
# float literal (e.g. Fraction(0.1)) captures that float's own pre-existing
# binary imprecision instead of the intended exact value. Write
# exact_tenth_from_string() that returns the exact Fraction one-tenth,
# built from the *string* "0.1" (never from the float literal 0.1).
def exact_tenth_from_string():
    # TODO:
    # return Fraction("0.1")
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — limit_denominator(): find the simplest fraction close to a
# messy float, trading a small amount of error for a short denominator.
# Write simplest_fraction_near(value, max_denominator) that:
#   - builds a Fraction from the given float `value`
#   - returns the result of calling .limit_denominator(max_denominator) on it
def simplest_fraction_near(value, max_denominator):
    # TODO:
    # return Fraction(value).limit_denominator(max_denominator)
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
    result = sum_of_thirds()
    if result is None:
        return False
    return result == 1 and result.numerator == 1 and result.denominator == 1


def _ex2():
    result = exact_tenth_from_string()
    if result is None:
        return False
    return result == Fraction(1, 10) and result.numerator == 1 and result.denominator == 10


def _ex3():
    result = simplest_fraction_near(3.1415926535897932, 1000)
    return result == Fraction(355, 113)


if __name__ == "__main__":
    results = [
        check("Ex 1: three Fraction(1, 3) values sum to exactly 1", _ex1),
        check("Ex 2: Fraction built from a string avoids the float-construction trap", _ex2),
        check("Ex 3: limit_denominator() finds the simplest nearby fraction", _ex3),
    ]
    print("\nAll green — lesson 110 done. 🎉" if all(results)
          else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
