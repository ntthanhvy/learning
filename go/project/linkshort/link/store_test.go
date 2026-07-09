package link

import (
	"context"
	"errors"
	"log/slog"
	"testing"
)

type fakeStore struct {
	saved []Link
}

func (f *fakeStore) Save(ctx context.Context, l Link) error {
	f.saved = append(f.saved, l)
	return nil
}

func (f *fakeStore) Get(ctx context.Context, code string) (Link, error) {
	return Link{}, ErrNotFound
}

func TestLoggingStoreDelegates(t *testing.T) {
	fake := &fakeStore{}
	s := NewLoggingStore(fake, slog.Default())

	if err := s.Save(context.Background(), Link{Code: "x", URL: "https://go.dev"}); err != nil {
		t.Fatal(err)
	}
	if len(fake.saved) != 1 || fake.saved[0].Code != "x" {
		t.Fatalf("save was not delegated to the inner store: %+v", fake.saved)
	}
}

// TODO A — TestGetMissingReturnsErrNotFound:
//
//	NewMemStore, Get a code you never saved, assert errors.Is(err, ErrNotFound).
//	If it fails with "want ErrNotFound, got <nil>" — that's yesterday's bug talking.
func TestGetMissingReturnsErrNotFound(t *testing.T) {
	s := NewMemStore()
	_, err := s.Get(context.Background(), "missing")
	if !errors.Is(err, ErrNotFound) {
		t.Fatalf("want ErrNotFound, got %v", err)
	}
}

// TODO B — TestSaveThenGet:
//   Save a Link, Get it back, assert err is nil and got == want.
//   (Link is comparable — plain == works on the whole struct.)
func TestSaveThenGet(t *testing.T) {
	s := NewMemStore()
	want := Link{Code: "x", URL: "https://go.dev"}
	if err := s.Save(context.Background(), want); err != nil {
		t.Fatal(err)
	}
	got, err := s.Get(context.Background(), "x")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if got != want {
		t.Fatalf("got %+v, want %+v", got, want)
	}
}
