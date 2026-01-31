import os
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml
from google.cloud import storage


logger= get_logger(__name__)

class DataIngestion:
    def __init__(self,config_path):
        self.config_dict=read_yaml(config_path)
        self.config=self.config_dict["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.bucket_file_name=self.config["bucket_file_name"]
        self.train_ratio=self.config["train_ratio"]
        
        #Creating folder for raw data storage
        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info("Raw file folder created")
        
        #extracting data from cloud to local storage raw file
    def _download_csv_from_gcp(self):
        """Download csv file from GCP in Raw FIle path
        """
        try:
            #creating connect with gcp
            client=storage.Client()
            bucket=client.bucket(self.bucket_name)
            blob=bucket.blob(self.bucket_file_name)
            
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info("Successfully downloaded csv from GCP")
        
        except Exception as e:
            logger.error("Failed to download file from GCP")
            raise CustomException(f"Failed to download file from GCP : {str(e)}") from e

    #Splitting data as test file and train file in respective files
    def _split_data(self):
        try:
            logger.info("Starting splitting process of data")
            data=pd.read_csv(RAW_FILE_PATH)
            train_data, test_data = train_test_split(data, test_size= 1 -self.train_ratio , random_state=42)
            
            train_data.to_csv(TRAIN_FILE_PATH,index=False)
            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            
            test_data.to_csv(TEST_FILE_PATH , index=False)
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
            
        except Exception as e:
            logger.error("Failed to Split file from raw file")
            raise CustomException(f"Failed to split file as train and test from bucket {self.bucket_name} : {str(e)}") from e
            
    def run(self):
        """
        Loading the data from GCP to local file and then splitting it Train & Test and saving it locally
        """
        try:
            logger.info("Starting Data Ingestion Process")
            self._download_csv_from_gcp()
            self._split_data()
            logger.info(" Data Ingestion Process Completed Successfully")
        
        except CustomException as ce:
            logger.error(f"CustomException : {str(ce)}")
            raise ce
            
        finally:
            logger.info("Data Ingestion Completed")
                

if __name__== "__main__":
    data_ingestion=DataIngestion(CONFIG_PATH)
    data_ingestion.run()