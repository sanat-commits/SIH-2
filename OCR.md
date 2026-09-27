# OCR Subsystem

## Goal

Provide real local OCR for scanned industrial material.

## Architecture

```text
Vision/Document Agent
        |
        v
     OCR Adapter
        |
   configured engine
        |
        v
 OCR normalized result
```

## Adapter design

Define an OCR interface independent of the selected engine.

The configured engine is loaded through configuration.

The implementation must not contain:
- hardcoded executable paths
- hardcoded language lists
- hardcoded page sizes
- hardcoded document-specific extraction rules

## Normalized result

```json
{
  "source_ref": "...",
  "pages": [
    {
      "page_number": 1,
      "text": "...",
      "regions": [],
      "confidence": null
    }
  ]
}
```

Fields unavailable from an OCR engine may be null/empty according to the schema.

## Preprocessing

Use configurable:
- resolution
- rotation handling
- deskew
- contrast
- thresholding
- page selection

Only apply preprocessing that is configured and supported.

## Security

OCR must operate locally. No external OCR API is allowed unless explicitly configured by an administrator, and the sovereign deployment profile should disable external network access.
