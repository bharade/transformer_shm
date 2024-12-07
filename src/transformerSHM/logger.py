import logging,os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd) #get current working directory
os.makedirs(logs_path,exist_ok=True)#create directory if not created before
#exit_ok=True suppresses the error if a directory with that name has already been created
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")