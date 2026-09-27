# Vision Agent

## Purpose

Process visual inputs and scanned content.

## Responsibilities

- inspect images/pages
- request OCR when text extraction is needed
- interpret visual structure
- identify tables/regions where supported
- return evidence with page/image references
- use multimodal Gemma input when configured and supported

## OCR

OCR is a service/tool invoked by the Vision Agent.

The OCR implementation must be pluggable through configuration. Do not hardcode a single OCR engine into agent logic.

## Output

Return structured visual evidence:
- source reference
- page/image identifier
- extracted text where applicable
- regions/coordinates where supported
- confidence where supported
- visual observations
