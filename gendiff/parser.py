import json
from pathlib import Path

import yaml


def parse_data(file_path):
    path = Path(file_path)
    content = path.read_text(encoding='utf-8')
    
    if path.suffix in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    elif path.suffix == '.json':
        return json.loads(content)   
    