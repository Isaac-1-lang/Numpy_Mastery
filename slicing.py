import numpy as np


np1= np.arange(100)


# slicing from first to last with steps


print(np1[::2]);
print(np1[1::2]);

# Slicing multidimensional arrays
np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np2[0, :])  # First row
print(np2[:, 1])  # Second column
print(np2[1:, 1:])  # Subarray from second row and second column to the end
print(np2[::2, ::2])  # Every second row and every second column
print(np2[::-1, ::-1])  # Reverse the array
