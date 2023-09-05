import logging
import os,sys
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(),LOG_DIR)
os.makedirs(LOG_DIR,exist_ok=True)

# file extension amd current time stamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#output -> log_2023_-7_3_3_4_5_.log

log_file_path = os.path.join(LOG_DIR,file_name)
logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO )