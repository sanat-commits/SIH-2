# Implementation Checklist

## Before coding
- [ ] Inspect repository
- [ ] Identify current Gemma runtime
- [ ] Identify current attachment handling
- [ ] Identify current RAG
- [ ] Identify current tools
- [ ] Identify current artifact generation
- [ ] Identify all hardcoded routing/value paths

## Runtime
- [ ] Gemma adapter
- [ ] configuration validation
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
- [ ] no keyword router
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
