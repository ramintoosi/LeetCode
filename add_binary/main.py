import time


def addBinary(a: str, b: str, return_time=False) -> str | list[float]:
    """
    adds two binary strings
    :param a: binary string
    :param b: binary string
    :param return_time: if True, returns process times
    :return: sum of a and b
    """
    t1 = time.process_time()
    conv = {
        "1": 1, "0": 0
    }

    result = ""

    m, n = len(a), len(b)

    t2 = time.process_time()
    # make sure that a is longer
    if m < n:
        a, b = b, a
        m, n = n, m
    t3 = time.process_time()
    a = a[::-1]
    b = b[::-1]

    overflow_flag = 0

    t4 = time.process_time()
    for i in range(n):
        c = conv[a[i]] + conv[b[i]] + overflow_flag
        if c == 1 or c == 0:
            result = "{}".format(c) + result
            overflow_flag = 0
        else:
            c = c - 2
            overflow_flag = 1
            result = "{}".format(c) + result
    t5 = time.process_time()
    for i in range(n, m):
        c = conv[a[i]] + overflow_flag
        if c == 1 or c == 0:
            result = "{}".format(c) + result
            overflow_flag = 0
        else:
            c = c - 2
            overflow_flag = 1
            result = "{}".format(c) + result
    t6 = time.process_time()
    if overflow_flag == 1:
        result = "1" + result
    if return_time:
        return [t2-t1, t3-t2, t4-t3, t5-t4, t6-t5]
    else:
        return result
