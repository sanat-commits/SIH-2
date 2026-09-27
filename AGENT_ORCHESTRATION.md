# Agent Orchestration

## Main Agent responsibilities

The Main Agent:

1. interprets the objective
2. inspects available agent capabilities
3. creates a plan
4. delegates subtasks
5. observes specialist results
6. updates the plan when evidence changes
7. requests another specialist when needed
8. verifies completion
9. finalizes the answer

## Dynamic routing

The Main Agent must receive machine-readable agent descriptors containing:
- agent_id
- description
- capabilities
- accepted input types
- output types
- available tools
- constraints

Gemma chooses the appropriate agent based on the task and descriptors.

The implementation must not contain keyword rules such as:
`if "python" in query`.

A deterministic fallback may exist only for infrastructure failures and must be capability-based, not query-keyword-based.

## Delegation loop

```text
Main Agent
  |
  +--> delegate(task)
  |
  +<-- observation/result
  |
  +--> continue/delegate/verify
```

## Completion

The Main Agent can finalize only when:
- requested outputs exist
- required evidence has been obtained
- required tools completed successfully
- generated artifacts have passed verification
- unresolved failures are explicitly represented

## Bounded execution

Limits must come from configuration:
- maximum agent turns
- maximum delegation depth
- maximum tool calls
- maximum wall-clock task duration

Never hardcode these values inside agent logic.

## Parallelism

Parallel specialist execution is allowed only when tasks are independent and configuration permits it.

Dependent tasks must consume prior observations.
