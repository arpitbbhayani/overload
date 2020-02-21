# encoding=utf-8
import logging

import pytest
from hamcrest import assert_that, close_to
from overload import OverloadException, overload

logger = logging.getLogger(__name__)


@overload
def area(length, breadth):
    return length * breadth


@overload
def area(radius):  # noqa: F811
    import math

    return math.pi * radius ** 2


@overload
def area(length, breadth, height):  # noqa: F811
    return 2 * (length * breadth + breadth * height + height * length)


def test_overload_functions():
    assert area(4, 3, 6) == 108
    assert area(4, 3) == 12
    assert_that(area(4), close_to(50.26, 0.01))


def test_no_such_function():
    with pytest.raises(OverloadException):
        area(1, 2, 3, 4)
