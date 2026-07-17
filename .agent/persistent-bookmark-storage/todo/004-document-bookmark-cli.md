# Document bookmark CLI usage

## Type

ship

## Goal

Provide concise README instructions that exactly match the completed module CLI and persistence behavior.

## Context

The CLI from task 003 is invoked with `python -m bookmarks` and uses a `.bookmarks.json` file in the current working directory. Users need runnable examples for adding tags, listing all bookmarks, and filtering by a single or multiple tags. Multiple list tags require all-tags matching.

## Scope

- Add `README.md` if it does not exist.
- Explain the `src` layout invocation/setup required to run `python -m bookmarks` from a checkout.
- Document the current-directory `.bookmarks.json` persistence location.
- Include copyable examples for `add`, unfiltered `list`, one `--tag`, and repeated `--tag` all-tags filtering.
- State that tags are repeatable and all supplied list tags must be present.
- Verify every documented command against the implemented CLI in a temporary directory.

## Out Of Scope

- New CLI features, packaging/publishing instructions, storage migration guides, or unrelated project documentation.

## Dependencies

- 003-add-bookmarks-cli.md

## Parallel

No. It depends on the shared public CLI contract and output behavior implemented in task 003, so the examples can be executed and verified verbatim.

## Predicted Paths and Symbols

- `README.md` — CLI setup and usage examples
- `src/bookmarks/__main__.py` — documented `python -m bookmarks` command contract
- `tests/test_cli.py` — reference for verified CLI behavior

## Acceptance Criteria

- README contains working setup and invocation instructions for the repository layout.
- README examples cover add, list, one-tag filtering, and multi-tag all-tags filtering.
- README correctly identifies `.bookmarks.json` as local persistent storage in the current directory.
- Every command copied from the README succeeds with the final implementation under its documented setup.

## Test Notes

Run the README commands manually in a clean temporary directory after setting `PYTHONPATH` to `src`, then run `python -m unittest -v` for the full test suite.
