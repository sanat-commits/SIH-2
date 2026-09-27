# Tool Contracts

## Common contract

Inputs:
- task_id
- session_id
- caller_agent_id
- arguments
- security context

Outputs:
- status
- structured data
- artifacts
- citations
- diagnostics
- error information

## search_knowledge

Input:
- query
- optional filters
- retrieval configuration reference

Output:
- evidence list
- citations
- source metadata
- retrieval metadata

## calculate

Input:
- validated calculation expression/data

Output:
- result
- units when available
- calculation metadata

## run_python

Input:
- code
- execution policy reference
- optional input files

Output:
- stdout
- stderr
- exit_code
- duration
- produced files
- sandbox metadata

## read_file

Input:
- authorized file reference

Output:
- extracted content/metadata

## create_docx

Input:
- structured content
- artifact metadata

Output:
- artifact reference
- validation result

## create_xlsx

Input:
- structured workbook model

Output:
- artifact reference
- sheet metadata
- validation result

## OCR

Input:
- authorized image/page/document reference
- OCR configuration reference

Output:
- extracted text
- page/region metadata where available
- confidence where available
