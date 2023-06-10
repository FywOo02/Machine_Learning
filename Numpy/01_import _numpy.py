import numpy as np

if __name__ == "__main__":
    """
    arr_test = np.array((1, 2, 3, 4, 5))
    print(arr_test)
    print(type(arr_test))
    """

    a = np.array(42)
    b = np.array([1, 2, 3, 4, 5])
    c = np.array([[1, 2, 3], [4, 5, 6]])
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

    print(a.ndim)
    print(b.ndim)
    print(c.ndim)
    print(d.ndim)

    arr = np.array([1, 2, 3, 4], ndmin=5)

    print(arr)
    print('number of dimensions :', arr.ndim)



