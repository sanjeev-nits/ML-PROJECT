import sys
from src.mlproject.logger import logging
from src.mlproject.exceptions import CustomException


from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_ingestion import DataIngestionConfig





if __name__ == "__main__":
    logging.info("the execution started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logging.info("Data transformation completed successfully")
    except Exception as e:
        logging.info("error occured in the code")
        raise CustomException(e,sys)
    