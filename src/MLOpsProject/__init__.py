import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(filename=log_filepath, 
                    level=logging.INFO, 
                    format=logging_str, 
                    
                    )

                        

logger = logging.getLogger("MLOpsProjectLogger")
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(logging_str))
logger.addHandler(console_handler)
console_handler = logging.FileHandler(log_filepath)
logger.addHandler(console_handler)