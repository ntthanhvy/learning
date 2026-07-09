package link

import (
	"context"
	"log/slog"
)

type LoggingStore struct {
	Store
	log *slog.Logger
}

func NewLoggingStore(store Store, log *slog.Logger) *LoggingStore {
	return &LoggingStore{
		Store: store,
		log:   log,
	}
}

func (s *LoggingStore) Save(ctx context.Context, l Link) error {
	s.log.Info("Saving link", "code", l.Code, "url", l.URL)
	return s.Store.Save(ctx, l)
}
