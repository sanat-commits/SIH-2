# Document Agent

## Purpose

Handle document-oriented tasks.

## Responsibilities

- parse supported documents
- extract text and structure
- coordinate OCR for scanned documents
- summarize actual document content
- extract tables
- transform content
- create requested artifacts
- verify artifacts

## Supported formats

Support must be adapter-based and configuration-driven.

Initial adapters should cover the formats that the implementation can reliably process:
- PDF
- DOCX
- XLSX
- TXT
- common image formats

Additional formats may be added through adapters.

Do not hardcode document-specific schemas.

## Summarization

Summaries must be generated from the actual current document content.

Never use a fixed template containing unrelated fields or values.

## Artifact creation

Use registered artifact tools such as:
- create_docx
- create_xlsx
