"""
This module measures the memory usage and running time of the written function
"""
from memory_profiler import memory_usage
import timeit

from add_binary.main import addBinary

memory_result = memory_usage(
    (addBinary, ("1010101010101010", "10101010101010100010100101010101101010")),
    interval=0.0001,
    max_usage=True
)
n = 100
time_result = timeit.timeit(stmt='addBinary("1010101010101010", "10101010101010100010100101010101101010")',
                            globals=globals(), number=n)

print(f'{memory_result:.4f} MiB memory usage')
print(f'{time_result / n * 1000: .4f} ms running time')
