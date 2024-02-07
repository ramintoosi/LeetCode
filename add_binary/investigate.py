from add_binary.main import addBinary
import numpy as np

a, b = "1010101010101010", "10101010101010100010100101010101101010"

times = []
for _ in range(10000):
    times.append(addBinary(a, b, return_time=True))

times = np.array(times)

print(times.mean(axis=0).astype(int))
print(times.std(axis=0).astype(int))
