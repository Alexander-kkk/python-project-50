import sys

import pytest

from gendiff.cli import parse_args


def test_help_command(capsys):
    with pytest.raises(SystemExit):
        sys.argv = ['gendiff', '-h']
        parse_args()