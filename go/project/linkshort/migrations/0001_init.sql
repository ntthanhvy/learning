CREATE TABLE links (
    code       text PRIMARY KEY,
    url        text NOT NULL CHECK (url <> ''),
    created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE clicks (
    id         bigint GENERATED ALWAYS AS  IDENTITY PRIMARY KEY,
    link_code  text NOT NULL REFERENCES links(code) ON DELETE CASCADE,
    clicked_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX clicks_link_code_clicked_at_idx
    ON clicks (link_code, clicked_at DESC);