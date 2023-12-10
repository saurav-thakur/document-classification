import os
import sys
import logging

logging_str = "[%(asctime)s -- %(levelname)s -- %(lineno)d -- %(message)s]"
logs_dir = "logs"
log_filepath = os.path.join(logs_dir, "project_logs.logs")
os.makedirs(logs_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        # this handler logs out on log folder
        logging.FileHandler(log_filepath),

        # this handler logs out on terminal
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("document_classification_logger")
