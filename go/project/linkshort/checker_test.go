package main

import (
    "testing"
    "time"

    "linkshort/link"
)

func TestCheckAllChecksEveryLink(t *testing.T) {
    links := []link.Link{
        {Code: "go", URL: "https://go.dev"},
        {Code: "bad", URL: "http://insecure.example"},
        {Code: "rust", URL: "https://www.rust-lang.org"},
    }
    got := checkAll(links, time.Second)
    if len(got) != 3 {
        t.Fatalf("checked %d links, want 3: %v", len(got), got)
    }
    if !got["go"] || got["bad"] || !got["rust"] {
        t.Fatalf("wrong verdicts: %v", got)
    }
}

func TestCheckAllTimesOut(t *testing.T) {
    links := []link.Link{{Code: "a", URL: "https://a.dev"}, {Code: "b", URL: "https://b.dev"}}
    got := checkAll(links, time.Millisecond) // far below checkOne's 50ms
    if len(got) == 2 {
        t.Fatal("expected partial results under a 1ms timeout, got all of them")
    }
}