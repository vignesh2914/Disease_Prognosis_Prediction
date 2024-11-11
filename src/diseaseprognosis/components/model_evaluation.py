import os
import json
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from pathlib import Path
from diseaseprognosis.entity.config_entity import ModelEvaluationConfig
from urllib.parse import urlparse
import numpy as np
import joblib
import mlflow
import mlflow.sklearn




# Function to save JSON data
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        conf_matrix = confusion_matrix(actual, pred)
        class_report = classification_report(actual, pred, output_dict=True)
        return accuracy, conf_matrix, class_report

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        predicted_classes = model.predict(test_x)

        accuracy, conf_matrix, class_report = self.eval_metrics(test_y, predicted_classes)

        # Saving metrics as JSON
        scores = {
            "accuracy": accuracy,
            "confusion_matrix": conf_matrix.tolist(),  # Convert to list for JSON serialization
            "classification_report": class_report
        }
        save_json(path=Path(self.config.metric_file_name), data=scores)

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
 
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            score = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"score": score}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("score", score)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestModel")
            else:
                mlflow.sklearn.log_model(model, "model")