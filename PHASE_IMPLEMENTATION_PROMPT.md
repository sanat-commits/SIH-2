# PHASE IMPLEMENTATION GUIDE

## Purpose

This document is the authoritative implementation guide for developing the SIH 2026 project phase by phase.

The project is a:

**Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work**

This document contains the permanent architecture, implementation rules, coding constraints, testing requirements, documentation requirements, security requirements, and development workflow that must be followed when implementing any phase of the project.

The user will explicitly specify which phase is being implemented in their instruction.

When the user says something such as:

> Implement Phase 1 — Gemma Runtime. Read `PHASE_IMPLEMENTATION.md` and follow it exactly.

implement that requested phase only.

Do not implement future phases unless explicitly instructed.

---

# 1. PROJECT DEVELOPMENT PRINCIPLE

The project is developed incrementally, one phase at a time.

For every phase:

1. Read this document completely.
2. Read the project's current state and relevant specifications.
3. Inspect the actual repository.
4. Understand the existing implementation.
5. Implement only the phase specified by the user.
6. Test the implementation.
7. Run relevant regression tests.
8. Update all required project documentation.
9. Verify that documentation matches the actual implementation.
10. Report the actual result honestly.
11. STOP.

Do not automatically continue to the next phase.