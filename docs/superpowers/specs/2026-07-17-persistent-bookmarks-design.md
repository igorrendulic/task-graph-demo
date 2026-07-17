# Persistent Bookmark Storage Design

## Scope

Provide persistent bookmark storage, tag filtering, a module CLI, unit tests,
and usage documentation. Use only the Python standard library.

## Architecture

- `src/bookmarks/models.py` owns the `Bookmark` dataclass.
- `src/bookmarks/storage.py` owns JSON encoding, decoding, validation, and
  storage-specific errors. It receives an explicit `pathlib.Path`.
- `src/bookmarks/service.py` owns loading, adding, persistence orchestration,
  and all-tags filtering. It depends on `BookmarkStorage`.
- `src/bookmarks/__main__.py` owns `argparse`, command dispatch, output, and
  converting storage errors into concise non-zero command failures.

The CLI constructs storage at `Path.cwd() / ".bookmarks.json"`, so each
invocation persists data in its current directory.

## Behavior

Storage serializes bookmarks as a JSON array of objects with string `url`,
string `title`, and list-of-string `tags` fields. A missing file loads as an
empty list. Malformed JSON, a non-array root, or invalid records raise a clear
storage error. A failed load never causes the file to be overwritten.

The service loads persisted bookmarks during construction and saves the full
collection after a successful add. `list_all()` preserves insertion order.
When tags are supplied, it returns only bookmarks containing every supplied
tag; repeated CLI `--tag` options are supported.

The module CLI is:

```text
python -m bookmarks add URL TITLE [--tag TAG ...]
python -m bookmarks list [--tag TAG ...]
```

Each displayed bookmark uses one stable human-readable line containing its
title, URL, and tags when present.

## Validation

Separate `unittest` modules cover storage validation/round trips, service
persistence/filtering, and subprocess-level CLI behavior. The README includes
copyable setup, add, list, and one- and multi-tag filtering examples.
