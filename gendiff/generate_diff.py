from gendiff.parser import parse_data


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_values = []

    for key in all_keys:
        if key not in data2:
            diff_values.append(f'  - {key}: {format_value(data1[key])}')
        elif key not in data1:
            diff_values.append(f'  + {key}: {format_value(data2[key])}')
        elif data1[key] == data2[key]:
            diff_values.append(f'    {key}: {format_value(data1[key])}')
        else:
            diff_values.append(f'  - {key}: {format_value(data1[key])}')
            diff_values.append(f'  + {key}: {format_value(data2[key])}')
    
    return "{\n" + "\n".join(diff_values) + "\n}"
    