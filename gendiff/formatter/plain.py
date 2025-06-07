def format_plain(diff, parent_key=''):
    lines = []
    
    for node in diff:
        key = node['key']
        type_ = node['type']
        full_path = f"{parent_key}{key}"
        
        if type_ == 'nested':
            nested_lines = format_plain(node['children'], f"{full_path}.")
            if nested_lines:
                lines.append(nested_lines)
        elif type_ == 'added':
            value = format_value(node['new_value'])
            message = f"Property '{full_path}' was added with value: {value}"
            lines.append(message)
        elif type_ == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif type_ == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            message = (
                f"Property '{full_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
            lines.append(message)
    
    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)