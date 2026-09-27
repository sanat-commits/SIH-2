# State and Memory

## State scopes

### Session state
Conversation-level state.

### Task state
State for one user objective.

### Agent state
Short-lived specialist execution state scoped to a task.

### Persistent KB state
Long-lived organizational documents/indexes.

These scopes must not be mixed.

## Task state

Store:
- task_id
- session_id
- objective
- plan
- active agent
- completed steps
- observations
- tool calls
- evidence
- attachments
- artifacts
- verification
- errors
- timestamps

## No leakage

A task must never see another user's or task's:
- attachments
- tool results
- KB-private metadata
- temporary files
- agent state

unless explicitly authorized by access policy.
