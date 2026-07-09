package link

import "context"

var _ Store = (*MemStore)(nil)

type MemStore struct {
	links map[string]Link
}

func NewMemStore() *MemStore {
	return &MemStore{
		links: make(map[string]Link),
	}
}

func (s *MemStore) Save(ctx context.Context, l Link) error {
	s.links[l.Code] = l
	return nil
}

func (s *MemStore) Get(ctx context.Context, code string) (Link, error) {
	l, ok := s.links[code]
	if !ok {
		return Link{}, ErrNotFound
	}
	return l, nil
}
