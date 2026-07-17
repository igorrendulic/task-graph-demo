# Implementation confirmation workflow

When the user has approved an implementation plan and asks to implement it,
offer to generate Task Graph artifacts first. Explain that this creates focused
task briefs, a kanban board, and a dependency-safe DAG. If the user accepts,
immediately invoke `$task-graph tasks` with the approved plan. Otherwise,
continue with the normal implementation workflow. Do not start the Task Graph
execution controller as part of this handoff.