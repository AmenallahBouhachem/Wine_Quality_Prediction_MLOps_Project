from  MLOpsProject import logger
from MLOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLOpsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
if __name__ == "__main__":
    try :
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME = "Data Validation stage"
if __name__ == "__main__":
    try :
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME = "Data Transformation stage"
if __name__ == "__main__":
    try :
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e