import pytest

from main.utils import format_output


def test_format_output():
    test1 = 999
    test2 = 5000
    test3 = 99999
    test4 = 5000000
    assert format_output(test1) == '999'
    assert format_output(test2) == '5K'
    assert format_output(test3) == '99K'
    assert format_output(test4) == '5M'
