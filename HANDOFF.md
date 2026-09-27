# Antigravity Handoff

## First action

Read:
1. README.md
2. PROJECT_CONTEXT.md
3. ARCHITECTURE.md
4. AGENT_ORCHESTRATION.md
5. PHASES.md
6. CODING_RULES.md
7. ACCEPTANCE_MATRIX.md

Then implement one phase at a time.

## Before modifying code

Inspect the existing repository and identify:
- model runtime
- APIs
- UI
- storage
- legacy routing
- current tools
- current document pipeline
- current RAG
- current artifact generation

Do not blindly overwrite working components.

## If existing code conflicts

The specification wins for architecture, but preserve working low-level implementations when they satisfy the contracts.

Refactor toward adapters/interfaces instead of deleting working capabilities.

## Required developer workflow

After every phase:
1. run tests
2. inspect logs
3. run the phase exit tests
4. fix failures
5. only then continue

Never claim a feature works without exercising it.
