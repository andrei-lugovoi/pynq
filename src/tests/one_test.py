import pytest

from core.pynq import Pynq

import core.extensions


def test_one_returns_item_if_col_has_one_item():
    list = ['Only you.']

    actual = list.one()
    expected = 'Only you.'

    assert actual == expected


def test_one_raises_exception_if_col_has_not_one_item():
    list = [
        'We',
        'are',
        'the',
        'champions'
    ]

    with pytest.raises(Exception):
        Pynq(list).one()
