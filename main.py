from src.datascience import logger
from src.datascience.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.datavalidationpipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.datatransformationpipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.modeltrainerpipeline import ModelTrainingPipeline
from src.datascience.pipeline.modelevaluationpipeline import ModelEvaluationPipeline

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['MLFLOW_TRACKING_URI'] = os.getenv('MLFLOW_TRACKING_URI')
os.environ['MLFLOW_TRACKING_USERNAME'] = os.getenv('MLFLOW_TRACKING_USERNAME')
os.environ['MLFLOW_TRACKING_PASSWORD'] = os.getenv('MLFLOW_TRACKING_PASSWORD')

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



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>>Stage : {STAGE_NAME} Started <<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} Completed <<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>>Stage : {STAGE_NAME} Started <<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} Completed <<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>Stage : {STAGE_NAME} Started <<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} Completed <<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e