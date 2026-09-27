# MASTER PROMPT FOR ANTIGRAVITY

You are implementing the SIH26117 Sovereign On-Premise Agentic AI Workbench.

Read every specification file in this directory before changing the code.

## 1. Non-negotiable model constraint

Use **Gemma only as the generative model**.

Do not introduce another generative LLM.

Specialist agents are logical roles powered by Gemma with:
- different system prompts
- different capabilities
- different authorized tools
- task-local state

Use embeddinggemma only for embeddings/RAG.

## 2. Required architecture

```text
USER
  |
  v
MAIN AGENT (Gemma)
  |
  +--> Reasoning Agent (Gemma)
  +--> Coding Agent (Gemma) --> run_python --> Sandbox
  +--> Vision Agent (Gemma) --> OCR / multimodal processing
  +--> Knowledge Agent (Gemma) --> search_knowledge --> RAG
  +--> Document Agent (Gemma) --> parsers/artifacts
  +--> Data Agent (Gemma) --> calculations/Python
```

Main Agent orchestrates.

Specialist agents execute domain tasks.

Tools execute bounded operations.

Infrastructure implements OCR, sandbox, RAG, parsers and artifact services.

## 3. Dynamic behavior

The Main Agent must select specialists from registered capability descriptors.

Specialists must select tools from registered tool descriptors.

DO NOT implement:
- `if "python" in query`
- `if "excel" in query`
- `if "summary" in query`
- `if "knowledge" in query`
- `if "ocr" in query`
- fixed agent sequence
- fixed tool sequence

Equivalent user requests with different wording must still route correctly.

## 4. ReAct-style execution

Implement:

```text
understand
 -> plan
 -> delegate
 -> observe
 -> replan if needed
 -> verify
 -> finalize
```

The loop must be bounded using configuration.

Never silently stop after planning.

Never finalize solely because a plan exists.

Never return a generic success message when a tool returned useful output.

## 5. Tool registry

Build one authoritative dynamic ToolRegistry.

Each tool must declare:
- ID
- description
- capabilities
- input schema
- output schema
- security class
- authorized agents
- enabled state

Tool implementations must be independent of the agent router.

## 6. Agent registry

Build one authoritative AgentRegistry.

Each agent must declare:
- ID
- description
- capabilities
- accepted inputs
- output types
- authorized tools
- enabled state

Main Agent gets these descriptors.

## 7. A2A

All delegation must use a structured A2A message.

Include:
- task_id
- session_id
- sender
- recipient
- objective
- context references
- requested outputs
- constraints
- observations
- artifacts
- citations
- errors
- status

## 8. OCR

Implement a real local OCR adapter.

Do not fake OCR.

Do not hardcode an OCR executable path.

Make the engine configurable.

Normalize OCR output into the project schema.

## 9. Sandbox

Implement a real Python execution sandbox.

`run_python` must execute the supplied code.

Return:
- stdout
- stderr
- exit code
- duration
- produced files
- status

Enforce configured timeout/resource/filesystem/network policies.

The Coding Agent must never execute unrestricted shell commands itself.

## 10. RAG

Implement persistent KB separately from transient attachments.

Transient attachment:
- current task/session
- not automatically indexed

Explicit KB ingestion:
- persistent
- chunked
- embedded
- indexed

Use:
- BM25
- embeddinggemma
- dense retrieval
- RRF
- configurable ranking/filtering

Return citations/evidence.

## 11. Documents

Implement adapter-based document processing.

At minimum support the formats the current environment can reliably process, with PDF/DOCX/XLSX/TXT/image support as the initial target.

Do not create document-specific parsing rules.

Summaries must be based on actual extracted content.

## 12. Artifacts

Implement:
- create_docx
- create_xlsx

Then verify the actual generated files.

Do not use fixed filenames or fixed workbook structures unless they are explicitly requested by the user/task.

## 13. Security

Sovereign mode must default to local execution.

No external model API.

No external OCR API.

No outbound network for sandbox execution.

Use least privilege and task-scoped file access.

## 14. State

All state must be task/session scoped.

No cross-user leakage.

Persist only what configuration requires.

Keep evidence provenance.

## 15. Existing prototype

Before rebuilding:
- inspect the repository
- preserve useful working components
- identify broken routing
- identify hardcoded behavior
- refactor rather than blindly duplicating systems

If a feature is already correct, wrap it behind the required interface instead of rewriting it unnecessarily.

## 16. Phase discipline

Follow PHASES.md.

At the end of every phase:
- run unit tests
- run integration tests relevant to the phase
- run its exit tests
- report failures
- fix them before continuing

Do not implement all phases at once if an earlier phase is failing.

## 17. No fake completion

Never say:
- "implemented" without tests
- "working" without execution
- "sandboxed" without testing the policy
- "RAG working" without retrieval test
- "OCR working" without an OCR test
- "multi-agent" if only one agent is actually executing
- "dynamic" if routing is keyword-based

## 18. Final acceptance

The final system must pass:

1. local Gemma chat
2. dynamic Main Agent delegation
3. reasoning task
4. Python execution with actual stdout
5. sandbox restriction test
6. OCR test
7. multimodal/vision test where supported by the configured Gemma runtime
8. transient attachment summary
9. explicit KB ingestion
10. KB retrieval with citations
11. DOCX creation + verification
12. XLSX creation + verification
13. multi-agent workflow
14. failure and replan
15. task isolation
16. audit trail
17. no-keyword-routing regression tests

Do not add hardcoded shortcuts to make these tests pass. Fix the architecture instead.
