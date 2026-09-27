# Events

Use structured events for UI observability.

Suggested event types:

- task.created
- plan.created
- agent.delegated
- agent.started
- agent.completed
- tool.started
- tool.completed
- evidence.retrieved
- artifact.created
- artifact.verified
- task.replanned
- task.failed
- task.completed

Events must include task/session correlation IDs.

The UI should render these events generically. Do not hardcode a special event sequence for a particular query.
