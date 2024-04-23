# OS library will help to determine which OS and make
# the application OS independent
import os
# In order to make the application OS independent.
# Based on the Operating system it will append the path
from pathlib import Path
# This will help to log the details of the application
# and also to debug the application in case of errors.
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# logging string for despalyting the messages while executing this template.py
# instead of printing them the best practice is to log everything
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s: %(levelname)s]: %(message)s:'
    )

while True:
    project_name = input("Enter the project name: ")
    if project_name != '':
        break
logging.info(f"Creating project by name: {project_name}")
             
# Following are the list of files that will be created            
list_of_files = [
    ".github/workflows/.gitkeep",  # gitkeep is an empty file as per the structure
    #f"{project_name}/src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "LICENSE",
    "pyproject.toml",
    "setup.cfg",
    "README.md",
    "tox.ini"  # python packages need to be tested in various environments
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory at: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
        
        
