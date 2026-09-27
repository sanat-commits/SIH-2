# Configuration

All operational values must be configuration-driven.

## Required configuration groups

### Model
- Gemma model identifier
- runtime endpoint/provider
- context limits
- generation parameters

### Embeddings
- Qwen3-Embedding-0.6B identifier
- embedding runtime settings

### Agents
- enabled agents
- agent prompts
- capabilities
- tool permissions

### Tools
- enabled/disabled state
- tool limits
- schemas
- security classes

### Sandbox
- timeout
- CPU/memory limits where supported
- output limits
- network policy
- filesystem policy

### OCR
- selected adapter
- executable/service configuration
- preprocessing settings
- languages

### RAG
- chunking
- retrieval counts
- fusion parameters
- thresholds
- index paths

### Storage
- task storage
- artifact storage
- KB storage
- audit storage

### Orchestration
- maximum turns
- maximum delegations
- maximum tool calls
- task timeout

No agent or tool may define these as hidden constants when they are operational settings.
