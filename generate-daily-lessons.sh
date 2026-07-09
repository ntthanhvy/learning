#!/bin/zsh
# Daily lesson generation for ~/learning courses. Run by launchd at 06:00
# (com.ntthanhvy.daily-lessons); safe to run manually anytime — idempotent,
# skips courses whose lesson for today already exists.
#
# 2026-07-08 revision: reads/records progress in the Neon DB (course_progress
# table, creds in ~/.config/learning/db.env) and allows the full verification
# toolchain (go test/run, cargo test/run/clippy, node, psql, record-progress).
set -uo pipefail
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:/usr/local/bin:/opt/homebrew/bin:/opt/homebrew/opt/libpq/bin:$PATH"
source "$HOME/.config/learning/db.env"
cd "$HOME/learning"
LOG="$HOME/learning/.daily-gen.log"

run_generation() {
  claude -p "$(cat "$HOME/learning/daily-lessons-prompt.md")" \
    --permission-mode acceptEdits \
    --allowedTools "Read,Write,Edit,Glob,Grep,Bash(date:*),Bash(ls:*),Bash(mkdir:*),Bash(cat:*),Bash(cp:*),Bash(grep:*),Bash(source:*),Bash(go vet:*),Bash(go build:*),Bash(go mod:*),Bash(go test:*),Bash(go run:*),Bash(gofmt:*),Bash(cargo check:*),Bash(cargo test:*),Bash(cargo run:*),Bash(cargo clippy:*),Bash(cargo new:*),Bash(node:*),Bash(psql:*),Bash(bin/record-progress:*),Bash(~/learning/bin/record-progress:*)"
}

# The 2026-07-09 06:00 run died on "API Error: Connection closed" after
# generating nothing, yet exited 0. So: verify the run actually concluded
# (the prompt ends with a per-course summary containing "go:") and retry
# once after a pause if it didn't.
{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') daily lesson generation start ==="
  for attempt in 1 2; do
    OUT="$(run_generation)"
    status=$?
    printf '%s\n' "$OUT"
    if [ $status -eq 0 ] && printf '%s' "$OUT" | grep -q "go:"; then
      break
    fi
    echo "--- attempt $attempt incomplete (exit $status); $( [ $attempt -eq 1 ] && echo 'retrying in 5 min' || echo 'giving up — run me manually' )"
    [ $attempt -eq 1 ] && sleep 300
  done
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') done ==="
} >>"$LOG" 2>&1
