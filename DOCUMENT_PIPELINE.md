# Document Pipeline

## Pipeline

```text
Input
 -> type detection
 -> parser adapter
 -> extraction
 -> OCR when required
 -> normalized document representation
 -> agent processing
 -> artifact generation
 -> artifact verification
```

## Normalized representation

The internal document model should represent:
- document id
- source type
- pages/sections
- text
- tables
- images
- metadata
- provenance

## Transient versus persistent

Transient attachment processing and persistent KB ingestion must use separate storage lifecycles.

## No document-specific hardcoding

Do not implement special cases for filenames, known reports, equipment tags or expected values.
