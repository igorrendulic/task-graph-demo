# Task Graph Demo

Task Graph turns an approved implementation plan into focused task briefs, a
kanban board, and a dependency-safe execution DAG. This repository is a small
demo of that workflow.

## Quick start

Task Graph is used from Codex. Start with an approved implementation plan,
then send these prompts to Codex in order.

### 1. Generate the task plan

```
Invoke `$task-graph tasks` to turn this approved implementation plan into Task Graph artifacts.
```

This writes plan-specific files under `.agent/<plan-slug>/`:

```text
.agent/<plan-slug>/
├── todo/          # focused task briefs waiting to run
├── in-progress/   # task briefs currently being worked
├── done/          # completed task briefs
├── kanban.md      # human-readable board
└── dag.json       # canonical task dependencies and schedule
```

Generating these artifacts plans the work only; it does not start execution.

### 2. Start implementation

Commit any intended changes and ensure the checkout is clean. Then send:

```
Invoke `$task-graph start` for `<plan-slug>` with up to 4 workers.
```

Task Graph creates an isolated run and returns a command like:

```bash
tmux attach-session -t task-graph-<plan-slug>-<run-id>
```

Run that command to watch the controller and worker windows.

### 3. Check or resume a run

Use the plan slug and run ID returned when the run started:

```
Invoke `$task-graph status` for `<plan-slug>`.
Invoke `$task-graph status` for `<plan-slug>` run `<run-id>`.
Invoke `$task-graph resume` for `<plan-slug>` run `<run-id>`.
```

`status` reports whether the run is running, succeeded, failed, or already
merged. Use `resume` after an interruption; it reconnects to the live
controller when possible or restarts it from the saved run snapshot.

### 4. Check out the feature branch for review

After a successful run, you can check out its feature branch to explore and
review the implementation manually:

```bash
$task-graph checkout task-graph-<plan-slug>-<run-id>
```

Use this branch to inspect the diff, run tests, and try the changes yourself.
It is a review workspace only; return to the recorded base branch before using
Task Graph to promote the run.

### 5. Merge a successful run

From the recorded base branch with a clean checkout, send:

```
Invoke `$task-graph merge` for `<plan-slug>` run `<run-id>`.
```

Merging is always explicit. Task Graph promotes only that run's feature branch
with a no-fast-forward merge; do not merge worker-attempt branches directly.

## Rules to remember

- Generate artifacts only after the implementation plan is approved.
- Start only a validated DAG from a clean, committed checkout.
- Treat `dag.json` as the source of truth for task dependencies.
- Keep the returned `<run-id>`: it is required to resume or merge a specific run.
