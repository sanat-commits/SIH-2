# Implementation Phases

Do not skip an exit gate.

## Phase 0 — Reset and baseline

Build a clean repository.

Exit tests:
- application starts
- health check works
- configuration loads
- no legacy hardcoded router remains

## Phase 1 — Gemma runtime

Implement one reliable local Gemma runtime adapter.

Exit tests:
- Gemma responds
- timeout/error handled
- structured generation available
- no second generative model introduced

## Phase 2 — Schemas and state

Implement:
- task state
- agent message
- tool call/result
- evidence
- artifact references

Exit tests:
- serialization round trips
- task isolation test passes

## Phase 3 — Registries and A2A

Implement:
- AgentRegistry
- ToolRegistry
- capability descriptors
- A2A protocol

Exit tests:
- agents/tools discovered dynamically
- no query keyword routing

## Phase 4 — Main Agent

Implement:
- planning
- dynamic delegation
- observation handling
- replanning
- completion

Exit tests:
- simple question can complete
- multi-step task can delegate

## Phase 5 — Specialist framework

Implement common specialist-agent runtime.

Exit tests:
- every required specialist starts
- each receives only authorized tools

## Phase 6 — Reasoning Agent

Exit tests:
- evidence comparison
- assumptions and uncertainty represented

## Phase 7 — Coding Agent + Sandbox

Implement real sandbox and run_python.

Exit tests:
- actual stdout captured
- stderr captured
- exit code captured
- timeout enforced
- network policy enforced

## Phase 8 — Vision + OCR

Implement OCR adapter and multimodal path.

Exit tests:
- scanned page produces extracted text
- page provenance retained

## Phase 9 — Document Agent

Implement document adapters and normalized representation.

Exit tests:
- sample PDF/DOCX/XLSX processed
- transient attachment lifecycle works

## Phase 10 — Knowledge Agent + persistent RAG

Implement:
- ingestion
- chunking
- Qwen3-Embedding-0.6B
- BM25
- dense search
- RRF
- citations

Exit tests:
- explicit ingestion persists
- search retrieves correct evidence
- transient uploads do not become KB entries

## Phase 11 — Data Agent

Exit tests:
- calculations are executed
- structured data can be analyzed
- Python is delegated when required

## Phase 12 — Artifact generation

Implement DOCX/XLSX generation and verification.

Exit tests:
- files open
- expected content exists
- generated files are returned

## Phase 13 — Security and audit

Implement:
- permissions
- sandbox policy
- audit events
- network restrictions
- file isolation

Exit tests:
- unauthorized tool call denied
- task cannot access another task's files

## Phase 14 — End-to-end acceptance

Run:
1. chat
2. Python execution
3. KB query
4. attachment summary
5. OCR
6. DOCX
7. XLSX
8. multimodal multi-agent workflow
9. failure/replan
10. security isolation

Only after all tests pass should the prototype be considered complete.
