import os

import pytest

from gendiff.generate_diff import generate_diff


def read_file(path):
    with open(path) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1,file2", [
    ('file1.json', 'file2.json')   
])
def test_flat_files(file1, file2):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_data = os.path.join(dir_path, 'test_data')
    
    file1_path = os.path.join(test_data, file1)
    file2_path = os.path.join(test_data, file2)
    expected_path = os.path.join(test_data, 'expected_result.txt')
    
    result = generate_diff(file1_path, file2_path)
    assert result == read_file(expected_path)