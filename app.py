import sys
from src.mlproject.logger import logging
from src.mlproject.exceptions import CustomException


from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig





if __name__ == "__main__":
    logging.info("the execution started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully")
    except Exception as e:
        logging.info("error occured in the code")
        raise CustomException(e,sys)
    