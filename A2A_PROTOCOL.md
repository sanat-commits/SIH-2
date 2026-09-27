# Agent-to-Agent Protocol

## Message

```json
{
  "message_id": "...",
  "task_id": "...",
  "parent_task_id": "...",
  "session_id": "...",
  "sender_agent_id": "...",
  "recipient_agent_id": "...",
  "objective": "...",
  "context_refs": [],
  "constraints": [],
  "requested_outputs": [],
  "status": "requested",
  "observations": [],
  "artifacts": [],
  "citations": [],
  "errors": []
}
```

## Rules

- Every delegation has a task identity.
- Every result references its originating task.
- Context is passed by explicit references or scoped state.
- Do not copy entire unrelated conversation state into every agent.
- Preserve provenance of evidence.
- Reject messages from unauthorized agents.
- Enforce delegation depth and task lifetime limits from configuration.
