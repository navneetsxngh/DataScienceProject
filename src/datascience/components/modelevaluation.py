import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from pathlib import Path

from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.main_utils import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
    
    def eval_metrics(self, actual, pred):
        r2 = r2_score(actual, pred)
        mae = mean_absolute_error(actual, pred)
        mse = mean_squared_error(actual, pred)
        rmse = np.sqrt(mse)
        return r2, mae, mse, rmse
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns= [self.config.target_column])
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_experiment("datascience-project")
        tracking_uri_type_score = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted = model.predict(test_x)
            (r2, mae, mse, rmse) = self.eval_metrics(test_y, predicted)

            ## Saving metrics as local
            scores = {"r2" : r2, "MAE" : mae, "MSE" : mse, "RMSE" : rmse}
            save_json(Path(self.config.metric_file_name), scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("R2", r2)
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("MSE", mse)
            mlflow.log_metric("RMSE", rmse)

            if tracking_uri_type_score != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")