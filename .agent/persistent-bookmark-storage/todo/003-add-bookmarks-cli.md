# Add the bookmarks module CLI

## Type

ship

## Goal

Expose bookmark add and list operations through `python -m bookmarks` with repeatable `--tag` options.

## Context

Task 002 provides a persistence-backed `BookmarkService`. The CLI must use `.bookmarks.json` in the current working directory, parse commands with the standard library, save immediately on add, filter with all repeated list tags, and return non-zero errors rather than replacing unreadable data.

## Scope

- Add `src/bookmarks/__init__.py` and `src/bookmarks/__main__.py` so `python -m bookmarks` is the supported invocation.
- Use `argparse` with `add URL TITLE [--tag TAG ...]` and `list [--tag TAG ...]` subcommands.
- Create `BookmarkStorage(Path.cwd() / ".bookmarks.json")` and pass it to `BookmarkService` for every command.
- Render add confirmation and list results in one stable, human-readable line per bookmark, including title, URL, and tags where present.
- Convert storage errors to concise stderr messages and non-zero process status; preserve normal argparse usage errors.
- Add CLI unit tests that execute the module command in temporary working directories using `subprocess`.

## Out Of Scope

- Alternate storage paths, installed console-script packaging, interactive editing/deleting, or output formats such as JSON/CSV.
- Changes to storage decoding or service filtering semantics.

## Dependencies

- 002-persist-and-filter-service.md

## Parallel

No. It depends on the shared `BookmarkService` constructor and `list_all(tags=...)` contract from task 002; its test suite also validates the end-to-end storage behavior provided by earlier tasks.

## Predicted Paths and Symbols

- `src/bookmarks/__init__.py` — package marker/public imports if useful
- `src/bookmarks/__main__.py` — parser builder, command dispatcher, `main`
- `tests/test_cli.py` — subprocess add/list/error cases
- `src/bookmarks/service.py` — consumed `BookmarkService` contract
- `src/bookmarks/storage.py` — consumed `BookmarkStorage` contract

## Acceptance Criteria

- `python -m bookmarks add URL TITLE --tag work --tag python` creates/updates `.bookmarks.json` in the invocation directory.
- `python -m bookmarks list` shows all saved bookmarks.
- `python -m bookmarks list --tag work --tag python` shows only bookmarks having both tags.
- Invalid command syntax uses argparse’s non-zero behavior.
- Unreadable or malformed JSON causes a concise non-zero CLI error and leaves the file intact.

## Test Notes

Run `python -m unittest tests.test_cli -v`. Set `PYTHONPATH` to the repository `src` directory for subprocesses. Cover add persistence, all-list output, repeated-tag filtering, missing results, malformed-file error, and argument errors.
