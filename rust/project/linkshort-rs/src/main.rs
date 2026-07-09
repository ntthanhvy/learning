use std::env;

// A short link: a code that redirects to a URL. Same domain as your Go project.
struct Link {
    code: String,
    url: String,
}

impl Link {
    // TODO 3: return "<code> -> <url>" using format!(…) as an EXPRESSION body:
    // no `return`, no trailing `;`. Until then, todo!() keeps the compiler happy.
    fn describe(&self) -> String {
        format!("{} -> {}", self.code, self.url)
    }
}

// TODO 1: define `enum Command` with three variants:
//   Save { code: String, url: String }   — save a new link
//   Get  { code: String }                — look one up
//   Help                                 — no data at all
// (This is the heart of today. Write it, then run `cargo check`.)
enum Command {
    Save { code: String, url: String },
    Get { code: String },
    Help,
}

// GIVEN: turns CLI words into a Command. `match` on a slice: each pattern
// describes a SHAPE of the arguments ([three words], [two words], anything else).
fn parse_command(args: &[String]) -> Command {
    match args {
        [cmd, code, url] if cmd == "save" => Command::Save {
            code: code.clone(), // .clone(): make an owned copy — the why is Day 2
            url: url.clone(),
        },
        [cmd, code] if cmd == "get" => Command::Get { code: code.clone() },
        _ => Command::Help,
    }
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    let cmd = parse_command(&args); // &: lend it, don't give it away — Day 2's topic

    let mut links = vec![
        Link {
            code: String::from("go"),
            url: String::from("https://go.dev"),
        },
        Link {
            code: String::from("rust"),
            url: String::from("https://www.rust-lang.org"),
        },
    ];

    // TODO 2: `match cmd { … }` — step 5 walks you through it.
    match cmd {
        Command::Help => {
            println!("Usage: linkshort-rs save <code> <url> | get <code>");
        }
        Command::Save { code, url } => {
            links.push(Link { code, url });
            println!("Saved link, {} links now:", links.len());
            for l in &links {
                println!(" {}", l.describe());
            }
        }
        Command::Get { code } => {
            let mut found = false;
            for l in &links {
                if l.code == code {
                    println!("Found: {}", l.describe());
                    found = true;
                }
            }

            if !found {
                println!("No link found for code: {}", code);
            }
        }
    }
}

fn status_text(code: u16) -> String {
    match code {
        200 => "ok".to_string(),
        404 => "not found".to_string(),
        500 => "server error".to_string(),
        _ => "unknown".to_string(),
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn empty_args_means_help() {
        let cmd = parse_command(&Vec::<String>::new());
        assert!(matches!(cmd, Command::Help)); // matches!: "does cmd have this shape?"
    }

    #[test]
    fn save_parses_code_and_url() {
        let args = vec![
            "save".to_string(),
            "rs".to_string(),
            "https://www.rust-lang.org".to_string(),
        ];
        assert!(matches!(parse_command(&args), Command::Save { .. }));
    }

    #[test]
    fn status_text_works() {
        assert_eq!(status_text(200), "ok");
        assert_eq!(status_text(404), "not found");
        assert_eq!(status_text(500), "server error");
        assert_eq!(status_text(418), "unknown");
    }
}
