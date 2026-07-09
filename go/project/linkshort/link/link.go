package link

import (
	"context"
	"errors"
	"time"
)

type Link struct {
	Code, URL string
	CreatedAt time.Time
}

var ErrNotFound = errors.New("link: not found")

type Store interface {
	Save(ctx context.Context, l Link) error
	Get(ctx context.Context, code string) (Link, error)
}
