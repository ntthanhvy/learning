package main

import (
	"linkshort/link"
	"strings"
	"sync"
	"time"
)

type result struct {
	code string
	ok   bool
}

func checkOne(l link.Link) result {
	time.Sleep(50 + time.Millisecond)

	return result{code: l.Code, ok: strings.HasPrefix(l.URL, "https://")}
}

func checkAll(links []link.Link, timeout time.Duration) map[string]bool {
	results := make(chan result)

	// TODO 1: loop over links; for each one wg.Add(1) and launch a goroutine
	//         that defer wg.Done()s and sends checkOne(l) into results.
	//         (Section 1 has this shape almost verbatim.)
	var wg sync.WaitGroup

	for _, l := range links {
		wg.Add(1)

		go func(l link.Link) {
			defer wg.Done()
			results <- checkOne(l)
		}(l)
	}

	// GIVEN — the closer: when every worker is done, close the channel so
	// the receive loop knows nothing else is coming. This runs in its OWN
	// goroutine because wg.Wait() blocks — and we need to start receiving NOW.
	go func() {
		wg.Wait()
		close(results)
	}()

	out := make(map[string]bool, len(links))
	deadline := time.After(timeout)
	for {
		// TODO 2: select over two cases —
		//   receive `r, open := <-results`: if !open return out, else store r
		//   receive from deadline: return out (partial results)
		//   (Section 3 is this select, minus the loop.)

		select {
		case r, open := <-results:
			if !open {
				return out
			}
			out[r.code] = r.ok
		case <-deadline:
			return out
		}

	}
}
