from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.datavalidation import DataValidation
from src.datascience import logger

STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.error(e)
            raise e
