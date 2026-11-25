# Practice 119 — review day 23: retrieval across Days 116-118
# Run:  cd ~/learning/python && uv run python3 practice/119_review_retrieval_day_23.py
# Standard library only — no dependencies, no `--with` flag needed.
#
# No new syntax here — every mechanism below was taught in Days 116, 117, and 118.
# Replace each `pass`/TODO body and re-run until every check prints ✓.
# Try each from memory before reopening the old lesson.

import ipaddress
import unicodedata
from urllib.parse import urlencode, parse_qs


# ---------------------------------------------------------------------------
# Exercise 1 (Day 116 — urllib.parse: round-tripping a dict of query
# parameters through urlencode() and back through parse_qs(), confirming
# they're exact inverses of each other)
def round_trip_query(params):
    """Given a dict of plain Python values (str or int), build a query
    string with urlencode(params), then parse that string back with
    parse_qs(). Return (built, parsed_back) where `built` is the query
    string and `parsed_back` is the dict parse_qs() returns."""
    # TODO: built = urlencode(params)
    # TODO: parsed_back = parse_qs(built)
    # TODO: return built, parsed_back
    pass


# ---------------------------------------------------------------------------
# Exercise 2 (Day 117 — unicodedata: normalizing two differently-built but
# identical-looking strings so a set-membership check finds the match that
# the raw, un-normalized strings would miss)
def normalized_membership(needle, haystack):
    """Given a string `needle` and a list of strings `haystack`, return True
    if needle is "the same text" as any string in haystack ONCE both sides
    are normalized to NFC form -- even if needle's raw code points don't
    exactly match any raw entry in haystack."""
    # TODO: target = unicodedata.normalize("NFC", needle)
    # TODO: return any(target == unicodedata.normalize("NFC", s) for s in haystack)
    pass


# ---------------------------------------------------------------------------
# Exercise 3 (Day 118 — ipaddress: separating a list of candidate IP/CIDR
# strings into genuinely valid network objects versus ones that fail to
# parse, using ip_network() with strict=False so a non-start address never
# raises)
def valid_networks(candidates):
    """Given a list of CIDR strings (e.g. "192.168.1.5/24", "not-a-cidr"),
    return a list of the ipaddress network objects built from every string
    that parses successfully via ipaddress.ip_network(c, strict=False),
    in original order, skipping any string that still raises ValueError."""
    # TODO: walk candidates, try ipaddress.ip_network(c, strict=False) in a
    # try/except ValueError, and append the result only on success.
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
    built, parsed_back = round_trip_query({"q": "hello world", "page": 2})
    return built == "q=hello+world&page=2" and parsed_back == {
        "q": ["hello world"], "page": ["2"],
    }


def _ex2():
    s1 = "café"              # precomposed: e-acute is ONE code point
    s2 = "cafe" + "́"   # plain e + a SEPARATE combining acute accent
    return (
        s1 != s2
        and normalized_membership(s2, [s1]) is True
        and normalized_membership("zzz", [s1]) is False
    )


def _ex3():
    nets = valid_networks(["192.168.1.5/24", "not-a-cidr", "10.0.0.0/8"])
    return [str(n) for n in nets] == ["192.168.1.0/24", "10.0.0.0/8"]


if __name__ == "__main__":
    results = [
        check("Ex 1 (Day 116): urlencode()/parse_qs() round-trip a query dict", _ex1),
        check("Ex 2 (Day 117): NFC normalization finds a code-point-different match", _ex2),
        check("Ex 3 (Day 118): ip_network(strict=False) skips invalid, keeps valid", _ex3),
    ]

    print("\nAll green — lesson 119 done. 🎉" if all(results)
          else "\nSome ✗ left — fix and re-run. Stuck? Ask your teacher (tiếng Việt OK).")
