package main

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"time"

	"errors"

	"linkshort/link"

	"github.com/jackc/pgx/v5/pgxpool"
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

	ctx := context.Background()

	var store link.Store
	dsn := os.Getenv("LINKSHORT_DB_URL")
	if dsn != "" {
		// TODO: pg, err := link.NewPostgresStore(ctx, dsn)
		//       if err != nil { panic(err) }
		//       store = link.NewLoggingStore(pg, slog.Default())
		pg, err := link.NewPostgresStore(ctx, dsn)
		if err != nil {
			panic(err)
		}
		store = link.NewLoggingStore(pg, slog.Default())
	} else {
		store = link.NewLoggingStore(link.NewMemStore(), slog.Default())
	}

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

	health := checkAll([]link.Link{
		{Code: "go", URL: "https://go.dev"},
		{Code: "bad", URL: "http://insecure.example"},
		{Code: "rust", URL: "https://www.rust-lang.org"},
	}, time.Second)

	fmt.Println("health:", health)

	// A *pgxpool.Pool, not a Store — ClicksPerLink/RecentClicks/SeedDemoClicks
	// work at the SQL level directly, same database, different door in.
	pool, err := pgxpool.New(ctx, dsn)
	if err != nil {
		panic(err)
	}

	// TODO: link.SeedDemoClicks(ctx, pool, "go", "https://golang.org", 5)
	// then link.ClicksPerLink(ctx, pool) and print each LinkStats — check
	// both errors, panic like the calls above if non-nil.
	link.SeedDemoClicks(ctx, pool, "go", "https://golang.org", 5)
	linkStat, err := link.ClicksPerLink(ctx, pool)
	if err != nil {
		panic(err)
	}
	for _, stat := range linkStat {
		fmt.Printf("Link: %s, Clicks: %d\n", stat.Code, stat.Clicks)
	}
}
