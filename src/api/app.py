"""FastAPI baseline application for SIH26117 Sovereign Agentic AI Workbench."""
from __future__ import annotations

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import WorkbenchSettings, get_settings
from src.core.logging import logger


def create_app(settings: WorkbenchSettings | None = None) -> FastAPI:
    if settings is None:
        settings = get_settings()

    app = FastAPI(
        title=settings.app.name,
        version=settings.app.version,
        description="Sovereign On-Premise Agentic AI Workbench API",
    )

    # Local sovereign CORS policy
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["System"])
    async def health_check():
        return {
            "status": "healthy",
            "app": settings.app.name,
            "version": settings.app.version,
            "environment": settings.app.environment,
            "sovereign_mode": settings.security.sovereign_mode,
        }

    @app.get("/readiness", tags=["System"])
    async def readiness_check():
        # Check model runtime accessibility without blocking
        model_ready = False
        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                res = await client.get(f"{settings.model.endpoint}/api/version")
                if res.status_code == 200:
                    model_ready = True
        except Exception:
            model_ready = False

        return {
            "status": "ready" if model_ready else "degraded",
            "model_runtime_reachable": model_ready,
            "model_id": settings.model.model_id,
            "embeddings_id": settings.embeddings.model_id,
        }

    @app.get("/api/config", tags=["System"])
    async def get_public_config():
        """Safe non-sensitive configuration parameters for clients."""
        return {
            "app_name": settings.app.name,
            "version": settings.app.version,
            "model": settings.model.model_id,
            "embeddings": settings.embeddings.model_id,
            "enabled_agents": settings.agents.enabled_agents,
            "enabled_tools": settings.tools.enabled_tools,
            "sovereign_mode": settings.security.sovereign_mode,
        }

    return app


app = create_app()
