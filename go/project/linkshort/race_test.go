package main

import (
	"sync"
	"testing"
)

func TestCounterMutex(t *testing.T) {
	var (
		mu    sync.Mutex
		count int
		wg    sync.WaitGroup
	)

	const n = 1000
	wg.Add(n)
	for i := 0; i < n; i++ {
		go func() {
			mu.Lock()
			count++
			mu.Unlock()
			wg.Done()
		}()
	}
	wg.Wait()

	if count != n {
		t.Fatalf("expected count %d, got %d", n, count)
	}
}
