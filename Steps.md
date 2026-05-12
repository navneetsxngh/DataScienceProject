## Data Science Project
1. Setting up your Environment
```bash
python -m venv <env name>

## or
uv init
.venv\Scripts\activate
uv venv
```

2. Create a `template.py` file
- Inside this we create our whole project structure.

3. Custom Logging Implementation 
- Inside `src/datascience/__init__.py` we create our logger

4. Commom Utilities Functions
- Inside `src/datascience/utils/main_utils.py` added function `load_yaml()`, `create_directories()`, `save_json()`, `load_json()`, `save_bin()`, `load_bin()`
- Inside `research/research.ipynb` we demonstrate the functions 


```markdown
### Workflow
1. Data Ingestion
2. Data Validataion
3. Data Transformation
4. Nodel Trainer
5. Model Evaluation
```


5. Data Ingestion
Workflows --> ML Pipeline
- Inside `src/datascience/components/dataingestion.py` --> Add DataIngestion
- Inside `src/datascience/config/configuration.py` --> Add Configuration Manager
- Inside `src/datascience/entity/config_entity.py` --> Add DataIngestionConfig
- Inside `src/datascience/pipeline/dataingestionpipeline.py` --> Add DataIngestionTrainingPipeline

UPDATE config.yaml (Important)
UPDATE schema.yaml
UPDATE params.yaml
UPDATE the entity
UPDATE the configuration manager in `src/datascience/config`
UPDATE the components
UPDATE the pipeline
UPDATE the main.py

`schema.yaml` and `params.yaml` not required in Data Ingestion

6. Data Validation
- Inside `src/datasciencs/components/datavalidation.py` --> Add DataVaidation
- Inside `src/datascience/config/configuration.py` --> Update Configuration Manager
- Inside `src/datascience/entity/config_entity.py` --> Add DataValidationConfig
- Inside `src/datascience/pipeline/datavalidationpipeline.py` --> Add DataValidationTrainingPipeline

UPDATE schema.yaml (Important)

7. Data Transformation
Mainly Feature Engineering or Data Preprocessing
- Inside `src/datasciencs/components/datatransformation.py` --> Add DataTransformation
- Inside `src/datascience/config/configuration.py` --> Update Configuration Manager
- Inside `src/datascience/entity/config_entity.py` --> Add DataTransformationConfig
- Inside `src/datascience/pipeline/datatransformationpipeline.py` --> Add DataTransformationTrainingPipeline

8. Model Trainer
Training the Machine Learning Model
- Inside `src/datasciencs/components/modeltrainer.py` --> Add ModelTrainer
- Inside `src/datascience/config/configuration.py` --> Update Configuration Manager
- Inside `src/datascience/entity/config_entity.py` --> Add ModelTrainerConfig
- Inside `src/datascience/pipeline/modeltrainingpipeline.py` --> Add ModelTrainingPipeline

Update `params.yml` (Important)