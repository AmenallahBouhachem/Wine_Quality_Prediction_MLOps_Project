
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.data_transformation import DataTransformation
from MLOpsProject import logger
stage_name = "Data Transformation stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        print(f"********Starting {stage_name}********")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()
        print(f"********Finished {stage_name}********")


if __name__=='__main__' :
    try: 
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e