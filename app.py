import sys
from src.mlproject.logger import logging
from src.mlproject.exceptions import CustomException





if __name__ == "__main__":
    logging.info("the execution started")
    
    try:
        a=1/0
    except Exception as e:
        logging.info("error occured in the code")
        raise CustomException(e,sys)
    