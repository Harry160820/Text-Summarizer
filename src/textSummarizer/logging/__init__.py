import os
import sys
import logging
from pathlib import Path

# Logging format
logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"

# Define log directory relative to this file — safe for any environment
log_dir = Path(__file__).resolve().parent.parent.parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

# Log file path
log_filepath = log_dir / "running_logs.log"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Get the logger
logger = logging.getLogger("TextSummarizerLogger")
