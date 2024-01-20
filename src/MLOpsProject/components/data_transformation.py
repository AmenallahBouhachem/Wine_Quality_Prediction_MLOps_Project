import os
from MLOpsProject import logger
from sklearn.model_selection import train_test_split
from MLOpsProject.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
            data = pd.read_csv(self.config.data_path)
            train, test = train_test_split(data, test_size=0.25, random_state=0)
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False, encoding='utf-8')
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False, encoding='utf-8')
            logger.info("Splitted data into train and test set and saved at %s", self.config.root_dir)
            logger.info(train.shape)
            logger.info(test.shape)