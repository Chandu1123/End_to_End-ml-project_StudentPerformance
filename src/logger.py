import logging
import os

from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(), 'logs',LOG_FILE)

os.makedirs(log_path,exist_ok=True)


LoG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LoG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s",

)

