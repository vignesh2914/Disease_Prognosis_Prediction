from sklearn.ensemble import RandomForestClassifier
from diseaseprognosis.entity.config_entity import ModelTrainerConfig
import pandas as pd
import joblib
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        # Initialize Random Forest model with parameters from the config
        self.model = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            min_samples_split=self.config.min_samples_split,
            random_state=self.config.random_state
        )

    def train(self):
        # Load training and testing data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Split into features and target
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        # Train the Random Forest model
        self.model.fit(train_x, train_y)

        # Save the trained model to a file
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(self.model, model_path)
        print(f"Model saved at {model_path}")

        return model_path
