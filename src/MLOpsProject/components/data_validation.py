import os 
import pandas as pd
from MLOpsProject.config.configuration import DataValidationConfig
from MLOpsProject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            column_dict = dict(zip(data.columns, data.dtypes))
            all_schema = self.config.all_schema
            for col,dtype in column_dict.items():
                if not((col  in all_schema) and (dtype == self.config.all_schema[col])):
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            logger.exception(e)
            raise e




