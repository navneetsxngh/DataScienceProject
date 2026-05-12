import os
import sys
import logging

logging_format="[ %(asctime)s : %(levelname)s : %(module)s : %(message)s ]"

LOG_DIR = "logs"
LOG_FILEPATH= os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_format,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")