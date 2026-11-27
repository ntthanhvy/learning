# Practice 141 — Series.cov() and np.cov(): the unscaled number behind
# corr(), and the matrix-shape trap
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/141_cov.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import numpy as np
import pandas as pd

# Same small inline reps table as Lesson 50's own corr() lesson.
demo = pd.DataFrame({
    "rep":             ["Mai", "Long", "Chi", "Huy", "Trang"],
    "calls_made":      [10, 25, 15, 40, 30],
    "deals_closed":    [2, 6, 3, 9, 7],
})

# ---------------------------------------------------------------------------
# Exercise 1 — Section 1: Series.cov() between two columns equals
# corr() * std(A) * std(B). Build both sides and confirm they match.
def series_cov():
    # Return demo["calls_made"].cov(demo["deals_closed"]).
    #   return demo["calls_made"].cov(demo["deals_closed"])
    ...


def series_corr():
    # Return demo["calls_made"].corr(demo["deals_closed"]).
    #   return demo["calls_made"].corr(demo["deals_closed"])
    ...


ex1_cov = series_cov()
ex1_corr = series_corr()
try:
    std_a = float(demo["calls_made"].std())
    std_b = float(demo["deals_closed"].std())
    ex1_rebuilt = float(ex1_corr) * std_a * std_b
    ex1_matches = bool(abs(float(ex1_cov) - ex1_rebuilt) < 1e-9)
except Exception:
    ex1_matches = False

# ---------------------------------------------------------------------------
# Exercise 2 — Section 3: np.cov() on two raw 1-D arrays returns a 2x2
# matrix, not a single number. The one value matching Series.cov() sits at
# [0, 1] (or equivalently [1, 0]) of that matrix.
a = demo["calls_made"].to_numpy()
b = demo["deals_closed"].to_numpy()


def np_cov_matrix():
    # Return np.cov(a, b) -- the full 2x2 matrix, not one number.
    #   return np.cov(a, b)
    ...


ex2_matrix = np_cov_matrix()
try:
    ex2_shape_is_2x2 = bool(ex2_matrix.shape == (2, 2))
    ex2_offdiag_matches_series_cov = bool(abs(float(ex2_matrix[0, 1]) - float(ex1_cov)) < 1e-9)
    ex2_diag_matches_var = bool(abs(float(ex2_matrix[0, 0]) - float(demo["calls_made"].var())) < 1e-9)
except Exception:
    ex2_shape_is_2x2 = False
    ex2_offdiag_matches_series_cov = False
    ex2_diag_matches_var = False

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
    check("Exercise 1: Series.cov() equals corr() * std(A) * std(B)",
          lambda: ex1_matches is True),
    check("Exercise 2: np.cov(a, b) is a 2x2 matrix whose [0,1] cell matches Series.cov(), [0,0] matches var()",
          lambda: ex2_shape_is_2x2 is True and ex2_offdiag_matches_series_cov is True
          and ex2_diag_matches_var is True),
]

print("\nAll green — lesson 141 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
