// progress-sync: localhost bridge between the static course pages and the
// Neon course_progress table. The pages hold no credentials — they POST here,
// and this process (which reads LEARNING_DB_URL from the environment) inserts.
//
// Run by launchd (com.ntthanhvy.progress-sync) or manually:
//
//	source ~/.config/learning/db.env && go run .
package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

type event struct {
	Course string          `json:"course"`
	Kind   string          `json:"kind"`
	Day    *int            `json:"day"`
	Lesson string          `json:"lesson"`
	Detail json.RawMessage `json:"detail"`
}

var (
	allowedCourse = map[string]bool{"go": true, "rust": true, "backend": true}
	// Browser-originated kinds only; lesson_generated stays with the nightly job.
	allowedKind = map[string]bool{"quiz": true, "kata": true, "review": true, "note": true, "lesson_completed": true}
)

func main() {
	url := os.Getenv("LEARNING_DB_URL")
	if url == "" {
		log.Fatal("LEARNING_DB_URL not set (source ~/.config/learning/db.env)")
	}
	pool, err := pgxpool.New(context.Background(), url)
	if err != nil {
		log.Fatal(err)
	}
	defer pool.Close()

	mux := http.NewServeMux()
	mux.HandleFunc("GET /health", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("ok"))
	})
	mux.HandleFunc("POST /record", func(w http.ResponseWriter, r *http.Request) {
		var e event
		if err := json.NewDecoder(http.MaxBytesReader(w, r.Body, 16<<10)).Decode(&e); err != nil {
			http.Error(w, "bad json", http.StatusBadRequest)
			return
		}
		if !allowedCourse[e.Course] || !allowedKind[e.Kind] {
			http.Error(w, "bad course or kind", http.StatusBadRequest)
			return
		}
		if len(e.Detail) == 0 {
			e.Detail = json.RawMessage("{}")
		}
		ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
		defer cancel()
		_, err := pool.Exec(ctx,
			`INSERT INTO course_progress (course, kind, day, lesson, detail)
			 VALUES ($1, $2, $3, NULLIF($4, ''), $5)`,
			e.Course, e.Kind, e.Day, e.Lesson, e.Detail)
		if err != nil {
			log.Println("insert:", err)
			http.Error(w, "db error", http.StatusBadGateway)
			return
		}
		w.WriteHeader(http.StatusNoContent)
	})

	log.Println("progress-sync listening on 127.0.0.1:8477")
	log.Fatal(http.ListenAndServe("127.0.0.1:8477", cors(mux)))
}

// cors lets the file:// and localhost course pages call us. Loopback-only
// listener, so "any origin" still means "this machine's browser".
func cors(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusNoContent)
			return
		}
		next.ServeHTTP(w, r)
	})
}
