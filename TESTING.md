# Testing Strategy

## Unit tests

Test:
- schemas
- registry
- state isolation
- A2A protocol
- parsers
- OCR adapter normalization
- sandbox result normalization
- RAG ranking
- artifact validation

## Integration tests

Test:
- Main Agent -> specialist
- specialist -> tool
- tool -> observation
- observation -> Main Agent
- verification -> final

## Required behavioral tests

### Test 1: arithmetic execution

Request a calculation that requires Python execution.

Expected:
- Main Agent delegates appropriately
- Coding/Data Agent calls run_python
- sandbox executes
- actual stdout/result returns
- final answer uses returned result

### Test 2: knowledge search

Request information that exists in the persistent KB.

Expected:
- Knowledge Agent is selected
- search_knowledge is called
- evidence/citations return
- final response references evidence

### Test 3: transient attachment

Upload a document and ask for a summary.

Expected:
- document is used in current task
- it is not automatically inserted into persistent KB

### Test 4: explicit KB ingestion

Explicitly ingest a document.

Expected:
- document persists
- index updates
- later search can retrieve it

### Test 5: OCR

Use a scanned page.

Expected:
- Vision/Document Agent invokes OCR
- extracted text is returned
- no external OCR service in sovereign mode

### Test 6: DOCX

Ask for a DOCX artifact.

Expected:
- Document Agent selects create_docx
- real file generated
- verifier validates it

### Test 7: XLSX

Ask for spreadsheet extraction.

Expected:
- real workbook generated
- workbook verified

### Test 8: multi-agent

Use a task requiring OCR + KB + calculation + artifact.

Expected:
- multiple specialists participate
- each result is passed through A2A/shared state
- Main Agent integrates results

### Test 9: no keyword routing

Use semantically equivalent requests with different wording.

Expected:
- capability-based routing remains correct
- no literal keyword dependency

### Test 10: failure

Force a tool failure.

Expected:
- failure is represented
- agent can retry/replan within limits
- final answer does not claim success when execution failed
