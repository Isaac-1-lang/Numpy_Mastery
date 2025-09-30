import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
d=a*b
print(c)
print(d)


e = np.arange(10)
print(e.shape);
# print the dimensions of the array
print(e.ndim)
# print the number of dimensions of the array
print(e.size)
# print the total number of elements in the array
print(e.dtype)
# print the data type of the array elements
print(e.itemsize)
# print the size in bytes of each element in the array
print(e.nbytes)
# print the total size in bytes of the array
print(e)
# print the array itself
print(e[0:5])
# print the first five elements of the array
print(e[5:])
# print the elements from index 5 to the end of the array
print(e[::2])
# print every second element of the array
print(e[::-1])
# print the array in reverse order
print(e.reshape(2, 5))
# reshape the array to 2 rows and 5 columns
print(e.reshape(5, 2))
# reshape the array to 5 rows and 2 columns
print(e.reshape(10, 1))
# reshape the array to 10 rows and 1 column
print(e.reshape(1, 10))
# reshape the array to 1 row and 10 columns
print(e.reshape(-1, 5))
# reshape the array to an unknown number of rows with 5 columns
print(e.reshape(2, -1))
# reshape the array to 2 rows with an unknown number of columns
print(e.reshape(5, -1))
# reshape the array to 5 rows with an unknown number of columns
print(e.reshape(10, -1))
# reshape the array to 10 rows with an unknown number of columns
print(e.reshape(-1, 2))
# reshape the array to an unknown number of rows with 2 columns
print(e.reshape(1, -1))
# reshape the array to 1 row with an unknown number of columns
print(e.reshape(-1, 1))
# reshape the array to an unknown number of rows with 1 column
print(e.reshape(2, 5, 1))
# reshape the array to 2 rows, 5 columns, and 1 depth
print(e.reshape(5, 2, 1))
# reshape the array to 5 rows, 2 columns, and 1 depth
print(e.reshape(10, 1, 1))
# reshape the array to 10 rows, 1 column, and 1 depth
print(e.reshape(1, 10, 1))  
