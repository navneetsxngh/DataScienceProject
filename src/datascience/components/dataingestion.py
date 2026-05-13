import urllib.request as request
import zipfile
import os

from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_zip(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded! with following info: \n{header}")
        else:
            logger.info("File already exists")

    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_path)
