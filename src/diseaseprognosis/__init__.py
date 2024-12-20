import logging
import os
from datetime import datetime
import sys


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(

    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # save everything in the file 
        logging.StreamHandler(sys.stdout)  # show u in the terminal
    ]
)


logger = logging.getLogger("ML_Project_logger")