import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion/__init__.py",
    f"src/{project_name}/components/data_transformation/__init__.py",
    f"src/{project_name}/components/model_trainer/__init__.py",
    f"src/{project_name}/components/model_monitering/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline/__init__.py",
    f"src/{project_name}/exceptions/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "app.py",
    "Dockerfile",
    "main.py"
]


for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename=os.path.split(file_path)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    
    else:
        logging.info(f"{filename} already exists")