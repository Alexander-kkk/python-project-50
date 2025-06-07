import json
import os

import pytest

from gendiff.generate_diff import generate_diff


def read_file(path):
    with open(path) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1,file2,format_name,expected_file", [
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.yml', 'stylish', 'expected_stylish.txt'),
    ('file1.yml', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.yml', 'file2.yml', 'plain', 'expected_plain.txt'),
    ('file1.json', 'file2.yml', 'plain', 'expected_plain.txt'),
    ('file1.yml', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'expected_json.txt'),
    ('file1.yml', 'file2.yml', 'json', 'expected_json.txt'),
    ('file1.json', 'file2.yml', 'json', 'expected_json.txt'),
    ('file1.yml', 'file2.json', 'json', 'expected_json.txt'),
])
def test_generate_diff(file1, file2, format_name, expected_file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_data = os.path.join(dir_path, 'test_data')
    
    file1_path = os.path.join(test_data, file1)
    file2_path = os.path.join(test_data, file2)
    expected_path = os.path.join(test_data, expected_file)
    
    result = generate_diff(file1_path, file2_path, format_name)
    expected = read_file(expected_path)
    
    if format_name == 'json':
        assert json.loads(result) == json.loads(expected)
    else:
        assert result.strip() == expected.strip()