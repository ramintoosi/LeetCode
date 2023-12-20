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
