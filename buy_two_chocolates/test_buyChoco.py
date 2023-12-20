import pytest

from .main import buyChoco, buyChoco_2


@pytest.mark.parametrize("prices,money,expected", [
    ([1, 2, 2], 3, 0),
    ([3, 2, 3], 3, 3),
    ([88, 43, 61], 72, 72)
])
def test_buyChoco(prices, money, expected):
    assert buyChoco(prices=prices, money=money) == expected


@pytest.mark.parametrize("prices,money,expected", [
    ([1, 2, 2], 3, 0),
    ([3, 2, 3], 3, 3),
    ([88, 43, 61], 72, 72)
])
def test_buyChoco_low_mem(prices, money, expected):
    assert buyChoco_2(prices=prices, money=money) == expected
