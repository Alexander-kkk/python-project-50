import json
from pathlib import Path


def parse_data(file_path):
    path = Path(file_path)
    content = path.read_text(encoding='utf-8')
    return json.loads(content)
    