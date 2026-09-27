"""Configuration provider and validation schema.
All operational values must be externalized here per CONFIG.md.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import List, Optional
import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    name: str = "SIH26117 Sovereign Agentic Workbench"
    version: str = "0.1.0"
    environment: str = "development"
    host: str = "127.0.0.1"
    port: int = 8000
    log_level: str = "INFO"


class SecurityConfig(BaseModel):
    sovereign_mode: bool = True
    allow_external_network: bool = False
    session_timeout_seconds: int = 3600


class ModelConfig(BaseModel):
    provider: str = "ollama"
    model_id: str = "gemma4:e2b"
    endpoint: str = "http://127.0.0.1:11434"
    context_window: int = 131072
    temperature: float = 0.1
    request_timeout_seconds: float = 120.0


class EmbeddingsConfig(BaseModel):
    provider: str = "ollama"
    model_id: str = "embeddinggemma:latest"
    endpoint: str = "http://127.0.0.1:11434"
    dimension: int = 768
    batch_size: int = 16
    request_timeout_seconds: float = 60.0


class OrchestrationConfig(BaseModel):
    max_turns: int = 15
    max_delegation_depth: int = 3
    max_tool_calls_per_turn: int = 5
    task_timeout_seconds: float = 300.0


class AgentsConfig(BaseModel):
    enabled_agents: List[str] = Field(
        default_factory=lambda: [
            "main_agent",
            "reasoning_agent",
            "coding_agent",
            "vision_agent",
            "knowledge_agent",
            "document_agent",
            "data_agent",
        ]
    )


class ToolsConfig(BaseModel):
    enabled_tools: List[str] = Field(
        default_factory=lambda: [
            "delegate_to_agent",
            "search_knowledge",
            "calculate",
            "run_python",
            "read_file",
            "create_docx",
            "create_xlsx",
            "ocr_extract",
            "verify_artifact",
        ]
    )


class SandboxConfig(BaseModel):
    execution_timeout_seconds: float = 30.0
    max_stdout_bytes: int = 1048576
    max_stderr_bytes: int = 1048576
    max_file_size_bytes: int = 10485760
    network_disabled: bool = True
    working_dir_base: str = "storage/sandbox"


class OCRConfig(BaseModel):
    engine: str = "pytesseract"
    tesseract_cmd: str = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    languages: List[str] = Field(default_factory=lambda: ["eng"])
    dpi: int = 300
    contrast_adjustment: bool = True


class RAGConfig(BaseModel):
    chunk_size: int = 512
    chunk_overlap: int = 64
    top_k_dense: int = 10
    top_k_lexical: int = 10
    top_k_final: int = 5
    rrf_k: int = 60
    min_relevance_threshold: float = 0.25


class StorageConfig(BaseModel):
    base_dir: str = "storage"
    task_state_dir: str = "storage/tasks"
    kb_dir: str = "storage/kb"
    artifacts_dir: str = "storage/artifacts"
    audit_dir: str = "storage/audit"


class WorkbenchSettings(BaseSettings):
    """Authoritative system configuration model."""
    app: AppConfig = Field(default_factory=AppConfig)
    security: SecurityConfig = Field(default_factory=SecurityConfig)
    model: ModelConfig = Field(default_factory=ModelConfig)
    embeddings: EmbeddingsConfig = Field(default_factory=EmbeddingsConfig)
    orchestration: OrchestrationConfig = Field(default_factory=OrchestrationConfig)
    agents: AgentsConfig = Field(default_factory=AgentsConfig)
    tools: ToolsConfig = Field(default_factory=ToolsConfig)
    sandbox: SandboxConfig = Field(default_factory=SandboxConfig)
    ocr: OCRConfig = Field(default_factory=OCRConfig)
    rag: RAGConfig = Field(default_factory=RAGConfig)
    storage: StorageConfig = Field(default_factory=StorageConfig)

    model_config = SettingsConfigDict(
        env_prefix="SIH_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    @classmethod
    def load_from_yaml(cls, path: Path | str) -> WorkbenchSettings:
        target_path = Path(path)
        if not target_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {target_path}")
        with open(target_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return cls(**data)


_SETTINGS_INSTANCE: Optional[WorkbenchSettings] = None


def get_settings(config_path: Path | str | None = None) -> WorkbenchSettings:
    """Retrieve the singleton settings instance, or load from file."""
    global _SETTINGS_INSTANCE
    if _SETTINGS_INSTANCE is not None and config_path is None:
        return _SETTINGS_INSTANCE

    if config_path:
        _SETTINGS_INSTANCE = WorkbenchSettings.load_from_yaml(config_path)
    else:
        default_file = Path("config/default.yaml")
        if default_file.exists():
            _SETTINGS_INSTANCE = WorkbenchSettings.load_from_yaml(default_file)
        else:
            _SETTINGS_INSTANCE = WorkbenchSettings()

    return _SETTINGS_INSTANCE
