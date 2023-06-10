# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 17:33
# @Author  : Cho
# @FileName: 04_array_join.py
# @Software: PyCharm

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
arr3 = np.array([[13, 14, 15], [16, 17, 18]])
combine = np.concatenate([arr1, arr2, arr3], axis=1)
print(combine)
