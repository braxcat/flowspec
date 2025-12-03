---
id: task-203
title: Integrate Event Emission into /jpspec Commands
status: To Do
assignee:
  - '@pm-planner'
created_date: '2025-12-03 00:41'
labels:
  - implement
  - integration
  - hooks
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add event emission to all /jpspec workflow commands (assess, specify, plan, implement, validate, operate). Events emitted after successful command completion.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Emit events from /jpspec:assess (workflow.assessed)
- [ ] #2 Emit events from /jpspec:specify (spec.created, tasks.created)
- [ ] #3 Emit events from /jpspec:plan (plan.created, adr.created)
- [ ] #4 Emit events from /jpspec:implement (implement.completed)
- [ ] #5 Emit events from /jpspec:validate (validate.completed)
- [ ] #6 Emit events from /jpspec:operate (deploy.completed)
- [ ] #7 Integration tests verifying event payloads for each command
<!-- AC:END -->
