"""Phase 0 Exit Gate Tests:
- Application starts
- Health check works
- Configuration loads
- No legacy hardcoded router remains
"""
import os
import re
from pathlib import Path
import pytest
from starlette.testclient import TestClient

from src.core.config import WorkbenchSettings, get_settings
from src.api.app import create_app


def test_configuration_loads():
    """Verify configuration loads properly from config/default.yaml."""
    settings = get_settings("config/default.yaml")
    assert settings is not None
    assert settings.app.name == "SIH26117 Sovereign Agentic Workbench"
    assert settings.security.sovereign_mode is True
    assert settings.security.allow_external_network is False

    # Gemma must be the model
    assert "gemma" in settings.model.model_id.lower()
    assert settings.model.provider == "ollama"

    # Embedding model
    assert settings.embeddings.model_id == "embeddinggemma:latest"

    # Required specialist agents
    assert "main_agent" in settings.agents.enabled_agents
    assert "reasoning_agent" in settings.agents.enabled_agents
    assert "coding_agent" in settings.agents.enabled_agents
    assert "vision_agent" in settings.agents.enabled_agents
    assert "knowledge_agent" in settings.agents.enabled_agents
    assert "document_agent" in settings.agents.enabled_agents
    assert "data_agent" in settings.agents.enabled_agents

    # Sandboxing and limits
    assert settings.sandbox.execution_timeout_seconds > 0
    assert settings.sandbox.network_disabled is True
    assert settings.orchestration.max_turns > 0


def test_application_starts_and_health_check():
    """Verify application boots and /health endpoint functions."""
    settings = get_settings("config/default.yaml")
    app = create_app(settings)
    client = TestClient(app)

    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app"] == settings.app.name
    assert data["sovereign_mode"] is True


def test_readiness_check():
    """Verify readiness check endpoint returns structured operational state."""
    settings = get_settings("config/default.yaml")
    app = create_app(settings)
    client = TestClient(app)

    response = client.get("/readiness")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "model_runtime_reachable" in data
    assert data["model_id"] == settings.model.model_id
    assert data["embeddings_id"] == settings.embeddings.model_id


def test_public_config_endpoint():
    """Verify public config endpoint exposes expected agent/tool metadata."""
    settings = get_settings("config/default.yaml")
    app = create_app(settings)
    client = TestClient(app)

    response = client.get("/api/config")
    assert response.status_code == 200
    data = response.json()
    assert data["model"] == settings.model.model_id
    assert "main_agent" in data["enabled_agents"]
    assert "run_python" in data["enabled_tools"]


def test_no_legacy_hardcoded_router_remains():
    """Static audit: ensure no query keyword-based routing rules exist in src/."""
    banned_patterns = [
        re.compile(r'if\s+["\']python["\']\s+in', re.IGNORECASE),
        re.compile(r'if\s+["\']excel["\']\s+in', re.IGNORECASE),
        re.compile(r'if\s+["\']summary["\']\s+in', re.IGNORECASE),
        re.compile(r'if\s+["\']knowledge["\']\s+in', re.IGNORECASE),
        re.compile(r'if\s+["\']ocr["\']\s+in', re.IGNORECASE),
    ]

    src_dir = Path("src")
    assert src_dir.exists(), "src directory must exist"

    violations = []
    for py_file in src_dir.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8")
        for line_num, line in enumerate(text.splitlines(), start=1):
            for pattern in banned_patterns:
                if pattern.search(line):
                    violations.append(f"{py_file}:{line_num}: {line.strip()}")

    assert not violations, f"Banned keyword routing detected:\n" + "\n".join(violations)
