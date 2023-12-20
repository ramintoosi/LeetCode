import pytest

from .main import buyChoco


@pytest.mark.parametrize("prices,money,expected", [
    ([1, 2, 2], 3, 0),
    ([3, 2, 3], 3, 3)
])
def test_case_1(prices, money, expected):
    assert buyChoco(prices=prices, money=money) == expected
