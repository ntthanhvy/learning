package main

import (
	"math"
	"net/http"
	"sync"
	"time"
)

type bucket struct {
	mu           sync.Mutex
	tokens       float64
	capacity     float64
	refillPerSec float64
	last         time.Time
}

func (b *bucket) allow() bool {
	b.mu.Lock()
	defer b.mu.Unlock()

	now := time.Now()
	elapsed := now.Sub(b.last).Seconds()
	b.tokens = math.Min(b.capacity, b.tokens+elapsed*b.refillPerSec)
	b.last = now

	if b.tokens < 1 {
		return false
	}
	b.tokens--
	return true
}

func rateLimit(next http.Handler, buckets *sync.Map) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		key := r.Header.Get("X-API-Key")
		b, _ := buckets.LoadOrStore(key, &bucket{tokens: 20, capacity: 20, refillPerSec: 10, last: time.Now()})
		if !b.(*bucket).allow() {
			w.Header().Set("Retry-After", "1")
			w.WriteHeader(http.StatusTooManyRequests)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func main() {}
