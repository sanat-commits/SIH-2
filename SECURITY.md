# Security and Sovereignty

## Principles

- Local-first
- Least privilege
- Explicit tool authorization
- Task isolation
- Sandbox execution
- Auditability
- No secret leakage
- No external network dependency in sovereign mode

## Tool permissions

Each agent receives only the tools required by its registered capabilities.

## Files

File access must use authorized references.

Never allow arbitrary paths supplied by the model to escape the task workspace.

## Network

Default sovereign mode:
- outbound network disabled for model/tool execution
- external APIs disabled unless an administrator explicitly enables them

## Secrets

Secrets must come from a secure configuration/secret provider.

Never place secrets in prompts, source code, logs or model-visible tool descriptions.

## Audit

Record:
- task
- agent
- tool
- timestamp
- status
- relevant metadata
- artifact references

Avoid logging sensitive document contents unnecessarily.
