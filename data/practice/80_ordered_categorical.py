# Practice 80 — ordered categoricals: making "small < medium < large" sort correctly
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/80_ordered_categorical.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import pandas as pd

raw = pd.read_csv("practice/data/orders_raw.csv")

# Same cleaned rows as Lessons 6-25:
# An 120.0/01-05, An 42.0/01-10, Binh 35.5/01-06, Binh 180.0/01-09
clean = raw.dropna(subset=["order_date"]).copy()
clean = clean[pd.to_numeric(clean["amount"], errors="coerce").notna()]
clean["amount"] = clean["amount"].astype(float)
clean = clean.sort_values(["customer", "order_date"]).reset_index(drop=True)

# Bucket into size tiers by hand (small < 50, medium < 150, else large) —
# same three labels pd.cut() will be asked to reproduce in Exercise 4.
clean["size"] = pd.cut(
    clean["amount"], bins=[0, 50, 150, 1000], labels=["small", "medium", "large"]
).astype(str)

# ---------------------------------------------------------------------------
# Exercise 1 — build an ORDERED CategoricalDtype ranking small < medium < large
# (in that order), convert clean["size"] to it, and confirm sort_values()
# follows that business order instead of alphabetical order.
# order = pd.CategoricalDtype(categories=["small", "medium", "large"], ordered=True)
try:
    order = pd.CategoricalDtype(categories=[...], ordered=...)
    clean["size_ordered"] = clean["size"].astype(order)
    ex1_is_ordered = clean["size_ordered"].cat.ordered
    ex1_sorted = clean.sort_values("size_ordered")["size"].tolist()
except Exception:
    clean["size_ordered"] = clean["size"].astype("category")
    ex1_is_ordered, ex1_sorted = None, None

# ---------------------------------------------------------------------------
# Exercise 2 — comparisons: an ORDERED category supports >, min(), max(); a
# plain UNORDERED category (Lesson 25's default) raises TypeError on >. Fill
# in the plain unordered conversion, then confirm the contrast directly.
# unordered = clean["size"].astype("category")
try:
    unordered = clean["size"].astype(...)
    ex2_ordered_gt_small = (clean["size_ordered"] > "small").tolist()
    ex2_min = clean["size_ordered"].min()
    ex2_max = clean["size_ordered"].max()
    try:
        unordered > "small"
        ex2_unordered_raised = False
    except TypeError:
        ex2_unordered_raised = True
except Exception:
    ex2_ordered_gt_small = ex2_min = ex2_max = ex2_unordered_raised = None

# ---------------------------------------------------------------------------
# Exercise 3 — comparing an ordered category to a value OUTSIDE its fixed
# category list raises TypeError too (unlike Lesson 25's silent-NaN astype()
# gotcha). Fill in a real string value that is NOT one of small/medium/large
# to trigger it (must be an actual str, not a placeholder -- checks the type
# and membership directly, to avoid a freebie pass).
# out_of_range_value = "huge"
try:
    out_of_range_value = ...
    clean["size_ordered"] > out_of_range_value
    ex3_raised = False
except TypeError:
    ex3_raised = True
except Exception:
    ex3_raised = False

# ---------------------------------------------------------------------------
# Exercise 4 — pd.cut()'s own bucketed output is already an ordered
# categorical. Fill in the attribute name (on a Series with category dtype,
# reached via the .cat accessor) that reports whether it's ordered — the same
# attribute checked in Exercise 1 (not just any placeholder -- checks the
# literal attribute name, to avoid a freebie pass).
# ex4_cat_attr = "ordered"
try:
    ex4_cat_attr = ...
    cut_result = pd.cut(
        clean["amount"], bins=[0, 50, 150, 1000], labels=["small", "medium", "large"]
    )
    ex4_cut_is_ordered = getattr(cut_result.cat, ex4_cat_attr)
    ex4_matches_hand_built = bool((cut_result.astype(str) == clean["size_ordered"].astype(str)).all())
except Exception:
    ex4_cut_is_ordered = ex4_matches_hand_built = None

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
    check("Exercise 1: ordered categorical sorts small < medium < large, not alphabetically",
          lambda: ex1_is_ordered is True
          and ex1_sorted == ["small", "small", "medium", "large"]),
    check("Exercise 2: ordered supports >/min/max; plain unordered raises TypeError on >",
          lambda: ex2_ordered_gt_small == [True, False, False, True]
          and ex2_min == "small" and ex2_max == "large"
          and ex2_unordered_raised is True),
    check("Exercise 3: comparing to a category outside the fixed list raises TypeError",
          lambda: isinstance(out_of_range_value, str)
          and out_of_range_value not in ["small", "medium", "large"]
          and ex3_raised is True),
    check("Exercise 4: pd.cut()'s bucketed output is already an ordered categorical",
          lambda: ex4_cat_attr == "ordered" and ex4_cut_is_ordered is True
          and ex4_matches_hand_built is True),
]

print("\nAll green — lesson 80 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
