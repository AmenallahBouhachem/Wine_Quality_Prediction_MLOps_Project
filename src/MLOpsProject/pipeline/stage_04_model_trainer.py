from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject.components.model_trainer import ModelTrainer
from MLOpsProject import logger




STAGE_NAME = "Model Trainer stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        logger.info(f"********Starting {STAGE_NAME}********")
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()
        logger.info(f"********Finished {STAGE_NAME}********")



if __name__ == "__main__":
    try :
        model_trainer_pipeline = ModelTrainingPipeline()
        model_trainer_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e