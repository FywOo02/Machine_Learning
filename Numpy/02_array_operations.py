# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 10:47
# @Author  : Cho
# @FileName: 02_array_operations.py
# @Software: PyCharm

import numpy as np

# Array Slicing
"""
arr = np.array([1, 2, 3, 4, 5])
print(arr[:5])
print(arr[4::-1])
"""

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# From the second element, slice elements from index 1 to index 4 (not included)
print(arr[1, 1:4])
# From both elements, return index 2
print(arr[0:2, 2])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])
print(arr.ndim)

