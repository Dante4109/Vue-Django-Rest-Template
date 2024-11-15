import pytest

from mixer.backend.django import mixer


def test_case_1():

    # arranage

    x = 1
    y = 2

    # act
    z = x + y

    # assert
    assert z == 3
