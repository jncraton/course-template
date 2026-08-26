#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


COMMONS_SIZE_RE = re.compile(
    r"(https?://upload\.wikimedia\.org/wikipedia/commons/thumb/"
    r"[^)\s]+/)\d+px(-[^)\s]+)"
)

IMAGE_RE = re.compile(
    r"(!\[[^\]]*\]\()([^)]+)(\)(?:\{[^}]*\})?)"
)


def normalize_url(url):
    """Replace a Wikimedia Commons thumbnail size with 500px.

    >>> normalize_url("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/TI-89.jpg/250px-TI-89.jpg")
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/TI-89.jpg/500px-TI-89.jpg'
    >>> normalize_url("https://example.com/image.jpg")
    'https://example.com/image.jpg'
    """
    return COMMONS_SIZE_RE.sub(r"\g<1>500px\g<2>", url)


def normalize_attributes(attributes):
    """Set an image height attribute to 540px.

    >>> normalize_attributes("{height=250px}")
    '{height=540px}'
    >>> normalize_attributes("{width=500px}")
    '{width=500px height=540px}'
    >>> normalize_attributes("")
    '{height=540px}'
    """
    if not attributes:
        return "{height=540px}"

    if re.search(r"\bheight\s*=", attributes):
        return re.sub(r"\bheight\s*=[0-9]+px", "height=540px", attributes)

    return attributes[:-1].rstrip() + " height=540px}"


def rewrite_image(match):
    prefix, url, suffix = match.groups()
    url = normalize_url(url)

    if suffix.endswith("}"):
        closing_paren = ")"
        attributes = suffix[suffix.index("{"):]
        attributes = normalize_attributes(attributes)
        suffix = closing_paren + attributes
    elif "upload.wikimedia.org/wikipedia/commons/thumb/" in url:
        suffix = "){height=540px}"

    return prefix + url + suffix


def rewrite_markdown(text):
    """Rewrite Wikimedia Commons image URLs and image heights.

    >>> rewrite_markdown(
    ...     '![TI-89](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/TI-89.jpg/250px-TI-89.jpg){height=200px}'
    ... )
    '![TI-89](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/TI-89.jpg/500px-TI-89.jpg){height=540px}'
    """
    return IMAGE_RE.sub(rewrite_image, text)


def rewrite_file(path):
    """Rewrite one Markdown file in place."""
    original = path.read_text(encoding="utf-8")
    rewritten = rewrite_markdown(original)

    if rewritten != original:
        path.write_text(rewritten, encoding="utf-8")

    return rewritten != original


def main():
    parser = argparse.ArgumentParser(
        description="Normalize Wikimedia Commons images in Markdown files."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    for path in args.files:
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue

        if not path.is_file():
            parser.error(f"not a file: {path}")

        changed = rewrite_file(path)
        print(f"{path}: {'rewritten' if changed else 'unchanged'}")


if __name__ == "__main__":
    main()
