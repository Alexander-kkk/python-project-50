from gendiff.build_diff import build_diff
from gendiff.formatter.plain import format_plain
from gendiff.formatter.stylish import format_stylish
from gendiff.parser import parse_data

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)
    diff = build_diff(data1, data2)

    formatter = FORMATTERS.get(format_name)
    if not formatter:
        raise ValueError(f"Unknown format: {format_name}")
    
    result = formatter(diff)
    
    if format_name == 'stylish':
        return f"{{\n{result}\n}}"
    return result
    