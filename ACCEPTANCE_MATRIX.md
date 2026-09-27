# Acceptance Matrix

| Capability | Acceptance condition |
|---|---|
| Gemma | All generative agent roles use Gemma |
| Main Agent | Dynamically delegates using capabilities |
| Reasoning | Performs evidence-based multi-step reasoning |
| Coding | Executes code through sandbox |
| Vision | Handles visual/scanned inputs |
| OCR | Real local OCR adapter works |
| Knowledge | Persistent KB retrieval works |
| RAG | BM25 + dense + RRF works |
| Embeddings | Qwen3-Embedding-0.6B used for vectors |
| Documents | PDF/DOCX/XLSX processing works |
| Attachments | Transient by default |
| KB ingestion | Explicit and persistent |
| Python | Actual stdout/stderr/exit code returned |
| DOCX | Real file generated and verified |
| XLSX | Real file generated and verified |
| Multi-agent | Multiple specialists can collaborate |
| State | Session/task isolation enforced |
| Security | Unauthorized access is denied |
| Audit | Agent/tool/task events are recorded |
| Routing | No keyword-based hardcoded routing |
| Values | No document-specific hardcoded values |
| Configuration | Operational settings externalized |
