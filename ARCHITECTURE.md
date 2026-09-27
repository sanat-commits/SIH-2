# Architecture

## Layers

1. UI/API layer
2. Main Agent orchestration layer
3. Specialist Agent layer
4. Shared state and A2A protocol
5. Tool registry
6. Tool implementations
7. Infrastructure services
8. Model runtime
9. Persistence and audit

## High-level architecture

```text
                           USER
                            |
                            v
                     +-------------+
                     | MAIN AGENT  |
                     |    Gemma    |
                     +------+------+
                            |
                 Agent Registry / A2A
                            |
       +--------------------+--------------------+
       |          |          |         |         |
       v          v          v         v         v
 Reasoning    Coding      Vision   Knowledge  Document
   Agent       Agent       Agent     Agent      Agent
       |          |          |         |         |
       |          v          v         v         v
       |       Sandbox      OCR       RAG      Parsers
       |          |          |         |      Artifacts
       +----------+----------+---------+---------+
                            |
                         Data Agent
                            |
                       calculations
```

## Shared infrastructure

- ModelRuntime
- AgentRegistry
- ToolRegistry
- TaskStateStore
- EventBus
- ArtifactStore
- DocumentStore
- KnowledgeStore
- AuditStore
- SecurityPolicy
- ConfigurationProvider

## Important distinction

Agents decide what to do.

Tools perform deterministic or bounded operations.

Infrastructure provides reusable services.

The Gemma runtime provides generation.

Do not embed business routing logic inside individual tools.

## Model reuse

A specialist agent is not required to own a separate model process.

Each agent has:
- role prompt
- capability description
- tool permissions
- task-local state
- input/output contract

The same Gemma runtime may execute multiple agent turns.

## State isolation

Every request must have a unique:
- session_id
- task_id

Agent state, temporary files, attachment context, tool observations and artifacts must be scoped by task/session.

No cross-session state leakage.
