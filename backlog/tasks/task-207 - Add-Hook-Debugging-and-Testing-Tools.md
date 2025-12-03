---
id: task-207
title: Add Hook Debugging and Testing Tools
status: To Do
assignee:
  - '@pm-planner'
created_date: '2025-12-03 00:41'
labels:
  - implement
  - cli
  - dx
  - hooks
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
CLI commands for hook development: list hooks, test hooks, validate config, view audit log.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 specify hooks list - show all configured hooks and their matchers
- [ ] #2 specify hooks test --event-type <type> --dry-run - test without execution
- [ ] #3 specify hooks validate - validate hooks.yaml against schema
- [ ] #4 specify hooks audit - view execution history from audit log
- [ ] #5 specify hooks audit --tail - live tail of hook executions
- [ ] #6 Unit and integration tests for all CLI commands
<!-- AC:END -->
