# Main Agent

## Role

The Main Agent is the top-level Gemma-powered orchestrator.

It is not a general-purpose direct executor for every tool.

## Input

- user request
- session context
- attachment metadata/evidence
- available agent descriptors
- current task state
- prior observations

## Output

Structured task decisions, delegation requests, verification requests, or final response.

## Main Agent tools

The Main Agent should normally use:
- delegate_to_agent
- inspect_task_state
- verify_task
- finalize_response

Direct tool access should be limited to orchestration/infrastructure tools.

Domain-specific execution belongs to specialist agents.

## Planning contract

A plan contains:
- objective
- ordered or dependency-aware steps
- selected agent IDs
- requested outputs
- evidence requirements
- constraints
- completion criteria

The plan must be generated from the task, not from hardcoded workflow templates.

## Replanning

After each specialist observation, the Main Agent may:
- continue current plan
- delegate another task
- revise the plan
- request verification
- finalize

## Failure handling

If a specialist fails:
- preserve failure details
- determine whether retry is useful
- retry only within configured limits
- delegate to another capable agent only when its registered capability matches
- do not hide failures
