from gendiff.build_diff import build_diff
from gendiff.formatter.stylish import format_stylish
from gendiff.parser import parse_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return f"{{\n{format_stylish(diff)}\n}}"
    else:
        raise ValueError(f"Unknown format: {format_name}")
    