import heapq


def buyChoco(prices: list[int], money: int):
    """
    :type prices: List[int]
    :type money: int
    :rtype: int
    """

    two_smallest = heapq.nsmallest(2, prices)
    res = money - sum(two_smallest)
    return res if res >= 0 else money


def buyChoco_2(prices: list[int], money: int):
    """
    Another solution to find the minimum prices manually for comparison
    :type prices: List[int]
    :type money: int
    :rtype: int
    """
    min_1, min_2 = prices[0], prices[1]
    if min_1 > min_2:
        min_1, min_2 = min_2, min_1
    for p in prices[2:]:
        if p < min_1:
            min_2 = min_1
            min_1 = p
        elif p < min_2:
            min_2 = p
    res = money - min_1 - min_2
    return res if res >= 0 else money


def buyChoco_3(prices: list[int], money: int):
    """
    Another solution with sort
    :type prices: List[int]
    :type money: int
    :rtype: int
    """
    prices = sorted(prices)
    res = money - prices[0] - prices[1]
    return res if res >= 0 else money
