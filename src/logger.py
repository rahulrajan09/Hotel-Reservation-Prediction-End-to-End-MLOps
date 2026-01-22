import logging
import os
from datetime import datetime

#making the logs folder
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

#creating the log file paths
LOG_FILE= os.path.join(LOGS_DIR,f"log_{datetime.now().strftime('%Y_%m_%d - %H-%M-%S')}.log")

#logging module configration
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s ',
    level=logging.INFO
)

#function to implement logging
def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger