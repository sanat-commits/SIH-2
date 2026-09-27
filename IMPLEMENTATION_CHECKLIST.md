# Implementation Checklist

## Before coding
- [x] Inspect repository
- [x] Identify current Gemma runtime
- [x] Identify current attachment handling
- [x] Identify current RAG
- [x] Identify current tools
- [x] Identify current artifact generation
- [x] Identify all hardcoded routing/value paths

## Runtime
- [ ] Gemma adapter
- [x] configuration validation
- [ ] streaming/events
- [ ] structured model output

## Agent system
- [ ] AgentRegistry
- [ ] ToolRegistry
- [ ] A2A messages
- [ ] Main Agent
- [ ] Reasoning Agent
- [ ] Coding Agent
- [ ] Vision Agent
- [ ] Knowledge Agent
- [ ] Document Agent
- [ ] Data Agent

## Infrastructure
- [ ] OCR adapter
- [ ] Python sandbox
- [ ] document parsers
- [ ] RAG indexes
- [ ] artifact store
- [ ] verification
- [ ] audit store

## Regression protection
- [x] no keyword router (verified by test_no_legacy_hardcoded_router_remains)
- [ ] no hardcoded outputs
- [ ] no hardcoded sample documents
- [ ] no hardcoded citation counts
- [ ] no hardcoded filenames
- [ ] no fixed agent sequence
- [ ] no cross-task leakage

## Demonstration scenarios
- [ ] simple question
- [ ] calculation
- [ ] Python execution
- [ ] KB question
- [ ] uploaded document summary
- [ ] scanned document OCR
- [ ] DOCX
- [ ] XLSX
- [ ] combined OCR + KB + calculation + artifact
