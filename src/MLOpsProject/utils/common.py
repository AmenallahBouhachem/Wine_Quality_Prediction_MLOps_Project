import os
from box.exceptions import BoxValueError
import yaml
from MLOpsProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and returns
    Args:
        path_toyaml (str): path like inpuut
    Raises: 
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    
    """
    try:
        with open(path_to_yaml) as yaml_file :
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {path_to_yaml} is empty") from e
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories
    Args:
        path_to_directories (list): list of directories
        ignore_log (bool, optional): ignore if multiple irs is to be created. Defaults to False.
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")

@ensure_annotations
def save_json(dict_: dict, path: Path, data=dict):
    """
    save dict to json file
    Args:
        data (dict): data to be saved in json file
        path(Path): path to json file
        
    """
    with open(path, "w") as f:
        json.dump(dict_, f, indent=4)
       
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file
    Args:
        path(Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"json file loaded from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save data to binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")

    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary file
    Args:
        path (Path): path to binary file
    Returns:
        Any: data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """
    get size of file in kb
    Args:
        path (Path): path to file
    Returns:
        str: size of file in kb
    """
    size_in_kb = os.path.getsize(path)
    return f"~{size_in_kb/1024} kb"