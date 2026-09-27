# Project Context

## Problem

SIH26117 / PS117:
Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work.

## Intended environment

The workbench is designed for confidential industrial knowledge work. Sensitive content must remain on-premise/local.

Known prototype hardware:
- Intel Core i7-14700HX
- 16 GB DDR5
- RTX 4050 Laptop GPU
- 6 GB VRAM
- approximately 462 GB free storage at the time of planning

## Model policy

Generative model:
- Gemma only.

Embedding model:
- Qwen3-Embedding-0.6B for RAG embeddings.

Do not silently add another generative LLM.

Specialist agents are role-specific prompts/capability sets backed by Gemma.

## Required behavior

A normal uploaded attachment is transient task/session evidence unless the user explicitly requests persistent Knowledge Base ingestion.

Persistent KB documents are separately indexed and searchable.

`search_knowledge` returns evidence/observations. It must not directly fabricate a final answer.

`run_python` must execute code in a sandbox and return actual structured execution results including stdout/stderr/exit status.

Artifact tools must generate real files and verification must inspect the resulting artifacts.

## Design priority

Correct dynamic orchestration is more important than adding many features.

Never replace the agent architecture with keyword routing or fixed workflows.
