import os,sys
import pandas as pd
from pandas.io.json import build_table_schema
from housing.util.util import read_yaml_file
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig, data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'='*20}Data Validation log started{'='*20}")
            self.data_validation_config = data_validation_config
            self.data_ingstion_artifact = data_ingestion_artifact
            self.schema_file = read_yaml_file(file_path=self.data_validation_config.schema_file_path)

        except Exception as e:
            raise HousingException(e,sys) from e

    def is_train_test_file_exists(self)->bool:
        try: 
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingstion_artifact.train_file_path
            test_file_path = self.data_ingstion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)
        
            is_available = is_train_file_exist and is_test_file_exist
            logging.info(f"Is train and test file available ? -> {is_available}")

            if not is_available:
                training_file = self.data_ingstion_artifact.train_file_path
                testing_file = self.data_ingstion_artifact.test_file_path

                message = f"Training file : [{training_file}] or Testing file: [{testing_file}] is not present"
                
                raise Exception(message)

            return is_available

        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False

            train_dataframe = pd.read_csv(self.data_ingstion_artifact.train_file_path)
            test_dataframe = pd.read_csv(self.data_ingstion_artifact.test_file_path)

            train_dataframe_schema = build_table_schema(train_dataframe)
            test_dataframe_schema = build_table_schema(test_dataframe)

            print(train_dataframe_schema)
            print(test_dataframe_schema)
            print(self.schema_file)

            validation_status = True

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()    

        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Validation log completed{'='*20}")    