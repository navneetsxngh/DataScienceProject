## Data Science Project — Build Steps

---

### 1. Environment Setup

```bash
# Option A: standard venv
python -m venv .venv
.venv\Scripts\activate

# Option B: uv (faster)
uv init
uv venv
.venv\Scripts\activate
```

---

### 2. Project Scaffolding

- Run `template.py` to auto-generate the full folder and file structure.

---

### 3. Custom Logger

- Implemented in `src/datascience/__init__.py`
- Writes to both console and `logs/running_logs.log`

---

### 4. Common Utility Functions

File: `src/datascience/utils/main_utils.py`

| Function | Purpose |
|---|---|
| `read_yaml()` | Load a YAML file into a `ConfigBox` |
| `create_directories()` | Create one or more directories |
| `save_json()` | Persist a dict as a JSON file |
| `load_json()` | Load a JSON file into a `ConfigBox` |
| `save_bin()` | Save a Python object with `joblib` |
| `load_bin()` | Load a `joblib`-serialized object |

Usage is demonstrated in `research/research.ipynb`.

---

### Pipeline Workflow Overview

Each stage below follows this standard update sequence:

```
config.yaml  →  entity (dataclass)  →  configuration.py  →  component  →  pipeline  →  main.py
```

> `schema.yaml` — updated for validation and training stages  
> `params.yaml` — updated for model trainer and evaluation stages

---

### 5. Data Ingestion

**Goal:** Download the dataset from a remote URL and extract it locally.

Files to update:
- `config/config.yaml` — set `source_URL`, `local_data_file`, `unzip_dir`
- `src/datascience/entity/config_entity.py` — add `DataIngestionConfig`
- `src/datascience/config/configuration.py` — add `get_data_ingestion_config()`
- `src/datascience/components/dataingestion.py` — add `DataIngestion` (download + extract)
- `src/datascience/pipeline/dataingestionpipeline.py` — add `DataIngestionTrainingPipeline`
- `main.py` — run the pipeline stage

> `schema.yaml` and `params.yaml` are **not** required for this stage.

---

### 6. Data Validation

**Goal:** Verify the ingested CSV has all expected columns (defined in `schema.yaml`).

Files to update:
- `config/config.yaml` — set `unzip_data_dir`, `STATUS_FILE`
- `schema.yaml` — define expected column names and dtypes **(important)**
- `src/datascience/entity/config_entity.py` — add `DataValidationConfig`
- `src/datascience/config/configuration.py` — add `get_data_validation_config()`
- `src/datascience/components/datavalidation.py` — add `DataValidation`
- `src/datascience/pipeline/datavalidationpipeline.py` — add `DataValidationTrainingPipeline`
- `main.py` — run the pipeline stage

---

### 7. Data Transformation

**Goal:** Split the validated data into training and test sets (feature engineering goes here too).

Files to update:
- `config/config.yaml` — set `data_path`, `root_dir`
- `src/datascience/entity/config_entity.py` — add `DataTransformationConfig`
- `src/datascience/config/configuration.py` — add `get_data_transformation_config()`
- `src/datascience/components/datatransformation.py` — add `DataTransformation`
- `src/datascience/pipeline/datatransformationpipeline.py` — add `DataTransformationTrainingPipeline`
- `main.py` — run the pipeline stage

---

### 8. Model Trainer

**Goal:** Train a machine learning model (ElasticNet) on the training split.

Files to update:
- `config/config.yaml` — set train/test data paths and `model_name`
- `params.yaml` — set `ElasticNet.alpha` and `ElasticNet.l1_ratio` **(important)**
- `src/datascience/entity/config_entity.py` — add `ModelTrainerConfig`
- `src/datascience/config/configuration.py` — add `get_model_trainer_config()`
- `src/datascience/components/modeltrainer.py` — add `ModelTrainer`
- `src/datascience/pipeline/modeltrainerpipeline.py` — add `ModelTrainingPipeline`
- `main.py` — run the pipeline stage

---

### 9. Model Evaluation

**Goal:** Evaluate the trained model and log metrics + parameters to MLflow via DagsHub.

Files to update:
- `config/config.yaml` — set `model_path`, `metric_file_name`
- `.env` — add `MLFLOW_TRACKING_URI`, `MLFLOW_TRACKING_USERNAME`, `MLFLOW_TRACKING_PASSWORD`
- `src/datascience/entity/config_entity.py` — add `ModelEvaluationConfig`
- `src/datascience/config/configuration.py` — add `get_model_evaluation_config()`
- `src/datascience/components/modelevaluation.py` — add `ModelEvaluation`
- `src/datascience/pipeline/modelevaluationpipeline.py` — add `ModelEvaluationPipeline`
- `main.py` — run the pipeline stage

Metrics logged: **R²**, **MAE**, **MSE**, **RMSE**

---

### 10. Prediction Pipeline & Flask App

**Goal:** Serve predictions via a web interface.

- `src/datascience/pipeline/predictionpipeline.py` — loads `model.joblib` and runs `predict()`
- `app.py` — Flask app with three routes:
  - `GET /` — input form (`templates/index.html`)
  - `GET /train` — re-runs `main.py` to retrain the model
  - `POST /predict` — returns the quality prediction (`templates/results.html`)

Run locally:
```bash
python app.py
# Visit http://localhost:8080
```

---

### 11. Deployment (Docker + CI/CD)

- `Dockerfile` — containerize the Flask app
- `.github/workflows/` — add GitHub Actions pipeline for automated build and deploy
