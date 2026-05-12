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