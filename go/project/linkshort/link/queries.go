package link

import (
	"context"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

type LinkStats struct {
	Code   string
	Clicks int64
}

func ClicksPerLink(ctx context.Context, pool *pgxpool.Pool) ([]LinkStats, error) {
	rows, err := pool.Query(ctx, `
        SELECT link_code AS code, count(*) AS clicks
        FROM clicks
        GROUP BY link_code
        ORDER BY clicks DESC`)
	if err != nil {
		return nil, err
	}
	return pgx.CollectRows(rows, pgx.RowToStructByName[LinkStats])
}

type Click struct {
	ClickedAt time.Time
}

// RecentClicks returns the next page of clicks for code, newest first.
// before is the keyset cursor: time.Now() for page one, then the ClickedAt
// of the last row from the previous page for page two, and so on.
func RecentClicks(ctx context.Context, pool *pgxpool.Pool, code string, before time.Time, limit int) ([]Click, error) {
	// TODO: pool.Query(ctx, `
	//     SELECT clicked_at
	//     FROM clicks
	//     WHERE link_code = $1 AND clicked_at < $2
	//     ORDER BY clicked_at DESC
	//     LIMIT $3`, code, before, limit)
	// then pgx.CollectRows(rows, pgx.RowToStructByName[Click]) — same shape
	// as ClicksPerLink above, different T.

	rows, err := pool.Query(ctx, `
			SELECT clicked_at
			FROM clicks
			WHERE link_code = $1 AND clicked_at < $2
			ORDER BY clicked_at DESC
			LIMIT $3`, code, before, limit)

	if err != nil {
		return nil, err
	}

	return pgx.CollectRows(rows, pgx.RowToStructByName[Click])
}

func SeedDemoClicks(ctx context.Context, pool *pgxpool.Pool, code, url string, n int) error {
	tx, err := pool.Begin(ctx)
	if err != nil {
		return err
	}
	defer tx.Rollback(ctx) // no-op once Commit succeeds

	// TODO: tx.Exec(ctx,
	//     `INSERT INTO links (code, url) VALUES ($1, $2) ON CONFLICT (code) DO NOTHING`,
	//     code, url,
	// ) — check the error, return it if non-nil.
	_, err = tx.Exec(ctx,
		`INSERT INTO links (code, url) VALUES ($1, $2) ON CONFLICT (code) DO NOTHING`,
		code, url,
	)

	if err != nil {
		return err
	}

	for i := 0; i < n; i++ {
		// TODO: tx.Exec(ctx, `INSERT INTO clicks (link_code) VALUES ($1)`, code)
		// — check the error, return it if non-nil.
		_, err = tx.Exec(ctx, `INSERT INTO clicks (link_code) VALUES ($1)`, code)
		if err != nil {
			return err
		}
	}

	return tx.Commit(ctx)
}
