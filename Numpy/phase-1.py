import numpy as np

arr_1d = np.array([1,2,3,4,5])
print("1D array:",arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array:",arr_2d)

l1 = [1,2,3,4,5,6]
print("List of multiplication:",l1 * 2)

a1 = np.array([1,2,3])
print("Array of multiplication:",a1 * 2)

import time

start = time.time()
py_list = [i*2 for i in range(1000000)]
print("\n List operation time:",time.time() - start)

start = time.time()
np_array = np.arange(1000000) * 2
print("\n Numpy operation time:",time.time() - start)