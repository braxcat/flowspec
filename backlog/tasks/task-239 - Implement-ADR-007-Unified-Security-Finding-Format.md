---
id: task-239
title: 'Implement ADR-007: Unified Security Finding Format'
status: To Do
assignee:
  - '@platform-engineer'
created_date: '2025-12-03 02:31'
labels:
  - architecture
  - security
  - data-model
  - implement
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Define canonical data model for security findings with SARIF compatibility. See docs/adr/ADR-007-unified-security-finding-format.md
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Define Finding and Location dataclasses in src/specify_cli/security/models.py
- [ ] #2 Implement fingerprinting for deduplication
- [ ] #3 Implement finding merging (when multiple scanners find same issue)
- [ ] #4 Implement JSON serialization (to_dict/from_dict)
- [ ] #5 Implement SARIFExporter for SARIF 2.1.0 export
- [ ] #6 Implement MarkdownExporter for human-readable reports
- [ ] #7 Validate SARIF export against official schema
- [ ] #8 Unit tests for all export formats
<!-- AC:END -->
