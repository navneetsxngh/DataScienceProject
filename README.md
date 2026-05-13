# Wine Quality Predictor

An end-to-end machine learning project that predicts the quality of red wine (score 0–10) from its physicochemical properties. Built with a modular, production-style pipeline and served via a Flask web application.

---

## Features

- Automated ML pipeline: ingestion → validation → transformation → training → evaluation
- ElasticNet regression model tracked with MLflow on DagsHub
- Flask web app with a prediction form and visual results page
- Docker-ready for containerized deployment
- CI/CD via GitHub Actions

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.13 |
| ML | scikit-learn, joblib |
| Experiment Tracking | MLflow, DagsHub |
| Web Server | Flask |
| Data | pandas, numpy |
| Config | PyYAML, python-box |
| Package Manager | uv |
| Deployment | Docker, GitHub Actions |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/navneetsxngh/DataScienceProject.git
cd DataScienceProject
```

### 2. Create and activate a virtual environment

```bash
uv venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo>.mlflow
MLFLOW_TRACKING_USERNAME=<your_dagshub_username>
MLFLOW_TRACKING_PASSWORD=<your_dagshub_token>
```

### 5. Run the training pipeline

```bash
python main.py
```

### 6. Start the web app

```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

---

## Pipeline Stages

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation
```

| Stage | Output |
|---|---|
| Data Ingestion | `artifacts/data_ingestion/winequality-red.csv` |
| Data Validation | `artifacts/data_validation/status.txt` |
| Data Transformation | `artifacts/data_transformation/train.csv`, `test.csv` |
| Model Training | `artifacts/model_trainer/model.joblib` |
| Model Evaluation | `artifacts/model_evaluation/metrics.json` |

---

## Model

- **Algorithm:** ElasticNet
- **Hyperparameters:** `alpha=0.2`, `l1_ratio=0.1`
- **Target:** `quality` (integer, 0–10)

**Current metrics:**

| Metric | Value |
|---|---|
| R² | 0.279 |
| MAE | 0.539 |
| MSE | 0.467 |
| RMSE | 0.683 |

---

## Web App Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Input form for wine features |
| `/predict` | POST | Returns the predicted quality score |
| `/train` | GET | Re-runs the full training pipeline |

---

## Docker

```bash
# Build the image
docker build -t wine-quality-predictor .

# Run the container
docker run -p 8080:8080 --env-file .env wine-quality-predictor
```

---

## CI/CD — Deploy to AWS EC2

Every push to `main` automatically builds the Docker image, pushes it to Amazon ECR, and deploys it to an EC2 instance.

### How it works

```
Push to main
    │
    ▼
Job 1: Build & Push (GitHub runner)
  ├── Authenticate with AWS IAM
  ├── Log in to Amazon ECR
  └── docker build → docker push → ECR
    │
    ▼
Job 2: Deploy (SSH into EC2)
  ├── EC2 pulls the image from ECR
  ├── Stops the old container
  └── Runs the new container on port 8080
```

### GitHub Secrets

Go to your repository → **Settings → Secrets and variables → Actions → New repository secret** and add the following:

| Secret | Where to find it |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS Console → IAM → Users → your user → Security credentials |
| `AWS_SECRET_ACCESS_KEY` | Same page (shown once when created) |
| `AWS_REGION` | Region you created your ECR and EC2 in, e.g. `us-east-1` |
| `AWS_ECR_REPOSITORY_URI` | AWS Console → ECR → Repositories → click your repo → copy **URI** (e.g. `123456789.dkr.ecr.us-east-1.amazonaws.com/wine-quality-predictor`) |
| `MLFLOW_TRACKING_URI` | DagsHub → your repo → MLflow tracking URL |
| `MLFLOW_TRACKING_USERNAME` | Your DagsHub username |
| `MLFLOW_TRACKING_PASSWORD` | DagsHub → Settings → Access Tokens |
| `EC2_HOST` | AWS Console → EC2 → your instance → **Public IPv4 address** |
| `EC2_SSH_KEY` | Open your `.pem` file in a text editor → copy the entire contents |

> `AWS_ACCOUNT_ID`, `ECR_REPOSITORY`, and `EC2_USERNAME` are not required — the account ID and registry are derived from `AWS_ECR_REPOSITORY_URI`, and the username is hardcoded as `ubuntu`.

### One-time EC2 setup

SSH into your instance and run:

```bash
sudo apt update && sudo apt install -y docker.io awscli
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu
```

Then attach an IAM role to the EC2 instance with the **`AmazonEC2ContainerRegistryReadOnly`** policy so it can pull images from ECR:

```
AWS Console → EC2 → select instance → Actions → Security → Modify IAM role → attach role
```

### IAM permissions required

The IAM user whose keys are stored in GitHub secrets needs the following ECR permissions to push images:

```
ecr:GetAuthorizationToken
ecr:BatchCheckLayerAvailability
ecr:CompleteLayerUpload
ecr:InitiateLayerUpload
ecr:PutImage
ecr:UploadLayerPart
```

---

## Project Structure

```
DataScienceProject/
├── src/datascience/
│   ├── components/        # Pipeline stage logic
│   ├── pipeline/          # Stage orchestrators
│   ├── config/            # ConfigurationManager
│   ├── entity/            # Typed config dataclasses
│   ├── constants/         # File path constants
│   └── utils/             # YAML / JSON / joblib helpers
├── config/config.yaml     # Paths and URLs
├── params.yaml            # Model hyperparameters
├── schema.yaml            # Dataset schema
├── main.py                # Runs the full training pipeline
├── app.py                 # Flask web application
├── Dockerfile
└── .github/workflows/deploy.yaml
```

---

## License

MIT
