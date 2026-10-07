# Practice 70 — decimal: exact arithmetic for money
# Run:  cd ~/learning/python && uv run python3 practice/70_decimal_exact_arithmetic.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.

from decimal import Decimal, ROUND_HALF_UP


# ---------------------------------------------------------------------------
# Exercise 1 — confirm float addition drifts away from the exact answer.
# Write float_addition_is_inexact() that returns True if adding 0.1 and 0.2
# as plain floats does NOT equal 0.3, and False if it does.
def float_addition_is_inexact():
    # TODO: return (0.1 + 0.2) != 0.3
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — build a Decimal correctly, from a string, not a float.
# Write decimal_from_text(text) that returns Decimal(text) — text is
# always a str like "0.1", never a float.
def decimal_from_text(text):
    # TODO: return Decimal(text)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — sum a list of price strings exactly with Decimal.
# Write total_price(price_strings) that returns the exact Decimal sum of a
# list of price strings like ["19.99", "5.01", "3.33"].
def total_price(price_strings):
    # TODO: return sum(Decimal(p) for p in price_strings)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — round a Decimal to exactly two places with quantize().
# Write round_to_cents(amount) that returns amount.quantize(
#     Decimal("0.01"), rounding=ROUND_HALF_UP)
def round_to_cents(amount):
    # TODO: return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
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
    result = float_addition_is_inexact()
    if result is None:
        return False
    return result is True


def _ex2():
    result = decimal_from_text("0.1")
    if result is None:
        return False
    return result == Decimal("0.1") and isinstance(result, Decimal)


def _ex3():
    result = total_price(["19.99", "5.01", "3.33", "0.10", "0.10", "0.10"])
    if result is None:
        return False
    return result == Decimal("28.63")


def _ex4():
    result = round_to_cents(Decimal("19.995"))
    if result is None:
        return False
    return result == Decimal("20.00")


results = [
    check("Ex 1: 0.1 + 0.2 != 0.3 with plain floats", _ex1),
    check("Ex 2: Decimal built from a string is exact", _ex2),
    check("Ex 3: summing price strings with Decimal has no drift", _ex3),
    check("Ex 4: quantize() rounds a Decimal to exactly two places", _ex4),
]
print("\nAll green — lesson 70 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
