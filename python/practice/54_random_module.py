# Practice 54 — the random module
# Run:  cd ~/learning/python && uv run python3 practice/54_random_module.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `...` (or the marked TODO body) and re-run until every check
# prints ✓.

import random


# ---------------------------------------------------------------------------
# Exercise 1 — a reproducible sequence.
# Seed the module's random generator with the given seed, then return a list
# of 3 calls to random.randint(1, 100), in order.
def seeded_rolls(seed):
    # TODO: random.seed(seed)
    #       return [random.randint(1, 100) for _ in range(3)]
    ...


# ---------------------------------------------------------------------------
# Exercise 2 — pick exactly one element.
# Return one element from `options`, chosen with random.choice.
def pick_one(options):
    # TODO: return random.choice(options)
    ...


# ---------------------------------------------------------------------------
# Exercise 3 — sample distinct elements.
# Return `k` DISTINCT elements from `pool`, using random.sample (not
# random.choices — sample never repeats an element).
def pick_distinct(pool, k):
    # TODO: return random.sample(pool, k)
    ...


# ---------------------------------------------------------------------------
# Exercise 4 — shuffle a copy, not the original.
# Return a NEW list containing the same elements as `items` but shuffled,
# leaving the original `items` list untouched and in its original order.
def shuffled_copy(items):
    # TODO: copy = items[:]
    #       random.shuffle(copy)
    #       return copy
    ...


# ---------------------------------------------------------------------------
# Exercise 5 — an inclusive-range integer.
# Return a random integer that could be as low as `low` or as high as `high`,
# both ends inclusive. Use random.randint.
def roll(low, high):
    # TODO: return random.randint(low, high)
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


def _check_seeded_rolls():
    random.seed(7)
    expected = [random.randint(1, 100) for _ in range(3)]
    return seeded_rolls(7) == expected


def _check_shuffled_copy_preserves_original():
    original = [1, 2, 3, 4, 5, 6, 7, 8]
    before = list(original)
    result = shuffled_copy(original)
    return (
        original == before
        and result is not original
        and sorted(result) == sorted(original)
    )


results = [
    check("Ex 1: seeded_rolls reproduces the same sequence for the same seed",
          _check_seeded_rolls),
    check("Ex 2: pick_one returns an element that is actually in options",
          lambda: pick_one(["a", "b", "c"]) in ["a", "b", "c"]),
    check("Ex 3: pick_distinct returns k distinct elements from pool",
          lambda: (lambda r: len(r) == 3 and len(set(r)) == 3
                   and all(x in range(20) for x in r))(pick_distinct(list(range(20)), 3))),
    check("Ex 4: shuffled_copy returns a reordered copy, original untouched",
          _check_shuffled_copy_preserves_original),
    check("Ex 5: roll(low, high) stays within the inclusive bounds",
          lambda: all(1 <= roll(1, 6) <= 6 for _ in range(50))),
]
print("\nAll green — lesson 54 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
