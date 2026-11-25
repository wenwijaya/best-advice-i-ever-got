"""Best Advice I Ever Got -- make.fun entry.

Writes one sentence (at most 200 characters) about the best advice I
ever received to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ADVICE = (
    "My first boss told me to write the email, sleep on it, and send it "
    "in the morning — and the unsent drafts in my outbox have saved more "
    "relationships than any apology ever did."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ADVICE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.count(".") == 1, "entry must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
