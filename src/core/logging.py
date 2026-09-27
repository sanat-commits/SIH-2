"""Audit-ready structured logging for the Workbench."""
from __future__ import annotations

import logging
import sys
from typing import Any, Dict


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("sih_workbench")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    return logger


logger = setup_logging()
