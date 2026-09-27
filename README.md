# SIH26117 Sovereign On-Premise Agentic AI Workbench

This package is the implementation specification for the SIH26117 prototype.

## Core rule

The system uses **Gemma as the only generative model**. Specialist agents are logical agent roles powered by the same Gemma runtime. Qwen3-Embedding-0.6B is used only for embeddings/RAG and is not an agent.

The architecture is deliberately capability-driven and configuration-driven.

There must be NO hardcoded routing such as:
- `if "python" in query`
- `if "summary" in query`
- `if "excel" in query`
- `if "knowledge" in query`
- fixed tool selection based on keywords
- fixed document-specific answers
- fixed outputs such as `5050`
- fixed source counts
- fixed filenames
- fixed citation text
- hardcoded agent ordering

The Main Agent must choose specialist agents from their registered capabilities. Specialist agents must choose tools from their registered tool contracts.

## Main capabilities

- Local Gemma inference
- Main Agent orchestration
- Reasoning Agent
- Coding Agent
- Vision Agent
- Knowledge Agent
- Document Agent
- Data Agent
- Agent-to-agent delegation
- Dynamic tool registry
- Dynamic agent registry
- Shared task state with strict session/task isolation
- OCR
- Multimodal image/document processing
- Persistent Knowledge Base
- BM25 + dense retrieval + RRF
- Qwen3-Embedding-0.6B embeddings
- Python sandbox
- File reading
- Calculations
- DOCX generation
- XLSX generation
- Artifact verification
- Citations/evidence
- Audit events
- Security controls

## Non-negotiable architecture

USER
 -> MAIN AGENT
 -> SPECIALIST AGENT(S)
 -> TOOLS / INFRASTRUCTURE
 -> OBSERVATIONS
 -> MAIN AGENT
 -> VERIFICATION
 -> FINAL RESPONSE

The Main Agent is an orchestrator, not a giant hardcoded router.

The specialist agents are logical roles. They may use the same Gemma model instance sequentially to fit local hardware constraints.

OCR and sandbox are real implemented subsystems, not placeholders.

## Source of truth

Read all files in this package before implementing. Follow `PHASES.md` in order. Do not jump ahead when an exit gate fails.
