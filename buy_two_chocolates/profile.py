"""
This module measures the memory usage and running time of the written function
"""
from memory_profiler import memory_usage
import timeit

from buy_two_chocolates.main import buyChoco as buyChoco

memory_result = memory_usage(
    (buyChoco, ([3, 2, 3], 3)),
    interval=0.0001,
    max_usage=True
)
n = 100
time_result = timeit.timeit(stmt='buyChoco([3, 2, 3], 3)', globals=globals(), number=n)

print(f'{memory_result:.4f} MiB memory usage')
print(f'{time_result / n * 1000: .4f} ms running time')
