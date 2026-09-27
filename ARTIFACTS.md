# Artifact System

## Supported initial artifacts

- DOCX
- XLSX
- CSV where useful
- generated code/text files where authorized

## Artifact lifecycle

```text
Agent request
 -> artifact tool
 -> file creation
 -> validation
 -> artifact store
 -> observation
```

## Verification

Verify generated artifacts structurally.

For XLSX:
- workbook opens
- expected sheets from the request exist
- cells/tables contain generated data
- file is not empty/corrupt

For DOCX:
- document opens
- expected content is present
- file is not empty/corrupt

Verification must derive expected content from the actual task state, not hardcoded sample documents.

## Naming

Artifact names must be generated from configured naming rules and task metadata, not fixed filenames.
