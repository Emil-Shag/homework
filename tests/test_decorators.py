import pytest

from src.decorators import log


@log(filename="mylog.txt")
def first_function(x, y):
    return x + y


@log(filename="mylog.txt")
def second_function(x, y):
    return x / y


def test_first_function(capsys):
    result = first_function(1, 2)
    assert result == 3


def test_second_function(capsys):
    with pytest.raises(ZeroDivisionError):
        second_function(1, 0)
