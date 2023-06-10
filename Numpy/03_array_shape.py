# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 11:30
# @Author  : Cho
# @FileName: 03_array_shape.py
# @Software: PyCharm

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
new_arr = arr.reshape(4, 2)
# iterate 2-D
for x in new_arr:
    print(x)

# iterate each scalar element
for x in np.nditer(new_arr):
    print(x)