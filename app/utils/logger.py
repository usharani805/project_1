import logging
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    """Create and return a configured logger."""

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        project_root = Path(__file__).resolve().parents[2]
        log_file = project_root / "application.log"

        handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger