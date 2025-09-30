import numpy as np


np1 = np.arange(100)

# finding the square root of each element in the array
print(np.sqrt(np1))


# the absolute value of each element in the array
print(np.abs(np1 - 50))  # Absolute difference from 50
# Slicing from first to last with steps
print(np1[::2])
print(np1[1::2])