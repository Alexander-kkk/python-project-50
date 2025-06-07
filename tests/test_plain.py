from gendiff.formatter.plain import format_plain, format_value


def test_format_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value(42) == '42'
    assert format_value('text') == "'text'"
    assert format_value({'a': 1}) == '[complex value]'
    assert format_value([1, 2]) == '[complex value]'


def test_format_plain():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children': [
                {
                    'key': 'setting1',
                    'type': 'unchanged',
                    'value': 'Value 1'
                },
                {
                    'key': 'setting2',
                    'type': 'removed',
                    'old_value': 200
                }
            ]
        }
    ]
    
    expected = "Property 'common.setting2' was removed"
    assert format_plain(diff) == expected