import os
from diseaseprognosis import logger
from sklearn.model_selection import train_test_split
from diseaseprognosis.entity.config_entity import DataTransformationConfig
import pandas as pd




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config



    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.8, 0.2) split.
        train, test = train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)