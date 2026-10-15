# Mission now includes .NET (C# / ASP.NET Core) alongside Go + PostgreSQL

On 2026-10-15 the user asked "websocket vs signalR, what is the difference and why signalR is used more now" (Lesson 102). When asked whether their work uses ASP.NET Core / SignalR, they asked to "update the plan to .NET can be include". MISSION.md was confirmed and updated: examples may be grounded in Go + PostgreSQL **or** .NET (C# / ASP.NET Core), and ASP.NET Core building blocks (SignalR, middleware, EF Core) are now allowed when they are how a concept is actually done in .NET. Deep framework tutorials remain out of scope.

**Implications:** (1) Many earlier lessons (1–101) used only Go. Where a concept's .NET shape differs meaningfully (e.g. DI container, middleware pipeline, EF Core change tracking and N+1, `async`/`await` vs goroutines, background jobs via `IHostedService`), a short "how this looks in .NET" lesson is a high-value next step, because it ties existing concepts to the code the user reviews at work. (2) Lesson 102 corrected a premise ("SignalR is used more than WebSockets"). SignalR is a library *over* WebSocket, preferred within .NET. Watch for similar "X vs Y" questions where X is a library and Y is a protocol.

**Not yet evidence of learning:** no quiz outcome for Lesson 102 has been recorded yet.
