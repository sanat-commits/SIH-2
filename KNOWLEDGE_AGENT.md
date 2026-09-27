# Knowledge Agent

## Purpose

Search the persistent organizational Knowledge Base and return evidence.

## Tool

`search_knowledge`

## Retrieval

The KB supports:
- lexical retrieval
- dense retrieval using Qwen3-Embedding-0.6B
- reciprocal rank fusion
- technical identifier handling
- configurable query/evidence thresholds

All thresholds and retrieval parameters come from configuration.

## Output

Return:
- evidence items
- source identifiers
- document/page/chunk metadata when available
- relevance information
- citations
- retrieval diagnostics where permitted

The Knowledge Agent does not directly produce an unsupported final answer.

## Separation from attachments

Transient attachments are not automatically inserted into the persistent KB.
