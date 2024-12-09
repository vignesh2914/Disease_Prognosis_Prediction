from diseaseprognosis.config.configuration import ConfigurationManager
from diseaseprognosis.components.model_trainer import ModelTrainer
from diseaseprognosis import logger


STAGE_NAME = "Model Trainer"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()

        # Initialize ModelTrainer and train the model
        model_trainer = ModelTrainer(config=model_trainer_config)
        rf_model_path = model_trainer.train()