from diseaseprognosis import logger 
from diseaseprognosis.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from diseaseprognosis.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from diseaseprognosis.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from diseaseprognosis.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline




STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">stage{STAGE_NAME} STARTED<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">stage{STAGE_NAME} COMPLETED<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e





