import json

from gendiff.formatter.json import format_json


def test_format_json():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children': [
                {
                    'key': 'setting1',
                    'type': 'unchanged',
                    'value': 'Value 1'
                }
            ]
        }
    ]
    
    result = format_json(diff)
    assert json.loads(result) == diff
    assert isinstance(result, str)