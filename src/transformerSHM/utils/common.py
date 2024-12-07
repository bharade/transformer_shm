import os,yaml
from box.exceptions import BoxValueError
from transformerSHM.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    read the yaml file and return the configbox object
    Argss:
    path_to_yaml: path to the yaml file 
    returns: ConfigBox object
    """
    try:
        with open(path_to_yaml,'r') as file:
            config=ConfigBox(yaml.safe_load(file))
            logger.info(f"yaml file read successfully from {path_to_yaml}")
            return config
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    create directories if they do not exist
    Args: path_to_directories: list of directories to be created
    returns: None
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory created at {path}")

@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    Args: path: Path to the file
    Returns: size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"