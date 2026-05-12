from src.datascience import logger
from src.datascience.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.datavalidationpipeline import DataValidationTrainingPipeline

logger.info("Welcome to our Custom Logging Data Science")

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>Stage : {STAGE_NAME} Started <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} Completed <<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>>>>Stage : {STAGE_NAME} Started <<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} Completed <<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e
