# Add JSON storage foundation

## Type

ship

## Goal

Create an isolated JSON persistence layer for bookmarks and move the bookmark data model into a shared module without changing the current in-memory service behavior.

## Context

The project currently defines `Bookmark` and an in-memory `BookmarkService` in `src/bookmarks/service.py`. The approved design stores JSON records in `.bookmarks.json` in the process working directory, uses only the Python standard library, treats an absent file as empty, and must not overwrite malformed or invalid stored data.

## Scope

- Add `src/bookmarks/models.py` with the `Bookmark` dataclass (`url: str`, `title: str`, `tags: list[str]`).
- Add `src/bookmarks/storage.py` defining `BookmarkStorage`, constructed with a `pathlib.Path`.
- Implement `load() -> list[Bookmark]` to return `[]` for a missing path and otherwise decode a JSON array of records containing exactly usable string `url`, string `title`, and list-of-string `tags` values.
- Implement `save(bookmarks: list[Bookmark]) -> None` to serialize those records as JSON at the configured path, creating parent directories only when the supplied path has them.
- Define a storage-specific exception or clear `ValueError` behavior for malformed JSON, a non-array root, or invalid records, and ensure `save` is never called as part of a failed `load`.
- Update `src/bookmarks/service.py` to import the shared model while retaining its temporary in-memory constructor and current `add`/unfiltered `list_all` behavior until task 002 changes the service contract.
- Add isolated storage unit tests using `tempfile.TemporaryDirectory` and `unittest`.

## Out Of Scope

- Service initialization from storage, persistence on `add`, and tag filtering.
- CLI parsing, command output, package entry points, README changes, or third-party dependencies.

## Dependencies

None

## Parallel

No. This is the root task and establishes the shared `Bookmark` and `BookmarkStorage` contracts consumed by every later implementation task.

## Predicted Paths and Symbols

- `src/bookmarks/models.py` — `Bookmark`
- `src/bookmarks/storage.py` — `BookmarkStorage`, `load`, `save`, storage error type
- `src/bookmarks/service.py` — import of `Bookmark`
- `tests/test_storage.py` — storage round-trip and invalid-input tests

## Acceptance Criteria

- Saving then loading bookmarks preserves URL, title, tags, and input order.
- A missing storage file loads as an empty list.
- Malformed JSON, a non-array JSON root, and records with wrong field types raise a clear error.
- Failed reads leave the original storage file unchanged.
- `Bookmark` has one canonical definition outside service logic.

## Test Notes

Run `python -m unittest tests.test_storage -v`. Include tests for missing files, round-trip serialization, malformed JSON, non-list roots, and invalid record fields.
