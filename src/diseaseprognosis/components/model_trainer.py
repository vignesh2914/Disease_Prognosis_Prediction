import pandas as pd
import os
from diseaseprognosis import logger
from diseaseprognosis.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestClassifier
import joblib



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        

        # Initialize Random Forest model with parameters from the config
        self.model = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            min_samples_split=self.config.min_samples_split,
            min_samples_leaf=self.config.min_samples_leaf,
            random_state=self.config.random_state
        )


    def train(self):
        # Load training data
        train_data = pd.read_csv(self.config.train_data_path)

        # Split into features and target
        train_x = train_data.drop(columns=[self.config.target_column])
        train_y = train_data[self.config.target_column]

        # Train the Random Forest model
        self.model.fit(train_x, train_y)

        # Save the trained Random Forest model
        rf_model_path = os.path.join(self.config.root_dir, "model.joblib")
        joblib.dump(self.model, rf_model_path)
        print(f"Random Forest model saved at {rf_model_path}")

        return rf_model_path
