# Acceptance Matrix

| Capability | Acceptance condition | Status |
|---|---|---|
| Gemma | All generative agent roles use Gemma | PENDING (Phase 1) |
| Main Agent | Dynamically delegates using capabilities | PENDING (Phase 4) |
| Reasoning | Performs evidence-based multi-step reasoning | PENDING (Phase 6) |
| Coding | Executes code through sandbox | PENDING (Phase 7) |
| Vision | Handles visual/scanned inputs | PENDING (Phase 8) |
| OCR | Real local OCR adapter works | PENDING (Phase 8) |
| Knowledge | Persistent KB retrieval works | PENDING (Phase 10) |
| RAG | BM25 + dense + RRF works | PENDING (Phase 10) |
| Embeddings | Configured local embedding model (embeddinggemma / Qwen) used for vectors | PENDING (Phase 10) |
| Documents | PDF/DOCX/XLSX processing works | PENDING (Phase 9) |
| Attachments | Transient by default | PENDING (Phase 9) |
| KB ingestion | Explicit and persistent | PENDING (Phase 10) |
| Python | Actual stdout/stderr/exit code returned | PENDING (Phase 7) |
| DOCX | Real file generated and verified | PENDING (Phase 12) |
| XLSX | Real file generated and verified | PENDING (Phase 12) |
| Multi-agent | Multiple specialists can collaborate | PENDING (Phase 4/5) |
| State | Session/task isolation enforced | PENDING (Phase 2) |
| Security | Unauthorized access is denied | PENDING (Phase 13) |
| Audit | Agent/tool/task events are recorded | PENDING (Phase 13) |
| Routing | No keyword-based hardcoded routing | VERIFIED BASELINE (Phase 0) |
| Values | No document-specific hardcoded values | VERIFIED BASELINE (Phase 0) |
| Configuration | Operational settings externalized | COMPLETE (Phase 0) |
