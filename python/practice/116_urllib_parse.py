# Practice 116 — urllib.parse: taking a URL apart and putting one together
# Run:  cd ~/learning/python && uv run python3 practice/116_urllib_parse.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the lesson.

from urllib.parse import urlparse, parse_qs, urlencode, quote, unquote


# ---------------------------------------------------------------------------
# Exercise 1 — split a URL string into its named pieces. Write url_parts(url)
# that uses urlparse() and returns a (scheme, netloc, path) tuple.
def url_parts(url):
    # TODO: parsed = urlparse(url)
    # TODO: return (parsed.scheme, parsed.netloc, parsed.path)
    pass


# ---------------------------------------------------------------------------
# Exercise 2 — read a query string's values back out, including a repeated
# key. Write query_values(query_string, key) that uses parse_qs() to parse
# query_string and returns the list of values for `key` (an empty list if
# the key isn't present at all).
def query_values(query_string, key):
    # TODO: parsed = parse_qs(query_string)
    # TODO: return parsed.get(key, [])
    pass


# ---------------------------------------------------------------------------
# Exercise 3 — build a query string from a dict of plain Python values.
# Write build_query(params) that uses urlencode() to turn `params` into one
# query string.
def build_query(params):
    # TODO: return urlencode(params)
    pass


# ---------------------------------------------------------------------------
# Exercise 4 — round-trip one raw value through percent-encoding. Write
# roundtrip(value) that uses quote() to percent-encode `value`, then
# unquote() on the result, and returns a (encoded, decoded) tuple.
def roundtrip(value):
    # TODO: encoded = quote(value)
    # TODO: decoded = unquote(encoded)
    # TODO: return (encoded, decoded)
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
    return url_parts("https://api.example.com/search?q=hi&page=2") == (
        "https", "api.example.com", "/search",
    )


def _ex2():
    qs = "q=hello+world&page=2&tag=py&tag=web"
    return (
        query_values(qs, "page") == ["2"]
        and query_values(qs, "tag") == ["py", "web"]
        and query_values(qs, "missing") == []
    )


def _ex3():
    built = build_query({"q": "hello world", "page": 2})
    # The built string, re-parsed, must reproduce the original values —
    # confirms urlencode() and parse_qs() are inverses of each other.
    return built == "q=hello+world&page=2" and parse_qs(built) == {
        "q": ["hello world"], "page": ["2"],
    }


def _ex4():
    encoded, decoded = roundtrip("hello world/slash?q")
    return (
        encoded == "hello%20world/slash%3Fq"
        and decoded == "hello world/slash?q"
    )


results = [
    check("Ex 1: url_parts() reads scheme/netloc/path out of a URL", _ex1),
    check("Ex 2: query_values() reads parse_qs()'s list for a key", _ex2),
    check("Ex 3: build_query() builds a query string that parses back the same", _ex3),
    check("Ex 4: roundtrip() encodes then decodes back to the original value", _ex4),
]
print("\nAll green — lesson 116 done. 🎉" if all(results)
      else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
