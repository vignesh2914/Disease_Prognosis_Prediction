from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from diseaseprognosis.entity.config_entity import ModelTrainerConfig
import pandas as pd
import joblib
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

        # Initialize PCA with the number of components from the config
        self.pca = PCA(n_components=self.config.n_components, random_state=self.config.random_state)

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

        # Save the trained Random Forest model to a separate file
        rf_model_path = os.path.join(self.config.root_dir, f"{self.config.model_name}_rf")
        joblib.dump(self.model, rf_model_path)
        print(f"Random Forest model saved at {rf_model_path}")

        # Save the PCA model to a separate file
        pca_model_path = os.path.join(self.config.root_dir, f"{self.config.model_name}_pca")
        joblib.dump(self.pca, pca_model_path)
        print(f"PCA components saved at {pca_model_path}")

        return rf_model_path, pca_model_path
