# Python Sandbox

## Goal

Execute untrusted/generated Python safely enough for the prototype's configured threat model.

## Required controls

- isolated working directory per execution
- execution timeout
- resource limits where supported
- controlled environment variables
- restricted filesystem access
- network disabled by default
- subprocess restrictions
- stdout/stderr capture
- cleanup after execution
- maximum output size
- maximum generated file size
- audit event

All values come from configuration.

## Implementation

Provide a Sandbox interface:

```text
execute(code, policy, input_files) -> ExecutionResult
```

The Coding Agent must never call unrestricted `subprocess`, shell or OS execution directly.

The concrete sandbox implementation may use the safest mechanism supported by the target deployment environment.

## Result

Return actual execution results, never a generic success message when stdout/stderr are available.

## Failure

Timeout, policy violation, process failure and resource exhaustion must be distinct statuses.
