# Dynamic Tool Registry

## Requirement

There must be one authoritative ToolRegistry.

Every tool has a machine-readable descriptor:

```json
{
  "tool_id": "run_python",
  "description": "Execute Python in the configured sandbox",
  "capabilities": ["code_execution", "python", "data_analysis"],
  "input_schema": {},
  "output_schema": {},
  "security_class": "sandboxed",
  "allowed_agents": ["coding_agent", "data_agent"],
  "enabled": true
}
```

The actual schema must be generated from implementation contracts rather than duplicated manually.

## Required initial tools

- delegate_to_agent
- search_knowledge
- calculate
- run_python
- read_file
- create_docx
- create_xlsx
- OCR service/tool
- artifact verification

## Registration

Tools register during application startup.

Disabled/unavailable tools must not be presented as available.

## Selection

Agents receive relevant tool descriptors and decide which tool to call.

No:
- keyword router
- hardcoded if/else query classifier
- fixed tool sequence
- fixed tool count

## Tool result contract

Every tool returns structured data:

```json
{
  "status": "success|failure|partial",
  "data": {},
  "error": null,
  "metadata": {},
  "artifacts": [],
  "citations": []
}
```

Tool-specific schemas may extend `data`.
