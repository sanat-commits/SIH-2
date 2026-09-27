# Specialist Agents

All specialist agents use Gemma.

They are differentiated by:
- role system prompt
- capabilities
- allowed tools
- input/output contracts
- state scope

Required agents:

1. Reasoning Agent
2. Coding Agent
3. Vision Agent
4. Knowledge Agent
5. Document Agent
6. Data Agent

Agents may delegate only through the configured A2A mechanism. Avoid circular delegation using depth/task constraints.

Every agent must return structured observations rather than silently converting tool results into an unrelated final answer.
