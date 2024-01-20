from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.data_validation import DataValidation
from MLOpsProject import logger




STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        logger.info(f"********Starting {STAGE_NAME}********")
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        logger.info(f"********Finished {STAGE_NAME}********")



if __name__ == "__main__":
    try :
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e