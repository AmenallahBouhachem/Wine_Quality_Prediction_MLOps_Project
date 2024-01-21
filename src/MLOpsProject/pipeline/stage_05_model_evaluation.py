from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.model_evaluation import ModelEvaluation
from MLOpsProject import logger




STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        logger.info(f"********Starting {STAGE_NAME}********")
        config = ConfigurationManager()
        model_evaluation_conffig = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_conffig)
        model_evaluation.log_into_mlflow()
        logger.info(f"********Finished {STAGE_NAME}********")



if __name__ == "__main__":
    try :
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e














