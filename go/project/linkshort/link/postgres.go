package link

import (
	"context"
	"errors"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

var _ Store = (*PostgresStore)(nil)

type PostgresStore struct {
	pool *pgxpool.Pool
}

func NewPostgresStore(ctx context.Context, connString string) (*PostgresStore, error) {
	pool, err := pgxpool.New(ctx, connString)
	if err != nil {
		return nil, err
	}
	return &PostgresStore{pool: pool}, nil
}

func (s *PostgresStore) Save(ctx context.Context, l Link) error {
	_, err := s.pool.Exec(ctx,
		`INSERT INTO links (code, url) VALUES ($1, $2)
         ON CONFLICT (code) DO UPDATE SET url = EXCLUDED.url`,
		l.Code, l.URL,
	)
	return err
}

func (s *PostgresStore) Get(ctx context.Context, code string) (Link, error) {
	var l Link
	err := s.pool.QueryRow(ctx,
		`SELECT code, url, created_at FROM links WHERE code = $1`, code,
	).Scan(&l.Code, &l.URL, &l.CreatedAt)
	if errors.Is(err, pgx.ErrNoRows) {
		return Link{}, ErrNotFound
	}
	if err != nil {
		return Link{}, err
	}
	return l, nil
}
