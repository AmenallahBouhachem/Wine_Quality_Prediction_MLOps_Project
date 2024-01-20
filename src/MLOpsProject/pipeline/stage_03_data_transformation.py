
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.data_transformation import DataTransformation
from MLOpsProject import logger
from pathlib import Path
stage_name = "Data Transformation stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f :
                status = f.read().split(" ")[-1]
            if status == "True" :
                print(f"********Starting {stage_name}********")
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
                print(f"********Finished {stage_name}********")
            else :
                raise Exception("Data Validation failed")
        except Exception as e:
            logger.exception(e)
            print(e)

if __name__=='__main__' :
    try: 
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e