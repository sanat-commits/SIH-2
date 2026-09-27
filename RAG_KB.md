# Knowledge Base and RAG

## Persistent ingestion

Explicit KB ingestion:

```text
Document
 -> validation
 -> parsing
 -> structure-aware chunking
 -> Qwen3-Embedding-0.6B embedding
 -> vector index
 -> lexical index
 -> metadata store
```

## Retrieval

```text
Query
 -> query normalization
 -> lexical retrieval
 -> dense retrieval
 -> RRF fusion
 -> optional identifier boosting
 -> configurable filtering
 -> evidence
```

## Important separation

Attachment evidence and persistent KB evidence are different source types.

A normal attachment:
- belongs to the task/session
- can be parsed
- can be used by agents
- is not automatically persisted to KB

Explicit KB ingestion:
- persists the document
- indexes it
- makes it available for future searches

## Configuration

All:
- chunk sizes
- overlap
- retrieval counts
- RRF parameters
- thresholds
- embedding model settings
- index locations

must be configurable.

Do not hardcode them in retrieval code.
