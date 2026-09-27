# Coding Agent

## Purpose

Generate, inspect, debug and execute code when code execution is required.

## Tools

The agent may use registered coding tools, especially:
- run_python
- read_file
- write_file only if explicitly registered and authorized

## Execution

When execution is required, the Coding Agent must call `run_python`.

It must not simulate execution.

The tool result must contain actual:
- source/execution identifier
- stdout
- stderr
- exit code
- duration
- produced files
- failure information

The agent then interprets the result.

## Security

All code execution goes through the sandbox. Direct unrestricted subprocess execution from agent code is prohibited.
