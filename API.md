# API

## Core endpoints

The implementation may expose endpoints through the selected local API framework.

Required logical operations:

- create session
- submit task
- upload attachment
- stream task events
- inspect task state
- retrieve artifact
- explicitly ingest document into KB
- search KB
- health/readiness

Exact paths and HTTP details must be generated from the implementation framework and configuration. Do not hardcode frontend assumptions into agent logic.

## Task response

A task response should identify:
- task_id
- status
- final answer when complete
- artifact references
- citations
- unresolved errors where applicable
