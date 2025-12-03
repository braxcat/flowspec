---
id: task-202
title: Implement Hook Runner/Dispatcher
status: To Do
assignee:
  - '@pm-planner'
created_date: '2025-12-03 00:41'
labels:
  - implement
  - backend
  - cli
  - hooks
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
CLI command 'specify hooks run' that receives events and dispatches to configured hooks. Includes sandboxing, timeout, and audit logging.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 CLI command: specify hooks run --event-type <type> --payload <json>
- [ ] #2 Match events to hooks using configuration and dispatch scripts
- [ ] #3 Sandbox execution with timeout (default 30s, configurable)
- [ ] #4 Audit logging to .specify/hooks/audit.log with timestamps and results
- [ ] #5 Exit code reflects hook success/failure for CI integration
- [ ] #6 Integration tests with real hook scripts
<!-- AC:END -->
