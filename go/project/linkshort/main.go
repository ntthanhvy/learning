package main

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"time"

	"errors"

	"linkshort/link"
)

// resolve looks up a code and wraps any failure with context about THIS call.
// The %w verb keeps the original error inside the new one, findable by errors.Is.
func resolve(ctx context.Context, store link.Store, code string) (link.Link, error) {
	l, err := store.Get(ctx, code)
	if err != nil {
		return link.Link{}, fmt.Errorf("resolve %q: %w", code, err)
	}
	return l, nil
}

func main() {
	store := link.NewLoggingStore(link.NewMemStore(), slog.Default())
	ctx := context.Background()

	if err := store.Save(ctx, link.Link{Code: "go", URL: "https://golang.org", CreatedAt: time.Now()}); err != nil {
		panic(err)
	}

	for _, code := range []string{"go", "python"} {
		l, err := resolve(ctx, store, code)
		switch {
		case errors.Is(err, link.ErrNotFound):
			fmt.Printf("%q not found\n", code)
		case err != nil:
			fmt.Fprintln(os.Stderr, "unexpected:", err)
			os.Exit(1)
		default:
			fmt.Printf("%q -> %q\n", l.Code, l.URL)
		}
	}
}
