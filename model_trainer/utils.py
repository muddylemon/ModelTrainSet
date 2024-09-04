import yaml
from datasets import load_dataset


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def load_custom_dataset(file_path: str):
    return load_dataset(path=file_path, split="train")

