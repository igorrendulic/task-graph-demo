# Persist bookmarks and filter by tags

## Type

ship

## Goal

Make `BookmarkService` load and save through `BookmarkStorage` and support all-tags filtering.

## Context

Task 001 provides `Bookmark` and `BookmarkStorage`. The approved behavior keeps `.bookmarks.json` location decisions in the CLI, while the service receives a storage dependency. Repeated requested tags match a bookmark only when that bookmark includes every requested tag; a no-tag request returns every bookmark in insertion order.

## Scope

- Change `BookmarkService` construction to accept a `BookmarkStorage`.
- Load persisted bookmarks when the service is initialized.
- Persist the full current collection after each successful `add` call, then return the added bookmark.
- Extend `list_all` with an optional tag list parameter and implement all-tags matching without changing stored order.
- Propagate storage read/write failures to the caller; do not silently reset data.
- Add service tests using a real temporary `BookmarkStorage` rather than mocks where persistence behavior is under test.

## Out Of Scope

- JSON encoding/validation internals owned by `BookmarkStorage`.
- Argument parsing, output formatting, module entry points, or README examples.

## Dependencies

- 001-add-json-storage.md

## Parallel

No. It depends on the shared `Bookmark` and `BookmarkStorage` contracts from task 001 and modifies the shared `src/bookmarks/service.py` surface later consumed by the CLI.

## Predicted Paths and Symbols

- `src/bookmarks/service.py` — `BookmarkService.__init__`, `BookmarkService.add`, `BookmarkService.list_all`
- `tests/test_service.py` — persistence and tag-filter tests
- `src/bookmarks/models.py` — imported `Bookmark` contract
- `src/bookmarks/storage.py` — imported `BookmarkStorage` contract

## Acceptance Criteria

- A bookmark added through one service instance is available after constructing a new service with the same storage path.
- `list_all()` returns every stored bookmark in insertion order.
- `list_all(tags=["work"])` returns only bookmarks containing `work`.
- `list_all(tags=["work", "python"])` returns only bookmarks containing both tags.
- Storage failures remain visible to the caller and do not turn into empty collections.

## Test Notes

Run `python -m unittest tests.test_service -v`. Cover restart persistence, unfiltered listing, a single tag, multiple all-tags matching, unmatched tags, and empty collections.
