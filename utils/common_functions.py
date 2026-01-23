import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger=get_logger(__name__)

def read_yaml(file_path:str) -> dict :
    """reads a yaml file from given filepath link"""
    try:
        #check if file exists in path
        if not os.path.exists(file_path):
            logger.error(f"File not found in given path-{file_path}")
            raise FileNotFoundError(f"File not present in given path-{file_path}")
        #file present then
        with open(file_path,"r") as yaml_file:
            config=yaml.safe_load(yaml_file)
            logger.info("Succesfully read the YAML FILE")
            return config
        
        
    except Exception as e:
        logger.error(f"Failed to read yaml file - {file_path}")
        raise CustomException(f"Failed to read YAML file : {str(e)}") from e
    