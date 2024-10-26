from diseaseprognosis.config import ConfigurationManager
from diseaseprognosis.components.model_evaluation import ModelEvaluation
from diseaseprognosis import logger
from pathlib import Path

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()


