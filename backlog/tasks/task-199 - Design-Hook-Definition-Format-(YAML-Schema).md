---
id: task-199
title: Design Hook Definition Format (YAML Schema)
status: To Do
assignee:
  - '@pm-planner'
created_date: '2025-12-03 00:40'
labels:
  - design
  - schema
  - hooks
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Design the YAML configuration format for hook definitions in .specify/hooks/hooks.yaml. Must support event matching, script execution, and security constraints.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Define YAML schema with event matchers (type, wildcards, filters)
- [ ] #2 Support multiple execution modes (script, command, webhook placeholder)
- [ ] #3 Include security constraints (allowlist, timeout, env vars)
- [ ] #4 Create JSON Schema for hooks.yaml validation
- [ ] #5 Document hook definition with 5+ realistic examples
<!-- AC:END -->
