# Backend Foundations Resources

## Knowledge

- [Repo: "What happens when…" — alex/what-happens-when](https://github.com/alex/what-happens-when)
  Community-maintained deep trace of a request from keystroke to response. Use for: the request lifecycle, what sits between browser and handler.
- [Docs: MDN HTTP Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP)
  Canonical reference for methods, status codes, headers, caching, CORS. Use for: any HTTP semantics question — this is the arbiter.
- [Docs: PostgreSQL Manual — Data Definition](https://www.postgresql.org/docs/current/ddl.html)
  The primary source for tables, constraints, defaults, schemas. Use for: schema design details; always beats blog posts.
- [Book/Site: _Use The Index, Luke_ — Markus Winand](https://use-the-index-luke.com)
  The standard free text on SQL indexing and query performance. Use for: index selection, why a query is slow, pagination done right.
- [Book: _Designing Data-Intensive Applications_ — Martin Kleppmann](https://dataintensive.net)
  The backend book. Use for: data models (ch. 2), storage engines (ch. 3), transactions (ch. 7). Read chapters as topics come up, not cover-to-cover.
- [Book/Site: _The Copenhagen Book_](https://thecopenhagenbook.com)
  Free, focused guide to auth implementation: sessions, tokens, OAuth, CSRF. Use for: the auth & security track.
- [Site: OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org)
  High-trust, maintained security checklists. Use for: input validation, SQL injection, session management, secrets.
- [Site: The Twelve-Factor App](https://12factor.net)
  Classic operational manifesto for services. Use for: config, logs, statelessness, deployment vocabulary.
- [Talk: "Concurrency is not parallelism" — Rob Pike (Waza 2012)](https://go.dev/blog/waza-talk)
  The canonical treatment of the concurrency/parallelism distinction, by one of Go's designers ([slides](https://go.dev/talks/2012/waza.slide) read in ~10 min). Use for: the concurrency vocabulary — this is the arbiter for what those two words mean. Standing reference as of Lesson 25.
- [Docs: Effective Go — Goroutines](https://go.dev/doc/effective_go#goroutines)
  Primary source for what a goroutine is and why Go refused the words "thread" and "coroutine". Use for: the thread vs coroutine mechanism question.

- [Docs: Microsoft Learn — ASP.NET Core SignalR (overview + production hosting and scaling)](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction)
  Vendor primary source for SignalR: transports and fallback order, hubs, reconnect, sticky-session requirement, Redis backplane vs Azure SignalR Service ([scale page](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale)). Use for: any real-time/SignalR question (Lesson 102).
- [Docs: Microsoft Learn — EF Core Loading Related Data: Eager Loading](https://learn.microsoft.com/en-us/ef/core/querying/related-data/eager) and [Tracking vs. No-Tracking Queries](https://learn.microsoft.com/en-us/ef/core/querying/tracking)
  Vendor primary source for EF Core's `Include()` eager-loading method and the `AsNoTracking()` change-tracking opt-out. Use for: EF Core's own N+1/lazy-loading flavor and change-tracking overhead questions (Lesson 106).
- [Docs: Microsoft Learn — Asynchronous programming with async and await](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/) and [.NET Blog — ConfigureAwait FAQ](https://devblogs.microsoft.com/dotnet/configureawait-faq/)
  Vendor primary source for C#'s `Task<T>`/`async`/`await` model and exactly when sync-over-async deadlocks via a captured synchronization context. Use for: C# concurrency-mechanism questions, the `.Result`/`.Wait()` deadlock trap (Lesson 107).
- [Docs: pkg.go.dev — golang.org/x/sync/errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup)
  Primary source for Go's `errgroup.Group`, `WithContext`, `Go()`, and `Wait()`'s first-error-only return behavior. Use for: fan-out/fan-in concurrency questions, structured concurrency in Go (Lesson 108).
- [Docs: Microsoft Learn — Task.WhenAll](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall) and [Cancellation in Managed Threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)
  Vendor primary source for exactly when `Task.WhenAll`'s returned Task completes (only once every supplied task has completed, aggregating all faulted tasks' exceptions) and for `CancellationTokenSource`/`CancellationToken`'s source-vs-token split. Use for: C# structured-concurrency fan-out and the fail-fast-cancellation gap versus Go's errgroup (Lesson 108).
- [Docs: pkg.go.dev — golang.org/x/sync/errgroup (SetLimit section)](https://pkg.go.dev/golang.org/x/sync/errgroup) and [Docs: Microsoft Learn — SemaphoreSlim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
  Vendor primary source for `errgroup.Group.SetLimit`'s blocking-at-the-cap behavior and its "must not be modified while active" constraint, and for `SemaphoreSlim`'s initial/max count constructor, `WaitAsync()`'s non-blocking suspension, and `Release()`. Use for: bounding fan-out width — how many concurrent goroutines/Tasks a fan-out loop is allowed to run at once (Lesson 109).
- [Docs: Microsoft Learn — Task.WhenAny](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany) and [Docs: pkg.go.dev — context package](https://pkg.go.dev/context)
  Vendor primary source for `Task.WhenAny`'s documented tip that losing tasks "will continue running until completion" unless cancelled by hand, and the primary source for `context.WithCancel`'s derived-context behavior behind Go's `select`-based first-result-wins pattern. Use for: "first result wins" races and why the loser doesn't stop on its own (Lesson 110).
- [Docs: pkg.go.dev — context.WithTimeout](https://pkg.go.dev/context#WithTimeout) and [Docs: Microsoft Learn — CancellationTokenSource constructors](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtokensource.-ctor)
  Vendor primary source for `context.WithTimeout`'s exact definition as `WithDeadline(parent, time.Now().Add(timeout))`, and for the `CancellationTokenSource(TimeSpan)` overload's self-cancelling countdown plus `CancelAfter()`'s delay-reset behavior. Use for: attaching a deadline to a single call, as distinct from racing or bounding several (Lesson 111).
- [Docs: Microsoft Learn — CancellationTokenSource.CreateLinkedTokenSource](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtokensource.createlinkedtokensource)
  Vendor primary source confirming the method "creates a CancellationTokenSource that will be in the canceled state when any of the source tokens are in the canceled state." Use for: combining an outer caller deadline with a per-attempt timeout in a C# retry loop (Lesson 112). Lesson 32's own AWS backoff-and-jitter source still covers the retry strategy itself in full and is cited inline there rather than duplicated here, per that lesson's own precedent for single-mechanism citations.

## Wisdom (Communities)

- [Database Administrators Stack Exchange](https://dba.stackexchange.com)
  High-signal Q&A for schema and query design; strong PostgreSQL presence. Use for: schema-design critique with real reviewers.
- [r/ExperiencedDevs](https://reddit.com/r/ExperiencedDevs)
  Moderated, senior-leaning. Use for: "how do teams actually do X" questions — migrations, review culture, backend ownership.
- Work code review — the user's own backend PRs at work are the primary wisdom loop: apply each concept by reviewing or writing one real backend change.

## Gaps

- No vetted resource yet for API design specifically (REST semantics beyond MDN — resource modeling, versioning, error contracts). Candidates to evaluate when that track starts: Microsoft REST API Guidelines, Stripe's API as an exemplar.
