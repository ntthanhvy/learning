# Rust Intensive — one week + daily practice

A self-paced Rust course (2026-07-08 → 2026-07-14, then open-ended daily practice).
Open `index.html` in a browser. Lessons unlock on their calendar day; the glossary and
daily practice page are always available.

## Putting the quiz library online (optional)

Everything here is static HTML/JS, so GitHub Pages hosts it for free. From this
directory, once:

```sh
git init && git add -A && git commit -m "Rust course workspace"
gh repo create rust-intensive --public --source=. --push
gh api repos/{owner}/rust-intensive/pages -X POST \
  -f 'source[branch]=main' -f 'source[path]=/'
```

The course (including `daily.html` and the quiz bank) is then available at
`https://<your-username>.github.io/rust-intensive/` from any device.

Notes:
- Pages on the free plan requires a **public** repo. If you'd rather keep it private,
  alternatives: Cloudflare Pages or Netlify (both free for private repos).
- Quiz/kata **progress** is saved in each browser's localStorage — the site is shared,
  the progress is per-device. Fine for one learner; mention it to your teacher if you
  want cross-device progress someday.
- After each new lesson, `git add -A && git commit -m "day N" && git push` refreshes
  the site (the quiz bank grows with every lesson).
