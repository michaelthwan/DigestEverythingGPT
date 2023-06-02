import os
import yaml
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def get_config():
    with open(os.path.join(get_project_root(), 'config/config.yaml'), encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
