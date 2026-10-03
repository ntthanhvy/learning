# Practice 86 — pd.read_sql(): loading query results straight into a DataFrame
# Run:  cd ~/learning/data && uv run --with pandas python3 practice/86_read_sql.py
# Replace each `...` and re-run until every check prints ✓. No `for` loops allowed.
import sqlite3
import pandas as pd

# ---------------------------------------------------------------------------
# Shared fixture: an in-memory SQLite DB (stdlib sqlite3 -- no SQLAlchemy
# install needed, since sqlite3 connections work with pd.read_sql() directly,
# Section 3). An `orders` table with a nullable `quantity` INTEGER column,
# one real NULL row.
_conn = sqlite3.connect(":memory:")
_conn.execute("CREATE TABLE orders (order_id INTEGER, customer TEXT, quantity INTEGER)")
_conn.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    [(1, "An", 3), (2, "Binh", 2), (3, "Chi", None), (4, "An", 1)],
)
_conn.commit()

# ---------------------------------------------------------------------------
# Exercise 1 — a plain read_sql_query() SELECT (Section 1-2). Fill in the
# SQL string to select every column from `orders`.
# ex1_sql = "SELECT * FROM orders"
ex1_sql = ...
try:
    ex1_df = pd.read_sql_query(ex1_sql, _conn)
    ex1_row_count = len(ex1_df)
    ex1_columns = sorted(ex1_df.columns.tolist())
except Exception:
    ex1_row_count = None
    ex1_columns = None

# ---------------------------------------------------------------------------
# Exercise 2 — the Section 5 trap: a nullable INTEGER column with a real
# NULL row comes back as float64, not a whole-number dtype. Fill in the
# column name to check.
# ex2_col_name = "quantity"
ex2_col_name = ...
try:
    ex2_df = pd.read_sql_query("SELECT * FROM orders", _conn)
    ex2_dtype_str = str(ex2_df[ex2_col_name].dtype)
    ex2_is_float = ex2_dtype_str == "float64"
except Exception:
    ex2_dtype_str = None
    ex2_is_float = None

# ---------------------------------------------------------------------------
# Exercise 3 — the fix: dtype_backend="numpy_nullable" gives a real
# nullable Int64 with pd.NA, not a silent float upcast (Section 5). Fill
# in the dtype_backend value to pass.
# ex3_dtype_backend = "numpy_nullable"
ex3_dtype_backend = ...
try:
    ex3_df = pd.read_sql_query(
        "SELECT * FROM orders", _conn, dtype_backend=ex3_dtype_backend
    )
    ex3_dtype_str = str(ex3_df["quantity"].dtype)
    ex3_null_row = ex3_df.loc[ex3_df["order_id"] == 3, "quantity"].iloc[0]
    ex3_is_na = pd.isna(ex3_null_row)
except Exception:
    ex3_dtype_str = None
    ex3_is_na = None

# ---------------------------------------------------------------------------
# Exercise 4 — params=: binding a filter value safely instead of
# f-string-ing it into the SQL text (Section 4). Fill in the params dict
# binding ":min_qty" to 2.
# ex4_params = {"min_qty": 2}
ex4_params = ...
try:
    ex4_df = pd.read_sql_query(
        "SELECT * FROM orders WHERE quantity >= :min_qty", _conn, params=ex4_params
    )
    ex4_row_count = len(ex4_df)
except Exception:
    ex4_row_count = None

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
    check("Exercise 1: read_sql_query() returns all 4 rows and 3 columns",
          lambda: ex1_row_count == 4 and ex1_columns == ["customer", "order_id", "quantity"]),
    check("Exercise 2: nullable INTEGER column with a NULL row comes back float64",
          lambda: ex2_is_float is True),
    check("Exercise 3: dtype_backend='numpy_nullable' gives Int64 with real pd.NA",
          lambda: ex3_dtype_str == "Int64" and ex3_is_na is True),
    check("Exercise 4: params= safely filters -- 2 rows have quantity >= 2",
          lambda: ex4_row_count == 2),
]

print("\nAll green — lesson 86 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
