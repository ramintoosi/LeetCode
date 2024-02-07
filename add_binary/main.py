import time


def addBinary(a: str, b: str, return_time=False) -> str | list[float]:
    """
    adds two binary strings
    :param a: binary string
    :param b: binary string
    :param return_time: if True, returns process times
    :return: sum of a and b
    """

    t1 = time.time_ns()
    conv = {
        "1": 1, "0": 0
    }

    result = ""

    m, n = len(a), len(b)

    t2 = time.time_ns()
    # make sure that a is longer
    if m < n:
        a, b = b, a
        m, n = n, m
    t3 = time.time_ns()
    a = a[::-1]
    b = b[::-1]

    overflow_flag = False

    t4 = time.time_ns()
    for i in range(n):
        c = conv[a[i]] + conv[b[i]] + overflow_flag
        if c == 1 or c == 0:
            result = "{}".format(c) + result
            overflow_flag = False
        else:
            c = c - 2
            overflow_flag = True
            result = "{}".format(c) + result
    t5 = time.time_ns()
    for i in range(n, m):
        c = conv[a[i]] + overflow_flag
        if c == 1 or c == 0:
            result = "{}".format(c) + result
            overflow_flag = False
        else:
            c = c - 2
            overflow_flag = True
            result = "{}".format(c) + result
    t6 = time.time_ns()
    if overflow_flag:
        result = "1" + result
    t7 = time.time_ns()
    if return_time:
        return [t2-t1, t3-t2, t4-t3, t5-t4, t6-t5, t7-t1]
    else:
        return result


def add_binary2(a: str, b: str) -> str:
    """
        adds two binary strings
        :param a: binary string
        :param b: binary string
        :return: sum of a and b
        """
    return bin(int(a, 2) + int(b, 2))