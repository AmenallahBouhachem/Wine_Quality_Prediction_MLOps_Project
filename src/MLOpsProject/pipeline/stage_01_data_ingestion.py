from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.data_ingestion import DataIngestion
from MLOpsProject import logger




STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        logger.info(f"********Starting {STAGE_NAME}********")
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logger.info(f"********Finished {STAGE_NAME}********")



if __name__ == "__main__":
    try :
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e