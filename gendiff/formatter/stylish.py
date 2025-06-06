def format_stylish(diff, indent=0):
    lines = []
    indent_str = ' ' * (indent + 2)
    
    for node in diff:
        key = node['key']
        type_ = node['type']
        
        if type_ == 'nested':
            lines.append(f"{indent_str}  {key}: {{")
            lines.append(format_stylish(node['children'], indent + 4))
            lines.append(f"{indent_str}  }}")
        elif type_ == 'added':
            lines.append(format_value(
                f"{indent_str}+ {key}", node['new_value'], indent + 2
            ))
        elif type_ == 'removed':
            lines.append(format_value(
                f"{indent_str}- {key}", node['old_value'], indent + 2
            ))
        elif type_ == 'changed':
            lines.append(format_value(
                f"{indent_str}- {key}", node['old_value'], indent + 2
            ))
            lines.append(format_value(
                f"{indent_str}+ {key}", node['new_value'], indent + 2
            ))
        elif type_ == 'unchanged':
            lines.append(format_value(
                f"{indent_str}  {key}", node['value'], indent + 2
            ))
    
    return '\n'.join(lines)


def format_value(prefix, value, indent):
    if isinstance(value, dict):
        lines = [f"{prefix}: {{"]
        for key, val in value.items():
            lines.append(format_value(
                ' ' * (indent + 6) + key, val, indent + 4
            ))
        lines.append(f"{' ' * indent}  }}")
        return '\n'.join(lines)
    else:
        if value is None:
            value = 'null'
        elif isinstance(value, bool):
            value = str(value).lower()
        return f"{prefix}: {value}"