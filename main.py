from src.datascience import logger
from src.datascience.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline

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